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
import os
import re
import sys

sys.path.insert(0, os.path.abspath('..'))
sys.path.append(os.path.abspath('extensions'))


# -- Project information -----------------------------------------------------

project = 'asyncdagpi'
copyright = '2020, Daggy1234'
author = 'Daggy1234'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.coverage',
              'sphinx.ext.napoleon', 'sphinx.ext.viewcode', 'sphinx.ext.extlinks',
              'details', 'builder', 'sphinx.ext.intersphinx', 'sphinxcontrib_trio'
              ]

rst_prolog = """
.. |coro| replace:: This function is a |coroutine_link|_.
.. |maybecoro| replace:: This function *could be a* |coroutine_link|_.
.. |coroutine_link| replace:: *coroutine*
.. _coroutine_link: https://docs.python.org/3/library/asyncio-task.html#coroutine
"""

autodoc_member_order = 'bysource'

ntersphinx_mapping = {
  'py': ('https://docs.python.org/3', None),
  'aio': ('https://docs.aiohttp.org/en/stable/', None),
}

extlinks = {
    'issue': ('https://github.com/Daggy1234/asyncdagpi/issues/%s', 'issue '),
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
source_suffix = '.rst'
master_doc = 'index'
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
# pygments_style = 'sphinx'

version = ''
with open('../asyncdagpi/__init__.py') as f:
    version = re.search(r"^__version__:\s*str\s*=\s*['\"]([^'\"]*)['\"]", f.read(), re.MULTILINE).group(1)
# The full version, including alpha/beta/rc tags.
release = version
# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_experimental_html5_writer = True
html_theme = 'furo'
html_sidebars = {'**': ['localtoc.html', 'searchbox.html', 'globaltoc.html']}
# html_theme = 'alabaster'

pygments_style = "vs"
pygments_dark_style = "one-dark"

html_theme_options = {
    "light_logo": "dagpib.png",
    "dark_logo": "dagpi.png",
    'description': 'Powerful Asynchronous wrapper for https://dagpi.xyz',
    'navbar_site_name': "asyncdagpi",
    'navbar_links': [
        ("Dagpi", "https://dagpi.xyz", True),
        ("Github", "https://github.com/Daggy1234/dagpi", True),

    ],
    'external_links': [
        ("Dagpi", "https://dagpi.xyz"),
        ("Github", "https://github.com/Daggy1234/dagpi"),

    ],

}
html_static_path = ['_static']
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".

