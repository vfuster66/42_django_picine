#!/bin/bash

# Affiche la version de pip
echo "Pip version:"
pip --version

# Définir les variables
LIB_DIR="local_lib"
LOG_FILE="install.log"
PACKAGE="git+https://github.com/jaraco/path.py"

# Installer la bibliothèque
echo "Installing path.py in $LIB_DIR..."
pip install --target "$LIB_DIR" "$PACKAGE" > "$LOG_FILE" 2>&1

if [ $? -eq 0 ]; then
  echo "Installation réussie. Logs enregistrés dans $LOG_FILE"
  echo "Configuration du PYTHONPATH..."
  export PYTHONPATH=$PYTHONPATH:$(pwd)/$LIB_DIR
  echo "Exécution du script Python..."
  python3 my_program.py
else
  echo "Échec de l'installation. Consultez $LOG_FILE pour plus d'informations."
fi
