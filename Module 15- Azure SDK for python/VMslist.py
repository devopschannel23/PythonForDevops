from azure.identity import  DefaultAzureCredential
from azure.mgmt.compute import ComputeManagementClient

credential = DefaultAzureCredential()

compute_client = ComputeManagementClient(credential, subscription_id="992adee7-e65c-4c6c-abba-1a95aa93643f")

vms = compute_client.virtual_machines.list_all()

for vm in vms:
    print(f"VMName: {vm.name}, VM Size: {vm.hardware_profile.vm_size}, VMLocation: {vm.location}, DiskSize: {vm.storage_profile.os_disk.disk_size_gb}")