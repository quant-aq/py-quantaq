"""
"""
__version__ = "0.3.0"

try:
    from setuptools import setup
except:
    from distutils.core import setup

setup(
    name="quantaq",
    version=__version__,
    description="Python wrapper for the QuantAQ RESTful API",
    keywords=["QuantAQ", "Air Quality"],
    author="David H Hagan",
    author_email="david.hagan@quant-aq.com",
    url="https://github.com/quant-aq/py-quantaq",
    license="MIT",
    packages=["quantaq"],
    test_suite="tests",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Operating System :: OS Independent',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Scientific/Engineering :: Atmospheric Science',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
