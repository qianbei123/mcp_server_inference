from fastmcp import FastMCP
from tools.base import (
    predict_gas_properties,
)

from structs.tool_structs import (
    GasPropertiesInput, GasPropertiesResponse
)
from typing import Dict, Any, List, Union

mcp = FastMCP("Gas_Properties_Service")


@mcp.tool(
    name="Gas_Properties_Prediction",
    description="Predict gas-related properties of molecules, including S₀→S₁ transition energy, HOMO-LUMO gap, electron reorganization energy, and hole reorganization energy."
)
async def predict_gas_properties_tool(smiles: Union[str, List[str]]) -> GasPropertiesResponse:
    input_data = GasPropertiesInput(smiles=smiles)
    return await predict_gas_properties(input_data)


if __name__ == "__main__":
    mcp.run(transport='sse', host="0.0.0.0", port=5004) 