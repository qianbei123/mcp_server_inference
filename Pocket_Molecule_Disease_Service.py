from fastmcp import FastMCP
from tools.base import (
    retrieve_molecules_from_pocket,
    retrieve_pocket_from_smiles,
    retrieve_targets_from_disease,
    search_by_smiles,
)

from structs.tool_structs import (
    PocketMoleculeRetrievalInput, PocketMoleculeRetrievalResponse,
    MoleculePocketRetrievalInput, MoleculePocketRetrievalResponse,
    DiseaseTargetRetrievalInput, DiseaseTargetRetrievalResponse,
    MoleculeSearchInput, MoleculeSearchResponse,
)
from typing import Dict, Any, List, Union

mcp = FastMCP("Pocket_Molecule_Disease_Service")


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
    name="Disease_Target_Retrieval",
    description="Retrieve potential drug targets related to a specific disease."
)
async def retrieve_targets_from_disease_tool(disease: str) -> DiseaseTargetRetrievalResponse:
    input_data = DiseaseTargetRetrievalInput(disease=disease)
    return await retrieve_targets_from_disease(input_data)

@mcp.tool(
    name="Molecule_Search",
    description="Search for similar molecules based on a given molecule's SMILES string."
)
async def search_by_smiles_tool(smiles: str, k: int = 10, filter_ion: bool = True) -> MoleculeSearchResponse:
    input_data = MoleculeSearchInput(smiles=smiles, k=k, filter_ion=filter_ion)
    return await search_by_smiles(input_data)


if __name__ == "__main__":
    mcp.run(transport='sse', host="0.0.0.0", port=5006) 