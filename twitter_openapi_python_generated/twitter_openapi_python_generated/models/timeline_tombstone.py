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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from twitter_openapi_python_generated.models.content_item_type import ContentItemType
from twitter_openapi_python_generated.models.tombstone_info import TombstoneInfo
from twitter_openapi_python_generated.models.type_name import TypeName
from typing import Optional, Set
from typing_extensions import Self

class TimelineTombstone(BaseModel):
    """
    TimelineTombstone
    """ # noqa: E501
    typename: Optional[TypeName] = Field(default=None, alias="__typename")
    item_type: Optional[ContentItemType] = Field(default=None, alias="itemType")
    tombstone_display_type: Optional[StrictStr] = Field(default=None, alias="tombstoneDisplayType")
    tombstone_info: Optional[TombstoneInfo] = Field(default=None, alias="tombstoneInfo")
    __properties: ClassVar[List[str]] = ["__typename", "itemType", "tombstoneDisplayType", "tombstoneInfo"]

    @field_validator('tombstone_display_type')
    def tombstone_display_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Inline']):
            raise ValueError("must be one of enum values ('Inline')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of TimelineTombstone from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of tombstone_info
        if self.tombstone_info:
            _dict['tombstoneInfo'] = self.tombstone_info.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TimelineTombstone from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "__typename": obj.get("__typename"),
            "itemType": obj.get("itemType"),
            "tombstoneDisplayType": obj.get("tombstoneDisplayType"),
            "tombstoneInfo": TombstoneInfo.from_dict(obj["tombstoneInfo"]) if obj.get("tombstoneInfo") is not None else None
        })
        return _obj


