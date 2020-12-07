# coding: utf-8
from __future__ import unicode_literals

from spacy.lang.grc import AncientGreek
import pytest


@pytest.fixture(scope="session")
def grc_nlp():
    return AncientGreek()


@pytest.mark.parametrize(
    "string,lemma",
    [
        ("ἄνδρα", " ἀνήρ"),
        ("μοι", " ἐγώ"),
        ("πολύτροπον", "πολύτροπονος"),
        ("ὃς", "ὃς"),
        ("πολλὰ", "πολύς"),
        ("Τροίης", "Τροία"),
    ],
)
def test_grc_lemmatizer_lookup_assigns(grc_nlp, string, lemma):
    tokens = grc_nlp(string)
    assert tokens[0].lemma_ == lemma
