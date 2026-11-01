from kubernetes import client, config
from datetime import  datetime, timezone

#load kubeconfig
config.load_kube_config()

#initialize k8s API
v1 = client.AppsV1Api()

dep_name = "product-service"
ns = "azure-store"

body = {
    "spec": {
        "template": {
            "metadata": {
                "annotations": {
                    "kubectl.kubernetes.io/restartAt":
                        datetime.now(timezone.utc).isoformat()
                }
            }
        }
    }
}

v1.patch_namespaced_deployment(
    name=dep_name,
    namespace=ns,
    body=body
)