import json
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__),'..'))

from app.data.semantic_scholar import fetch_papers_by_query

def main():
    search_query = "carbon capture technologies"
    print(f"--> Running script to fetch papers for : '{search_query}'")

    data = fetch_papers_by_query(search_query, limit=20)

    if data and data.get('data'):
        output_path = 'data_store/raw_papers.json'
        with open(output_path, 'w') as f:
            json.dump(data['data'], f, indent=4)
        print(f"--> Succesfully fetched {len(data['data'])} papers")
        print(f"--> Raw data saved to '{output_path}'")
    else:
        print("failed to fetch or no papers found")

if __name__ == "__main__":
    main()