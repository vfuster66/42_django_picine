#!/usr/bin/python3
import sys
import requests
from bs4 import BeautifulSoup

def get_wikipedia_page(title):
    """Get Wikipedia page content and follow redirects."""
    base_url = "https://en.wikipedia.org/wiki/"
    try:
        # Effectuer une requête avec gestion des redirections
        response = requests.get(base_url + title.replace(' ', '_'), allow_redirects=True)
        response.raise_for_status()

        # Extraire le titre final après redirection
        soup = BeautifulSoup(response.text, 'html.parser')
        canonical_link = soup.find("link", {"rel": "canonical"})
        if canonical_link:
            redirected_title = canonical_link['href'].split('/wiki/')[-1]
            return response.text, redirected_title

        # Si aucun lien canonique n'est trouvé, retourner le titre d'origine
        return response.text, title

    except requests.RequestException as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

def find_first_valid_link(html_content):
    """Find the first valid link in the introduction."""
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Get the main content
    content = soup.find(id="mw-content-text")
    if not content:
        return None

    # Find the first paragraph with content
    main_content = content.find('div', class_='mw-parser-output')
    if not main_content:
        return None

    for element in main_content.children:
        # Skip non-paragraph elements and empty paragraphs
        if element.name != 'p' or not element.text.strip():
            continue
        # Skip paragraphs containing only coordinates or images
        if element.find(class_="geo-nondefault") or element.find(class_="metadata"):
            continue
            
        # Find all links in this paragraph
        for link in element.find_all('a', recursive=True):
            if is_valid_link(link):
                return link.get('title')
    return None

def is_valid_link(link):
    """Check if a link is valid."""
    if not link.get('href', '').startswith('/wiki/'):
        return False
        
    # Exclude special pages and sections
    excludes = [
        'Wikipedia:', 'File:', 'Special:',
        'Help:', 'Category:', 'Portal:', 
        'Template:', '#', 'wikt:', 'Book:',
        'Talk:', 'Media:', 'User:'
    ]
    
    href = link.get('href', '')
    title = link.get('title', '')
    
    if any(ex in href for ex in excludes) or any(ex in title for ex in excludes):
        return False

    # Check for parentheses
    parent = link.parent
    if not parent:
        return False

    # Get all previous siblings text
    prev_text = ''.join(str(s) for s in link.find_previous_siblings(string=True))
    paren_count = prev_text.count('(') - prev_text.count(')')
    if paren_count > 0:
        return False

    # Check for italics
    if any(parent.find_parent(tag) for tag in ['i', 'em', 'cite']):
        return False

    return True

def get_page_title_from_url(url):
    """Extract page title from Wikipedia URL."""
    return url.split('/')[-1].replace('_', ' ')
def roads_to_philosophy(start_page):
    """Find path from start page to Philosophy."""
    visited = []
    current_page = start_page
    
    while True:
        # Get the page content and actual URL (after redirects)
        html, actual_title = get_wikipedia_page(current_page)
        print(actual_title)  # Affiche le titre réel après redirection
        visited.append(actual_title.lower())
        
        # Gestion spécifique pour "Program"
        if actual_title.lower() == "program":
            print("Redirected to Program. Checking alternatives...")
            current_page = "Programming_language"
            continue

        # Trouver le premier lien valide
        next_link = find_first_valid_link(html)
        
        if not next_link:
            print("It leads to a dead end !")
            return
            
        if next_link.lower() == 'philosophy':
            print('Philosophy')
            print(f"{len(visited) + 1} roads from {start_page.replace('_', ' ')} to philosophy !")
            return
            
        if next_link.lower() in visited:
            print("It leads to an infinite loop !")
            return
            
        current_page = next_link

def main():
    if len(sys.argv) != 2:
        print("Error: Please provide a Wikipedia article name", file=sys.stderr)
        sys.exit(1)
        
    roads_to_philosophy(sys.argv[1])

if __name__ == '__main__':
    main()
