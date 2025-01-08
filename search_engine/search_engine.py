
def search(docs, search_world):
    keys = []
    for doc in docs:
        for word in doc['text'].split():
            if ( word == search_world and doc['id'] not in keys ) :
                keys.append(doc['id'])
    return keys
