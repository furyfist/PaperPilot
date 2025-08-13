import requests

def fetch_papers_by_query(query: str, limit: int = 10, fields: str = 'title,authors,citations.title'):
    """
    Fetches Papers from the Sementic Scholar API and return the raw data O_o
    """

    search_url = "https://api.semanticscholar.org/graph/v1/paper/search"
    params = {'query' : query, 'limit' : limit, 'fields': fields}

    try:
        response = requests.get(search_url, params=params)
        response.raise_for_status()
        return response.json()
    
    except requests.exceptions.RequestException as e:
        print(f"--> An error occured fething data: {e}")
        return None