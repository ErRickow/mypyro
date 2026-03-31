import os
import sys
sys.path.insert(0, os.path.abspath("../.."))

project = "MyPyro"
copyright = "2026, ErRickow"
author = "ErRickow"
import pyrogram
release = pyrogram.__version__

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx_rtd_theme",
]

templates_path = ["_templates"]
exclude_patterns = []

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
