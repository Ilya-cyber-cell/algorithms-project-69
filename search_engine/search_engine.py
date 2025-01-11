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


def search(docs:dict, search_pattern:str):
    search_results = []
    keys = []
    search_worlds = search_pattern.split()
    for i, search_world in enumerate(search_worlds):
        term = re.findall(r'\w+', search_world)
        search_worlds[i] = ''.join(term).lower()

    for doc in docs:
        relevance = 0
        word_matches = 0
        for search_world in search_worlds:
            word_matched = False
            for token in doc['text'].split():
                term = re.findall(r'\w+', token)
                result = ''.join(term).lower()
                if result == search_world:
                    relevance += 1
                    word_matched =True
            if word_matched:
                word_matches = +1
        if relevance > 0:
            search_results.append({'key': doc['id'], 'relevance': relevance, 'word_matches': word_matches})
    if len(search_results) > 0:
        search_results = quickSort(search_results, 'word_matches', 'desc')
        old_nuber = search_results[0]['word_matches']
        temp_dict = []
        for result in search_results:
            if result['word_matches'] != old_nuber:
                temp_dict = quickSort(temp_dict, 'relevance', 'desc')
                for tem_result in temp_dict:
                     keys.append(tem_result['key'])
                temp_dict = [result]
                old_nuber = result['word_matches']
            else:
                temp_dict.append(result)
        if len(temp_dict) > 0:
            temp_dict = quickSort(temp_dict, 'relevance', 'desc')
            for tem_result in temp_dict:
                keys.append(tem_result['key'])
#    for result in search_results:
#        keys.append(result['key'])
    return keys
