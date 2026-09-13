#kubectl set image deployment/payment-api payment=company/payment:v25 -n production
#kubectl scale deployment payment-api --replicas=10 -n production
#python3 project2-k8s-automation.py \
  # --app payment-api \
  # --container payment \
  # --namespace production \
  # --image company/payment:v25 \
  # --replicas 10
# az vm create --vmname ""
# docker run -d -p image

import argparse
import subprocess
import sys

# Create argument parser
parser = argparse.ArgumentParser(
    description="Kubernetes deployment utility"
)

# Application / Deployment name
parser.add_argument(
    "--app",
    required=True,
    help="Kubernetes Deployment name"
)

# Container name
parser.add_argument(
    "--container",
    required=True,
    help="Kubernetes container name"
)

# Namespace
parser.add_argument(
    "--namespace",
    default="default",
    help="Kubernetes namespace (default: default)"
)

# Container image
parser.add_argument(
    "--image",
    required=True,
    help="Container image, e.g. reg_name/nginx:1.27"
)

# Number of replicas
parser.add_argument(
    "--replicas",
    type=int,
    default=2,
    help="Number of replicas (default: 2)"
)

# Dry-run option
parser.add_argument(
    "--dry-run",
    action="store_true",
    help="Show commands without executing them"
)

# Parse arguments
args = parser.parse_args()

# Validate replicas
if args.replicas < 1:
    parser.error("Replicas must be greater than 0")

# Command to update image
image_command = [
    "kubectl",
    "set",
    "image",
    f"deployment/{args.app}",
    f"{args.container}={args.image}",
    "-n",
    args.namespace
]

# Command to scale deployment
scale_command = [
    "kubectl",
    "scale",
    "deployment",
    args.app,
    f"--replicas={args.replicas}",
    "-n",
    args.namespace
]

# Dry-run
if args.dry_run:
    print("Dry run enabled.")
    print("\nCommands that would be executed:")

    print("\n1. Update image:")
    print(" ".join(image_command))

    print("\n2. Scale deployment:")
    print(" ".join(scale_command))

    sys.exit(0)

# Execute Kubernetes commands
try:
    print("Updating container image...")
    subprocess.run(image_command, check=True)

    print("Scaling deployment...")
    subprocess.run(scale_command, check=True)

    print("\nDeployment successful!")

except FileNotFoundError:
    print("Error: kubectl is not installed or not available in PATH.")
    sys.exit(1)

except subprocess.CalledProcessError as error:
    print(
        f"Deployment failed. "
        f"kubectl returned exit code {error.returncode}."
    )
    sys.exit(1)

except Exception as error:
    print(f"Unexpected error: {error}")
    sys.exit(1)