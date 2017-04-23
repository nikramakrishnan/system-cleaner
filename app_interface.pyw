'''
System Cleaner Main App
This is a GUI Main App for Folder Sort and Sweep
Copyright (c) Nikhil Ramakrishnan
MIT License
Made as a part of B.Tech Semester 1 Project at Bennett University
'''
#Import the required Modules. Stop with SystemExit if modules not present 
try:
    import subprocess,platform
    import tkinter as tk
    import tkinter.constants as constants
    import tkinter.messagebox as mbox
except ImportError:
    print("Error: Tkinter and/or its modules were not found on system.")
    print("Make sure Python and its modules are installed correctly.")
    print("\nProgram will now exit.")
    raise SystemExit
#Import folder sort and sweep modules. Stop with SystemExit if modules not present
try:
    import folder_sort_GUI as sorter
    import temp_delete_GUI as sweep
except ImportError as e:
    print("Error:",e,"\nMake sure all three programs are in the same folder.")
    print("\nProgram will now exit.")
    raise SystemExit

version='2.2.2'
displayinfo="System Cleaner is a program for Academic Purpose, developed at \
Bennett University, India, by Nikhil Ramakrishnan.\n\nMIT License.\
\n\nTHIS SOFTWARE IS DEVELOPED UNDER THE SYSTEM CLEANER PROJECT AT BENNETT UNIVERSITY \
WITHOUT WARRANTY OF ANY KIND. IN NO EVENT SHALL THE DEVELOPER, COPYRIGHT OWNER, OR \
DISTRIBUTOR BE LIABLE FOR ANY CLAIM, DAMAGES, OR ANY OTHER LIABILITY IN ANY WAY \
OUT OF THE USE OF THIS SOFTWARE."

class FullApp():
    def __init__(self):
        self.root = tk.Tk()

        # Place the window in the center of the screen
        w = 600 # width for the Tk root
        h = 600 # height for the Tk root

        # get screen width and height
        ws = self.root.winfo_screenwidth() # width of the screen
        hs = self.root.winfo_screenheight() # height of the screen

        # calculate x and y coordinates for the Tk root window
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        #Deprecated: This sets geometry and opens frame at random position
        #self.root.geometry('600x600')
        # set the dimensions of the screen and place it
        self.root.geometry('%dx%d+%d+%d' % (w, h, x, y))

        #Set app title
        self.root.wm_title("System Cleaner")
        #Set app background
        self.root.configure(bg="#8BC34A")
        #I'm avoiding this because it gives unexpected errors
        #self.root.iconbitmap(r'plainicon.ico')
        button_opt = {'fill': constants.BOTH, 'padx': 10, 'pady':15}

        #Use the globally defined variable version everywhere in app
        global version
        
        #Text
        self.l1 = tk.Label(text="System Cleaner",font=("Corbel", 25))
        self.l1.configure(fg="#ffffff",bg="#8BC34A")
        self.l1.pack(**button_opt)
        self.l2 = tk.Label(text="Version "+version,font=("Corbel", 15))
        self.l2.configure(fg="#ffffff",bg="#8BC34A")
        self.l2.pack(**button_opt)

        #Blank Space
        #self.l3 = tk.Label(text="",font=("Corbel", 12))
        #self.l3.configure(fg="#ffffff",bg="#8BC34A")
        #self.l3.pack(pady=5)

        #Image
        photo = tk.PhotoImage(file="images/broom1600.gif")
        self.w = tk.Label(self.root, image=photo)
        self.w.configure(bg="#8BC34A")
        self.w.photo = photo
        self.w.pack()
        
        #Blank Space
        #self.l4 = tk.Label(text="",font=("Corbel", 12))
        #self.l4.configure(fg="#ffffff",bg="#8BC34A")
        #self.l4.pack(pady=5)
        
        #Folder Sort Button
        self.sort=tk.Button(self.root, text = 'Folder Sort', command=self.callsort,height='2',font=('Corbel',13))
        self.sort.configure(fg="#212121", bg="#ffffff",bd=-1,activebackground="#689F38")
        self.sort.pack(**button_opt)
        
        #Temp Cleaner button
        self.tempcl=tk.Button(self.root, text = 'Sweep', command=self.callsweep,height='2',font=('Corbel',13))
        self.tempcl.configure(fg="#212121", bg="#ffffff",bd=-1,activebackground="#689F38")
        self.tempcl.pack(**button_opt)

        #System Information button
        self.info=tk.Button(self.root, text = 'System Information', command=self.sysinfo,height='2',font=('Corbel',13))
        self.info.configure(fg="#212121", bg="#ffffff",bd=-1,activebackground="#689F38")
        self.info.pack(**button_opt)
        
        #Quit Button
        self.quit = tk.Button(self.root, text = 'Close',fg="#a1dbcd", bg="#383a39", command=self.quit,height='2',font=('Corbel',13))
        self.quit.configure(fg="#212121", bg="#ffffff",bd=-1,activebackground="#689F38")
        self.quit.pack(**button_opt)
        
        #Menu Bar
        menubar = tk.Menu(self.root)
        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label="About", command=self.onInfo)
        menubar.add_cascade(label="Help", menu=helpmenu)
        self.root.config(menu=menubar)

        #Start the frame
        self.root.mainloop()

    #Call Folder Sort
    def callsort(self):
        self.root.destroy()
        sorter.main()
        
    #Call Sweep
    def callsweep(self):
        self.root.destroy()
        sweep.main()

    #Open sysinfo
    def sysinfo(self):
        if platform.system().lower()=='windows':
            try:
                p = subprocess.Popen(["msinfo32.exe"])
            except FileNotFoundError:
                mbox.showerror("System Information Not Available", "System information is not accessible.\nSoftware may not have permission to access System Information.")
        else:
            mbox.showwarning("Operation Not Supported", "This operation is currently supported only on Windows systems.")
        #returncode=p.wait()
        #print(returncode)
        
    #Quit Application
    def quit(self):
        self.root.destroy()
        
    #About InfoBox
    def onInfo(self):
        global displayinfo
        mbox.showinfo("About System Cleaner", displayinfo)
if __name__=="__main__":
    fullapp=FullApp()
def main():
    fullapp=FullApp()
