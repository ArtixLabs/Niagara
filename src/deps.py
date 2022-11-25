import json
import pygit2
import requests
import subprocess
import platform
import os
import logging
from urllib.request import urlretrieve

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
            else:
                logging.fatal('Distribution "{}" is not supported.'.format(info["ID"]))
        def set_data_file():
            if os.path.exists(os.environ['HOME'] + "/.local/share/niagara/database.json"):
                return os.environ['HOME'] + '/.local/share/niagara/database.json'
            else:
                os.mkdir(os.environ['HOME'] + '/.local/share')
                os.mkdir(os.environ['HOME'] + '/.local/share/niagara')
                generate_database_file(os.environ['HOME'] + '/.local/share/niagara/database.json')
                return os.environ['HOME'] + '/.local/share/niagara/database.json'
        return dict([
            ('sudo', set_superuser()),
            ('pkgman', set_pkg_manager()),
            ('data', set_data_file()),
            ('pkgs', self.set_pkgs())
            ])
    def set_pkgs(self) -> dict:
        x = Deps(os.environ['HOME'] + '/.local/share/niagara/database.json')
        arch = []
        void = []
        for pkg in x.pkgs:
            arch.append({'pkgname': pkg.name, 'pkg': pkg.arch_pkg})
            void.append({'pkgname': pkg.name, 'pkg': pkg.void_pkg})
        return dict([
            ('arch', arch),
            ('void', void)
            ])
    def generate_full_cmd(self, path, opt):
        cmds = []
        for x in self.config['pkgs']['{}'.format(opt)]:
            cmds.append(x['pkgname'])
        vuln = Pkgs(path)
        pkgs = []
        for pkg in vuln.pkgs:
            if pkg.name in cmds:
                pkgs.append(pkg.name)
        return pkgs

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

def generate_database_file(path):
    templ = """
{
        "packages": [
            {
                "pkgname": "picom",
                "arch": "picom",
                "void": "picom"
                },
            {
                "pkgname": "kitty",
                "arch": "kitty",
                "void": "kitty"
                },
            {
                "pkgname": "alacritty",
                "arch": "alacritty",
                "void": "alacritty"
                },
            {
                "pkgname": "neofetch",
                "arch": "neofetch",
                "void": "neofetch"
                },
            {
                "pkgname": "feh",
                "arch": "feh",
                "void": "feh"
                },
            {
                "pkgname": "emacs",
                "arch": "emacs",
                "void": "emacs"
                },
            {
                "pkgname": "vim",
                "arch": "vim",
                "void": "vim"
                },
            {
                "pkgname": "neovim",
                "arch": "neovim",
                "void": "neovim"
                },
            {
                "pkgname": "rofi",
                "arch": "rofi",
                "void": "rofi"
                },
            {
                "pkgname": "flameshot",
                "arch": "flameshot",
                "void": "flameshot"
                },
    {
            "pkgname": "doas",
            "arch": "opendoas",
            "void": "opendoas"
            },
    {
            "pkgname": "dunst",
            "arch": "dunst",
            "void": "dunst"
            },
    {
            "pkgname": "firefox",
            "arch": "firefox",
            "void": "firefox"
            },
    {
            "pkgname": "ripgrep",
            "arch": "ripgrep",
            "void": "ripgrep"
            },
    {
            "pkgname": "mpv",
            "arch": "mpv",
            "void": "mpv"
            },
    {
            "pkgname": "dmenu",
            "arch": "dmenu",
            "void": "dmenu"
            },
    {
            "pkgname": "lynx",
            "arch": "lynx",
            "void": "lynx"
            },
    {
            "pkgname": "fzf",
            "arch": "fzf",
            "void": "fzf"
            },
    {
            "pkgname": "bat",
            "arch": "bat",
            "void": "bat"
            },
    {
            "pkgname": "ffmpeg",
            "arch": "ffmpeg",
            "void": "ffmpeg"
            },
    {
            "pkgname": "youtube-dl",
            "arch": "youtube-dl",
            "void": "youtube-dl"
            },
    {
            "pkgname": "",
            "arch": "",
            "void": ""
            }
    ]
}
"""
    with open(path, 'w+') as f:
        f.writelines(templ)
    f.close()

class Package:
    def __init__(self, name: str, arch_pkg: str, void_pkg: str):
        self.name = name
        self.arch_pkg = arch_pkg
        self.void_pkg = void_pkg
class UPackage:
    def __init__(self, name: str):
        self.name = name
class Deps:
    def __init__(self, file):
        self.file = file
        self.pkgs = []
        self.read_to_pkg()
    def read_to_pkg(self):
        with open(self.file) as f:
            _data = f.read()
            _json_data = json.loads(_data)
            _pkgs = _json_data["packages"]
            for package in _pkgs:
                self.pkgs.append(Package(name=package.get("pkgname"), arch_pkg=package.get("arch"), void_pkg=package.get("void")))
        f.close()

class Config():
    def __init__(self, file):
        self.file = file

    def operate(self):
        with open(self.file) as f:
            _data = f.read()
            _json_data = json.loads(_data)
            _config_opts = _json_data["config"]
            for opt in _config_opts:
                if opt.get("option") == "wallpaper": # ADD DEP CHECK FOR PKGS
                    file = str(opt.get("val").rsplit('/', 1).pop())
                    if os.path.exists(os.environ['HOME'] + '/.wallpaper'):
                        urlretrieve(str(opt.get("val")), file)
                        os.replace(file, os.environ['HOME'] + '/.wallpaper/' + file)
                    else:
                        os.mkdir(os.environ['HOME'] + '/.wallpaper')
                        urlretrieve(str(opt.get("val")), file)
                        os.replace(file, os.environ['HOME'] + '/.wallpaper/' + file)
                    subprocess.call(['feh', '--bg-scale', os.environ['HOME'] + '/.wallpaper/' + file])
                elif opt.get("option") == "dotfile":
                    for x in opt.get("val"):
                        pygit2.clone_repository(x, os.environ['HOME'] + '/.config/' + str(x.rsplit('/', 1).pop()))

class Pkgs:
    def __init__(self, file):
        self.file = file
        self.pkgs = []
        self.read_to_pkg()
    def read_to_pkg(self):
        with open(self.file) as f:
            _data = f.read()
            _json_data = json.loads(_data)
            _pkgs = _json_data["packages"]
            for package in _pkgs:
                self.pkgs.append(UPackage(name=package))
        f.close()

