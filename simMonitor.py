#!/usr/bin/env python3
# from os import system
from tkinter import Tk, Frame, Text
import tkinter
import sys
import re
import requests

SIM_LIST = {
    'Welcome Center': 'http://rs4.taggrid.org:8000/jsonSimStats',
    'Unknown': 'http://rs2.taggrid.org:9100/jsonSimStats'
}


class SimWatcher:
    def main(self):
        stats_string = ''
        try:
            req = requests.get(self.url).json()
            fps = req['SimFPS']
            up_time = req["Uptime"]
            upt = re.split(r":|\.", up_time)
            if len(upt) == 4:
                upt.insert(0, 0)
            agents = req['RootAg']
            prims = req['Prims']
            lps = req['ScrLPS']
            (tag_v, os_v) = req['Version'].split('\n')
            tag_v = tag_v.strip()
            os_v = os_v.strip()
            stats_string = \
                f"Sim FPS:\t\t {fps}\n"\
                f"Visitors:\t\t {agents}\n"\
                f"Prims: \t\t {prims}\n"\
                f"Script LPS:\t\t {lps}\n"\
                f"Tag Version:\t\t {tag_v}\n"\
                f"OpenSim Version:\t{os_v}\n\n"\
                f"Sim uptime:\t\t Days:{upt[0]}\n"\
                f"\t\t Hours:{upt[1]}\n"\
                f"\t\t Minutes:{upt[2]}\n"\
                f"\t\t Seconds:{upt[3]}"
        # except ConnectionResetError(args):
        #    stats_string = "Sim restarted"
        except requests.exceptions.RequestException:
            stats_string = f"Could not connect."
        except ValueError:
            stats_string = f"Invalid json."
            print(f"{self.url}")
        finally:
            self.sim_stats.delete(1.0, tkinter.END)
            self.sim_stats.insert(tkinter.INSERT, stats_string)
            self.sim_stats.pack()
            self.master.after(1000, SIM_GUI.main)

    def __init__(self, master, name, target):
        stats_string = "Loading Stats"
        self.sim_stats = Text(master)
        self.sim_stats.insert(tkinter.INSERT, stats_string)
        self.sim_stats.pack()
        self.master = master
        self.url = target
        self.name = name
        self.frame = Frame(self.master)
        master.title(f"Sim stats for {SIM_NAME}")


ROOT = Tk()
if len(sys.argv) == 2:
    if sys.argv[1] == "w":
        SIM_NAME = 'Welcome Center'
        URL = SIM_LIST['Welcome Center']
elif len(sys.argv) == 3:
    SIM_NAME = sys.argv[1]
    URL = sys.argv[2]
else:
    SIM_NAME = "Uknown"
    URL = 'http://rs2.taggrid.org:9100/jsonSimStats'

SIM_GUI = SimWatcher(ROOT, SIM_NAME, URL)
ROOT.after(1000, SIM_GUI.main)
ROOT.geometry("400x190+200+200")
ROOT.mainloop()
# if __name__ == "__main__":
