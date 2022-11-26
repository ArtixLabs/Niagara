import subprocess
import pygit2
import json

class Generic():
    def __init__(self, file):
        self.file = file

    def operate(self):
        with open(self.file) as f:
            _data = f.read()
            if "source" in json.loads(_data):
                for cmd in json.loads(_data)["source"]:
                    if "link" in cmd:
                        pygit2.clone_repository(cmd["link"], str(cmd["link"].rsplit('/', 1).pop()))
                    if "cmds" in cmd:
                            cmds = cmd["cmds"]
                            for x in cmds:
                                if "cmd" in x:
                                    if "dir" in x:
                                        subprocess.call(x["cmd"].split(), cwd=x["dir"])
                                    else:
                                        subprocess.call(x["cmd"].split())
