from datetime import timedelta

from azure.identity import DefaultAzureCredential
from azure.monitor import query
from azure.monitor.query import  LogsQueryClient

credential = DefaultAzureCredential()

client  = LogsQueryClient(credential)

# Azure activity logs

query = """
AzureActivity
| take 10
"""

response = client.query_workspace(
    workspace_id="<workspace-id>",
    query=query,
    timespan=timedelta(hours=24)
)
for table in response.tables:
    print(table.columns)

    for row in table.rows:
        print(row)