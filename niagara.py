import argparse
from src import deps
parser = argparse.ArgumentParser()

parser.add_argument('--config')

args = parser.parse_args()
def run():
    if args.config:
        x = deps.Packages()
        x.install_pkgs(args.config)



