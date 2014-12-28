try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'iDibo an online voting system',
    'author': 'Oluyemisi Satope',
    'url': '',
    'download_url': '',
    'author_email': 'satopeoladayo@gmail.com',
    'version': '0.1',
    'install_requires': [],
    'packages': [],
    'scripts': [],
    'name': 'iDibo'
}

setup(**config)