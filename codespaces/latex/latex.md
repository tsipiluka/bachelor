# LaTeX Codespace

<div style="display:flex;">
  <img src="https://www.latex-project.org/img/latex-project-logo.svg" style="max-height:100px; width:auto; margin-right:30px;">
  <img src="https://james-yu.gallerycdn.vsassets.io/extensions/james-yu/latex-workshop/9.9.0/1682778309479/Microsoft.VisualStudio.Services.Icons.Default" style="max-height:100px; width:auto; margin-right:30px;">
  <img src="https://valentjn.gallerycdn.vsassets.io/extensions/valentjn/vscode-ltex/13.1.0/1638117951493/Microsoft.VisualStudio.Services.Icons.Default" style="max-height:100px; width:auto;">
</div>

---
## How to use

1. Copy the contents of this folder into a repository. This includes the `.devcontainer` folder, the `tools` folder and the `init.sh` file.
2. Run the codespace by visiting the repository in GitHub and clicking the green "Code" button. Select "Open with Codespaces" and wait for the codespace to be created.
3. Wait for the Codespace to be created. **This takes 1-5 minutes for the first time**. The progress can be seen in the Codespace creation logs or within the belonging Terminal tab.

### How to use language checking and linting
The [vscode-ltex](https://marketplace.visualstudio.com/items?itemName=valentjn.vscode-ltex) extension is installed and enabled by default. It provides language checking and linting. To use it, simply open a `.tex` file and start typing. The extension will automatically check your code and display errors and warnings. In case of a different language, add a Magic Comment to the top of the file. For example, to use German, add the following line to the top of the file:

```tex
% LTeX: language=de-DE
```

### How to use the easy_package_install script
As already mentioned, the used TeX version includes the basic scheme. This means that not all packages are included. If you want to use a package that is not included, you can use the `easy_package_install` script. This script automatically detects the dependencies of the project and installs them. To use the script, simply run the following command in the terminal:

```shell
python3 tools/easy_package_install.py your_file.tex
```

The script will then automatically detect the dependencies and install them. If you want to install a package manually, you can do so by running the following command in the terminal:

```shell
/usr/local/texlive/VERSION/bin/x86_64-linux/tlmgr install package_name
```
Make sure to replace `VERSION` with the version of your TeX distribution.



---
## What this setup does
This Codespace is a pre-configured environment for building LaTeX documents fully in the browser. It lets you edit your LaTeX files in VS Code using the [LaTeX Workshop](https://marketplace.visualstudio.com/items?itemName=James-Yu.latex-workshop) extension and also compile them. Additionally it adds the [vscode-ltex](https://marketplace.visualstudio.com/items?itemName=valentjn.vscode-ltex) extension to provide language checking and linting

It includes the following components:

- [TeX Live](https://www.tug.org/texlive/) - A basic LaTeX distribution without src and docs (This drastically reduces the size of the image)
  -  [xetex](https://www.tug.org/xetex/) - A TeX typesetting engine using Unicode and supporting modern font technologies such as OpenType and Apple Advanced Typography (AAT).
  -  [biblatex](https://ctan.org/pkg/biblatex) - A complete reimplementation of the bibliographic facilities provided by LaTeX in conjunction with BibTeX.
  -  [biber](https://ctan.org/pkg/biber) - A BibTeX replacement for users of biblatex.
  -  [float](https://ctan.org/pkg/float) - Improved interface for floating objects.
  -  [standalone](https://ctan.org/pkg/standalone) - Compile TeX pictures stand-alone or as part of a document.


- Dynamic Configuration for LaTeX Workshop
  - Automatically detects the LaTeX distribution and tools.
  - Configures the LaTeX Workshop extension to use the detected tools.
  - Configures the recipe to use `xetex` to build the LaTeX project.

- An easy-to-use script that automatically detects `\usepackage{}` dependencies and installs them.
- Default TeX `.gitignore` file.