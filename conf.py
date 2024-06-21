# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

# project = 'DIOS-ViTO'
# copyright = '2024, HMS-IAC'
# author = 'HMS-IAC'
# release = 'v0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx_book_theme',
    'sphinx_design',
    'myst_parser',
    'sphinx_tags',
]

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

templates_path = ['_templates']
exclude_patterns = [] 





# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_book_theme"
html_static_path = ['_static']

html_css_files = [
    'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css',
    'css/custom.css'
]


# Add the path to the _templates directory
templates_path = ["_templates"]


html_js_files = [
    '_static/js/custom.js',  # Path to your custom JS file
]

html_title = "Bio-Image Analysis on O2"


html_theme_options = {
    "repository_url": "http://github.com/HMS-IAC/DIOS",
    "use_repository_button": True,
    "footer_start": ["footer.html"],
    "logo": {
      "image_light": "assets/logos/light.webp",
      "image_dark": "assets/logos/dark.webp",
   }
}

# Override the footer template
html_context = {
    "footer": "_templates/footer.html",
}

# Configure sphinx-tags (optional, here are some example settings)
tags_create_tags = True
tags_intro_text = ""
tags_page_title = "Tags Index"
tags_create_badges = True
tags_badge_colors = {"*":"dark"}
tags_extension = ["md", "rst"]