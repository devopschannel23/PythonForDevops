from kubernetes import client, config, watch

config.load_kube_config()

v1 = client.CoreV1Api()

w = watch.Watch()

for event in w.stream(
    v1.list_namespaced_pod, namespace="azure-store", timeout_seconds=60
):
    pod = event["object"]
    print(
        f"Event: {event['type']},"
        f"Pod: {pod.metadata.name}"
    )