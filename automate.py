from __future__ import print_function
import os, sys, subprocess, webbrowser,json

def setup():
    os.system("pip install npm")
    os.system("npm install -g lighthouse")
    os.system("npm install -g lighthouse-ci")

def main():
    setup()
    path = os.path.dirname(os.path.abspath(__file__))
    rules = os.path.join(path,"config.json")
    res = subprocess.call("lighthouse-ci https://www.tamm.abudhabi/journeys/discover-abudhabi-business/?lang=en --report="+ path + " --jsonReport --config-path=" + rules + " --score=1",shell=True)
    assert res == 0
    webbrowser.open(os.path.join(path, "report.html"))

if __name__ == "__main__":
    main()

