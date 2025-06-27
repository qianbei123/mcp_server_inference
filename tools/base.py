import httpx
from typing import cast, Literal
from structs.base import InputData, RES
from structs.admet import AdmetRawResult, AdmetInnerData
from structs.pk import InputPK,PKResult,ResponseData


async def admet_predict(data: InputData) -> RES[AdmetInnerData]:
    try:
        async with httpx.AsyncClient() as client:
            url = "http://101.126.67.113:7893/admet/sync_mcp_admet_predict"
            response = await client.post(url, json={
                'smiles': data.smiles,
            })
            response.raise_for_status()
            res = cast(RES[AdmetRawResult], response.json())

            if (
                res.code != 0
                or not res.data
                or not res.data.admet_result
                or not res.data.admet_result.data
            ):
                return RES(code=-1, msg=f"admet predict error: {res.msg}")
            if not res.data.admet_result.data:
                return RES(
                    code=-1, msg=f"admet predict error: {res.data.admet_result.msg}"
                )

            return RES(data=res.data.admet_result.data)
    except Exception as e:
        return RES(code=-1, msg=f"admet predict error: {e}")


async def Pharmacokinetics_predict(
    data: InputPK,
) -> RES[PKResult]:
    try:
        async with httpx.AsyncClient() as client:
            url = "http://101.126.67.113:7893/pk/sync_mcp_pk_predict"
            response = await client.post(
                url,
                json={
                    "mole": {"smiles": data.smiles, "sdf": ""},
                    "dose": data.dose,
                    "route": data.route,
                },
            )
            response.raise_for_status()
            res = cast(RES[ResponseData], response.json())
            if res.code != 0 or not res.data:
                return RES(code=-1, msg=f"Pharmacokinetics predict error: {res.msg}")
            if not res.data.pk_result.data:
                return RES(code=-1, msg=f"Pharmacokinetics predict error: {res.data.pk_result.msg}")

            return RES(data=res.data.pk_result.data)
    except Exception as e:
        return RES(code=-1, msg=f"Pharmacokinetics predict error: {e}")
