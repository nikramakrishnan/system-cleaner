'''
Sweep
This is a GUI Tool to remove unused Temporary Files
Copyright Nikhil Ramakrishnan
Made as a part of B.Tech Semester 1 Project at Bennett University
'''

import sys,tempfile,os,shutil,time
import app_interface as mainApp # Program main Window
import tkinter as tk
import tkinter.constants as constants
from tkinter.scrolledtext import ScrolledText
import tkinter.messagebox as mbox

version='2.2.2'
displayinfo="Sweep is a software (part of System Cleaner) for Academic Purpose, developed at \
Bennett University, India, by Nikhil Ramakrishnan.\n\nAll Rights Reserved.\
\n\nTHIS SOFTWARE IS DEVELOPED UNDER THE SYSTEM CLEANER PROJECT AT BENNETT UNIVERSITY \
WITHOUT WARRANTY OF ANY KIND. IN NO EVENT SHALL THE DEVELOPER, COPYRGIHT OWNER, OR \
DISTRIBUTOR BE LIABLE FOR ANY CLAIM, DAMAGES, OR ANY OTHER LIABILITY IN ANY WAY \
OUT OF THE USE OF THIS SOFTWARE."

# Subclass ScrolledText
class ScrolledTextOut(ScrolledText):
    '''This adds functionality to directly insert print statements to tkinter by redifing a few sys functions'''
    def write(self, s):
        '''This function overrides Python's default sys.stdout.write and inserts all print statements 
        to the tkinter ScrolledText Box'''
        self.insert(tk.INSERT, s)
        self.update()
        self.see(tk.END)
 
    def flush(self):
        pass

#Sweep App Class
class App():
    
    def __init__(self):
        self.root = tk.Tk()

        # Place the window in the center of the screen
        w = 600 # width for the Tk root
        h = 680 # height for the Tk root

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
        
        self.root.wm_title("Sweep")
        self.root.configure(bg="#8BC34A")
        #self.root.iconbitmap(r'plainicon.ico')
        global version
        button_opt = {'fill': constants.BOTH, 'padx': 10, 'pady': 10}
        #Text
        self.l1 = tk.Label(self.root,text="Sweep",font=("Corbel", 25))
        self.l1.configure(fg="#ffffff",bg="#8BC34A")
        self.l1.pack(**button_opt)
        self.l2 = tk.Label(self.root,text="Version "+version,font=("Corbel", 15))
        self.l2.configure(fg="#ffffff",bg="#8BC34A")
        self.l2.pack(**button_opt)
        #Start Button
        self.start=tk.Button(self.root, text="Start Cleaning", command=self.clean)
        self.start.configure(fg="#212121", bg="#ffffff",activebackground="#689F38",bd=-1,height='2',font=('Corbel',13))
        self.start.pack(**button_opt)
        #Quit Button
        self.quit = tk.Button(self.root, text = 'Close', command=self.quit)
        self.quit.configure(fg="#212121", bg="#ffffff",activebackground="#689F38",bd=-1,height='2',font=('Corbel',13))
        self.quit.pack(**button_opt)
        #Text Widget
        self.txt = ScrolledTextOut(self.root, undo=True)
        self.txt['font'] = ('Corbel', '12')
        self.txt.configure(fg="#ffffff", bg="#212121",bd=-1)
        self.txt.pack(**button_opt)
        self.txt.insert(tk.INSERT, "Welcome to Sweep Version %s\nClick start to proceed...\n"%version)
        #Disable scrolledtext
        self.txt.configure(state='disabled')

        #Menu Bar
        menubar = tk.Menu(self.root)
        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label="About", command=self.onInfo)
        menubar.add_cascade(label="Help", menu=helpmenu)
        self.root.config(menu=menubar)
        
        #Start the frame
        self.root.mainloop()
        
    #Quit Application
    def quit(self):
        self.root.destroy()
        mainApp.main()
        
    #About InfoBox
    def onInfo(self):
        global displayinfo
        mbox.showinfo("About Sweep", displayinfo)

    #Temp File deletion Program
    def clean(self):
        #Redirect all print statements to GUI
        sys.stdout = self.txt
        #Reenable scrolledtext
        self.txt.configure(state='normal')
        #Disable buttons to prevent accidental clicking
        self.start.config(state="disabled")
        self.quit.config(state="disabled")
        #Begin Cleaning
        try:
            path=tempfile.gettempdir()
            source=os.listdir(path)
        except:
            print("An error occurred: Could not perform operation. Please contact developer.")
            return
        #Get Current time
        curtime=time.time()
        #Save the current directory
        self.savedPath = os.getcwd()
        #Change current working dir to temp dir
        os.chdir(path)
        #Defining some variables to count stuff
        todel=0
        total=0
        toperms=0
        sizerec=0
        
        #Begin analysis
        print("Now program will analyze",os.getcwd())
        for file in source:
            total+=1
            if os.access((file),os.R_OK):
                try:
                    toperms+=1
                    modtime=os.path.getmtime(file)
                    if (curtime-modtime)>=432000:
                        #Begin Deletion
                        cursize=os.path.getsize(file)
                        print("Deleting ",file,"...",sep="")
                        #os.remove(file)
                        if not os.path.isfile(file):
                            sizerec+=cursize
                        todel+=1
                        #Deletion Complete
                except PermissionError:
                    print("Could not delete",file,"due to insufficient permissions.")
                except FileNotFoundError:
                    print("Could not delete",file,"because not found.")

        #We're done with the deletion part. Now print the success messages.
        sizeround=round((sizerec*0.001),2)
        print("\nTotal files:",total,"\nTotal deleted:",todel,"\nDisk Space Recovered:",sizeround,"Kb")
        if sizerec>0:
            mbox.showinfo("Sweep Complete", "Sweep Complete. "+str(sizeround)+" Kb space recovered.")
        #Disable scrolledtext
        self.txt.configure(state='disabled')
        #Reenable buttons
        self.start.config(state="normal")
        self.quit.config(state="normal")
        #Come Back to the saved path directory
        os.chdir(self.savedPath)
        
#Main Program
if __name__=="__main__":
    app2=App()
def main():
    app2=App()
