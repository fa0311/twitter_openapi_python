from pydantic import BaseModel as PydanticBaseModel
from pydantic.generics import GenericModel as PydanticGenericModel


class BaseModel(PydanticBaseModel):
    class Config:
        arbitrary_types_allowed = True


class GenericModel(PydanticGenericModel):
    class Config:
        arbitrary_types_allowed = True
