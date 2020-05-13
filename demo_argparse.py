import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--foo', type=int, required=True)
parser.add_argument('--goo', type=str, required=True)

args = parser.parse_args()

print args.foo
print args.goo
