import sys
import os

import sphinx_rtd_theme

sys.path.insert(0, os.path.abspath(".."))
sys.path.insert(0, os.path.abspath("sphinxext"))

print(sys.path)
from github_link import make_linkcode_resolve  # noqa

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
# sys.path.insert(0, os.path.abspath('.'))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.doctest",
    "sphinx.ext.intersphinx",
    "sphinx.ext.linkcode",
    # "numpydoc",
    #   'sphinx_gallery.gen_gallery',
    # "matplotlib.sphinxext.plot_directive",
]

## this is needed for some reason...
## see https://github.com/numpy/numpydoc/issues/69
# numpydoc_show_class_members = False

# pngmath / imgmath compatibility layer for different sphinx versions
import sphinx  # noqa: E402
from distutils.version import LooseVersion  # noqa: E402

if LooseVersion(sphinx.__version__) < LooseVersion("1.4"):
    extensions.append("sphinx.ext.pngmath")
else:
    extensions.append("sphinx.ext.imgmath")

autodoc_default_flags = ["members", "inherited-members", "private-members"]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# generate autosummary even if no references
autosummary_generate = True

# The suffix of source filenames.
source_suffix = ".rst"

# The encoding of source files.
# source_encoding = 'utf-8-sig'

# Generate the plots for the gallery
# plot_gallery = True

# The master toctree document.
master_doc = "index"

# General information about the project.
project = u"hummingbird"
copyright = u"2020, Microsoft"

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = "0.4.3"

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
# language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
# today = ''
# Else, today_fmt is used as the format for a strftime call.
# today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ["_build", "_templates"]

# The reST default role (used for this markup: `text`) to use for all
# documents.
# default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
# add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
# add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
# show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "default"

# Custom style
html_style = "css/hummingbird.css"

# A list of ignored prefixes for module index sorting.
# modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
# keep_warnings = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = "sphinx_rtd_theme"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    "collapse_navigation": False,
}

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

html_static_path = ["_static"]


# Output file base name for HTML help builder.
htmlhelp_basename = "hummingbirddoc"


# Example configuration for intersphinx: refer to the Python standard library.
# intersphinx configuration
intersphinx_mapping = {
    "python": ("https://docs.python.org/{.major}".format(sys.version_info), None),
    "numpy": ("https://docs.scipy.org/doc/numpy/", None),
    "scipy": ("https://docs.scipy.org/doc/scipy/reference", None),
    # "matplotlib": ("https://matplotlib.org/", None),
    "sklearn": ("http://scikit-learn.org/stable", None),
}

# sphinx-gallery configuration
# sphinx_gallery_conf = {
#    'doc_module': 'hummingbird',
#    'backreferences_dir': os.path.join('generated'),
#    'reference_url': {
#        'hummingbird': None}
# }


def setup(app):
    # a copy button to copy snippet of code from the documentation
    app.add_js_file("js/copybutton.js")
    app.add_css_file("basic.css")


# The following is used by sphinx.ext.linkcode to provide links to github
linkcode_resolve = make_linkcode_resolve(
    "hummingbird",
    "https://github.com/microsoft/" "hummingbird/blob/{revision}/hummingbird" "{package}/{path}#L{lineno}",
)
