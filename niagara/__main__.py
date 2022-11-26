import argparse
from .config import Config
from .generic import Generic
from .packages import Packages, force_gen
parser = argparse.ArgumentParser()
VERSION="0.0.0.6"
parser.add_argument('-c','--config')
parser.add_argument('--refresh-database', action="store_true")
parser.add_argument('-p', '--packages')
parser.add_argument('--set-os')
parser.add_argument('-d', '--dry')
parser.add_argument('-v', '--version', action="store_true")
args = parser.parse_args()
def run():
    if args.set_os:
        arch = args.set_os
    else:
        arch = 'arch'
    if args.refresh_database == True:
        force_gen()
    if args.dry:
        x = Packages()
        x.dry_run(args.dry, arch)
    if args.version == True:
        print(VERSION)
    if args.packages:
        x = Packages()
        x.dump_all_pkgs(args.packages)
    if args.config:
        x = Packages()
        x.install_pkgs(args.config)
        v = Config(args.config)
        v.operate()
        x = Generic(args.config)
        x.operate()




