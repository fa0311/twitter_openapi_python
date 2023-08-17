# twitter_openapi_python

Typed Twitter scrapers by Pydantic.

## Table of Contents

This repository contains two packages.

- [twitter_openapi_python](./twitter_openapi_python) Package for human-friendly Python
- [twitter_openapi_python_generated](./twitter_openapi_python_generated) Python package automatically generated from [twitter-openapi](https://github.com/fa0311/twitter-openapi) by OpenAPI generator

```mermaid
graph LR
  A[twitter-openapi]--Auto Generated-->B[twitter_openapi_python_generated]
  B--Simplified handling-->C[twitter_openapi_python]
```

---

## twitter_openapi_python

Learn more about people-friendly Python packages here.
[twitter_openapi_python/README.md](./twitter_openapi_python/README.md)

## twitter_openapi_python_generated

> Note! twitter-openapi-python-generated is a package for advanced users who are familiar with Twitter's API. In general, [twitter-openapi-python](./twitter-openapi-python) should be used!

Build

```shell
git clone https://github.com/fa0311/twitter_openapi_python.git
cd twitter_openapi_python_generated
```

```shell
python -V # Python 3.10.8
openapi-generator-cli version # 7.0.0 beta
```

```shell
openapi-generator-cli generate -g python -c tools/openapi-generator-config.yaml
```

Setup

```shell
pip install twitter-openapi-python-generated
```

Usage

[twitter_openapi_python_generated/README.md](./twitter_openapi_python_generated/README.md)
