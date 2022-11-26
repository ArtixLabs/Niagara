import json
import subprocess
from .template import generate_database_file
import platform
import os
import logging

class Packages():
    def __init__(self):
        self.config = self.set_config()
        logging.basicConfig(filename='niagara.log', encoding='utf-8', format='%(levelname)s -- %(message)s')
    def set_config(self):
        def set_superuser():
            logging.info('Checking for sudo binary...')
            if os.path.exists('/usr/bin/sudo'):
                logging.info('Found sudo binary.')
                return 'sudo'
            elif os.path.exists('/usr/bin/doas'):
                logging.info('Found doas binary.')
                return 'doas'
            else:
                logging.info('Found no superuser binary. Defaulting to "su"')
                return 'su -c'
        def set_pkg_manager():
            logging.info('Checking package manager...')
            info = platform.freedesktop_os_release()
            if info["ID"] == "arch":
                logging.info('Distribtion is ArchLinux. Checking for pacman binary...')
                if os.path.exists('/usr/bin/pacman'):
                    logging.info('Found pacman.')
                    return '/usr/bin/pacman'
                else:
                    logging.error('No pacman binary found.')
            elif info["ID"] == "void":
                logging.info('Distribution is VoidLinux. Checking for xbps binaries...')
                if os.path.exists('/usr/bin/xbps-install'):
                    logging.info('Found xbps-install.')
                    return '/usr/bin/xbps-install'
                else:
                    logging.error('No xbps binary found.')
            elif info["ID"] == "fedora":
                logging.info('Distribution is FedoraLinux. Checking for dnf binaries...')
                if os.path.exists('/usr/bin/dnf'):
                    logging.info('Found dnf.')
                    return '/usr/bin/dnf'
                else:
                    logging.error('No xbps binary found.')
            elif info["ID"] == "gentoo":
                logging.info('Distribution is GentooLinux. Checking for portage binaries...')
                if os.path.exists('/usr/bin/emerge'):
                    logging.info('Found portage.')
                    return '/usr/bin/emerge'
                else:
                    logging.error('No portage/emerge binary found.')
            else:
                logging.fatal('Distribution "{}" is not supported.'.format(info["ID"]))
        def set_data_file():
            if os.path.exists(os.environ['HOME'] + "/.local/share/niagara/database.json"):
                return os.environ['HOME'] + '/.local/share/niagara/database.json'
            else:
                if not (os.path.exists(os.environ['HOME'] + "/.local/share")):
                    os.mkdir(os.environ['HOME'] + '/.local/share')
                if not (os.path.exists(os.environ['HOME'] + "/.local/share/niagara")):
                    os.mkdir(os.environ['HOME'] + '/.local/share/niagara')
                generate_database_file(os.environ['HOME'] + '/.local/share/niagara/database.json')
                return os.environ['HOME'] + '/.local/share/niagara/database.json'
        return dict([
            ('sudo', set_superuser()),
            ('pkgman', set_pkg_manager()),
            ('data', set_data_file()),
            ('pkgs', self.set_pkgs())
            ])
    def force_gen(self):
        if os.path.exists(os.environ['HOME'] + "/.local/share/niagara/database.json"):
            generate_database_file(os.environ['HOME'] + '/.local/share/niagara/database.json')
        else:
            if not (os.path.exists(os.environ['HOME'] + "/.local/share")):
                os.mkdir(os.environ['HOME'] + '/.local/share')
            if not (os.path.exists(os.environ['HOME'] + "/.local/share/niagara")):
                os.mkdir(os.environ['HOME'] + '/.local/share/niagara')
            generate_database_file(os.environ['HOME'] + '/.local/share/niagara/database.json')

    def set_pkgs(self) -> dict:
        x = Deps(os.environ['HOME'] + '/.local/share/niagara/database.json')
        arch = []
        void = []
        gentoo = []
        fedora = []
        debian = []
        for pkg in x.pkgs:
            arch.append({'pkgname': pkg.name, 'pkg': pkg.arch_pkg})
            void.append({'pkgname': pkg.name, 'pkg': pkg.void_pkg})
            gentoo.append({'pkgname': pkg.name, 'pkg': pkg.gentoo_pkg})
            fedora.append({'pkgname': pkg.name, 'pkg': pkg.fedora_pkg})
            debian.append({'pkgname': pkg.name, 'pkg': pkg.debian_pkg})
        return dict([
            ('arch', arch),
            ('void', void),
            ('gentoo', gentoo),
            ('fedora', fedora),
            ('debian', debian)
            ])
    def dump_all_pkgs(self, opt):
        for x in self.config['pkgs']['{}'.format(opt)]:
            print(x)
    def generate_full_cmd(self, path, opt):
        cmds = {}
        for x in self.config['pkgs']['{}'.format(opt)]:
            cmds[x['pkgname']] = x['pkg']
        vuln = Pkgs(path)
        pkgs = []
        for pkg in vuln.pkgs:
            if pkg.name in cmds:
                pkgs.append(cmds[pkg.name])
        return pkgs
    def dry_run(self, path, opt):
        cmds = {}
        for x in self.config['pkgs']['{}'.format(opt)]:
            cmds[x['pkgname']] = x['pkg']
        vuln = Pkgs(path)
        for pkg in vuln.pkgs:
            if pkg.name in cmds:
                print(cmds[pkg.name])
    def install_pkgs(self, path):
        def conc(arr, lip):
            tmp = []
            for x in arr:
                tmp.append(x)
            for x in lip:
                tmp.append(x)
            return tmp
        if self.config['pkgman'] == '/usr/bin/pacman':
            subprocess.call(conc([self.config['sudo'], self.config['pkgman'], '-S'], self.generate_full_cmd(path, 'arch')))
        elif self.config['pkgman'] == '/usr/bin/xbps-install': # Not in use, yet.
            subprocess.call(conc([self.config['sudo'], self.config['pkgman'], '-S'], self.generate_full_cmd(path, 'void')))

class Package:
    def __init__(self, name: str, arch_pkg: str, void_pkg: str, gentoo_pkg: str, fedora_pkg: str, debian_pkg: str):
        self.name = name
        self.arch_pkg = arch_pkg
        self.void_pkg = void_pkg
        self.gentoo_pkg = gentoo_pkg
        self.fedora_pkg = fedora_pkg
        self.debian_pkg = debian_pkg
class UPackage:
    def __init__(self, name: str):
        self.name = name
class Pkgs:
    def __init__(self, file):
        self.file = file
        self.pkgs = []
        self.read_to_pkg()
    def read_to_pkg(self):
        with open(self.file) as f:
            _data = f.read()
            _json_data = json.loads(_data)
            if "packages" in _json_data:
                _pkgs = _json_data["packages"]
                for package in _pkgs:
                    self.pkgs.append(UPackage(name=package))
        f.close()

class Deps:
    def __init__(self, file):
        self.file = file
        self.pkgs = []
        self.read_to_pkg()
    def read_to_pkg(self):
        with open(self.file) as f:
            _data = f.read()
            _json_data = json.loads(_data)
            if "packages" in _json_data:
                _pkgs = _json_data["packages"]
                for package in _pkgs:
                    self.pkgs.append(Package(name=package.get("pkgname"), arch_pkg=package.get("arch"), void_pkg=package.get("void"), debian_pkg=package.get("debian"), fedora_pkg=package.get("fedora"), gentoo_pkg=package.get("gentoo")))
        f.close()


