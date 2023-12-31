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





class InstructionType(str, Enum):
    """
    InstructionType
    """

    """
    allowed enum values
    """
    TIMELINEADDENTRIES = 'TimelineAddEntries'
    TIMELINEADDTOMODULE = 'TimelineAddToModule'
    TIMELINECLEARCACHE = 'TimelineClearCache'
    TIMELINEPINENTRY = 'TimelinePinEntry'
    TIMELINEREPLACEENTRY = 'TimelineReplaceEntry'
    TIMELINESHOWALERT = 'TimelineShowAlert'
    TIMELINETERMINATETIMELINE = 'TimelineTerminateTimeline'
    TIMELINESHOWCOVER = 'TimelineShowCover'

    @classmethod
    def from_json(cls, json_str: str) -> InstructionType:
        """Create an instance of InstructionType from a JSON string"""
        return InstructionType(json.loads(json_str))


