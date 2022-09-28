# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'SIMILE GeoNode'
copyright = '2022, Juan Fernando Toro Herrera'
author = 'Juan Fernando Toro Herrera'

# The full version, including alpha/beta/rc tags
release = 'MIT'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "myst_nb"
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_book_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Update Left Menu Image
html_logo = "_static/img/assev_simile.png"
# Update Left Menu Title
html_title = "SIMILE - Collaborative Data Sharing Platform"

# Add link to GitHub Repo
html_theme_options = {
    "repository_url": "https://github.com/JFToro192/docsGeoNodeSIMILE",
    "use_repository_button": True,
    "home_page_in_toc": True
}

# Main Sidebar
# html_sidebars = {
#     "posts/*": ["posts.md"]
# }

# Secondary Sidebar
# html_theme_options = {
#     "toc_title": "{your-title}"
# }

# https://sphinx-book-theme.readthedocs.io/en/latest/customize/sidebar-secondary.html
# https://myst-parser.readthedocs.io/en/latest/syntax/syntax.html