import pkg_resources

from . import models
from . import controllers

# Update the readme when you change this
pkg_resources.require("""
py3o.template==0.10.0
py3o.formats==0.3
py3o.types==0.1.1
""")
