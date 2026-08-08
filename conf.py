# Configuration file for the Sphinx documentation builder.
# Kaliss Clients Documentation

import os
import sys

project = 'Kaliss Clients Documentation'
copyright = '2026, Kaliss Technologies'
author = 'Kaliss Core Banking Team'
release = '2.0'

# General configuration
extensions = [
    'myst_parser',
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'fr'

# Source suffix
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# HTML output configuration
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

html_theme_options = {
    'titles_only': False,
    'style_nav_header_background': '#1a365d',
    'collapse_navigation': False,
    'sticky_navigation': True,
    'includehidden': True,
}

myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "fieldlist",
]

# LaTeX / PDF export configuration
latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '11pt',
    'preamble': r'''
        \usepackage{microtype}
    ''',
}

latex_documents = [
    ('index', 'Kaliss_Clients_Documentation.tex', 'Kaliss Clients Documentation',
     'Kaliss Core Banking Team', 'manual'),
]

