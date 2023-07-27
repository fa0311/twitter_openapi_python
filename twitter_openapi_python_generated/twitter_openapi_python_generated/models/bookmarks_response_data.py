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



from pydantic import BaseModel, Field
from twitter_openapi_python_generated.models.bookmarks_timeline import BookmarksTimeline

class BookmarksResponseData(BaseModel):
    """
    BookmarksResponseData
    """
    bookmark_timeline_v2: BookmarksTimeline = Field(...)
    __properties = ["bookmark_timeline_v2"]

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
    def from_json(cls, json_str: str) -> BookmarksResponseData:
        """Create an instance of BookmarksResponseData from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of bookmark_timeline_v2
        if self.bookmark_timeline_v2:
            _dict['bookmark_timeline_v2'] = self.bookmark_timeline_v2.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> BookmarksResponseData:
        """Create an instance of BookmarksResponseData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return BookmarksResponseData.parse_obj(obj)

        _obj = BookmarksResponseData.parse_obj({
            "bookmark_timeline_v2": BookmarksTimeline.from_dict(obj.get("bookmark_timeline_v2")) if obj.get("bookmark_timeline_v2") is not None else None
        })
        return _obj


