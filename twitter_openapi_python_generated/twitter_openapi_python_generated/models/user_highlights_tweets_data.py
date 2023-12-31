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
from twitter_openapi_python_generated.models.user_highlights_tweets_user import UserHighlightsTweetsUser

class UserHighlightsTweetsData(BaseModel):
    """
    UserHighlightsTweetsData
    """
    user: UserHighlightsTweetsUser = Field(...)
    __properties = ["user"]

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
    def from_json(cls, json_str: str) -> UserHighlightsTweetsData:
        """Create an instance of UserHighlightsTweetsData from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of user
        if self.user:
            _dict['user'] = self.user.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> UserHighlightsTweetsData:
        """Create an instance of UserHighlightsTweetsData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return UserHighlightsTweetsData.parse_obj(obj)

        _obj = UserHighlightsTweetsData.parse_obj({
            "user": UserHighlightsTweetsUser.from_dict(obj.get("user")) if obj.get("user") is not None else None
        })
        return _obj


