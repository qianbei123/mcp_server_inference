import httpx
from typing import Dict, Any, Union, List
from httpx import Timeout
from structs.tool_structs import (
    PocketMoleculeRetrievalInput, PocketMoleculeRetrievalResponse,
    MoleculePocketRetrievalInput, MoleculePocketRetrievalResponse,
    MoleculeSearchInput, MoleculeSearchResponse,
    DiseaseTargetRetrievalInput, DiseaseTargetRetrievalResponse,
    GasPropertiesInput, GasPropertiesResponse
)

DEFAULT_TIMEOUT = Timeout(60.0, connect=300.0)


async def retrieve_molecules_from_pocket(input_data: PocketMoleculeRetrievalInput) -> PocketMoleculeRetrievalResponse:
    """
    Retrieve potential drug molecules that may bind to the input pocket (specified by its PDB ID).
    :param input_data: PocketMoleculeRetrievalInput with pocket_name and k (number of results)
    :return: List of matched molecule names and their scores
    """
    try:
        async with httpx.AsyncClient(timeout=DEFAULT_TIMEOUT) as client:
            url = "http://101.126.67.113:8020/retrieve_mol_from_pocket"
            response = await client.post(
                url, 
                json={"pocket_name": input_data.pocket_name, "k": input_data.k}
            )
            response.raise_for_status()
            return PocketMoleculeRetrievalResponse(**response.json())
    except Exception as e:
        raise Exception(f"retrieve molecules from pocket error: {e}")

async def retrieve_pocket_from_smiles(input_data: MoleculePocketRetrievalInput) -> MoleculePocketRetrievalResponse:
    """
    Retrieve the PDB IDs of potential protein pockets that may bind to the input molecule based on its SMILES string.
    :param input_data: MoleculePocketRetrievalInput with smiles and k (number of results)
    :return: List of matched pocket PDB IDs and their scores
    """
    try:
        async with httpx.AsyncClient(timeout=DEFAULT_TIMEOUT) as client:
            url = "http://101.126.67.113:8020/retrieve_pocket_from_smiles"
            response = await client.post(
                url, 
                json={"smiles": input_data.smiles, "k": input_data.k}
            )
            response.raise_for_status()
            return MoleculePocketRetrievalResponse(**response.json())
    except Exception as e:
        raise Exception(f"retrieve pocket from smiles error: {e}")
    

async def search_by_smiles(input_data: MoleculeSearchInput) -> MoleculeSearchResponse:
    """
    The input is the SMILES string of the target drug molecule to search for similar molecules, calling the API provided by api_server
    :param input_data: MoleculeSearchInput with smiles, k, and filter_ion parameters
    :return: List of search results
    """
    try:
        async with httpx.AsyncClient(timeout=DEFAULT_TIMEOUT) as client:
            url = "http://180.184.81.153:8021/mol_search/smiles"
            response = await client.post(
                url, 
                json={
                    "smiles": input_data.smiles, 
                    "limit_num": input_data.k, 
                    "filter_ion": input_data.filter_ion
                }
            )
            response.raise_for_status()
            return MoleculeSearchResponse(**response.json())
    except Exception as e:
        raise Exception(f"search by smiles error: {e}")

async def retrieve_targets_from_disease(input_data: DiseaseTargetRetrievalInput) -> DiseaseTargetRetrievalResponse:
    """
    Enter the disease name to return potentially related targets.
    :param input_data: DiseaseTargetRetrievalInput with disease name
    :return: Matched disease name, matching score, list of targets
    """
    try:
        async with httpx.AsyncClient(timeout=DEFAULT_TIMEOUT) as client:
            url = "http://101.126.67.113:8020/retrieve_target_from_disease"
            response = await client.post(
                url, 
                json={"disease": input_data.disease}
            )
            response.raise_for_status()
            return DiseaseTargetRetrievalResponse(**response.json())
    except Exception as e:
        raise Exception(f"retrieve targets from disease error: {e}")

async def predict_gas_properties(input_data: GasPropertiesInput) -> GasPropertiesResponse:
    """
    Predict gas-related properties of molecules, including S₀→S₁ transition energy, HOMO-LUMO gap,
    electron reorganization energy, and hole reorganization energy.
    :param input_data: GasPropertiesInput with smiles (single string or list of strings)
    :return: List of prediction results with property values for each molecule
    """
    try:
        async with httpx.AsyncClient(timeout=DEFAULT_TIMEOUT) as client:
            url = "http://101.126.67.113:8010/predict"
            response = await client.post(
                url, 
                json={"smiles": input_data.smiles}
            )
            response.raise_for_status()
            return GasPropertiesResponse(results=response.json())
    except Exception as e:
        raise Exception(f"Gas property prediction error: {e}")



