""" limpar terminal independente do SO (Windows, Macos ou linux)"""
import os
import subprocess

def limpar_terminal():
    subprocess.run("clear" if os.name != "nt" else "cls", shell=True)
