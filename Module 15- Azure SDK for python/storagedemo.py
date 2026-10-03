from azure.identity import DefaultAzureCredential
from azure.mgmt.resource.resources import ResourceManagementClient
from azure.mgmt.storage import StorageManagementClient
from azure.mgmt.storage.models import BlobContainer
from azure.storage.blob import  BlobServiceClient

credential = DefaultAzureCredential()

rg_name = "new-rg"
location = "Central India"
sub_id = "992adee7-e65c-4c6c-abba-1a95aa93643f"
storage_account_name = "newstg23081999"
container_name = "new-container"

#creating resource groups
resource_client = ResourceManagementClient(credential, subscription_id="992adee7-e65c-4c6c-abba-1a95aa93643f")
rg_result = resource_client.resource_groups.create_or_update(rg_name, {
    "location": location
})

#provision storage account
storage_client = StorageManagementClient(credential, subscription_id="992adee7-e65c-4c6c-abba-1a95aa93643f")
av_result = storage_client.storage_accounts.check_name_availability(
    {"name": storage_account_name, "type": "Microsoft.Storage/storageAccounts"}
)
if not av_result.name_available:
    print(f"Storage name: {storage_account_name} is already in use, try another name")

poller = storage_client.storage_accounts.begin_create(rg_name, storage_account_name, {
    "location": location,
    "kind": "StorageV2",
    "sku": {"name": "Standard_LRS"}
})
account_result = poller.result()
print(f"Provisioned storage Account {account_result.name}")

#create a blob account
storage_client.blob_containers.create(rg_name, storage_account_name, container_name, BlobContainer())

#authenticate to blob
account_Url = "azure-storage-account-url"
blob_service_client = BlobServiceClient(
    account_url=account_Url,
    credential=credential
)
#listing all blob
for container in blob_service_client.list_containers():
    print(container.name)
    
#upload a file to blob
container_client= blob_service_client.get_container_client("backup")
blob_client = container_client.get_blob_client("server.log")
with open("server.log", "rb") as data:
    blob_client.upload_blob(data, overwrite=True)


