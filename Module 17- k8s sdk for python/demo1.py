from kubernetes import client, config

#load kubeconfig
config.load_kube_config()

#initial k8s API
v1 = client.CoreV1Api()

#Get nodes
# nodes = v1.list_node()
# for node in nodes.items:
#     print(node.metadata.name)

#namespace
namespaces = v1.list_namespace()
for ns in namespaces.items:
    print(ns.metadata.name)