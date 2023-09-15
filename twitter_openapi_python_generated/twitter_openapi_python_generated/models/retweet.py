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



from pydantic import BaseModel, Field, constr, validator
from twitter_openapi_python_generated.models.retweet_legacy import RetweetLegacy

class Retweet(BaseModel):
    """
    Retweet
    """
    legacy: RetweetLegacy = Field(...)
    rest_id: constr(strict=True) = Field(...)
    __properties = ["legacy", "rest_id"]

    @validator('rest_id')
    def rest_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[0-9]+$", value):
            raise ValueError(r"must validate the regular expression /^[0-9]+$/")
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
    def from_json(cls, json_str: str) -> Retweet:
        """Create an instance of Retweet from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of legacy
        if self.legacy:
            _dict['legacy'] = self.legacy.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Retweet:
        """Create an instance of Retweet from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Retweet.parse_obj(obj)

        _obj = Retweet.parse_obj({
            "legacy": RetweetLegacy.from_dict(obj.get("legacy")) if obj.get("legacy") is not None else None,
            "rest_id": obj.get("rest_id")
        })
        return _obj


