from pydantic import BaseModel
from typing import Union, Optional, Generic, TypeVar, Literal


T = TypeVar("T")


class RES(BaseModel, Generic[T]):
    code: int = 0
    msg: str = ""
    data: Optional[T] = None


class InputData(BaseModel):
    smiles: str

