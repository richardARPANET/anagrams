from __future__ import absolute_import, unicode_literals

import itertools


with open('words.txt', 'r') as f:
    WORDS = f.read().splitlines()


def get_anagrams(word):
    if not word:
        return []
    anagrams = set(''.join(perm) for perm in
                   itertools.permutations(word)).intersection(WORDS)
    return sorted(anagrams)
