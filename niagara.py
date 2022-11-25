import argparse
from src import deps
parser = argparse.ArgumentParser()
VERSION="0.0.9"
parser.add_argument('-c','--config')
parser.add_argument('-p', '--packages', action="store_true")
parser.add_argument('-v', '--version', action="store_true")
args = parser.parse_args()
def run():
    if args.version == True:
        print(VERSION)
    if args.packages == True:
        x = deps.Packages()
        x.dump_all_pkgs()
    if args.config:
        x = deps.Packages()
        x.install_pkgs(args.config)
        v = deps.Config(args.config)
        v.operate()
        x = deps.Generic(args.config)
        x.operate()




