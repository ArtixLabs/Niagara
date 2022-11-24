import argparse
import deps
import packages
import builders
parser = argparse.ArgumentParser()

parser.add_argument('--run')

args = parser.parse_args()
def main():
    if args.run:
        x = packages.Packages()
        v = builders.Builder()
        x.install_pkgs()
        v.iterate_on('aur')


if __name__ == "__main__":
    main()

