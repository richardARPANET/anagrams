from __future__ import absolute_import, unicode_literals

from multiprocessing.pool import ThreadPool

import pytest

from anagrams import get_anagrams


class TestGetAnagrams(object):

    WORD_AND_EXPECTED_ANAGRAMS = [
        ('plates', ['palest', 'pastel', 'petals', 'plates', 'staple']),
        ('eat', ['ate', 'eat', 'tea']),
        ('NOT_IN_DICT', []),
        (None, []),
    ]

    @pytest.mark.parametrize(
        'word, expected_anagrams',
        WORD_AND_EXPECTED_ANAGRAMS
    )
    def test_returns_anagrams_in_dictionary(self, word, expected_anagrams):
        assert get_anagrams(word) == expected_anagrams, word

    @pytest.mark.parametrize('word, expected_anagrams', [
        ('Aaron', ['Aaron']),
        ('aaron', []),
    ])
    def test_returns_empty_list_for_anagrams_not_matching_case(
        self, word, expected_anagrams
    ):
        assert get_anagrams(word) == expected_anagrams, word

    def test_returns_anagrams_when_threaded(self):
        words = [i[0] for i in self.WORD_AND_EXPECTED_ANAGRAMS]
        expected_anagrams = [i[1] for i in self.WORD_AND_EXPECTED_ANAGRAMS]

        pool = ThreadPool(5)
        results = pool.map(get_anagrams, words)

        for idx, result_anagrams in enumerate(results):
            assert result_anagrams == expected_anagrams[idx]

        pool.close()
        pool.join()
