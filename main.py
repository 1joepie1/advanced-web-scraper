import json
from src.scraper_logic import get_soup, parse_books

def main():
    print("--- Scraper Ready ---")
    url = input("URL (Leave empty for test site): ").strip()
    
    if not url:
        url = "https://books.toscrape.com/"
    
    soup = get_soup(url)
    data = parse_books(soup)

    if data:
        print(f"\nFound {len(data)} items:\n")
        for i in data[:5]: 
            print(f"- {i['title']} | {i['price']}")
        
        save = input("\nSave to results.json? (y/n): ").lower()
        if save == 'y':
            with open("results.json", "w") as f:
                json.dump(data, f, indent=4)
            print("File saved.")
    else:
        print("Error: Could not fetch data.")

if __name__ == "__main__":
    main()
