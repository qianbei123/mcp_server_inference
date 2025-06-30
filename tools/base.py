import httpx
from typing import cast, Literal
from structs.base import InputData, RES
from structs.admet import AdmetRawResult, AdmetInnerData
from structs.pk import InputPK,PKResult,ResponseData
from structs.toxscan import ToxResult
from httpx import Timeout
DEFAULT_TIMEOUT = Timeout(60.0, connect=300.0)


async def ADMET_predict(data: InputData) -> RES[AdmetInnerData]:
    try:
        async with httpx.AsyncClient(timeout=DEFAULT_TIMEOUT) as client:
            url = "http://101.126.67.113:7893/admet/sync_mcp_admet_predict"
            response = await client.post(url, json={
                'smiles': data.smiles,
            })
            response.raise_for_status()
            res = RES[AdmetRawResult](**response.json())
            
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
        async with httpx.AsyncClient(timeout=DEFAULT_TIMEOUT) as client:
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
            res = RES[ResponseData](**response.json())

            if res.code != 0 or not res.data:
                return RES(code=-1, msg=f"Pharmacokinetics predict error: {res.msg}")
            if not res.data.pk_result.data:
                return RES(code=-1, msg=f"Pharmacokinetics predict error: {res.data.pk_result.msg}")

            return RES(data=res.data.pk_result.data)
    except Exception as e:
        return RES(code=-1, msg=f"Pharmacokinetics predict error: {e}")


async def ToxScan_predict(data: InputData) -> RES[ToxResult]:
    try:
        async with httpx.AsyncClient(timeout=DEFAULT_TIMEOUT) as client:
            url = "http://101.126.67.113:7893/funmg_api/task_mcp_sync/toxscan"

            payload = {
               "type": "smi",
               "content": [
                  data.smiles
               ]
            }
            response = await client.post(url, json=payload)
            response.raise_for_status()
            res_raw = response.json()
            res = RES[ToxResult](
                code = res_raw['code'],
                msg = res_raw['msg'],
                data = res_raw['data'][0]
            )

            return res
    except Exception as e:
        return RES(code=-1, msg=f"tox predict error: {e}")

