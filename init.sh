#!/usr/bin/sh

echo ""
echo "Downloading texlive..."
mkdir -p tmp
cd tmp
wget https://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz
zcat install-tl-unx.tar.gz | tar xf -
cd install-tl-*
sudo perl ./install-tl --no-interaction --no-doc-install --no-src-install --scheme=basic
cd ..

echo ""
echo "Detecting texlive version..."
TEXLIVE_VERSION=$(ls -1 /usr/local/texlive/ | grep "^[0-9][0-9][0-9][0-9]$")
echo "Detected texlive version: $TEXLIVE_VERSION"


echo ""
echo "Installing packages..."
sudo /usr/local/texlive/$TEXLIVE_VERSION/bin/x86_64-linux/tlmgr install pdflatex biblatex biber float standalone babel-german

echo ""
echo "Setting up environment..."
echo "export PATH=$PATH:/usr/local/texlive/$TEXLIVE_VERSION/bin/x86_64-linux" >> ~/.bashrc
cd ..
mkdir -p .vscode
wget -O .vscode/settings.json https://raw.githubusercontent.com/moritzrfs/codebrew/main/codespaces/latex/.vscode/settings.json
sed -i "s/TEXLIVE_VERSION/$TEXLIVE_VERSION/g" .vscode/settings.json
wget -O .gitignore https://raw.githubusercontent.com/moritzrfs/codebrew/main/codespaces/latex/.gitignore
mkdir tools
wget -O tools/easy_package_install.py https://raw.githubusercontent.com/moritzrfs/codebrew/main/codespaces/latex/tools/easy_package_install.py

echo "> Running clean up"

sudo rm -rf tmp/
echo ""
echo "> Done"
