import json

class Package:
    def __init__(self, name: str, arch_pkg: str):
        self.name = name
        self.arch_pkg = arch_pkg

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
                self.pkgs.append(Package(package.get("pkgname"), package.get("arch_pkg")))

        f.close()



