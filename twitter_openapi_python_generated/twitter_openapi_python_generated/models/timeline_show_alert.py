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


from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr, conlist, validator
from twitter_openapi_python_generated.models.instruction_type import InstructionType
from twitter_openapi_python_generated.models.timeline_show_alert_rich_text import TimelineShowAlertRichText
from twitter_openapi_python_generated.models.user_results import UserResults

class TimelineShowAlert(BaseModel):
    """
    TimelineShowAlert
    """
    alert_type: Optional[StrictStr] = Field(None, alias="alertType")
    color_config: Optional[Dict[str, Any]] = Field(None, alias="colorConfig")
    display_duration_ms: Optional[StrictInt] = Field(None, alias="displayDurationMs")
    display_location: Optional[StrictStr] = Field(None, alias="displayLocation")
    icon_display_info: Optional[Dict[str, Any]] = Field(None, alias="iconDisplayInfo")
    rich_text: TimelineShowAlertRichText = Field(..., alias="richText")
    trigger_delay_ms: Optional[StrictInt] = Field(None, alias="triggerDelayMs")
    type: InstructionType = Field(...)
    users_results: conlist(UserResults) = Field(..., alias="usersResults")
    __properties = ["alertType", "colorConfig", "displayDurationMs", "displayLocation", "iconDisplayInfo", "richText", "triggerDelayMs", "type", "usersResults"]

    @validator('alert_type')
    def alert_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('NewTweets'):
            raise ValueError("must be one of enum values ('NewTweets')")
        return value

    @validator('display_location')
    def display_location_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Top'):
            raise ValueError("must be one of enum values ('Top')")
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
    def from_json(cls, json_str: str) -> TimelineShowAlert:
        """Create an instance of TimelineShowAlert from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of rich_text
        if self.rich_text:
            _dict['richText'] = self.rich_text.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in users_results (list)
        _items = []
        if self.users_results:
            for _item in self.users_results:
                if _item:
                    _items.append(_item.to_dict())
            _dict['usersResults'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TimelineShowAlert:
        """Create an instance of TimelineShowAlert from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TimelineShowAlert.parse_obj(obj)

        _obj = TimelineShowAlert.parse_obj({
            "alert_type": obj.get("alertType"),
            "color_config": obj.get("colorConfig"),
            "display_duration_ms": obj.get("displayDurationMs"),
            "display_location": obj.get("displayLocation"),
            "icon_display_info": obj.get("iconDisplayInfo"),
            "rich_text": TimelineShowAlertRichText.from_dict(obj.get("richText")) if obj.get("richText") is not None else None,
            "trigger_delay_ms": obj.get("triggerDelayMs"),
            "type": obj.get("type"),
            "users_results": [UserResults.from_dict(_item) for _item in obj.get("usersResults")] if obj.get("usersResults") is not None else None
        })
        return _obj


