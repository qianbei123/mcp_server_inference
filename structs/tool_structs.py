from pydantic import BaseModel, Field
from typing import List, Union, Optional, Literal


# 基本响应结构
class BaseResponse(BaseModel):
    status: str


# Pocket_Molecule_Retrieval 工具
class PocketMoleculeRetrievalInput(BaseModel):
    pocket_name: str
    k: int = 10


class MoleculeScore(BaseModel):
    name: str
    score: float


class PocketMoleculeRetrievalResponse(BaseResponse):
    results: List[MoleculeScore]


# Molecule_Pocket_Retrieval 工具
class MoleculePocketRetrievalInput(BaseModel):
    smiles: str
    k: int = 10


class PocketScore(BaseModel):
    name: str
    score: float


class MoleculePocketRetrievalResponse(BaseResponse):
    results: List[PocketScore]


# Molecule_Search 工具
class MoleculeSearchInput(BaseModel):
    smiles: str
    k: int = 10
    filter_ion: bool = True


class MoleculeSearchResult(BaseModel):
    smiles: str
    score: float


class MoleculeSearchResponse(BaseResponse):
    results: List[MoleculeSearchResult]


# Disease_Target_Retrieval 工具
class DiseaseTargetRetrievalInput(BaseModel):
    disease: str


class DiseaseTargetRetrievalResponse(BaseResponse):
    disease: str
    best_match: str
    match_score: float
    targets: List[str]


# Gas_Properties_Prediction 工具
class GasPropertiesInput(BaseModel):
    smiles: Union[str, List[str]]


class GasPropertyResult(BaseModel):
    SMILES: str
    s0s1_transition_energy: float = Field(alias="S₀ → S₁ Transition Energy Prediction")
    homo_lumo_gap: float = Field(alias="HOMO-LUMO Gap Prediction")
    electron_reorganization_energy: float = Field(alias="Electron Reorganization Energy")
    hole_reorganization_energy: float = Field(alias="Hole Reorganization Energy")
    


class GasPropertiesResponse(BaseModel):
    status: str = "success"
    results: List[GasPropertyResult] 