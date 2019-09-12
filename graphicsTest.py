#!/usr/bin/env python3
from os import system
from tkinter import Tk, Label
import tkinter,requests

simName = "Uknown"
url = 'http://rs2.taggrid.org:9100/jsonSimStats'

class SimWatcher:
    def main(self):
        self.master.clear()
        req = requests.get(self.url).json()
        fps = req['SimFPS']
        up = req["Uptime"]
        statsString = f"Sim FPS:\t{fps}\n"\
            f"Sim uptime:\t {up}"
        simStats = Label(self.master,text=statsString)
        simStats.pack(side='left')
        self.master.after(1000, Sim_GUI.main)
        

    def __init__(self, master,name,url):
        self.master = master
        self.url = url
        self.name = name
        master.title(f"Sim stats for {simName}")


root = Tk()
Sim_GUI = SimWatcher(root, simName, url)
root.after(1000, Sim_GUI.main)
root.mainloop()
#if __name__ == "__main__":
    
