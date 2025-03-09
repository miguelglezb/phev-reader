import os
import sys

# Add the project's root directory to sys.path
sys.path.insert(0, os.path.abspath(".."))

# Project information
project = 'My Project'
copyright = '2025, My Name'
author = 'My Name'
release = '1.0'

# General configuration
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
]

templates_path = ['_templates']
exclude_patterns = []

autodoc_mock_imports = []  # Add any modules that shouldn't be imported

# HTML output options
html_theme = 'sphinx_rtd_theme'
html_static_path = []

def setup(app):
    app.add_css_file('custom.css')  # Optional: Add custom CSS styling
