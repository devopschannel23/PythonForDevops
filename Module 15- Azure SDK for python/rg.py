from azure.identity import DefaultAzureCredential
from azure.mgmt.resource.resources import ResourceManagementClient

credential = DefaultAzureCredential()

resource_client = ResourceManagementClient(credential, subscription_id="992adee7-e65c-4c6c-abba-1a95aa93643f")

# list all resource groups
# RGs = resource_client.resource_groups.list()
# for rg in RGs:
#     print(rg.name)

#Create resource group
# rg_name = "rg-created-bySDK"
# location = "Central India"
# resource_client.resource_groups.create_or_update(
#     rg_name, {
#         "location": location
#     }
# )
# print(f"Resource group {rg_name} was created")

#Delete all resource group that we created so far
rg_name = ["rg-created-bySDK", "NetworkWatcherRG", "new-rg"]

for rg in rg_name:
  poller = resource_client.resource_groups.begin_delete(
    rg
  )
  poller.result()