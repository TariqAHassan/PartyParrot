import os
from setuptools import setup, find_packages


def read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except:
        return 'Please see: https://github.com/TariqAHassan/PartyParrot.'


setup(
    name='party_parrot',
    version='0.1',
    author='Tariq A. Hassan',
    author_email='laterallattice@gmail.com',
    description='The future is parrot.',
    long_description=read('docs/README.md'),
    license='BSD',
    keywords='Party Parrot',
    url='https://github.com/TariqAHassan/PartyParrot.git',
    download_url='https://github.com/TariqAHassan/PartyParrot/archive/v0.1.tar.gz',
    packages=find_packages(),
    entry_points={
        "console_scripts": ['parrot = party_parrot.cli:main']
    },
    install_requires=['sklearn', 'pyperclip'],
    classifiers=['Development Status :: 3 - Alpha',
                 'Natural Language :: English',
                 'Intended Audience :: Science/Research',
                 'Programming Language :: Python :: 3.4',
                 'Programming Language :: Python :: 3.5',
                 'Programming Language :: Python :: 3.6',
                 'License :: OSI Approved :: BSD License'
    ],
    include_package_data=True
)
