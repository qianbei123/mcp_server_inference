from fastmcp import FastMCP
from tools.base import (
    search_by_smiles,
)

from structs.tool_structs import (
    MoleculeSearchInput, MoleculeSearchResponse,
)
from typing import Dict, Any, List, Union

mcp = FastMCP("Molecule_Search_Service")


@mcp.tool(
    name="Molecule_Search",
    description="Search for similar molecules based on a given molecule's SMILES string."
)
async def search_by_smiles_tool(smiles: str, k: int = 10, filter_ion: bool = True) -> MoleculeSearchResponse:
    input_data = MoleculeSearchInput(smiles=smiles, k=k, filter_ion=filter_ion)
    return await search_by_smiles(input_data)


if __name__ == "__main__":
    mcp.run(transport='sse', host="0.0.0.0", port=5005) 