#----------------Objective----------------#
# 1. Connect to the k8s cluster
# 2. Retrieve all nodes
# 3. Check whether pod is ready
# 4. Retrieve all the pods across namespace
# 5. Identify unhealthy containers
# 6. Collect logs from unhealthy pods
# 7. you generate a HC
# 8. Display alerts in your terminal

from kubernetes import client, config
from kubernetes.client.exceptions import ApiException
from datetime import datetime
import os


# Connect to Kubernetes
def connect_cluster():

    config.load_kube_config()

    print("[INFO] Connected to Kubernetes cluster")

    return (
        client.CoreV1Api(),
        client.AppsV1Api()
    )


# Check node health
def check_nodes(v1):

    print("\n========== NODE HEALTH ==========")

    nodes = v1.list_node()

    unhealthy_nodes = []

    for node in nodes.items:

        ready = False

        for condition in node.status.conditions:

            if condition.type == "Ready":
                ready = condition.status == "True"

        status = "Ready" if ready else "NotReady"

        print(f"{node.metadata.name}: {status}")

        if not ready:
            unhealthy_nodes.append(node.metadata.name)

    return unhealthy_nodes


# Check pod health
def check_pods(v1):

    print("\n========== POD HEALTH ==========")

    pods = v1.list_pod_for_all_namespaces()

    unhealthy_pods = []

    for pod in pods.items:

        namespace = pod.metadata.namespace
        name = pod.metadata.name

        problems = []

        if pod.status.phase not in ["Running", "Succeeded"]:
            problems.append(f"Pod phase: {pod.status.phase}")

        for container in pod.status.container_statuses or []:

            if not container.ready:
                problems.append(
                    f"Container {container.name} not ready"
                )

            if container.state.waiting:
                problems.append(
                    f"Waiting: {container.state.waiting.reason}"
                )

            if container.state.terminated:
                problems.append(
                    f"Terminated: {container.state.terminated.reason}"
                )

        if problems:

            unhealthy_pods.append((namespace, name))

            print(f"\n[ALERT] {namespace}/{name}")

            for problem in problems:
                print(f"  - {problem}")

        else:
            print(f"[OK] {namespace}/{name}")

    return unhealthy_pods


# Collect logs from unhealthy pods
def collect_logs(v1, unhealthy_pods):

    print("\n========== LOG COLLECTION ==========")

    os.makedirs("reports", exist_ok=True)

    for namespace, pod_name in unhealthy_pods:

        try:

            logs = v1.read_namespaced_pod_log(
                name=pod_name,
                namespace=namespace,
                tail_lines=50
            )

            filename = (
                f"reports/{namespace}_{pod_name}.log"
            )

            with open(filename, "w") as file:
                file.write(logs)

            print(f"[INFO] Logs saved: {filename}")

        except ApiException as e:

            print(
                f"[ERROR] Could not collect logs "
                f"for {pod_name}: {e.reason}"
            )


# Check deployment health
def check_deployments(apps_v1):

    print("\n========== DEPLOYMENT HEALTH ==========")

    deployments = (
        apps_v1.list_deployment_for_all_namespaces()
    )

    unhealthy_deployments = []

    for deployment in deployments.items:

        desired = deployment.spec.replicas or 0

        available = (
            deployment.status.available_replicas or 0
        )

        if available < desired:

            unhealthy_deployments.append(
                deployment.metadata.name
            )

            print(
                f"[ALERT] {deployment.metadata.name}: "
                f"Desired={desired}, Available={available}"
            )

        else:

            print(
                f"[OK] {deployment.metadata.name}: "
                f"{available}/{desired}"
            )

    return unhealthy_deployments


# Generate health report
def generate_report(
    unhealthy_nodes,
    unhealthy_pods,
    unhealthy_deployments
):

    os.makedirs("reports", exist_ok=True)

    filename = "reports/cluster_health_report.txt"

    with open(filename, "w") as file:

        file.write("KUBERNETES CLUSTER HEALTH REPORT\n")
        file.write(str(datetime.now()) + "\n\n")

        file.write(f"Unhealthy Nodes: {unhealthy_nodes}\n")
        file.write(f"Unhealthy Pods: {unhealthy_pods}\n")
        file.write(
            f"Unhealthy Deployments: "
            f"{unhealthy_deployments}\n"
        )

    print(f"\n[INFO] Report generated: {filename}")


# Main function
def main():

    try:

        v1, apps_v1 = connect_cluster()

        unhealthy_nodes = check_nodes(v1)

        unhealthy_pods = check_pods(v1)

        unhealthy_deployments = check_deployments(
            apps_v1
        )

        collect_logs(v1, unhealthy_pods)

        generate_report(
            unhealthy_nodes,
            unhealthy_pods,
            unhealthy_deployments
        )

        print("\n========== SUMMARY ==========")

        print("Unhealthy Nodes:", len(unhealthy_nodes))
        print("Unhealthy Pods:", len(unhealthy_pods))

        print(
            "Unhealthy Deployments:",
            len(unhealthy_deployments)
        )

    except ApiException as e:

        print(f"Kubernetes API error: {e.status} {e.reason}")

    except Exception as e:

        print(f"Automation failed: {e}")


if __name__ == "__main__":
    main()