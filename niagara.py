import argparse
from src import deps
parser = argparse.ArgumentParser()
VERSION="0.0.5"
parser.add_argument('-c','--config')
parser.add_argument('-v', '--version', action="store_true")
args = parser.parse_args()
def run():
    if args.version == True:
        print(VERSION)
    if args.config:
        x = deps.Packages()
        x.install_pkgs(args.config)
        v = deps.Config(args.config)
        v.operate()



