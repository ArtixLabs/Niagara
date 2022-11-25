import argparse
from src import deps
parser = argparse.ArgumentParser()
VERSION="0.0.3"
parser.add_argument('-c','--config')
parser.add_argument('-v', '--version')
args = parser.parse_args()
def run():
    if args.version:
        print(VERSION)
    if args.config:
        x = deps.Packages()
        x.install_pkgs(args.config)
        v = deps.Config(args.config)
        v.operate()



