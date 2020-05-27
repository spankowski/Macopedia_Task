try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
 'description': 'My Project',
 'author': 'Szymon Pankowski',
 'url': 'szymonpankowski.com',
 'download_url': 'Where to download it.',
 'author_email': 'szymon.p.pankowski@gmail.com',
 'version': '0.1',
 'install_requires': ['nose2'],
 'packages': ['Macopedia'],
 'scripts': [],
 'name': 'projectname'
}

setup(**config)
