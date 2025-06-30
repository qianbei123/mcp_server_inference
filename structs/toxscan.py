from  structs.base import RES
from pydantic import BaseModel,model_validator
from typing import Union, Optional, Generic, TypeVar, Literal, cast
import re


class ToxResult(BaseModel):
    Rat_oral_LD50: str
    LC50DM__48h_Daphnia_magna_LC50_: str
    BCF__Bioconcentration_factor_: str
    LC50__96h_Fathead_minnow_LC50_: str
    IGC50__40h_Tetrahymena_pyriformis_IGC50_: str
    Carcinogenicity: Literal["YES", "NO"]
    Ames_Mutagenicity: Literal["YES", "NO"]
    Respiratory_toxicity: Literal["YES", "NO"]
    Eye_irritation: Literal["YES", "NO"]
    Eye_corrosion: Literal["YES", "NO"]
    Cardiotoxicity1: Literal["YES", "NO"]
    Cardiotoxicity10: Literal["YES", "NO"]
    Cardiotoxicity30: Literal["YES", "NO"]
    Cardiotoxicity5: Literal["YES", "NO"]
    CYP1A2: Literal["YES", "NO"]
    CYP2C19: Literal["YES", "NO"]
    CYP2C9: Literal["YES", "NO"]
    CYP2D6: Literal["YES", "NO"]
    CYP3A4: Literal["YES", "NO"]
    NR_AR: Literal["YES", "NO"]
    NR_AR_LBD: Literal["YES", "NO"]
    NR_AhR: Literal["YES", "NO"]
    NR_Aromatase: Literal["YES", "NO"]
    NR_ER: Literal["YES", "NO"]
    NR_ER_LBD: Literal["YES", "NO"]
    NR_PPAR_gamma: Literal["YES", "NO"]
    SR_ARE: Literal["YES", "NO"]
    SR_ATAD5: Literal["YES", "NO"]
    SR_HSE: Literal["YES", "NO"]
    SR_MMP: Literal["YES", "NO"]
    SR_p53: Literal["YES", "NO"]

    @model_validator(mode="before")
    def pre_process(cls, value):
        if isinstance(value, dict):
            # 创建一个新字典来存储处理后的键值对
            processed = {}
            for key, val in value.items():
                if key in ['Index','SMILES']:
                    continue
                # 将键中的特殊字符替换为下划线
                new_key = re.sub(r'[ .()-]', '_', key)
                processed[new_key] = val
            return processed
        return value





