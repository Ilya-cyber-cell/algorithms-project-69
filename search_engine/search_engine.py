import re

def quickSort(items, key,direction='asc'):
    items_length = len(items)

    if items_length == 0:
        return []

    index = items_length // 2
    element = items[index]

    smaller_items = [
        items[i]
        for i in range(items_length)
            if items[i][key] < element[key] and i != index
    ]
    bigger_items = [
        items[i]
        for i in range(items_length)
        if items[i][key] >= element[key] and i != index
    ]

    sorted_smaller_items = quickSort(smaller_items, key, direction)
    sorted_bigger_items = quickSort(bigger_items, key, direction)

    if direction == 'asc':
        return [*sorted_smaller_items, element, *sorted_bigger_items]
    return [*sorted_bigger_items, element, *sorted_smaller_items]

def get_index(docs):
    index = {}
    for doc in docs:
        for token in doc['text'].split():
            term = re.findall(r'\w+', token)
            index_key = ''.join(term).lower()
            if index_key not in index:
                index[index_key] = []
            index[index_key].append(doc['id'])


    return index

def search(docs:dict, search_pattern:str):
    keys = []
    index = get_index(docs)
    search_worlds = search_pattern.split()
    for i, search_world in enumerate(search_worlds):
        term = re.findall(r'\w+', search_world)
        search_world_lower = ''.join(term).lower()
        if search_world_lower in index:
            for doc in index[search_world_lower]:
                if doc not in keys:
                    keys.append(doc)
    return keys
