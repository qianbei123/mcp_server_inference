import asyncio
from fastmcp import Client, FastMCP
from config import config

# In-memory server (ideal for testing)
server = FastMCP("TestServer")
client = Client(config)

# # HTTP server
# client = Client("https://example.com/mcp")

# # Local Python script
# client = Client("my_mcp_server.py")

async def main():
    async with client:
        # Basic server interaction
        await client.ping()
        
        # # List available operations
        tools = await client.list_tools()
        for tool in tools:
            print(f"Tool: {tool.name}")
            print(f"Description: {tool.description}")
            if tool.inputSchema:
                print(f"Parameters: {tool.inputSchema}")
            print("---")

        resources = await client.list_resources()
        for resource in resources:
            print(f"Resource URI: {resource.uri}")
            print(f"Name: {resource.name}")
            print(f"Description: {resource.description}")
            print(f"MIME Type: {resource.mimeType}")
            print("---")

            
        # prompts = await client.list_prompts()


        
        # Execute operations
        print("\n===== Testing Pocket_Molecule_Retrieval =====")
        result = await client.call_tool("Pocket_Molecule_Retrieval", {"pocket_name": "1L5S", "k": 5})
        print(result)
        
        print("\n===== Testing Molecule_Pocket_Retrieval =====")
        result = await client.call_tool("Molecule_Pocket_Retrieval", {"smiles": "CN1C=NC2=C1C(=O)N(C(=O)N2C)C"})
        print(result)
        
        # print("\n===== Testing Molecule_Search =====")
        # result = await client.call_tool("Molecule_Search", {"smiles": "CC(=O)OC1=CC=CC=C1C(=O)O", "k": 5})
        # print(result)
        
        print("\n===== Testing Disease_Target_Retrieval =====")
        result = await client.call_tool("Disease_Target_Retrieval", {"disease": "Anaemia, postpartum"})
        print(result)
        
        # print("\n===== Testing Gas_Properties_Prediction =====")
        # # 单个SMILES测试
        # result = await client.call_tool("Gas_Properties_Prediction", {"smiles": "c1ccccc1"})
        # print("Single SMILES result:")
        # print(result)
        
        # # 多个SMILES测试
        # result = await client.call_tool("Gas_Properties_Prediction", {"smiles": ["c1ccccc1", "CC(=O)O"]})
        # print("Multiple SMILES result:")
        # print(result)

asyncio.run(main())