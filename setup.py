from setuptools import setup

with open('README.md','r') as fh:
    long_description = fh.read()

setup(
    name = 'SCoinAPI',
    version = '1.1.7',
    description = "The light package for the SCU blockchain in the IOTA system.",
    py_modules = ['SCoinAPI'],
    package_dir = {'' : 'SCoinAPI'},
    long_description = long_description,
    long_description_content_type='text/markdown',
    install_requires = ["requests>=2.23.0",],
    classifiers=(
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    url = 'https://github.com/sefx5ever/SCoinAPI.git',
    author = 'Wyne Tan',
    author_email = 'sefx5ever@gmail.com',
)

# 創建 whl 檔 【python setup.py bdist_wheel】