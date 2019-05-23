# -*- coding: utf-8 -*-

from pythainlp.corpus import download, get_corpus, get_corpus_path, read_text_corpus

__all__ = [
    "countries",
    "provinces",
    "thai_female_names",
    "thai_male_names"
    "thai_negations",
    "thai_stopwords",
    "thai_syllables",
    "thai_words",
]


_THAI_COUNTRIES = set()
_THAI_COUNTRIES_FILENAME = "countries_th.txt"

_THAI_THAILAND_PROVINCES = set()
_THAI_THAILAND_PROVINCES_FILENAME = "thailand_provinces_th.txt"

_THAI_SYLLABLES = set()
_THAI_SYLLABLES_FILENAME = "syllables_th.txt"

_THAI_WORDS = set()
_THAI_WORDS_FILENAME = "words_th.txt"

_THAI_STOPWORDS = set()
_THAI_STOPWORDS_FILENAME = "stopwords_th.txt"

_THAI_NEGATIONS = set()
_THAI_NEGATIONS_FILENAME = "negations_th.txt"

_THAI_FEMALE_NAMES = set()
_THAI_MALE_NAMES = set()


def countries() -> frozenset:
    """
    Return a frozenset of country names in Thai
    """
    global _THAI_COUNTRIES
    if not _THAI_COUNTRIES:
        _THAI_COUNTRIES = get_corpus(_THAI_COUNTRIES_FILENAME)

    return _THAI_COUNTRIES


def provinces() -> frozenset:
    """
    Return a frozenset of Thailand province names in Thai
    """
    global _THAI_THAILAND_PROVINCES
    if not _THAI_THAILAND_PROVINCES:
        _THAI_THAILAND_PROVINCES = get_corpus(_THAI_THAILAND_PROVINCES_FILENAME)

    return _THAI_THAILAND_PROVINCES


def thai_syllables() -> frozenset:
    """
    Return a frozenset of Thai syllables
    """
    global _THAI_SYLLABLES
    if not _THAI_SYLLABLES:
        _THAI_SYLLABLES = get_corpus(_THAI_SYLLABLES_FILENAME)

    return _THAI_SYLLABLES


def thai_words() -> frozenset:
    """
    Return a frozenset of Thai words
    """
    global _THAI_WORDS
    if not _THAI_WORDS:
        _THAI_WORDS = get_corpus(_THAI_WORDS_FILENAME)

    return _THAI_WORDS


def thai_stopwords() -> frozenset:
    """
    Return a frozenset of Thai stopwords
    """
    global _THAI_STOPWORDS
    if not _THAI_STOPWORDS:
        _THAI_STOPWORDS = get_corpus(_THAI_STOPWORDS_FILENAME)

    return _THAI_STOPWORDS


def thai_negations() -> frozenset:
    """
    Return a frozenset of Thai negation words
    """
    global _THAI_NEGATIONS
    if not _THAI_NEGATIONS:
        _THAI_NEGATIONS = get_corpus(_THAI_NEGATIONS_FILENAME)

    return _THAI_NEGATIONS


def _get_thai_names(corpus_name: str) -> frozenset:
    download(corpus_name)
    names = read_text_corpus(get_corpus_path(corpus_name))

    return frozenset(names)


def thai_female_names() -> frozenset:
    """
    Return a frozenset of Thai female names
    """
    global _THAI_FEMALE_NAMES
    corpus_name = "female_names_th"
    if not _THAI_FEMALE_NAMES:
        _THAI_FEMALE_NAMES = _get_thai_names(corpus_name)

    return _THAI_FEMALE_NAMES


def thai_male_names() -> frozenset:
    """
    Return a frozenset of Thai male names
    """
    global _THAI_MALE_NAMES
    corpus_name = "male_names_th"
    if not _THAI_MALE_NAMES:
        _THAI_MALE_NAMES = _get_thai_names(corpus_name)

    return _THAI_MALE_NAMES
