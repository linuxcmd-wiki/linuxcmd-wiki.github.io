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
# import sys # sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Linux 命令指北'
copyright = '2021, linuxcmd.wiki'
author = 'linuxcmd@163.com'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'zh_CN'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The name for this set of Sphinx documents.
# "<project> v<release> documentation" by default.
html_title = 'Linux 命令指北'

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'cloud'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    'googleanalytics_id': 'G-V6EVW0T7Y3',

    'max_width': '11.5in',
    'bodylineheight': '1.25em',
    'default_layout_text_size': '90%',
    'minimal_layout_text_size': '80%',

    'sidebarwidth': '1.5in',
    'sidebar_localtoc_title': '本页内容',
    'sidebar_prev_title': '上一页',
    'sidebar_next_title': '下一页',

    'headlinkcolor': '#1a4162',
    'relbarbgcolor': '#4b6ba9',
    'sectionbgcolor': '#b9cde4',
    'relbartextcolor': '#f2f2f2',
    'relbarlinkcolor': '#f2f2f2',
    'bodytrimcolor': '#d0d0d0',
    'headtextcolor': '#000000',
    'bodyfont': "'Optima', 'Lucida Grande', 'Lucida Sans Unicode', 'Geneva', 'Verdana', sans-serif",
    'headfont': "'Optima', 'Lucida Grande', 'Lucida Sans Unicode', 'Geneva', 'Verdana', sans-serif",

    'link_hover_text_color': '#1a4162',
    'link_hover_bg_color': '#d0d3d9',
    'link_hover_trim_color': '',
    'highlightcolor': '#b9cde4',

    'codebgcolor': '#f2f2f2',
    'codetextcolor': '#333333',
    'codetrimcolor': '#aacc99',
    'codevarfont': '"Andale Mono", monospace',
    'codeblockfont': '"Andale Mono", monospace',

    'linkcolor': '#4b6ba9',
    'sidebarlinkcolor': '#4b6ba9',
}

# If not None, a 'Last updated on:' timestamp is inserted at every page
# bottom, using the given strftime format.
# The empty string is equivalent to '%b %d, %Y'.
html_last_updated_fmt = ''

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_css_files = [
    'cloud-patch.css',
    'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css',
]

html_copy_source = False

html_sidebars = {
   '**': ['localtoc.html'],
}

html_show_sourcelink = False

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = "_static/logo.png"


# The name of an image file (relative to this directory) to use as a favicon of
# the docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = "_static/favicon.png"

