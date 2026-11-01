from kubernetes import client, config

#load kubeconfig
config.load_kube_config()

#initial k8s API
v1 = client.CoreV1Api()

v1.delete_namespaced_pod(
    name="product-service-679857c745-j2q8v",
    namespace="azure-store"
)

print("Pod deleted!")