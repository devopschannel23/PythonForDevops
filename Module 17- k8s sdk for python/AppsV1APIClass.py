from kubernetes import client, config

#load kubeconfig
config.load_kube_config()

#initialize k8s API
v1 = client.AppsV1Api()

#list all deployments

deployments = v1.list_deployment_for_all_namespaces()
for deployment in deployments.items:
    print(f"Deployments: {deployment.metadata.name}")
    #replicas = deployment.spec.replicas
    #available = deployment.status.available_replicas
