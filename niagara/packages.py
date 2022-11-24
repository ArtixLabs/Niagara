import subprocess
from deps import *
import platform
import os
import sys
import logging





class Packages():
    def __init__(self):
        self.config = self.set_config()
        logging.basicConfig(filename='niagara.log', encoding='utf-8', format='%(levelname)s -- %(message)s')
    def __generate_config_file(self,dest):
        str = '''
        {
            "packages": [
                {
                    "pkgname": "feh",
                    "arch_pkg": "feh"
                },
                {
                    "pkgname": "picom",
                    "arch_pkg": "picom"
                }
            ],
            "tiers": [
                {
                    "tier": "basic",
                    "arch_pacman_pkgs": [
                        "feh",
                        "picom"
                    ],
                    "arch_aur_pkgs": [
                        "librewolf-bin"
                    ]
                }
            ]
        }'''
        with open(dest, 'w+') as f:
            f.writelines(str)
        f.close()
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
            else:
                logging.fatal('Distribution is not supported.')
        def set_data_file():
            if os.path.exists(os.environ['HOME'] + "/.local/share/niagara/data.json"):
                return os.environ['HOME'] + '/.local/share/niagara/data.json'
            else:
                os.mkdir(os.environ['HOME'] + '/.local/share/niagara')
                self.__generate_config_file(os.environ['HOME'] + '/.local/share/niagara/data.json')
                return os.environ['HOME'] + '/.local/share/niagara/data.json'
        def set_pkgs() -> list[str]:
            x = Deps(set_data_file())
            tmp = []
            for pkg in x.pkgs:
                tmp.append(pkg.arch_pkg)
            return tmp
        return dict([
            ('sudo', set_superuser()),
            ('pkgman', set_pkg_manager()),
            ('data', set_data_file()),
            ('pkgs', set_pkgs())
        ])
    def install_pkgs(self):
        def conc(arr, lip):
            tmp = []
            for x in arr:
                tmp.append(x)
            for x in lip:
                tmp.append(x)
            return tmp
        if self.config['pkgman'] == '/usr/bin/pacman':
            subprocess.call(conc([self.config['sudo'], self.config['pkgman'], '-Syu'], self.config['pkgs']))


