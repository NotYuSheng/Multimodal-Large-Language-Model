# Configuration file for the Sphinx documentation builder.

# -- Project information -----------------------------------------------------

project = 'Multimodal-Large-Language-Model'
author = 'Yu Sheng'
release = '1.1.0'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'recommonmark',  # Enable this if you use Markdown
    # 'myst_parser',  # Use this if you prefer MyST-Parser for Markdown
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

html_theme = 'alabaster'  # You can choose a different theme like 'sphinx_rtd_theme'
html_static_path = ['_static']

# -- Enable Markdown support -------------------------------------------------

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# -- Additional options ------------------------------------------------------

# Example: Add custom CSS files (for styling purposes)
# html_css_files = [
#     'css/custom.css',
# ]

# Example: Include any extra files, such as robots.txt or .htaccess
# html_extra_path = ['extra']
