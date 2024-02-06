from typing import TypeVar

from pydantic import BaseModel as PydanticBaseModel

T = TypeVar("T")


class BaseModel(PydanticBaseModel):
    model_config = {"arbitrary_types_allowed": True}
