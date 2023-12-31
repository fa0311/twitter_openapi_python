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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictInt, conlist
from twitter_openapi_python_generated.models.media_video_info_variant import MediaVideoInfoVariant

class MediaVideoInfo(BaseModel):
    """
    MediaVideoInfo
    """
    aspect_ratio: conlist(StrictInt) = Field(...)
    duration_millis: Optional[StrictInt] = None
    variants: conlist(MediaVideoInfoVariant) = Field(...)
    __properties = ["aspect_ratio", "duration_millis", "variants"]

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
    def from_json(cls, json_str: str) -> MediaVideoInfo:
        """Create an instance of MediaVideoInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in variants (list)
        _items = []
        if self.variants:
            for _item in self.variants:
                if _item:
                    _items.append(_item.to_dict())
            _dict['variants'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MediaVideoInfo:
        """Create an instance of MediaVideoInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return MediaVideoInfo.parse_obj(obj)

        _obj = MediaVideoInfo.parse_obj({
            "aspect_ratio": obj.get("aspect_ratio"),
            "duration_millis": obj.get("duration_millis"),
            "variants": [MediaVideoInfoVariant.from_dict(_item) for _item in obj.get("variants")] if obj.get("variants") is not None else None
        })
        return _obj


