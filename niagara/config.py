import os
import subprocess
from urllib.request import urlretrieve
import json
import pygit2


class Config():
    def __init__(self, file):
        self.file = file

    def operate(self):
        with open(self.file) as f:
            _data = f.read()
            _json_data = json.loads(_data)
            if "config" in _json_data:
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
                    elif opt.get("option") == "scripts":
                        for script in opt.get("val"):
                            if script.get("method"):
                                method = script.get("method")
                            else:
                                method = "git"
                            if method == "curl":
                                print(script.get("url"))
                                urlretrieve(str(script.get("url")), str(script.get("url").rsplit('/', 1).pop()))
                                subprocess.call(['sh', str(script.get("url").rsplit('/', 1).pop())])
                            elif method == "git":
                                pygit2.clone_repository(script.get("url"), str(script.get("url").rsplit('/', 1).pop()))
                                if script.get("trigger"):
                                    subprocess.call(script.get("trigger").split())
                                else:
                                    subprocess.call(['sh', script.get("url") + '/' + 'script.sh'])

