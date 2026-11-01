from kubernetes import client, config

#load kubeconfig
config.load_kube_config()

#initialize k8s API
v1 = client.AppsV1Api()

dep_name = "product-service"
ns = "azure-store"

body = {
    "spec": {
        "replicas": 2
    }
}

v1.patch_namespaced_deployment_scale(
    name=dep_name,
    namespace=ns,
    body=body
)