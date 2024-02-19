# coding: utf-8

"""
    Twitter OpenAPI

    Twitter OpenAPI(Swagger) specification

    The version of the OpenAPI document: 0.0.1
    Contact: yuki@yuki0311.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from setuptools import setup, find_packages  # noqa: H301

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools
NAME = "twitter_openapi_python_generated"
VERSION = "0.0.13"
PYTHON_REQUIRES = ">=3.7"
REQUIRES = [
    "urllib3 >= 1.25.3, < 2.1.0",
    "python-dateutil",
    "pydantic >= 2",
    "typing-extensions >= 4.7.1",
]

setup(
    name=NAME,
    version=VERSION,
    description="Twitter OpenAPI",
    author="OpenAPI Generator community",
    author_email="yuki@yuki0311.com",
    url="https://github.com/fa0311/twitter_openapi_python_generated",
    keywords=["OpenAPI", "OpenAPI-Generator", "Twitter OpenAPI"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="custom license or AGPL-3.0-or-later",
    long_description_content_type='text/markdown',
    long_description="""\
    Twitter OpenAPI(Swagger) specification
    """,  # noqa: E501
    package_data={"twitter_openapi_python_generated": ["py.typed"]},
)
