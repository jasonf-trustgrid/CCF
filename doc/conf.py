# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the Apache 2.0 License.
# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
import subprocess
import pathlib

from docutils import nodes

sys.path.insert(0, os.path.abspath("../python"))


# -- Project information -----------------------------------------------------

project = u"CCF"
copyright = u"2018, Microsoft Research"  # pylint: disable=redefined-builtin
author = u"Microsoft Research"

# The short X.Y version
version = u""
# The full version, including alpha/beta/rc tags
release = u""


# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.todo",
    "sphinx.ext.mathjax",
    "sphinx.ext.ifconfig",
    "sphinx.ext.viewcode",
    "breathe",
    "sphinxcontrib.mermaid",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.githubpages",
    "sphinx_multiversion",
    "sphinx_copybutton",
    "sphinx.ext.autodoc",
    "sphinxcontrib.openapi",
    "sphinx_panels"
]

autosectionlabel_prefix_document = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = ".rst"

# The master toctree document.
master_doc = "index"

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path .
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "solarizeddark"


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "pydata_sphinx_theme"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
html_sidebars = {
    "**": ["sidebar-nav-bs.html", "search-field.html"]
}

html_css_files = [
    "css/custom.css",
]


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = "CCFdoc"


# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',
    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',
    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',
    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, "CCF.tex", u"CCF Documentation", u"Microsoft Research", "manual")
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [(master_doc, "ccf", u"CCF Documentation", [author], 1)]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        master_doc,
        "CCF",
        u"CCF Documentation",
        author,
        "CCF",
        "One line description of project.",
        "Miscellaneous",
    )
]


# -- Extension configuration -------------------------------------------------

# -- Options for todo extension ----------------------------------------------

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

# -- Breathe configuration

# Setup the breathe extension
breathe_projects = {"CCF": "../doxygen/xml"}
breathe_default_project = "CCF"

# Set up multiversion extension

# Build tags from ccf-1.0.0
smv_tag_whitelist = r"^ccf-(1\.\d+\.\d+|2.*)$"
smv_branch_whitelist = r"^main$"
smv_remote_whitelist = None
smv_outputdir_format = "{ref.name}"

# PyData theme options

html_logo = "_static/ccf.svg"
html_favicon = "_static/favicon.ico"

html_theme_options = {
    "github_url": "https://github.com/Microsoft/CCF",
    "use_edit_page_button": True,
}

html_context = {
    "github_user": "Microsoft",
    "github_repo": "CCF",
    "github_version": "main",
    "doc_path": "doc/",
}

# Python autodoc options
autodoc_default_options = {
    "member-order": "bysource",
}

# sphinxcontrib.spelling options
spelling_show_suggestions = True
spelling_lang = "en_UK"
tokenizer_lang = "en_UK"
spelling_word_list_filename = ["spelling_wordlist.txt"]

# sphinx_js options (CCF 0.19.1 - 0.19.3)
# From 0.19.4 onwards, typedoc is used to generate HTML.
# Note that sphinx_js is enabled dynamically in setup().
js_language = "typescript"
js_source_path = "../src/js"
jsdoc_config_path = "../src/js/tsconfig.json"

# sphinxcontrib-mermaid options
mermaid_init_js = """mermaid.initialize({startOnLoad:true});

// Remove height from all mermaid diagrams
window.addEventListener(
  'load',
  function() {
    let nodes = document.querySelectorAll('.mermaid');
    for (let i = 0; i < nodes.length; i++) {
      const element = nodes[i];
      const svg = element.firstChild;
      svg.removeAttribute('height');
    }
  },
  false
);"""

