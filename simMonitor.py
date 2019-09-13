#!/usr/bin/env python3
# from os import system
from tkinter import Tk, Frame, Text
import tkinter
import requests
import re
import sys

simlist = {
    'Welcome Center': 'http://rs4.taggrid.org:8000/jsonSimStats',
    'Unknown': 'http://rs2.taggrid.org:9100/jsonSimStats'
}

simName = "Uknown"
url = 'http://rs2.taggrid.org:9100/jsonSimStats'


class SimWatcher:
    def main(self):
        statsString = ''
        try:
            req = requests.get(url).json()
            fps = req['SimFPS']
            up = req["Uptime"]
            upt = re.split(r":|\.", up)
            if len(upt) == 4:
                upt.insert(0, 0)
            agents = req['RootAg']
            prims = req['Prims']
            lps = req['ScrLPS']
            (tagV, osV) = req['Version'].split('\n')
            tagV = tagV.strip()
            osV = osV.strip()
            statsString = \
                f"Sim FPS:\t\t {fps}\n"\
                f"Visitors:\t\t {agents}\n"\
                f"Prims: \t\t {prims}\n"\
                f"Script LPS:\t\t {lps}\n"\
                f"Tag Version:\t\t {tagV}\n"\
                f"OpenSim Version:\t{osV}\n\n"\
                f"Sim uptime:\t\t Days:{upt[0]}\n"\
                f"\t\t Hours:{upt[1]}\n"\
                f"\t\t Minutes:{upt[2]}\n"\
                f"\t\t Seconds:{upt[3]}"
        # except ConnectionResetError(args):
        #    statsString = "Sim restarted"
        except requests.exceptions.RequestException:
            statsString = f"Could not connect."
        except ValueError:
            statsString = f"Invalid json."
        finally:
            self.simStats.delete(1.0, tkinter.END)
            self.simStats.insert(tkinter.INSERT, statsString)
            self.simStats.pack()
            self.master.after(1000, Sim_GUI.main)

    def __init__(self, master, name, url):
        statsString = "Loading Stats"
        self.simStats = Text(master)
        self.simStats.insert(tkinter.INSERT, statsString)
        self.simStats.pack()
        self.master = master
        self.url = url
        self.name = name
        self.frame = Frame(self.master)
        master.title(f"Sim stats for {simName}")


root = Tk()
if len(sys.argv) == 2:
    if sys.argv[1] == "w":
        simName = 'Welcome Center'
        url = simlist['Welcome Center']
elif len(sys.argv) == 3:
    simName = sys.argv[1]
    url = sys.argv[2]

Sim_GUI = SimWatcher(root, simName, url)
root.after(1000, Sim_GUI.main)
root.geometry("400x190+200+200")
root.mainloop()
# if __name__ == "__main__":
