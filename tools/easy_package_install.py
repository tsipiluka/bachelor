import sys
import re
import subprocess

class LatexInstaller:
    """
    Call this with a LaTeX file as argument to install all packages
    Example:
    python3 easy_package_install.py main.tex
    By default the script will use the latest TeXLive version (2023).
    For different version python3 easy_package_install.py main.tex 2021
    """

    def __init__(self, latex_filename, texlive_version="2023"):
        # latex_filename = "../" + latex_filename
        with open(latex_filename, "r") as f:
            latex_code = f.read()

        # Regex-Pattern zum Extrahieren der Paketnamen
        pattern = r"\\usepackage(?:\[(.*?)\])?\{(.*?)\}"

        # Paketnamen extrahieren
        packages = [pkg[1] for pkg in re.findall(pattern, latex_code)]
        packages = [pkg.replace(",", "") for pkg in packages]

        installs = ''
        for package in packages:
            installs += ' ' + package

        tlmgr_command = ["sudo", f"/usr/local/texlive/{texlive_version}/bin/x86_64-linux/tlmgr", "install"] + packages

        result = subprocess.run(tlmgr_command, capture_output=True)
        print(result.stdout.decode())
        print("Installed packages: " + installs)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        latex_filename = sys.argv[1]
        if len(sys.argv) > 2:
            texlive_version = sys.argv[2]
            LatexInstaller(latex_filename, texlive_version)
        else:
            LatexInstaller(latex_filename)
    else:
        print("No LaTeX file specified.")
        sys.exit()