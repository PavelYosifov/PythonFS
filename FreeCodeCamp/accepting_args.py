import sys
import argparse

name = sys.argv[1]
print(sys.argv)  # In the terminal we type python accepting_args. py Pavel 24
print("Hello " + name)  # In the terminal we type python accepting_args. py Pavel

parser = argparse.ArgumentParser(description="This program prints the name of my dogs.")
parser.add_argument(
    "-c",
    "--color",
    metavar="color",
    required=True,
    choices={"red", "yellow"},
    help="the color to search for",
)
args = parser.parse_args()
print(args.color)  # In the terminal we type "-c red" and it will print "red"
