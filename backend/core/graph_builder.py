# app/core/graph_builder.py

def parse_paper_data(raw_data: list):
    """
    Parses raw paper data, extracting nodes (papers, authors) and
    edges (authorship, citations).

    Args:
        raw_data: A list of paper dictionaries from the API.

    Returns:
        A tuple containing four lists:
        - papers: A list of clean paper dictionaries.
        - authors: A list of clean, unique author dictionaries.
        - authorship_edges: A list of author-to-paper relationships.
        - citation_edges: A list of paper-to-paper citation relationships.
    """
    papers = []
    authors = []
    authorship_edges = []
    citation_edges = []
    seen_author_ids = set()

    if not raw_data:
        # Return all four lists, even if empty
        return [], [], [], []

    # Loop through each paper entry in the raw data
    for paper_item in raw_data:
        # Skip if the item is not a dictionary or doesn't contain a paperId
        if not isinstance(paper_item, dict) or 'paperId' not in paper_item:
            continue

        current_paper_id = paper_item['paperId']

        # Add paper details to the papers list
        papers.append({
            'id': current_paper_id,
            'title': paper_item.get('title', 'No Title Provided')
        })

        # Process Authors and create Authorship Edges 
        paper_authors = paper_item.get('authors', [])
        for author_details in paper_authors:
            # This logic is now CORRECTLY INDENTED inside the loop
            if not isinstance(author_details, dict) or 'authorId' not in author_details:
                continue

            author_id = author_details['authorId']

            # Create the link between the author and the current paper
            authorship_edges.append({
                'source': author_id,
                'target': current_paper_id
            })

            # Only add the author to the main list if they are new
            if author_id not in seen_author_ids:
                seen_author_ids.add(author_id)
                authors.append({
                    'id': author_id,
                    'name': author_details.get('name', 'No Name Provided')
                })

        # Process Citations and create Citation Edges 
        paper_citations = paper_item.get('citations', [])
        for citation_details in paper_citations:
            if not isinstance(citation_details, dict) or 'paperId' not in citation_details:
                continue
            
            cited_paper_id = citation_details['paperId']

            # Create the link from the current paper to the paper it cites
            citation_edges.append({
                'source': current_paper_id,
                'target': cited_paper_id
            })

    # Return all four lists
    return papers, authors, authorship_edges, citation_edges