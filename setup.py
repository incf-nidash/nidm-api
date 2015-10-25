from setuptools.command.install import install as _install
from setuptools import setup, find_packages
import codecs
import sys
import os

# We will run script to download data after install
def _post_install(dir):
    from subprocess import call
    call([sys.executable, 'update_queries.py'],
         cwd=os.path.join(dir, 'nidm','script'))

class install(_install):
    def run(self):
        _install.run(self)
        self.execute(_post_install, (self.install_lib,),
                     msg="Downloading nidm-queries...")


here = os.path.abspath(os.path.dirname(__file__))

# Get the long description from the relevant file
with codecs.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    # Application name:
    name="nidm",

    # Version number (initial):
    version="1.0.0",

    # Application author details:
    author="NIDM Working Group",
    author_email="vsochat@stanford.edu",

    # Packages
    packages=find_packages(),

    # Data files
    include_package_data=True,
    zip_safe=False,

    # Details
    url="https://github.com/incf-nidash/nidm-api",

    license="LICENSE.txt",
    description="Python module and application for running a REST API server to perform queries and visualize graphs with NIDM results, experiments, and workflows.",
    long_description=long_description,
    keywords='nidm neuroscience',

    install_requires = ['numpy','Flask','gitpython'],

    entry_points = {
        'console_scripts': [
            'nidm=nidm.scripts:main',
        ],
    },

    # This will install an updated version of nidm-queries in home
    cmdclass={'install': install},
)
