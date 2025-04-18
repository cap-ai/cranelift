# Minimal configuration for Sphinx
import os
import sys

# Required Sphinx settings
project = 'Static Site'
copyright = '2025, Your Name'
author = 'Your Name'

# Required Sphinx stubs
extensions = []
master_doc = 'index'
language = 'en'
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# Basic theme required by Sphinx
html_theme = 'alabaster'