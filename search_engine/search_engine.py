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


def search(docs, search_world):
    search_results = []
    keys = []
    term = re.findall(r'\w+', search_world)
    search_world_lower = ''.join(term).lower()
    for doc in docs:
        relevance = 0
        for token in doc['text'].split():
            term = re.findall(r'\w+', token)
            result = ''.join(term).lower()
            if result == search_world_lower:
                relevance += 1
        if relevance > 0:
            search_results.append({'key': doc['id'], 'relevance': relevance})
    search_results = quickSort(search_results, 'relevance', 'desc')
    for result in search_results:
        keys.append(result['key'])
    return keys
