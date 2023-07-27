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


from typing import Any, Dict, Optional
from pydantic import BaseModel, Field, StrictBool, constr, validator
from twitter_openapi_python_generated.models.tweet_card import TweetCard
from twitter_openapi_python_generated.models.tweet_edit_control import TweetEditControl
from twitter_openapi_python_generated.models.tweet_edit_prespective import TweetEditPrespective
from twitter_openapi_python_generated.models.tweet_views import TweetViews
from twitter_openapi_python_generated.models.type_name import TypeName
from twitter_openapi_python_generated.models.user_result_core import UserResultCore

class Tweet(BaseModel):
    """
    Tweet
    """
    typename: Optional[TypeName] = Field(None, alias="__typename")
    card: Optional[TweetCard] = None
    core: UserResultCore = Field(...)
    edit_control: TweetEditControl = Field(...)
    edit_prespective: Optional[TweetEditPrespective] = None
    is_translatable: StrictBool = Field(...)
    legacy: TweetLegacy = Field(...)
    quoted_status_result: Optional[ItemResult] = None
    rest_id: constr(strict=True) = Field(...)
    unmention_data: Optional[Dict[str, Any]] = None
    views: TweetViews = Field(...)
    __properties = ["__typename", "card", "core", "edit_control", "edit_prespective", "is_translatable", "legacy", "quoted_status_result", "rest_id", "unmention_data", "views"]

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
    def from_json(cls, json_str: str) -> Tweet:
        """Create an instance of Tweet from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of card
        if self.card:
            _dict['card'] = self.card.to_dict()
        # override the default output from pydantic by calling `to_dict()` of core
        if self.core:
            _dict['core'] = self.core.to_dict()
        # override the default output from pydantic by calling `to_dict()` of edit_control
        if self.edit_control:
            _dict['edit_control'] = self.edit_control.to_dict()
        # override the default output from pydantic by calling `to_dict()` of edit_prespective
        if self.edit_prespective:
            _dict['edit_prespective'] = self.edit_prespective.to_dict()
        # override the default output from pydantic by calling `to_dict()` of legacy
        if self.legacy:
            _dict['legacy'] = self.legacy.to_dict()
        # override the default output from pydantic by calling `to_dict()` of quoted_status_result
        if self.quoted_status_result:
            _dict['quoted_status_result'] = self.quoted_status_result.to_dict()
        # override the default output from pydantic by calling `to_dict()` of views
        if self.views:
            _dict['views'] = self.views.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Tweet:
        """Create an instance of Tweet from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Tweet.parse_obj(obj)

        _obj = Tweet.parse_obj({
            "typename": obj.get("__typename"),
            "card": TweetCard.from_dict(obj.get("card")) if obj.get("card") is not None else None,
            "core": UserResultCore.from_dict(obj.get("core")) if obj.get("core") is not None else None,
            "edit_control": TweetEditControl.from_dict(obj.get("edit_control")) if obj.get("edit_control") is not None else None,
            "edit_prespective": TweetEditPrespective.from_dict(obj.get("edit_prespective")) if obj.get("edit_prespective") is not None else None,
            "is_translatable": obj.get("is_translatable") if obj.get("is_translatable") is not None else False,
            "legacy": TweetLegacy.from_dict(obj.get("legacy")) if obj.get("legacy") is not None else None,
            "quoted_status_result": ItemResult.from_dict(obj.get("quoted_status_result")) if obj.get("quoted_status_result") is not None else None,
            "rest_id": obj.get("rest_id"),
            "unmention_data": obj.get("unmention_data"),
            "views": TweetViews.from_dict(obj.get("views")) if obj.get("views") is not None else None
        })
        return _obj


