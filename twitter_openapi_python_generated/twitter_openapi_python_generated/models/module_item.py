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



from pydantic import BaseModel, Field, constr, validator
from twitter_openapi_python_generated.models.module_entry import ModuleEntry

class ModuleItem(BaseModel):
    """
    ModuleItem
    """
    entry_id: constr(strict=True) = Field(..., alias="entryId")
    item: ModuleEntry = Field(...)
    __properties = ["entryId", "item"]

    @validator('entry_id')
    def entry_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[a-z\-]+[0-9]+$", value):
            raise ValueError(r"must validate the regular expression /^[a-z\-]+[0-9]+$/")
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
    def from_json(cls, json_str: str) -> ModuleItem:
        """Create an instance of ModuleItem from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of item
        if self.item:
            _dict['item'] = self.item.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ModuleItem:
        """Create an instance of ModuleItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ModuleItem.parse_obj(obj)

        _obj = ModuleItem.parse_obj({
            "entry_id": obj.get("entryId"),
            "item": ModuleEntry.from_dict(obj.get("item")) if obj.get("item") is not None else None
        })
        return _obj


