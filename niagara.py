import argparse
from src import deps
parser = argparse.ArgumentParser()
VERSION="0.0.7"
parser.add_argument('-c','--config')
parser.add_argument('-p', '--packages')
parser.add_argument('-v', '--version', action="store_true")
args = parser.parse_args()
def run():
    if args.version == True:
        print(VERSION)
    if args.packages:
        x = deps.Packages()
        x.dump_all_pkgs(args.packages)
    if args.config:
        x = deps.Packages()
        x.install_pkgs(args.config)
        v = deps.Config(args.config)
        v.operate()



