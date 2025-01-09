import re

def search(docs, search_world):
    keys = []
    term = re.findall(r'\w+', search_world)
    search_world_lower = ''.join(term).lower()
    for doc in docs:
        for token in doc['text'].split():
            term = re.findall(r'\w+', token)
            result = ''.join(term).lower()
            if ( result == search_world_lower and doc['id'] not in keys ) :
                keys.append(doc['id'])
    return keys
