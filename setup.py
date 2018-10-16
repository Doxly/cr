try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description' : 'Cube rube',
    'author' : 'Pichugin Viacheslav',
    'url' : 'https://github.com/Doxly',
    'download_url' : 'https://github.com/Doxly',
    'author_email' : 'pva33@mail.ru',
    'version' : '0.1',
    'install_requeries' : ['nose'],
    'packages' : ['CR'],
    'scripts' : [],
    'name' : 'cr'
}

setup(**config)