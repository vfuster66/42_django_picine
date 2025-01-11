#!/bin/sh

# Vérifie qu'un argument est fourni
if [ $# -ne 1 ]; then
    echo "Usage: $0 <bit.ly_url>"
    exit 1
fi

# Récupère l'URL de redirection directement à partir du header Location
curl -sI "$1" | grep -i "^location:" | cut -d' ' -f2-