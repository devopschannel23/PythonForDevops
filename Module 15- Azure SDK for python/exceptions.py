#official link: https://learn.microsoft.com/en-us/python/api/azure-core/azure.core.exceptions?view=azure-python
from azure.core.exceptions import HttpResponseError
from azure.identity import  DefaultAzureCredential
from azure.mgmt.compute import ComputeManagementClient

credential = DefaultAzureCredential()

compute_client = ComputeManagementClient(credential, subscription_id="992adee7-e65c-4c6c-abba-1a95aa93643f")

vms = compute_client.virtual_machines.list_all()
try:
    vm = compute_client.virtual_machines.get(
        resource_group_name="new-rg",
        vm_name="vm1"
    )
    print(vm.name)
except HttpResponseError as e:
    print(f"Response API Error: {e}")
