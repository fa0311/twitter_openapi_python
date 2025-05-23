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
import json
import pprint
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Any, List, Optional
from twitter_openapi_python_generated.models.timeline_community import TimelineCommunity
from twitter_openapi_python_generated.models.timeline_message_prompt import TimelineMessagePrompt
from twitter_openapi_python_generated.models.timeline_notification import TimelineNotification
from twitter_openapi_python_generated.models.timeline_prompt import TimelinePrompt
from twitter_openapi_python_generated.models.timeline_timeline_cursor import TimelineTimelineCursor
from twitter_openapi_python_generated.models.timeline_tombstone import TimelineTombstone
from twitter_openapi_python_generated.models.timeline_trend import TimelineTrend
from twitter_openapi_python_generated.models.timeline_tweet import TimelineTweet
from twitter_openapi_python_generated.models.timeline_user import TimelineUser
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

ITEMCONTENTUNION_ONE_OF_SCHEMAS = ["TimelineCommunity", "TimelineMessagePrompt", "TimelineNotification", "TimelinePrompt", "TimelineTimelineCursor", "TimelineTombstone", "TimelineTrend", "TimelineTweet", "TimelineUser"]

class ItemContentUnion(BaseModel):
    """
    ItemContentUnion
    """
    # data type: TimelineTweet
    oneof_schema_1_validator: Optional[TimelineTweet] = None
    # data type: TimelineTimelineCursor
    oneof_schema_2_validator: Optional[TimelineTimelineCursor] = None
    # data type: TimelineUser
    oneof_schema_3_validator: Optional[TimelineUser] = None
    # data type: TimelinePrompt
    oneof_schema_4_validator: Optional[TimelinePrompt] = None
    # data type: TimelineMessagePrompt
    oneof_schema_5_validator: Optional[TimelineMessagePrompt] = None
    # data type: TimelineCommunity
    oneof_schema_6_validator: Optional[TimelineCommunity] = None
    # data type: TimelineTombstone
    oneof_schema_7_validator: Optional[TimelineTombstone] = None
    # data type: TimelineTrend
    oneof_schema_8_validator: Optional[TimelineTrend] = None
    # data type: TimelineNotification
    oneof_schema_9_validator: Optional[TimelineNotification] = None
    actual_instance: Optional[Union[TimelineCommunity, TimelineMessagePrompt, TimelineNotification, TimelinePrompt, TimelineTimelineCursor, TimelineTombstone, TimelineTrend, TimelineTweet, TimelineUser]] = None
    one_of_schemas: Set[str] = { "TimelineCommunity", "TimelineMessagePrompt", "TimelineNotification", "TimelinePrompt", "TimelineTimelineCursor", "TimelineTombstone", "TimelineTrend", "TimelineTweet", "TimelineUser" }

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
    )


    discriminator_value_class_map: Dict[str, str] = {
    }

    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = ItemContentUnion.model_construct()
        error_messages = []
        match = 0
        # validate data type: TimelineTweet
        if not isinstance(v, TimelineTweet):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TimelineTweet`")
        else:
            match += 1
        # validate data type: TimelineTimelineCursor
        if not isinstance(v, TimelineTimelineCursor):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TimelineTimelineCursor`")
        else:
            match += 1
        # validate data type: TimelineUser
        if not isinstance(v, TimelineUser):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TimelineUser`")
        else:
            match += 1
        # validate data type: TimelinePrompt
        if not isinstance(v, TimelinePrompt):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TimelinePrompt`")
        else:
            match += 1
        # validate data type: TimelineMessagePrompt
        if not isinstance(v, TimelineMessagePrompt):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TimelineMessagePrompt`")
        else:
            match += 1
        # validate data type: TimelineCommunity
        if not isinstance(v, TimelineCommunity):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TimelineCommunity`")
        else:
            match += 1
        # validate data type: TimelineTombstone
        if not isinstance(v, TimelineTombstone):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TimelineTombstone`")
        else:
            match += 1
        # validate data type: TimelineTrend
        if not isinstance(v, TimelineTrend):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TimelineTrend`")
        else:
            match += 1
        # validate data type: TimelineNotification
        if not isinstance(v, TimelineNotification):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TimelineNotification`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in ItemContentUnion with oneOf schemas: TimelineCommunity, TimelineMessagePrompt, TimelineNotification, TimelinePrompt, TimelineTimelineCursor, TimelineTombstone, TimelineTrend, TimelineTweet, TimelineUser. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in ItemContentUnion with oneOf schemas: TimelineCommunity, TimelineMessagePrompt, TimelineNotification, TimelinePrompt, TimelineTimelineCursor, TimelineTombstone, TimelineTrend, TimelineTweet, TimelineUser. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Union[str, Dict[str, Any]]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        match = 0

        # use oneOf discriminator to lookup the data type
        _data_type = json.loads(json_str).get("__typename")
        if not _data_type:
            raise ValueError("Failed to lookup data type from the field `__typename` in the input.")

        # check if data type is `TimelineCommunity`
        if _data_type == "TimelineCommunity":
            instance.actual_instance = TimelineCommunity.from_json(json_str)
            return instance

        # check if data type is `TimelineMessagePrompt`
        if _data_type == "TimelineMessagePrompt":
            instance.actual_instance = TimelineMessagePrompt.from_json(json_str)
            return instance

        # check if data type is `TimelineNotification`
        if _data_type == "TimelineNotification":
            instance.actual_instance = TimelineNotification.from_json(json_str)
            return instance

        # check if data type is `TimelinePrompt`
        if _data_type == "TimelinePrompt":
            instance.actual_instance = TimelinePrompt.from_json(json_str)
            return instance

        # check if data type is `TimelineTimelineCursor`
        if _data_type == "TimelineTimelineCursor":
            instance.actual_instance = TimelineTimelineCursor.from_json(json_str)
            return instance

        # check if data type is `TimelineTombstone`
        if _data_type == "TimelineTombstone":
            instance.actual_instance = TimelineTombstone.from_json(json_str)
            return instance

        # check if data type is `TimelineTrend`
        if _data_type == "TimelineTrend":
            instance.actual_instance = TimelineTrend.from_json(json_str)
            return instance

        # check if data type is `TimelineTweet`
        if _data_type == "TimelineTweet":
            instance.actual_instance = TimelineTweet.from_json(json_str)
            return instance

        # check if data type is `TimelineUser`
        if _data_type == "TimelineUser":
            instance.actual_instance = TimelineUser.from_json(json_str)
            return instance

        # deserialize data into TimelineTweet
        try:
            instance.actual_instance = TimelineTweet.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into TimelineTimelineCursor
        try:
            instance.actual_instance = TimelineTimelineCursor.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into TimelineUser
        try:
            instance.actual_instance = TimelineUser.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into TimelinePrompt
        try:
            instance.actual_instance = TimelinePrompt.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into TimelineMessagePrompt
        try:
            instance.actual_instance = TimelineMessagePrompt.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into TimelineCommunity
        try:
            instance.actual_instance = TimelineCommunity.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into TimelineTombstone
        try:
            instance.actual_instance = TimelineTombstone.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into TimelineTrend
        try:
            instance.actual_instance = TimelineTrend.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into TimelineNotification
        try:
            instance.actual_instance = TimelineNotification.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into ItemContentUnion with oneOf schemas: TimelineCommunity, TimelineMessagePrompt, TimelineNotification, TimelinePrompt, TimelineTimelineCursor, TimelineTombstone, TimelineTrend, TimelineTweet, TimelineUser. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into ItemContentUnion with oneOf schemas: TimelineCommunity, TimelineMessagePrompt, TimelineNotification, TimelinePrompt, TimelineTimelineCursor, TimelineTombstone, TimelineTrend, TimelineTweet, TimelineUser. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        if hasattr(self.actual_instance, "to_json") and callable(self.actual_instance.to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Optional[Union[Dict[str, Any], TimelineCommunity, TimelineMessagePrompt, TimelineNotification, TimelinePrompt, TimelineTimelineCursor, TimelineTombstone, TimelineTrend, TimelineTweet, TimelineUser]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(self.actual_instance.to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())


