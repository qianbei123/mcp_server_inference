from pydantic import BaseModel,model_validator
from typing import Union, Optional, Generic, TypeVar, Literal
import re


class AdmetValueItem(BaseModel):
    color: Union[Literal["g", "r", "y"], None] # green, red, yellow, None
    value: Union[float, bool]


class AdmetInnerData(BaseModel):
    AR: AdmetValueItem
    ER: AdmetValueItem
    GR: AdmetValueItem
    MW: AdmetValueItem
    TR: AdmetValueItem
    ARE: AdmetValueItem
    AhR: AdmetValueItem
    CLr: AdmetValueItem
    HIA: AdmetValueItem
    HSE: AdmetValueItem
    MMP: AdmetValueItem
    P53: AdmetValueItem
    nha: AdmetValueItem
    nhd: AdmetValueItem
    Carc: AdmetValueItem
    HIA2: AdmetValueItem
    ames: AdmetValueItem
    dili: AdmetValueItem
    herg: AdmetValueItem
    logP: AdmetValueItem
    nrot: AdmetValueItem
    tpsa: AdmetValueItem
    ATAD5: AdmetValueItem
    HIA_c: AdmetValueItem
    n_het: AdmetValueItem
    nring: AdmetValueItem
    AR_LBD: AdmetValueItem
    ER_LBD: AdmetValueItem
    hERG_1: AdmetValueItem
    nRigid: AdmetValueItem
    BCRP_dp: AdmetValueItem
    hERG_10: AdmetValueItem
    hERG_30: AdmetValueItem
    hia_hou: AdmetValueItem
    ppbr_az: AdmetValueItem
    BSEP_aid: AdmetValueItem
    HLM_chen: AdmetValueItem
    OCT1_aid: AdmetValueItem
    RLM_chen: AdmetValueItem
    VDss_dog: AdmetValueItem
    VDss_rat: AdmetValueItem
    ld50_zhu: AdmetValueItem
    max_ring: AdmetValueItem
    AOT_C_wym: AdmetValueItem
    Aromatase: AdmetValueItem
    Half_life: AdmetValueItem
    OCT2_kido: AdmetValueItem
    Pgp_human: AdmetValueItem
    egan_rule: AdmetValueItem
    Papp_Caco2: AdmetValueItem
    VDss_human: AdmetValueItem
    caco2_wang: AdmetValueItem
    ghose_rule: AdmetValueItem
    veber_rule: AdmetValueItem
    Flexibility: AdmetValueItem
    LogD_pH_7_4: AdmetValueItem
    OATP1B1_aid: AdmetValueItem
    OATP1B3_aid: AdmetValueItem
    OATP2B1_aid: AdmetValueItem
    VDss_monkey: AdmetValueItem
    bbb_martins: AdmetValueItem
    CL_total_dog: AdmetValueItem
    CL_total_rat: AdmetValueItem
    Micronucleus: AdmetValueItem
    cyp2c9_veith: AdmetValueItem
    cyp2d6_veith: AdmetValueItem
    cyp3a4_veith: AdmetValueItem
    hERG_binding: AdmetValueItem
    total_charge: AdmetValueItem
    Eye_Corrosion: AdmetValueItem
    Neurotoxicity: AdmetValueItem
    eye_corrosion: AdmetValueItem
    lipinski_rule: AdmetValueItem
    thermo_logSaq: AdmetValueItem
    vdss_lombardo: AdmetValueItem
    CL_total_human: AdmetValueItem
    Nephrotoxicity: AdmetValueItem
    eye_irritation: AdmetValueItem
    nStereoCenters: AdmetValueItem
    skin_corrosion: AdmetValueItem
    CL_total_monkey: AdmetValueItem
    half_life_obach: AdmetValueItem
    ocular_toxicity: AdmetValueItem
    pgp_broccatelli: AdmetValueItem
    skin_irritation: AdmetValueItem
    CL_microsome_rat: AdmetValueItem
    CYP2C8_inhibition: AdmetValueItem
    CYP2C9_inhibition: AdmetValueItem
    CYP2D6_inhibition: AdmetValueItem
    CYP3A4_inhibition: AdmetValueItem
    CL_microsome_human: AdmetValueItem
    CL_microsome_mouse: AdmetValueItem
    bioavailability_ma: AdmetValueItem
    skin_sensitization: AdmetValueItem
    solubility_aqsoldb: AdmetValueItem
    Carcinogenicity_Rat: AdmetValueItem
    Respiratory_toxicity: AdmetValueItem
    ugts_substance_huang: AdmetValueItem
    Mouse_carcinogenicity: AdmetValueItem
    Reproductive_toxicity: AdmetValueItem
    Mitochondrial_toxicity: AdmetValueItem
    clearance_microsome_az: AdmetValueItem
    clearance_hepatocyte_az: AdmetValueItem
    Carcinogenicity_Rat_TD50: AdmetValueItem
    lipophilicity_astrazeneca: AdmetValueItem
    Carcinogenicity_Mouse_TD50: AdmetValueItem
    Dog_fraction_unbound_plasma: AdmetValueItem
    Rat_fraction_unbound_plasma: AdmetValueItem
    Human_fraction_unbound_plasma: AdmetValueItem
    Monkey_fraction_unbound_plasma: AdmetValueItem
    cyp2c9_substrate_carbonmangels: AdmetValueItem
    cyp2d6_substrate_carbonmangels: AdmetValueItem
    cyp3a4_substrate_carbonmangels: AdmetValueItem

    @model_validator(mode="before")
    def pre_process(cls, value):
        if isinstance(value, dict):
            # 创建一个新字典来存储处理后的键值对
            processed = {}
            for key, val in value.items():
                new_key = re.sub(r'[ .()-]', '_', key)
                processed[new_key] = val
            return processed
        return value


