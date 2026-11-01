from kubernetes import client, config

#load kubeconfig
config.load_kube_config()

#initial k8s API
v1 = client.CoreV1Api()

logs = v1.read_namespaced_pod_log(
    name="product-service-679857c745-j2q8v",
    namespace="azure-store",
    tail_lines=50
)
print(logs)