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



from pydantic import BaseModel, Field
from twitter_openapi_python_generated.models.media_size import MediaSize

class MediaSizes(BaseModel):
    """
    MediaSizes
    """
    large: MediaSize = Field(...)
    medium: MediaSize = Field(...)
    small: MediaSize = Field(...)
    thumb: MediaSize = Field(...)
    __properties = ["large", "medium", "small", "thumb"]

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
    def from_json(cls, json_str: str) -> MediaSizes:
        """Create an instance of MediaSizes from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of large
        if self.large:
            _dict['large'] = self.large.to_dict()
        # override the default output from pydantic by calling `to_dict()` of medium
        if self.medium:
            _dict['medium'] = self.medium.to_dict()
        # override the default output from pydantic by calling `to_dict()` of small
        if self.small:
            _dict['small'] = self.small.to_dict()
        # override the default output from pydantic by calling `to_dict()` of thumb
        if self.thumb:
            _dict['thumb'] = self.thumb.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MediaSizes:
        """Create an instance of MediaSizes from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return MediaSizes.parse_obj(obj)

        _obj = MediaSizes.parse_obj({
            "large": MediaSize.from_dict(obj.get("large")) if obj.get("large") is not None else None,
            "medium": MediaSize.from_dict(obj.get("medium")) if obj.get("medium") is not None else None,
            "small": MediaSize.from_dict(obj.get("small")) if obj.get("small") is not None else None,
            "thumb": MediaSize.from_dict(obj.get("thumb")) if obj.get("thumb") is not None else None
        })
        return _obj


