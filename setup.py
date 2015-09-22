try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

__version__ = "1.0"
__description__ = ""
__long_description__ = ""
__license__ = ""

entry_points = {}

setup(
    name='catalog',
    version=__version__,
    author='Ross Jones',
    author_email='ross@servercode.co.uk',
    license=__license__,
    url='http://github.com/rossjones/catalog',
    description=__description__,
    keywords='data packaging component tool server',
    long_description=__long_description__,
    zip_safe=False,
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=[],
    include_package_data=True,
    package_data={'catalog': []},
    message_extractors={},
    entry_points=entry_points,
    install_requires=[
        "flask==0.10.1",
        "flask-classy==0.6.10",
        "flask-pymongo==0.3.1",
        "flask-login==0.3.0",
        "flask-wtf==0.12"
    ]
)
