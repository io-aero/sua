# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
sys.path.insert(0, os.path.abspath('../../src/'))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'SUA'
copyright = '2023, IO-Aero'
author = 'IO-Aero Team'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []
extensions.append('sphinx.ext.autodoc')
extensions.append('sphinx.ext.coverage')
extensions.append('sphinx.ext.napoleon')
extensions.append('sphinx.ext.viewcode')

# templates_path = ['_templates']
# exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_favicon = 'img/IO-Aero_Favicon.ico'
html_logo = 'img/IO-Aero_logo.png'
html_static_path = ['_static']
html_theme = 'furo'
html_theme_options = {
    "sidebar_hide_name": True,
}
