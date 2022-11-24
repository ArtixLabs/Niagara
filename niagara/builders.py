import json
import packages
import subprocess
import pygit2
import os
import shutil
class Builder():
    def __init__(self):
        self.aur_pkgs = self.get_aur_pkgs()
        os.mkdir('/tmp/niagara')
    def __del__(self):
        shutil.rmtree('/tmp/niagara')
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
    def set_data_file(self, nam):
        if os.path.exists(os.environ['HOME'] + "/.local/share/niagara/{}.json".format(nam)):
            return os.environ['HOME'] + '/.local/share/niagara/{}.json'.format(nam)
        else:
            os.mkdir(os.environ['HOME'] + '/.local/share/niagara')
            self.__generate_config_file(os.environ['HOME'] + '/.local/share/niagara/{}.json'.format(nam))
            return os.environ['HOME'] + '/.local/share/niagara/{}.json'.format(nam)
    def get_aur_pkgs(self):
        pkgs = []
        with open(self.set_data_file('data')) as f:
            _data = f.read()
            _json_data = json.loads(_data)
            _aur_pkgs = _json_data["aur"]
            for pkg in _aur_pkgs:
                pkgs.append(pkg)
        f.close()
        return pkgs

    def iterate_on(self, style):
        x = packages.Packages()
        print(style)
        def build_aur_pkg(pkg):
            def clone_repo(pkg):
                pygit2.clone_repository('https://aur.archlinux.org/{}.git'.format(pkg), '/tmp/niagara/{}'.format(pkg))
            def run_makepkg(pkg):
                subprocess.call(['makepkg', '-si'], cwd="/tmp/niagara/{}".format(pkg))
            clone_repo(pkg)
            run_makepkg(pkg)
        def build_ninja_pkg(pkg):
            def clone_repo(pkg):
                pygit2.clone_repository('https://aur.archlinux.org/{}.git'.format(pkg), '/tmp/niagara/{}'.format(pkg))
            def run_ninja(pkg):
                subprocess.call(['git', 'submodule', 'update', '--init', '--recursive'], cwd="/tmp/niagara/{}".format(pkg))
                subprocess.call(['meson', '--buildtype=release', '.', 'build'], cwd="/tmp/niagara/{}".format(pkg))
                subprocess.call([str(x.config['sudo']), 'ninja', '-C', 'build', 'install'], cwd="/tmp/niagara/{}".format(pkg))
        if style == 'aur':
            for pkg in self.aur_pkgs:
                build_aur_pkg(pkg)
x = Builder()
x.iterate_on('aur')
