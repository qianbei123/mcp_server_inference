from structs.base import InputData, RES
from typing import Literal, Any
from pydantic import BaseModel


class InputPK(InputData):
    dose: float  # mg/kg
    route: Literal["p.o.", "i.v."]

class Curve(BaseModel):
    times:list[float] # hours
    concentrations:list[float] # ng/mL

class Params(BaseModel):
    Vd: float # Volume of distribution
    Cmax: float # Maximum concentration reached in the blood after dosing
    Tmax: float # Time taken to reach the maximum concentration (C_max)
    Auclast: float # Area under the C-T curve with a final time of 24 h
    Aucinf: float # Area under the C-T curve extrapolated to infinity
    Cl: float # Clearance. In this case, the average clearance of a drug from the body
    T1_2: float # Half-life, the time it takes for the drug concentration to reduce by half
    mrt: float # Mean residence time, the average time the drug stays in the body

class PKResult(BaseModel):
    params: dict
    curve: dict

class PKResultRaw(BaseModel):
    model_version: str
    msg: str
    data: PKResult

class ResponseData(BaseModel):
    mole: Any
    dose: float
    route: Literal["i.v.", "p.o."]
    pk_result: PKResultRaw