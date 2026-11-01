from kubernetes import client, config

#load kubeconfig
config.load_kube_config()

#initial k8s API
v1 = client.CoreV1Api()

pods = v1.list_pod_for_all_namespaces()

for pod in pods.items:

    #get all details of pods
    # print(
    #     f"Namespace: {pod.metadata.namespace},"
    #     f"Pod: {pod.metadata.name},"
    #     f"Status: {pod.status.phase},"
    #     f"IP: {pod.status.pod_ip}"
    # )

    #identify unhealthy pods
    if pod.status.phase != "Running":
        print(
             f"Namespace: {pod.metadata.namespace},"
             f"Pod: {pod.metadata.name},"
             f"IP: {pod.status.pod_ip}"
         )
