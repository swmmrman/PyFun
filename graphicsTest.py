#!/usr/bin/env python3
from os import system
from tkinter import Tk, Label, Frame, Text
import tkinter,requests,re

simName = "Uknown"
url = 'http://rs2.taggrid.org:9100/jsonSimStats'

class SimWatcher:
    def main(self):
        req = requests.get(url).json()
        fps = req['SimFPS']
        up = req["Uptime"]
        upt = re.split(r":|\.", up)
        agents = req['RootAg']
        prims = req['Prims']
        lps = req['ScrLPS']
        (tagV, osV) = req['Version'].split('\n')
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
        self.simStats.delete(1.0,tkinter.END)
        self.simStats.insert(tkinter.INSERT,statsString)
        self.simStats.pack()
        self.master.after(1000, Sim_GUI.main)
        

    def __init__(self, master,name,url):
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
Sim_GUI = SimWatcher(root, simName, url)
root.after(1000, Sim_GUI.main)
root.geometry("400x190+200+200")
root.mainloop()
#if __name__ == "__main__":
    
