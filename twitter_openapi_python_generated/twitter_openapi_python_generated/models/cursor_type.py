# coding: utf-8

"""
    Twitter OpenAPI

    Twitter OpenAPI(Swagger) specification

    The version of the OpenAPI document: 0.0.1
    Contact: yuki@yuki0311.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class CursorType(str, Enum):
    """
    CursorType
    """

    """
    allowed enum values
    """
    TOP = 'Top'
    BOTTOM = 'Bottom'
    SHOWMORE = 'ShowMore'
    SHOWMORETHREADS = 'ShowMoreThreads'
    GAP = 'Gap'

    @classmethod
    def from_json(cls, json_str: str) -> CursorType:
        """Create an instance of CursorType from a JSON string"""
        return CursorType(json.loads(json_str))


