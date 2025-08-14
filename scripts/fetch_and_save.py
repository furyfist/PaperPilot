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
    papers, authors, authorship_edges, citation_edges = parse_paper_data(data.get('data', []))


    if data and data.get('data'):
        # Save the processed papers
        with open('data_store/processed_papers.json', 'w') as f:
            json.dump(papers, f, indent=4)

        # Save the processed authors
        with open('data_store/processed_authors.json', 'w') as f:
            json.dump(authors, f, indent=4)
        # Save the edges 
        with open('data_store/authorship_edges.json', 'w') as f:
            json.dump(authorship_edges, f, indent=4)
            
        with open('data_store/citation_edges.json', 'w') as f:
            json.dump(citation_edges, f, indent=4)
        

        print(f"--> Found {len(authorship_edges)} authorship links and {len(citation_edges)} citation links.")
        print("--> All processed data has been saved to the 'data_store' directory.")
    else:
        print("failed to fetch or no papers found")

if __name__ == "__main__":
    main()