"""Setup script of zinnia-disqus"""
from setuptools import setup
from setuptools import find_packages

import zinnia_disqus

setup(
    name='zinnia-disqus',
    version='1.0',

    description='Implements Disqus comments and disables the default comment system while preserving trackbacks and pingbacks',
    long_description=open('README.rst').read(),
    keywords='django, zinnia, url, disqus',

    author=zinnia_disqus.__author__,
    author_email=zinnia_disqus.__email__,
    url=zinnia_disqus.__url__,

    classifiers=[
        'Framework :: Django',
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: BSD License',
        'Topic :: Software Development :: Libraries :: Python Modules'],

    license=zinnia_disqus.__license__,
    include_package_data=True,
    zip_safe=False,
    install_requires=['django-disqus']
)
