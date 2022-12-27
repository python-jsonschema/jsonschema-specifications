import importlib.metadata
import re

project = "jsonschema-specifications"
author = "Julian Berman"
copyright = f"2022, {author}"

release = importlib.metadata.version("jsonschema-specifications")
version = release.partition("-")[0]

language = "en"
default_role = "any"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.coverage",
    "sphinx.ext.doctest",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx_copybutton",
    "sphinxcontrib.spelling",
    "sphinxext.opengraph",
]

pygments_style = "lovelace"
pygments_dark_style = "one-dark"

html_theme = "furo"

# = Builders =


def entire_domain(host):
    return r"http.?://" + re.escape(host) + r"($|/.*)"


linkcheck_ignore = [
    entire_domain("img.shields.io"),
    "https://github.com/python-jsonschema/jsonschema/actions",
    "https://github.com/python-jsonschema/jsonschema/workflows/CI/badge.svg",
]

# = Extensions =

# -- autosectionlabel --

autosectionlabel_prefix_document = True

# -- intersphinx --

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "referencing": ("https://referencing.readthedocs.io/en/latest/", None),
}

# -- sphinxcontrib-spelling --

spelling_word_list_filename = "spelling-wordlist.txt"
spelling_show_suggestions = True
