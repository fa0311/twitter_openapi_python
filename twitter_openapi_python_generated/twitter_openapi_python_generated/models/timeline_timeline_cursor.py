# coding: utf-8

"""
    Twitter OpenAPI

    Twitter OpenAPI(Swagger) specification  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Contact: yuki@yuki0311.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictStr, validator
from twitter_openapi_python_generated.models.content_entry_type import ContentEntryType
from twitter_openapi_python_generated.models.type_name import TypeName

class TimelineTimelineCursor(BaseModel):
    """
    TimelineTimelineCursor
    """
    typename: TypeName = Field(..., alias="__typename")
    cursor_type: StrictStr = Field(..., alias="cursorType")
    entry_type: Optional[ContentEntryType] = Field(None, alias="entryType")
    item_type: Optional[ContentEntryType] = Field(None, alias="itemType")
    value: StrictStr = Field(...)
    __properties = ["__typename", "cursorType", "entryType", "itemType", "value"]

    @validator('cursor_type')
    def cursor_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('Top', 'Bottom', 'ShowMore', 'ShowMoreThreads', 'Gap'):
            raise ValueError("must be one of enum values ('Top', 'Bottom', 'ShowMore', 'ShowMoreThreads', 'Gap')")
        return value

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
    def from_json(cls, json_str: str) -> TimelineTimelineCursor:
        """Create an instance of TimelineTimelineCursor from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TimelineTimelineCursor:
        """Create an instance of TimelineTimelineCursor from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TimelineTimelineCursor.parse_obj(obj)

        _obj = TimelineTimelineCursor.parse_obj({
            "typename": obj.get("__typename"),
            "cursor_type": obj.get("cursorType"),
            "entry_type": obj.get("entryType"),
            "item_type": obj.get("itemType"),
            "value": obj.get("value")
        })
        return _obj


