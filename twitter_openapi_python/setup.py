# coding: utf-8

import re

from setuptools import find_packages, setup

NAME = "twitter_openapi_python"
VERSION = "0.0.41"
PYTHON_REQUIRES = ">=3.7"
REQUIRES = [
    "twitter_openapi_python_generated == 0.0.33",
    "pydantic >= 2.6",
    "urllib3 >= 2.1.0, < 3.0.0",
    "xclienttransaction >= 1.0.0, < 2.0.0"
]
GITHUB_RAW_URL = (
    "https://raw.githubusercontent.com/fa0311/twitter_openapi_python/refs/heads/master/twitter_openapi_python/"
)


def image_replace(text: str, url: str):
    return re.sub(
        r"!\[(.*?)\]\((.*?)\)",
        r"![\1](" + url + r"\2)",
        text,
    )


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
    license="proprietary or AGPL-3.0-or-later",
    long_description_content_type="text/markdown",
    long_description=image_replace(open("README.md").read(), GITHUB_RAW_URL),
    package_data={"twitter_openapi_python": ["py.typed"]},
)
