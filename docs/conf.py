#!/usr/bin/env python
import sphinx_rtd_theme

from sprockets.clients.memcached import version_info, __version__

needs_sphinx = '1.0'
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.inheritance_diagram',
    'sphinxcontrib.httpdomain',
]
templates_path = []
source_suffix = '.rst'
master_doc = 'index'
project = 'sprockets.clients.memcached'
copyright = '2014, AWeber Communications'
version = '.'.join(__version__.split('.')[0:1])
release = __version__
if len(version_info) > 3:
    release += '-{0}'.format(str(v) for v in version_info[3:])
exclude_patterns = []
pygments_style = 'sphinx'
html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
intersphinx_mapping = {
    'python': ('https://docs.python.org/2/', None)
}