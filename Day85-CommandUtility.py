import argparse

parser = argparse.ArgumentParser(description="Greet a user")
parser.add_argument("name", help="Name of the person")
args = parser.parse_args()

print(f"Hello, {args.name}!")
