from setuptools import setup, find_packages
VERSION = '0.0.1'
DESCRIPTION = 'A simple linux ricing tool.'

# Setting up
setup(
    name="niagara",
    version=VERSION,
    author="kavulox",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=['argparse'],
    keywords=['python'],
)
