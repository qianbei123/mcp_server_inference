from tools.base import (
    ADMET_predict,
    Pharmacokinetics_predict,
    ToxScan_predict,
    InputData,
    InputPK,
    RES
)
import asyncio

input_data = InputData(smiles="CN1C=NC2=C1C(=O)N(C(=O)N2C)C")
input_pk = InputPK(smiles="CN1C=NC2=C1C(=O)N(C(=O)N2C)C")

async def test():
    tasks = [
        ADMET_predict(input_data),
        Pharmacokinetics_predict(input_pk),
        ToxScan_predict(input_data)
    ]
    res_list:list[RES] = await asyncio.gather(*tasks)
    for res in res_list:
        print(res.code == 0)

if __name__ == "__main__":
    asyncio.run(test())

