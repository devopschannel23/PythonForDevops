from kubernetes import client, config

#load in-cluster config
config.load_incluster_config()

v1 = client.CoreV1Api()

pods = v1.list_namepsaced_pod(namespace="kube-system")

for pod in pods.items:
    print(pod.metadata.name)