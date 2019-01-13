import webbrowser
import os
import subprocess

path = os.path.dirname(os.path.realpath(__file__))

webbrowser.open(path + '\start.html')

os.system("python server.py")