class AdmetResult(BaseModel):
    model_version: str
    msg: str
    data: Optional[AdmetInnerData] = None


class AdmetRawResult(BaseModel):
    smiles: str
    admet_result: Optional[AdmetResult] = None


description = """Detail decription for Admet result items:
        {
      MW: {
        label: 'MW',
        hint: 'Molecular Weight',
        numberRange: [100, 500],
      },
      nha: {
        label: 'nHA',
        hint: 'Number of Hydrogen Acceptors',
        numberRange: [0, 10],
      },
      nhd: {
        label: 'nHD',
        hint: 'Number of Hydrogen Donors',
        numberRange: [0, 5],
      },
      nrot: {
        label: 'nRot',
        hint: 'Number of Rotatable Bonds',
        numberRange: [0, 10],
      },
      nring: {
        label: 'nRing',
        hint: 'Number of Rings',
        numberRange: [0, 6],
      },
      max_ring: {
        label: 'MaxRing',
        hint: 'Maximum Ring Size',
        numberRange: [0, 18],
      },
      n_het: {
        label: 'nHet',
        hint: 'Number of Heteroatoms',
        numberRange: [1, 15],
      },
      total_charge: {
        label: 'TotalCharge',
        hint: 'Total Charge',
        numberRange: [-4, 4],
      },
      nRigid: {
        label: 'nRigid',
        hint: 'Number of Rigid Bonds',
        numberRange: [0, 20],
      },
      Flexibility: {
        label: 'Flexibility',
        hint: 'Flexibility: nRot/nRigid',
        numberRange: [0, 0.3],
      },
      nStereoCenters: {
        label: 'nStereoCenters',
        hint: 'Number of Stereo Centers',
        numberRange: [0, 2],
      },
      tpsa: {
        label: 'TPSA',
        hint: 'Topological Polar Surface Area',
        numberRange: [0, 140],
      },
      solubility_aqsoldb: {
        label: 'LogS',
        hint: 'Log of the aqueous solubility, unit: log mol/L',
        numberRange: [-4, 0.5],
      },
      // thermo_logSaq: {
      //   label: "LogS",
      //   hint: "Log of the aqueous solubility, unit: log mol/L",
      //   numberRange: [-4, 0.5],
      // },
      logP: {
        label: 'LogP',
        hint: 'Log of the octanol/water partition coefficient.',
        numberRange: [0, 3],
      },
      lipophilicity_astrazeneca: {
        label: 'LogD7.4',
        hint: 'logP at physiological pH 7.4.',
        numberRange: [1, 3],
      },
      // 'LogD_pH_7.4': {
      //   label: 'LogD7.4',
      //   hint: 'logP at physiological pH 7.4.',
      //   numberRange: [1, 3]
      // },

      AR: {
        label: 'AR',
        hint: 'Androgen Receptor',
      },
      ER: {
        label: 'ER',
        hint: 'Estrogen Receptor',
        numberRange: [],
      },
      'AR-LBD': {
        label: 'AR-LBD',
        hint: 'Androgen Receptor Ligand Binding Domain',
        numberRange: [],
      },
      'ER-LBD': {
        label: 'ER-LBD',
        hint: 'Estrogen Receptor Ligand Binding Domain',
        numberRange: [],
      },
      Aromatase: {
        label: 'Aromatase',
        hint: 'Aromatase',
        numberRange: [],
      },
      ARE: {
        label: 'ARE',
        hint: 'Aryl Hydrocarbon Receptor Element',
        numberRange: [],
      },
      AhR: {
        label: 'AhR',
        hint: 'Aryl Hydrocarbon Receptor',
        numberRange: [],
      },
      ATAD5: {
        label: 'ATAD5',
        hint: 'ATPase family, AAA domain containing 5',
        numberRange: [],
      },
      HSE: {
        label: 'HSE',
        hint: 'Heat Shock Element',
        numberRange: [],
      },
      P53: {
        label: 'P53',
        hint: 'P53 Protein',
        numberRange: [],
      },
      MMP: {
        label: 'MMP',
        hint: 'Matrix Metalloproteinase',
        numberRange: [],
      },
      TR: {
        label: 'TR',
        hint: 'Thyroid Hormone Receptor',
        numberRange: [],
      },
      GR: {
        label: 'GR',
        hint: 'Glucocorticoid Receptor',
        numberRange: [],
      },

      caco2_wang: {
        label: 'Caco2',
        hint: 'Caco-2 cell permeability; Apparent Permeability Coefﬁcient (Papp), measured in log10(cm/s). ',
        numberRange: [-5.15, 0.5],
      },
      // Papp_Caco2: {
      //   label: "Caco2",
      //   hint: "Caco-2 cell permeability; Apparent Permeability Coefﬁcient (Papp), measured in log10(cm/s). ",
      //   numberRange: [-5.15, 0.5],
      // },
      Pgp_human: {
        label: 'Pgp inhibitor',
        hint: 'Pgp inhibitors. The value is the probability of being inhibitor.',
        numberRange: [],
      },
      pgp_broccatelli: {
        label: 'Pgp inhibitor',
        hint: 'Pgp inhibitors. The value is the probability of being inhibitor.',
        numberRange: [],
      },
      HIA_c: {
        label: 'HIA',
        hint: 'Human Intestinal Absorption',
        numberRange: [],
      },
      HIA: {
        label: 'HIA',
        hint: 'Human Intestinal Absorption',
        numberRange: [],
      },
      HIA2: {
        label: 'HIA',
        hint: 'Human Intestinal Absorption',
        numberRange: [],
      },
      hia_hou: {
        label: 'HIA',
        hint: 'Human Intestinal Absorption, positive if %FA > 30%.',
        numberRange: [],
      },
      bioavailability_ma: {
        label: 'Bioavailability',
        hint: 'Bioavailability,  positive if bioavailavility >= 20%.',
        numberRange: [],
      },

      CYP2C9_inhibition: {
        label: 'CYP2C9 inhibition',
        hint: 'CYP2C9 inhibition. The value is the probability of being inhibitor.',
      },
      CYP2D6_inhibition: {
        label: 'CYP2D6 inhibition',
        hint: 'CYP2D6 inhibition. The value is the probability of being inhibitor.',
      },
      CYP3A4_inhibition: {
        label: 'CYP3A4 inhibition',
        hint: 'CYP3A4 inhibition. The value is the probability of being inhibitor.',
      },
      CYP2C8_inhibition: {
        label: 'CYP2C8 inhibition',
        hint: 'CYP2C8 inhibition. The value is the probability of being inhibitor.',
      },
      cyp2c9_veith: {
        label: 'CYP2C9 inhibition',
        hint: 'CYP2C9 inhibition. The value is the probability of being inhibitor.',
      },
      cyp2d6_veith: {
        label: 'CYP2D6 inhibition',
        hint: 'CYP2D6 inhibition. The value is the probability of being inhibitor.',
      },
      cyp3a4_veith: {
        label: 'CYP3A4 inhibition',
        hint: 'CYP3A4 inhibition. The value is the probability of being inhibitor.',
      },
      cyp2d6_substrate_carbonmangels: {
        label: 'CYP2D6 substrate',
        hint: 'CYP2D6 substrate. The value is the probability of being substrate.',
      },
      cyp2c9_substrate_carbonmangels: {
        label: 'CYP2C9 substrate',
        hint: 'CYP2C9 substrate. The value is the probability of being substrate.',
      },
      cyp3a4_substrate_carbonmangels: {
        label: 'CYP3A4 substrate',
        hint: 'CYP3A4 substrate. The value is the probability of being substrate.',
      },

      clearance_hepatocyte_az: {
        label: 'CL hepatocyte human',
        hint: 'clearance of human hepatocyte, unit: ml/(min*kg)',
      },
      clearance_microsome_az: {
        label: 'CL microsome human',
        hint: 'clearance of human microsome, unit: ml/(min*kg)',
      },
      CL_microsome_human: {
        label: 'CL microsome human',
        hint: 'clearance of human microsome, unit: ml/(min*kg)',
      },
      CL_microsome_rat: {
        label: 'CL microsome rat',
        hint: 'clearance of rat microsome, unit: ml/(min*kg)',
      },
      CL_microsome_mouse: {
        label: 'CL microsome mouse',
        hint: 'clearance of mouse microsome, unit: ml/(min*kg)',
      },
      CL_total_human: {
        label: 'CL total human',
        hint: 'Total clearance of human, unit: ml/(min*kg)',
      },
      CL_total_monkey: {
        label: 'CL total monkey',
        hint: 'Total clearance of monkey, unit: ml/(min*kg)',
      },
      CL_total_dog: {
        label: 'CL total dog',
        hint: 'Total clearance of dog, unit: ml/(min*kg)',
      },
      CL_total_rat: {
        label: 'CL total rat',
        hint: 'Total clearance of rat, unit: ml/(min*kg)',
      },
      half_life_obach: {
        label: 'T1/2',
        hint: 'half life, unit: hours',
      },
      'Half-life': {
        label: 'T1/2',
        hint: 'half life',
      },
      CLr: {
        label: 'CL total human',
        hint: 'Total clearance of human',
      },
      ames: {
        label: 'AMES',
        hint: 'Mutagenicity means the ability of a drug to induce genetic alterations.',
      },
      dili: {
        label: 'DILI',
        hint: 'Drug-induced liver injury',
      },
      ld50_zhu: {
        label: 'LD50',
        hint: 'Lethal Dose 50 of rats. Unit: mol/kg',
      },
      herg: {
        label: 'hERG Block',
        hint: 'The human ether-à-go-go related gene, blocks(1) or not block(0)',
      },
      hERG_binding: {
        label: 'hERG IC50',
        hint: 'The human ether-à-go-go related gene, unit: μm',
      },
      AOT_C_wym: {
        label: 'Acute Oral Toxicity',
        hint: 'Acute oral toxicity',
      },
      Carc: {
        label: 'Carcinogenicity human',
        hint: 'Carcinogenicity of human, positive if carcinogenicity is true',
      },
      Carcinogenicity_Rat: {
        label: 'Carcinogenicity rat',
        hint: 'Carcinogenicity of rat, positive if carcinogenicity is true',
      },
      Carcinogenicity_Mouse_TD50: {
        label: 'Carcinogenicity mouse TD50',
        hint: 'The TD50 of Carcinogenicity in mouse, unit: mg/kg/day',
      },
      Carcinogenicity_Rat_TD50: {
        label: 'Carcinogenicity rat TD50',
        hint: 'The TD50 of Carcinogenicity in rat, unit: mg/kg/day',
      },
      Mouse_carcinogenicity: {
        label: 'Carcinogenicity mouse',
        hint: 'Carcinogenicity of mouse, positive if carcinogenicity is true',
      },
      Eye_Corrosion: {
        label: 'Eye Corrosion',
        hint: 'Eye corrosion refers to the damage to the eye tissue.',
      },
      lipinski_rule: {
        label: 'Lipinski (Pfizer) Rule',
        hint: 'Lipinski (Pfizer) Rule',
      },
      veber_rule: {
        label: 'Veber (GSK) Rule',
        hint: 'Veber (GSK) Rule',
      },
      ghose_rule: {
        label: 'Ghose (Amgen) Rule',
        hint: 'Ghose (Amgen) Rule',
      },
      egan_rule: {
        label: 'Egan (Pharmacia) Rule',
        hint: 'Egan (Pharmacia) Rule',
      },

      ppbr_az: {
        label: 'PPB',
        hint: 'The human plasma protein binding rate, unit: %',
      },
      bbb_martins: {
        label: 'BBB',
        hint: 'blood-brain barrier',
      },
      vdss_lombardo: {
        label: 'VDss human',
        hint: 'The volume of distribution at steady state of human, unit: L/kg',
      },
      VDss_human: {
        label: 'VDss human',
        hint: 'The volume of distribution at steady state of human, unit: L/kg',
      },
      VDss_monkey: {
        label: 'VDss monkey',
        hint: 'The volume of distribution at steady state of monkey, unit: L/kg',
      },
      VDss_dog: {
        label: 'VDss dog',
        hint: 'The volume of distribution at steady state of dog, unit: L/kg',
      },
      VDss_rat: {
        label: 'VDss rat',
        hint: 'The volume of distribution at steady state of rat, unit: L/kg',
      },
      Human_fraction_unbound_plasma: {
        label: 'Fu human',
        hint: 'The unbound fraction of drug in human plasma, unit: %',
      },
      Monkey_fraction_unbound_plasma: {
        label: 'Fu monkey',
        hint: 'The unbound fraction of drug in monkey plasma, unit: %',
      },
      Dog_fraction_unbound_plasma: {
        label: 'Fu dog',
        hint: 'The unbound fraction of drug in dog plasma, unit: %',
      },
      Rat_fraction_unbound_plasma: {
        label: 'Fu rat',
        hint: 'The unbound fraction of drug in rat plasma, unit: %',
      },
      eye_corrosion: {
        label: 'Eye Corrosion',
        hint: 'Eye corrosion refers to the damage to the eye tissue.',
      },
      eye_irritation: {
        label: 'Eye Irritation',
        hint: 'Eye irritation refers to the inflammation or discomfort in the eye.',
      },
      ocular_toxicity: {
        label: 'Ocular Toxicity',
        hint: 'Ocular toxicity refers to the toxic effects on the eye.',
      },
      skin_corrosion: {
        label: 'Skin Corrosion',
        hint: 'Skin corrosion refers to the damage to the skin tissue.',
      },
      skin_irritation: {
        label: 'Skin Irritation',
        hint: 'Skin irritation refers to the inflammation or discomfort in the skin.',
      },
      skin_sensitization: {
        label: 'Skin Sensitization',
        hint: 'Skin sensitization refers to the allergic reaction of the skin.',
      },
      hERG_1: {
        label: 'hERG Block 1',
        hint: 'The human ether-à-go-go related gene, blocks(1) or not block(0) at 1 µM.',
      },
      hERG_10: {
        label: 'hERG Block 10',
        hint: 'The human ether-à-go-go related gene, blocks(1) or not block(0) at 10 µM.',
      },
      hERG_30: {
        label: 'hERG Block 30',
        hint: 'The human ether-à-go-go related gene, blocks(1) or not block(0) at 30 µM.',
      },
      Micronucleus: {
        label: 'Micronucleus',
        hint: 'Formation of small nucleus in cells indicating genotoxicity.',
      },
      Mitochondrial_toxicity: {
        label: 'Mitochondrial Toxicity',
        hint: 'Toxic effects on the mitochondria.',
      },
      Nephrotoxicity: {
        label: 'Nephrotoxicity',
        hint: 'Toxic effects on the kidneys.',
      },
      Neurotoxicity: {
        label: 'Neurotoxicity',
        hint: 'Toxic effects on the nervous system. Unit: pLD50.',
      },
      Reproductive_toxicity: {
        label: 'Reproductive Toxicity',
        hint: 'Toxic effects on the reproductive system.',
      },
      Respiratory_toxicity: {
        label: 'Respiratory Toxicity',
        hint: 'Toxic effects on the respiratory system.',
      },
      BCRP_dp: {
        label: 'BCRP inhibition',
        hint: 'Breast Cancer Resistance Protein, The value is the probability of being inhibitor.',
      },
      BSEP_aid: {
        label: 'BSEP inhibition',
        hint: 'Fluorescent substrates of sister-P-glycoprotein. The value is the probability of being inhibitor.',
      },
      HLM_chen: {
        label: 'HLM Chen',
        hint: 'Human Liver Microsomes stability. Unstable (t1/2 ≤ 30 min) and stable (t1/2 > 30 min)',
      },
      RLM_chen: {
        label: 'RLM Chen',
        hint: 'Rat Liver Microsomes stability. Unstable (t1/2 ≤ 30 min) and stable (t1/2 > 30 min)',
      },
      OATP1B1_aid: {
        label: 'OATP1B1 inhibition',
        hint: 'inhibition of hepatic organic anion transporting polypeptides 1B1. The value is the probability of being inhibitor.',
      },
      OATP1B3_aid: {
        label: 'OATP1B3 inhibition',
        hint: 'inhibition of hepatic organic anion transporting polypeptides 1B3. The value is the probability of being inhibitor.',
      },
      OATP2B1_aid: {
        label: 'OATP2B1 inhibition',
        hint: 'inhibition of hepatic organic anion transporting polypeptides 2B1. The value is the probability of being inhibitor.',
      },
      OCT1_aid: {
        label: 'OCT1 inhibition',
        hint: 'Inhibition of human organic cation transporter 1. The value is the probability of being inhibitor.',
      },
      OCT2_kido: {
        label: 'OCT2 inhibition',
        hint: 'Inhibition of human organic cation transporter 2. The value is the probability of being inhibitor.',
      },
      ugts_substance_huang: {
        label: 'UGTs Substance',
        hint: 'Uridine 5-diphosphoglucuronosyl transferase enzymes substrate. The value is the probability of being substrate.',
      },
    }
    """