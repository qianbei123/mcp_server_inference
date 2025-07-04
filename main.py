from fastmcp import FastMCP
from tools.base import (
    retrieve_molecules_from_pocket,
    retrieve_pocket_from_smiles,
    search_by_smiles,
    retrieve_targets_from_disease,
    predict_gas_properties,
)

from structs.tool_structs import (
    PocketMoleculeRetrievalInput, PocketMoleculeRetrievalResponse,
    MoleculePocketRetrievalInput, MoleculePocketRetrievalResponse,
    MoleculeSearchInput, MoleculeSearchResponse,
    DiseaseTargetRetrievalInput, DiseaseTargetRetrievalResponse,
    GasPropertiesInput, GasPropertiesResponse
)
from typing import Dict, Any, List, Union

mcp = FastMCP("Demo 🚀")




@mcp.tool(
    name="Pocket_Molecule_Retrieval",
    description="Retrieve potential drug molecules that may bind to a specific protein pocket (specified by PDB ID)."
)
async def retrieve_molecules_from_pocket_tool(pocket_name: str, k: int = 10) -> PocketMoleculeRetrievalResponse:
    input_data = PocketMoleculeRetrievalInput(pocket_name=pocket_name, k=k)
    return await retrieve_molecules_from_pocket(input_data)

@mcp.tool(
    name="Molecule_Pocket_Retrieval",
    description="Retrieve potential protein pockets that may bind to a specific molecule (specified by SMILES string)."
)
async def retrieve_pocket_from_smiles_tool(smiles: str, k: int = 10) -> MoleculePocketRetrievalResponse:
    input_data = MoleculePocketRetrievalInput(smiles=smiles, k=k)
    return await retrieve_pocket_from_smiles(input_data)

@mcp.tool(
    name="Molecule_Search",
    description="Search for similar molecules based on a given molecule's SMILES string."
)
async def search_by_smiles_tool(smiles: str, k: int = 10, filter_ion: bool = True) -> MoleculeSearchResponse:
    input_data = MoleculeSearchInput(smiles=smiles, k=k, filter_ion=filter_ion)
    return await search_by_smiles(input_data)

@mcp.tool(
    name="Disease_Target_Retrieval",
    description="Retrieve potential drug targets related to a specific disease."
)
async def retrieve_targets_from_disease_tool(disease: str) -> DiseaseTargetRetrievalResponse:
    input_data = DiseaseTargetRetrievalInput(disease=disease)
    return await retrieve_targets_from_disease(input_data)

@mcp.tool(
    name="Gas_Properties_Prediction",
    description="Predict gas-related properties of molecules, including S₀→S₁ transition energy, HOMO-LUMO gap, electron reorganization energy, and hole reorganization energy."
)
async def predict_gas_properties_tool(smiles: Union[str, List[str]]) -> GasPropertiesResponse:
    input_data = GasPropertiesInput(smiles=smiles)
    return await predict_gas_properties(input_data)


if __name__ == "__main__":
    mcp.run(transport='sse',host="0.0.0.0",port=5003)
