import argparse

parser = argparse.ArgumentParser(description="Add numbers provided as command-line arguments")

parser.add_argument("numbers",
                    type=int,
                    nargs="+",
                    help="Enter one or more integers",
                    )

args = parser.parse_args()
total = sum(args.numbers)

print(f"Total is : {total}")