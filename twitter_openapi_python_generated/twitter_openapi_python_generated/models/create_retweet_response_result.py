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
from twitter_openapi_python_generated.models.create_retweet import CreateRetweet

class CreateRetweetResponseResult(BaseModel):
    """
    CreateRetweetResponseResult
    """
    retweet_results: CreateRetweet = Field(...)
    __properties = ["retweet_results"]

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
    def from_json(cls, json_str: str) -> CreateRetweetResponseResult:
        """Create an instance of CreateRetweetResponseResult from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of retweet_results
        if self.retweet_results:
            _dict['retweet_results'] = self.retweet_results.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CreateRetweetResponseResult:
        """Create an instance of CreateRetweetResponseResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CreateRetweetResponseResult.parse_obj(obj)

        _obj = CreateRetweetResponseResult.parse_obj({
            "retweet_results": CreateRetweet.from_dict(obj.get("retweet_results")) if obj.get("retweet_results") is not None else None
        })
        return _obj


