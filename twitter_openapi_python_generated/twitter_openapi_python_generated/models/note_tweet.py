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



from pydantic import BaseModel, Field, StrictBool
from twitter_openapi_python_generated.models.note_tweet_result import NoteTweetResult

class NoteTweet(BaseModel):
    """
    NoteTweet
    """
    is_expandable: StrictBool = Field(...)
    note_tweet_results: NoteTweetResult = Field(...)
    __properties = ["is_expandable", "note_tweet_results"]

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
    def from_json(cls, json_str: str) -> NoteTweet:
        """Create an instance of NoteTweet from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of note_tweet_results
        if self.note_tweet_results:
            _dict['note_tweet_results'] = self.note_tweet_results.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> NoteTweet:
        """Create an instance of NoteTweet from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return NoteTweet.parse_obj(obj)

        _obj = NoteTweet.parse_obj({
            "is_expandable": obj.get("is_expandable"),
            "note_tweet_results": NoteTweetResult.from_dict(obj.get("note_tweet_results")) if obj.get("note_tweet_results") is not None else None
        })
        return _obj


