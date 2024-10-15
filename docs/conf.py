# conf.py

# Add any Sphinx extension module names here, as strings.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',  # For Google style docstrings if needed
    'sphinx.ext.viewcode'   # To include links to source code
]

# Optionally, set the default role to make references to Python objects easier
default_role = 'py:obj'

# If you want to include the __init__ method docstrings
autoclass_content = 'both'
