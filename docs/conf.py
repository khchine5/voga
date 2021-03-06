# -*- coding: utf-8 -*-
#
# This file is execfile()d with the current directory set to its containing dir.
#
# The contents of this file are pickled, so don't put values in the namespace
# that aren't pickleable (module imports are okay, they're removed automatically).
#
# All configuration values have a default; values that are commented out
# serve to show the default.

intersphinx_mapping = {}
# from importlib import import_module
# for n in 'atelier lino_cosi'.split():
#     m = import_module(n)
#     # p = Path(m.__file__).parent().parent()
#     n = n.replace('_', "")
#     intersphinx_mapping[n] = (m.intersphinx_urls['docs'], None)

from atelier.sphinxconf import interproject
interproject.configure(globals(), 'atelier lino_cosi')

extlinks = {}
extensions = []

from lino.sphinxcontrib import configure
# configure(globals(), 'lino_voga.projects.roger.settings.doctests')
# configure(globals(), 'lino.projects.std.settings_test')
configure(globals())

extensions += ['atelier.sphinxconf.blog']
extensions += ['lino.sphinxcontrib.base']
# extensions += ['lino.sphinxcontrib.actordoc']
extensions += ['lino.sphinxcontrib.logo']
# extensions += ['sphinxcontrib.taglist']

# from django.conf import settings


# If your extensions are in another directory, add it here. If the directory
# is relative to the documentation root, use os.path.abspath to make it
# absolute, like shown here.
#sys.path.append(os.path.abspath('.'))

# General configuration
# ---------------------

primary_domain = 'py'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['.templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'Lino Voga'
copyright = '2012-2018 Luc Saffre'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The full version, including alpha/beta/rc tags.
import lino_voga
release = lino_voga.__version__

# The short X.Y version.
version = '.'.join(release.split('.')[:2])


# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
language = 'en'

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of documents that shouldn't be included in the build.
#unused_docs = []

# List of directories, relative to source directory, that shouldn't be searched
# for source files.
exclude_patterns = [
    '.build/*',
    'include/*',
]

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'


# Options for HTML output
# -----------------------

# The style sheet to use for HTML and HTML Help pages. A file of that name
# must exist either in Sphinx' static/ path, or in one of the custom paths
# given in html_static_path.
# html_style = 'default.css'

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = u"OpenTIM Developer's Reference"

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#~ html_logo = 'logo.jpg'
# html_logo = 'logo.png'

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
# html_favicon = 'favicon.ico'

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%b %d, %Y'
#~ last_updated = True

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#~ html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
# http://sphinx.pocoo.org/latest/config.html#confval-html_sidebars
html_sidebars = {
   '**': ['globaltoc.html', 'searchbox.html', 'links.html'],
}


# Additional templates that should be rendered to pages, maps page names to
# template names.
#~ html_additional_pages = {
    #~ '*': 'links.html',
#~ }


# If false, no module index is generated.
html_use_modindex = False

# If false, no index is generated.
html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, the reST sources are included in the HTML build as _sources/<name>.
html_copy_source = False

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
html_use_opensearch = ''
#~ html_use_opensearch = 'http://lino.saffre-rumma.net'

# If nonempty, this is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = ''

# Output file base name for HTML help builder.
htmlhelp_basename = 'voga'


#language="de"

#~ show_source = True

#~ srcref_base_uri="http://code.google.com/lino"
#~ srcref_base_uri="http://code.google.com/p/lino/source/browse/#hg" 



#~ nitpicky = True # use -n in Makefile instead

# http://sphinx.pocoo.org/theming.html
# html_theme = "classic"
# html_theme_options = dict(collapsiblesidebar=True,externalrefs=True)

#~ todo_include_todos = True


extlinks = dict()
extlinks.update(ticket=('http://bugs.saffre-rumma.net/tickets/Ticket/%s', '#'))



