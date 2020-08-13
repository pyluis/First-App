import tkinter as tk
from tkinter import filedialog, Text, messagebox
import os
from Apps import Apps


class FirstGuiApp(object):
    """docstring for ."""

    def __init__(self, master):
        self.master = master
        master.title('Application')

        self.canvas = tk.Canvas(master, height=700, width=700, bg='#348feb')
        self.canvas.pack()

        self.frame = tk.Frame(master, bg='white')
        self.frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=.1)

        self.openAppButton = tk.Button(master, text="Open File", padx=10,
                                       pady=5, fg='white', bg='black',
                                       command=self.addApps)
        self.openAppButton.pack()

        self.runAppsButton = tk.Button(master, text='Run Apps', padx=10,
                                       pady=5, fg='white', bg='black',
                                       command=self.runApps)
        self.runAppsButton.pack()

        self.closeAppsButton = tk.Button(master, text='Close Apps', padx=10,
                                         pady=5, fg='white', bg='black',
                                         command=self.closeApps)
        self.closeAppsButton.pack()

        if os.path.isfile('save.txt'):
            self.apps = Apps.fromTextFile('save.txt')
            for app in self.apps.getApps():
                label = tk.Label(self.frame, text=app.getPath(), bg='gray')
                label.pack()
        else:
            self.apps = Apps()

    def runApps(self):
        for app in self.apps.getApps():
            app.openApp()

    def addApps(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

        filename = filedialog.askopenfilename(initialdir="/",
                                              title='Select File',
                                              filetypes=(("executables", "*.exe"),
                                                         ("all files", "*.*"))
                                              )
        if filename.strip():
            self.apps.addApp(filename)

            for app in self.apps.getApps():
                label = tk.Label(self.frame, text=app.getPath(), bg='gray')
                label.pack()

    def closeApps(self):
        msgBox = messagebox.askyesno('Exit Application',
                                     'Are you sure you want to close the applications?',
                                     icon='warning')
        if msgBox == 'yes':
            for app in self.apps.getApps():
                app.closeApp()
