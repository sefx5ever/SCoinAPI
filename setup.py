from setuptools import setup

with open('README.md','r') as fh:
    long_description = fh.read()

setup(
    name = 'SCoinAPI',
    version = '1.0',
    description = "The light package for the SCU blockchain in the IOTA system.",
    py_modules = ['centralbank','bank','retailer'],
    package_dir = {'' : 'src'},
    long_description = long_description,
    long_description_content_type='text/markdown',
    install_requires = ["requests>=2.23.0",],
    url = 'https://github.com/sefx5ever/SCoinAPI',
    author = 'Wyne Tan',
    author_email = 'sefx5ever@gmail.com',
)
