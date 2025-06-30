from fastmcp import FastMCP
from tools.base import (
    ADMET_predict,
    Pharmacokinetics_predict,
    ToxScan_predict,
    InputData,
    RES,
    AdmetInnerData,
    InputPK,
    PKResult,
    ToxResult
)
from structs.admet import description as admet_description
from structs.pk import description as pk_description

mcp = FastMCP("Demo 🚀")


@mcp.tool(
    name="ADMET predict", description="Predict the ADMET properties of a molecule"
)
async def ADMET_predict_tool(data: InputData) -> RES[AdmetInnerData]:
    return await ADMET_predict(data)

@mcp.resource("data://ADMET_reference", name="ADMET Reference Data")
async def admet_meta():
    return {
        "name": "ADMET",
        "description": "ADMET is a collection of 20 molecular descriptors that are commonly used to predict the pharmacokinetic and pharmacodynamic properties of drugs.",
        "properties": admet_description
    }


@mcp.tool(
    name="Pharmacokinetics predict",
    description="Predict the Pharmacokinetics properties of a molecule",
)
async def Pharmacokinetics_predict_tool(data: InputPK) -> RES[PKResult]:
    return await Pharmacokinetics_predict(data)

@mcp.resource("data://Pharmacokinetics_reference", name="Pharmacokinetics Reference Data")
async def pk_meta():
    return {
        "name": "Pharmacokinetics",
        "description": "Pharmacokinetics is a collection of 10 molecular descriptors that are commonly used to predict the pharmacokinetic and pharmacodynamic properties of drugs.",
        "properties": pk_description
    }

@mcp.tool(
    name="ToxScan predict",
    description="Predict the ToxScan properties of a molecule",
)
async def ToxScan_predict_tool(data: InputData) -> RES[ToxResult]:
    return await ToxScan_predict(data)




if __name__ == "__main__":
    mcp.run(transport='sse',host="0.0.0.0",port=5001)
