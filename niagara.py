import argparse
from src import deps
parser = argparse.ArgumentParser()
VERSION="0.1.1"
parser.add_argument('-c','--config')
parser.add_argument('-p', '--packages')
parser.add_argument('-d', '--dry')
parser.add_argument('-v', '--version', action="store_true")
args = parser.parse_args()
def run():
    if args.dry:
        x = deps.Packages()
        x.generate_full_cmd(args.dry, 'arch')
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
        x = deps.Generic(args.config)
        x.operate()




