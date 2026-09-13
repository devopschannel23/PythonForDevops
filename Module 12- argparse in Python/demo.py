import argparse

parser = argparse.ArgumentParser(description="""
Script to deploy resources on Azure
This is script to deploy the resources in Azure
After using OIDC token
""",
                                 prog="deploy-azure",
                                 usage="%(prog)s --replicas how-many-replicas",
                                 formatter_class=argparse.RawTextHelpFormatter,
                                 argument_default="N/A"
                                 )

parser.add_argument("--replicas", type=int, default=3)
# parser.add_argument("--env", required=True, choices=["dev", "prod"])
#boolean flags
# parser.add_argument("--dry-run", action="store_true")
#nargs- to provide multiple types of arguments of same kind
# parser.add_argument("--resources", nargs="+")

#logic checks or argument validation
# if args.replicas < 1:
#     parser.error("Replica must be greater than 0!")


args= parser.parse_args()

print(args.replicas)
