import json
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__),'..'))

from app.data.semantic_scholar import fetch_papers_by_query
from app.core.graph_builder import parse_paper_data

def main():
    search_query = "carbon capture technologies"
    print(f"--> Running script to fetch papers for : '{search_query}'")

    data = fetch_papers_by_query(search_query, limit=20)
    papers, authors = parse_paper_data(data.get('data', []))


    if data and data.get('data'):
        # Save the processed papers
        with open('data_store/processed_papers.json', 'w') as f:
            json.dump(papers, f, indent=4)

        # Save the processed authors
        with open('data_store/processed_authors.json', 'w') as f:
            json.dump(authors, f, indent=4)

        print(f"--> Success! Found {len(papers)} papers and {len(authors)} unique authors.")
        print("--> Processed data saved to 'data_store/processed_papers.json' and 'data_store/processed_authors.json'")
    else:
        print("failed to fetch or no papers found")

if __name__ == "__main__":
    main()