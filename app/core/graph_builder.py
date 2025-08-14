
def parse_paper_data(raw_data: list):
    papers = []
    authors =[]
    seen_author_ids = set()

    if not raw_data:
        return [],[]
    
    for paper_item in raw_data:

        if not isinstance(paper_item, dict) or 'paperId' not in paper_item:
            continue

        papers.append({
            'id' : paper_item['paperId'],
            'title' : paper_item.get('title', 'No title Provided')

        })

        paper_authors = paper_item.get('authors',[])
        if not paper_authors:
            continue

        for author_details in paper_authors:
            if not isinstance(author_details, dict) or 'authorId' not in author_details:
                continue

        author_id = author_details['authorId']

        if author_id not in seen_author_ids:
            seen_author_ids.add(author_id)
            authors.append({
                'id' : author_id,
                'name' : author_details.get('name', 'No name provided')
            })

    return papers, authors