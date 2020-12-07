from ..tokenizer_exceptions import BASE_EXCEPTIONS
from ...symbols import ORTH, NORM
from ...util import update_exc

_exc = {}

for token in ["᾽Απ'", "᾽ΑΠ'", "ἀφ'", "᾽Αφ", "ἀπὸ"]:
    _exc[token] = [{ORTH: token, NORM: "από"}]

for token in ["᾽Αλλ'", "᾽"]:
    _exc[token] = [{ORTH: token, NORM: "ἀλλά"}]

for token in ["παρ'", "Παρ'", "ΠΑΡ'", "παρὰ", "παρ"]:
    _exc[token] = [{ORTH: token, NORM: "παρά"}]

for token in ["καθ'", "Καθ'","κατ'", "Κατ'", "κατὰ"]:
    _exc[token] = [{ORTH: token, NORM: "κατά"}]

for token in ["Επ'", "επ'", "εφ'", "Εφ'"]:
    _exc[token] = [{ORTH: token, NORM: "επί"}]

for token in ["Δι'", "δι'"]:
    _exc[token] = [{ORTH: token, NORM: "δια"}]


for token in ["υπ'", "Υπ'"]:
    _exc[token] = [{ORTH: token, NORM: "υπό"}]

for token in ["Μετ'", "ΜΕΤ'", "'μετ"]:
    _exc[token] = [{ORTH: token, NORM: "μετά"}]

for token in ["Μ'", "μ'"]:
    _exc[token] = [{ORTH: token, NORM: "με"}]

for token in ["Σ'", "σ'"]:
    _exc[token] = [{ORTH: token, NORM: "σε"}]

for token in ["Τ'", "τ'"]:
    _exc[token] = [{ORTH: token, NORM: "τε"}]

'''
_other_exc = {
    "καὶ": [{ORTH: "καὶ", NORM: "καί"}],
}

_exc.update(_other_exc)
'''


TOKENIZER_EXCEPTIONS = update_exc(BASE_EXCEPTIONS, _exc)
