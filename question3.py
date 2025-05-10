from collections import defaultdict


def group_anagrams(words:list)->list:

    '''
    Groups anagrams together in a list

    Args:
    words (list): A list of words
    
    Returns:
    list: A list of lists where each sublist contains anagrams
    '''


    map = defaultdict(list)

    for word in words:
        sorted_word = ''.join(sorted(word))
        map[sorted_word].append(word)

        
    return list(map.values())


words = input("Enter words seperated by space: ").split()

anagram_groups = group_anagrams(words)

for group in anagram_groups:
    print(group)  