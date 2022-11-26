from setuptools import setup, find_packages
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()
setup(
    name = 'niagara',
    version = '0.0.0.7',
    author = 'kavulox',
    license = 'AGPL-3.0',
    description = 'A simple ricing tool for Linux systems.',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = 'https://github.com/ArtixLabs/Niagara',
    py_modules = ['niagara'],
    packages = find_packages(),
    install_requires = [requirements],
    python_requires='>=3.9',
    classifiers=[
        "Programming Language :: Python :: 3.9"
    ],
    entry_points = '''
        [console_scripts]
        niagara=niagara.__main__:run
    '''
)
