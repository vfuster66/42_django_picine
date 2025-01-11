#!/bin/sh

# Définir des couleurs pour une meilleure lisibilité
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Fonction pour tester le script
test_script() {
    echo "\nTest case: $1"
    echo "Input: $2"
    result=$(../ex00/myawesomescript.sh "$2")
    echo "Output: $result"
    if [ $? -eq 0 ]; then
        echo "${GREEN}Status: OK${NC}"
    else
        echo "${RED}Status: FAILED${NC}"
    fi
}

# En-tête
echo "=== Testing myawesomescript.sh ==="

# Test 1: URL valide (exemple du sujet)
test_script "Valid URL (sujet example)" "bit.ly/1O72s3U"

# Test 2: URL invalide
test_script "Invalid URL" "bit.ly/invalid"

# Test 3: URL malformée
test_script "Malformed URL" "not_a_url"

# Test 4: Sans argument
../ex00/myawesomescript.sh
echo "Test without arguments completed"

# Test 5: URL https
test_script "HTTPS URL" "https://bit.ly/1O72s3U"

# Résumé
echo "\n=== Tests completed ==="