def typedoc_role(name: str, rawtext: str, text: str, lineno, inliner, options={}, content=[]):
    """
    Supported syntaxes:
    :typedoc:package:`ccf-app`
    :typedoc:module:`ccf-app/global`
    :typedoc:function:`ccf-app/crypto#wrapKey`
    :typedoc:interface:`ccf-app/endpoints/Body`
    :typedoc:class:`ccf-app/kv/TypedKvMap`
    :typedoc:classmethod:`ccf-app/kv/TypedKvMap#delete`
    :typedoc:interfacemethod:`ccf-app/endpoints/Body#json`
    :typedoc:interface:`Body <ccf-app/endpoints/Body>`
    """
    # check for custom label
    if '<' in text:
        label, text = text.split(' <')
        text = text[:-1]
    else:
        label = text
    
    # extract hash if any, has to be appended after .html later on
    text_without_hash, *hash_name = text.split('#')
    url_hash = f'#{hash_name[0].lower()}' if hash_name else ''
    
    # translate role kind into typedoc subfolder
    # and add '()' for functions/methods
    kind_name = name.replace('typedoc:', '')
    is_kind_package = False
    if kind_name == 'package':
        is_kind_package = True
    elif kind_name in ['module', 'interface']:
        kind_name += 's'
    elif kind_name == 'class':
        kind_name += 'es'
    elif kind_name == 'function':
        kind_name = 'modules'
        label += '()'
    elif kind_name == 'classmethod':
        kind_name = 'classes'
        label += '()'
    elif kind_name == 'interfacemethod':
        kind_name = 'interfaces'
        label += '()'
    else:
        raise ValueError(f'unknown typedoc kind: {kind_name}')

    # build typedoc url relative to doc root
    pkg_name, *element_path = text_without_hash.split('/')
    typedoc_path = f'js/{pkg_name}'
    if not is_kind_package:
        element_path = '.'.join(element_path).lower()
        typedoc_path += f'/{kind_name}/{element_path}.html{url_hash}'

    # construct final url relative to current page
    source = inliner.document.attributes['source']
    rel_source = source.split('/doc/', 1)[1]
    levels = rel_source.count('/')
    refuri = '../' * levels + typedoc_path

    # build docutils node
    text_node = nodes.literal(label, label, classes=['xref'])
    ref_node = nodes.reference('', '', refuri=refuri)
    ref_node += text_node
    
    return [ref_node], []


def config_inited(app, config):
    # anything that needs to access app.config goes here

    srcdir = pathlib.Path(app.srcdir)
    outdir = pathlib.Path(app.outdir)

    # typedoc (CCF 0.19.4 onwards)
    js_pkg_dir = srcdir / ".." / "js" / "ccf-app"
    js_docs_dir = outdir / "js" / "ccf-app"
    if js_pkg_dir.exists():
        # make versions.json from sphinx-multiversion available
        if app.config.smv_metadata_path:
            os.environ['SMV_METADATA_PATH'] = app.config.smv_metadata_path
            os.environ['SMV_CURRENT_VERSION'] = app.config.smv_current_version
        subprocess.run(["sed", "-i", "s/\^4.2.3/4.2.4/g", "package.json"], cwd=js_pkg_dir, check=True)
        subprocess.run(["npm", "install", "--no-package-lock", "--no-audit", "--no-fund"],
                       cwd=js_pkg_dir, check=True)
        subprocess.run(["npm", "run", "docs", "--", "--out", str(js_docs_dir)],
                       cwd=js_pkg_dir, check=True)    
        # allow to link to typedoc pages
        for kind in ['package', 'module', 'interface', 'class', 'function',
                     'interfacemethod', 'classmethod']:
            app.add_role(f'typedoc:{kind}', typedoc_role)

def setup(app):
    app.connect("config-inited", config_inited)

    srcdir = pathlib.Path(app.srcdir)

    # doxygen
    breathe_projects["CCF"] = str(srcdir / breathe_projects["CCF"])
    if not os.environ.get("SKIP_DOXYGEN"):
        subprocess.run(["doxygen"], cwd=srcdir / "..", check=True)

    # sphinx_js (CCF 0.19.1 - 0.19.3)
    global js_source_path
    global jsdoc_config_path
    js_source_path = str(srcdir / js_source_path)
    jsdoc_config_path = str(srcdir / jsdoc_config_path)
    if os.path.exists(jsdoc_config_path):
        subprocess.run(["npm", "install", "--no-package-lock", "--no-audit", "--no-fund",
                        "typescript@4.0.7", "typedoc@0.19.2"],
                       cwd=srcdir / "..", check=True)
        os.environ['PATH'] += os.pathsep + str(srcdir / ".." / "node_modules" / ".bin")
        app.setup_extension("sphinx_js")
