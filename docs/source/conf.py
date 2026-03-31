import os
import sys
sys.path.insert(0, os.path.abspath("../.."))
import pyrogram

project = "MyPyro"
copyright = "2026, ErRickow"
author = "ErRickow"
release = pyrogram.__version__

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.intersphinx",
]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
}

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "furo"
html_static_path = ["_static"]

# Furo theme options
html_theme_options = {
    "light_css_variables": {
        "color-brand-primary": "#336791",
        "color-brand-content": "#336791",
    },
}
