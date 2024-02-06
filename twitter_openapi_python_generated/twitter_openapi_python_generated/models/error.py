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


from typing import Any, ClassVar, Dict, List
from pydantic import BaseModel, StrictInt, StrictStr
from twitter_openapi_python_generated.models.error_extensions import ErrorExtensions
from twitter_openapi_python_generated.models.location import Location
from twitter_openapi_python_generated.models.tracing import Tracing
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class Error(BaseModel):
    """
    Error
    """ # noqa: E501
    code: StrictInt
    extensions: ErrorExtensions
    kind: StrictStr
    locations: List[Location]
    message: StrictStr
    name: StrictStr
    path: List[StrictStr]
    retry_after: StrictInt
    source: StrictStr
    tracing: Tracing
    __properties: ClassVar[List[str]] = ["code", "extensions", "kind", "locations", "message", "name", "path", "retry_after", "source", "tracing"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of Error from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of extensions
        if self.extensions:
            _dict['extensions'] = self.extensions.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in locations (list)
        _items = []
        if self.locations:
            for _item in self.locations:
                if _item:
                    _items.append(_item.to_dict())
            _dict['locations'] = _items
        # override the default output from pydantic by calling `to_dict()` of tracing
        if self.tracing:
            _dict['tracing'] = self.tracing.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of Error from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "code": obj.get("code"),
            "extensions": ErrorExtensions.from_dict(obj.get("extensions")) if obj.get("extensions") is not None else None,
            "kind": obj.get("kind"),
            "locations": [Location.from_dict(_item) for _item in obj.get("locations")] if obj.get("locations") is not None else None,
            "message": obj.get("message"),
            "name": obj.get("name"),
            "path": obj.get("path"),
            "retry_after": obj.get("retry_after"),
            "source": obj.get("source"),
            "tracing": Tracing.from_dict(obj.get("tracing")) if obj.get("tracing") is not None else None
        })
        return _obj


