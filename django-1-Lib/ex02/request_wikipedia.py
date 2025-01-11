#!/usr/bin/python3
import sys
import requests
import json
import dewiki

def get_wikipedia_content(search_term):
    """
    Get content from Wikipedia API for a given search term.
    """
    # API endpoint
    api_url = "https://en.wikipedia.org/w/api.php"
    
    # First, search for the page
    search_params = {
        "action": "query",
        "format": "json",
        "list": "search",
        "srsearch": search_term,
        "utf8": 1
    }

    try:
        search_response = requests.get(api_url, params=search_params)
        search_response.raise_for_status()
        search_data = search_response.json()
        
        # Check if we found any results
        search_results = search_data.get("query", {}).get("search", [])
        if not search_results:
            return None

        # Get the title of the first result
        page_title = search_results[0]["title"]

        # Now get the content using the exact title
        content_params = {
            "action": "query",
            "format": "json",
            "titles": page_title,
            "prop": "extracts",
            "explaintext": True,
        }

        content_response = requests.get(api_url, params=content_params)
        content_response.raise_for_status()
        content_data = content_response.json()

        # Extract the content
        pages = content_data["query"]["pages"]
        page = next(iter(pages.values()))

        # Get the text content
        content = page.get("extract", "")
        if not content:
            return None

        # Remove wiki markup using dewiki
        clean_content = dewiki.from_string(content)
        return clean_content

    except requests.RequestException as e:
        print(f"Error: Unable to connect to Wikipedia API: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

def create_output_file(search_term, content):
    """
    Create a .wiki file with the provided content.
    """
    # Format filename: replace spaces with underscores and add .wiki extension
    filename = search_term.replace(" ", "_") + ".wiki"
    
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
    except IOError as e:
        print(f"Error: Unable to write to file {filename}: {e}", file=sys.stderr)
        sys.exit(1)

def main():
    # Check if search term is provided
    if len(sys.argv) != 2:
        print("Error: Please provide a search term", file=sys.stderr)
        sys.exit(1)

    search_term = sys.argv[1]
    
    # Get content from Wikipedia
    content = get_wikipedia_content(search_term)
    
    if content is None:
        print("Error: No Wikipedia page found for this search term", file=sys.stderr)
        sys.exit(1)
    
    # Create output file
    create_output_file(search_term, content)

if __name__ == "__main__":
    main()