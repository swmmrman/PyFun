#!/usr/bin/env python3
# from os import system
from tkinter import Tk, Frame, Text, Menu
import tkinter
import sys
import re
import requests

SIM_LIST = {
    'Welcome Center': 'http://rs4.taggrid.org:8000/jsonSimStats',
    'Unknown': 'http://rs2.taggrid.org:9100/jsonSimStats'
}


class SimWatcher:
    """  Just a class to hold the functions."""

    def fetch(self):
        """
        Fetch funtion that fetches the stats. Probably should call this fetch.
        """
        stats_string = ''
        try:
            req = requests.get(self.url).json()
            up_time = req["Uptime"]
            upt = re.split(r":|\.", up_time)
            if len(upt) == 4:
                upt.insert(0, 0)
            lps = req['ScrLPS']
            pki = req['PktsIn']
            pnd_down = req['PendDl']
            pko = req['PktOut']
            pnd_up = req['PendUl']
            stc = req['XEngine Thread Count']
            utc = req['Util Thread Count']
            (tag_v, os_v) = req['Version'].split('\n')
            tag_v = tag_v.strip()
            os_v = os_v.strip()
            stats_string = \
                f"Sim FPS:\t\t\t {req['SimFPS']}\n"\
                f"Visitors:\t\t\t {req['RootAg']}\n"\
                f"Prims Total/Reg/Mesh: \t\t {req['Prims']}/"\
                f"{req['GeoPrims']}/{req['Mesh Objects']}\n"\
                f"Script LPS:\t\t\t {lps}\n"\
                f"Script Threads:\t\t\t {stc}\n"\
                f"Util Thread Count:\t\t\t {utc}\n"\
                f"Packets Int/Pend\t\t\t {pki}/{pnd_down}\n"\
                f"Packets Out/Pend\t\t\t {pko}/{pnd_up}\n"\
                f"Tag Version:\t\t\t {tag_v}\n"\
                f"OpenSim Version:\t\t\t {os_v}\n\n"\
                f"Sim uptime:\t\t Days:{upt[0]}\n"\
                f"\t\t Hours:{upt[1]}\n"\
                f"\t\t Minutes:{upt[2]}\n"\
                f"\t\t Seconds:{upt[3]}"
        # except ConnectionResetError(args):
        #    stats_string = "Sim restarted"
        except requests.exceptions.RequestException:
            self.update("Could not connect.")
        except ValueError:
            self.update(F"Invalid json.")
        finally:
            self.update(stats_string)

    def update(self, info_string):
        """ Update the display.  Take a string as and displays it to screen """
        self.sim_stats.delete(1.0, tkinter.END)
        self.sim_stats.insert(tkinter.INSERT, info_string)
        self.sim_stats.pack()
        self.master.after(1000, SIM_GUI.fetch)

    def change_sim(self):
        """change the active sim"""
        print(f"{self.name}")

    def __init__(self, master, name, target):
        stats_string = "Loading Stats"
        self.master = master
        self.top_menu = Menu(self.master)
        self.file_menu = Menu(self.top_menu, tearoff=0)
        self.file_menu.add_command(label="Change", command=self.change_sim)
        self.top_menu.add_cascade(label="File", menu=self.file_menu)
        self.sim_stats = Text(master)
        self.sim_stats.insert(tkinter.INSERT, stats_string)
        self.sim_stats.pack()
        self.url = target
        self.name = name
        self.frame = Frame(self.master)
        self.master.config(menu=self.top_menu)
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
ROOT.after(1000, SIM_GUI.fetch)
ROOT.geometry("440x265+200+200")
ROOT.mainloop()
