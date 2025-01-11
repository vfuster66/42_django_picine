#!/bin/bash

# Vérifie si le script est exécuté directement ou sourcé
if [["${BASH_SOURCE[0]}" == "${0}" ]]; then
    echo "❗❗❗ This script must be sourced to activate the virtual environment."
    echo "Please run: . ./my_script.sh"
    exit 1
fi

# Nom du VirtualEnv
VENV_NAME="django_venv"

echo "Creating virtual environment: $VENV_NAME"
python3 -m venv $VENV_NAME

echo "Activating virtual environment"
source $VENV_NAME/bin/activate

echo "Installing dependencies from requirement.txt"
pip install --upgrade pip
pip install -r requirement.txt

echo "✅ Virtual environment '$VENV_NAME' is now activated."
echo "To deactivate, use the 'deactivate' command."
