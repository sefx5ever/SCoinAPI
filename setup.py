from setuptools import setup

with open('README.md','r') as fh:
    long_description = fh.read()

setup(
    name = 'SCoinAPI',
    version = '1.0',
    description = long_description,
    py_modules = ['centralbank','bank','retailer'],
    package_dir = {'' : 'src'},
    classifiers = [
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    install = ["requests>=2.23.0",],
    url = 'https://github.com/sefx5ever/scoinAPI',
    author = 'Wyne Tan',
    author_email = 'sefx5ever@gmail.com',
)