# coding: utf-8

"""
    Twitter OpenAPI

    Twitter OpenAPI(Swagger) specification

    The version of the OpenAPI document: 0.0.1
    Contact: yuki@yuki0311.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List
from pydantic import BaseModel, Field, conlist
from twitter_openapi_python_generated.models.instruction_type import InstructionType
from twitter_openapi_python_generated.models.timeline_add_entry import TimelineAddEntry

class TimelineAddEntries(BaseModel):
    """
    TimelineAddEntries
    """
    entries: conlist(TimelineAddEntry) = Field(...)
    type: InstructionType = Field(...)
    __properties = ["entries", "type"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> TimelineAddEntries:
        """Create an instance of TimelineAddEntries from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in entries (list)
        _items = []
        if self.entries:
            for _item in self.entries:
                if _item:
                    _items.append(_item.to_dict())
            _dict['entries'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TimelineAddEntries:
        """Create an instance of TimelineAddEntries from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TimelineAddEntries.parse_obj(obj)

        _obj = TimelineAddEntries.parse_obj({
            "entries": [TimelineAddEntry.from_dict(_item) for _item in obj.get("entries")] if obj.get("entries") is not None else None,
            "type": obj.get("type")
        })
        return _obj


