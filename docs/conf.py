#!/usr/bin/env python3
import os
import sys
import sphinx_rtd_theme

# find the vix module
sys.path.insert(0, os.path.abspath('..'))
from vix import __version__

extensions = [
    'sphinx.ext.autodoc',
]

source_suffix = ['.rst']

master_doc = 'index'

# General information about the project.
project = 'vix'
copyright = '2018, Naim A.'
author = 'Naim A.'
version = __version__
language = 'en'

todo_include_todos = True

autoclass_content = 'class'
autodoc_member_order = 'bysource'

html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_theme_options = {
    'display_version': True,
    'analytics_id': 'UA-11289087-19',
}

html_show_sourcelink = False
htmlhelp_basename = 'vixdoc'
