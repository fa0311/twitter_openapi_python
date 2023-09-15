# coding: utf-8

from setuptools import find_packages, setup

NAME = "twitter_openapi_python"
VERSION = "0.0.4"
PYTHON_REQUIRES = ">=3.7"
REQUIRES = [
    "twitter_openapi_python_generated >= 0.0.1, < 1",
    "pydantic >= 1.10.5, < 2",
]

setup(
    name=NAME,
    version=VERSION,
    description="Twitter OpenAPI",
    author="fa0311",
    author_email="yuki@yuki0311.com",
    url="https://github.com/fa0311/twitter_openapi_python",
    keywords=["OpenAPI", "OpenAPI-Generator", "Twitter OpenAPI"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="GNU Affero General Public License v3.",
    long_description_content_type="text/markdown",
    long_description="""\
        Twitter scraping with data validation by pydantic.
    """,  # noqa: E501
    package_data={"twitter_openapi_python": ["py.typed"]},
)
