'''
Folder Sort
This is a GUI Tool to sort a folder
Copyright (c) Nikhil Ramakrishnan
MIT License
Made as a part of B.Tech Semester 1 Project at Bennett University
'''

import sys, shutil,os,time,platform
from os.path import expanduser
import app_interface as mainApp #Program main window
import report #Report Generator
import tkinter as tk
import tkinter.constants as constants
import tkinter.filedialog as filediag
from tkinter.scrolledtext import ScrolledText
import tkinter.messagebox as mbox

version='2.4'
displayinfo="Folder Sort is a program (part of System Cleaner) for Academic Purpose, developed at \
Bennett University, India, by Nikhil Ramakrishnan.\n\nMIT License.\
\n\nTHIS SOFTWARE IS DEVELOPED UNDER THE SYSTEM CLEANER PROJECT AT BENNETT UNIVERSITY \
WITHOUT WARRANTY OF ANY KIND. IN NO EVENT SHALL THE DEVELOPER, COPYRIGHT OWNER, OR \
DISTRIBUTOR BE LIABLE FOR ANY CLAIM, DAMAGES, OR ANY OTHER LIABILITY IN ANY WAY \
OUT OF THE USE OF THIS SOFTWARE."

#Settings
checkupto=100

# Subclass ScrolledText
class ScrolledTextOut(ScrolledText):
    '''This adds functionality to directly insert print statements to tkinter by redifing a few sys functions'''
    def write(self, s):
        '''This function overrides Python's default sys.stdout.write and inserts all print statements
        to the tkinter ScrolledText Box'''
        self.insert(tk.END, s)
        self.update()
        self.see(tk.END)

    def flush(self):
        pass

#Classes for File Sorting
#Directory Class
class Directory(object):

    def __init__(self,path):
        self.path=path

    def isdir(self):
        '''Returns 1 if directory exists, else returns 0'''
        if os.path.isdir(self.path):
            return 1
        else:
            return 0

    def isAllowed(self):
        '''Checks if it is safe to sort the supplied directory'''
        self.flag=0

        #Get User's home Directory
        home = expanduser("~")
        home = os.path.normcase(os.path.realpath(home))

        #Get program's current directory
        #progdir=os.path.normcase(os.path.realpath(os.getcwd()))

        #Initializing lists for non-Windows systems
        fulldirs=[]
        dirs=[home]

        #Windows specific implementations (only excecuted if platform is Windows)
        if platform.system().lower()=='windows':
            winpath = os.environ['WINDIR']
            winpath = os.path.normcase(os.path.realpath(winpath))
            #These are the directories that cannot be sorted at all, including all subdirectories - Only for Windows
            #TODO - The same for Mac and Linux
            fulldirs=[winpath,'c:\\drivers','c:\\program files','c:\\program files(x86)','c:\\intel','c:\\perflogs','c:\\programdata','c:\\system.sav']
            #These directories are the ones that cannot be directly sorted, but subfolders can
            dirs=['c:\\users','c:\\',home]

        normname=os.path.normcase(os.path.realpath(self.path))
        for folder in fulldirs:
            if os.path.commonprefix([normname, folder]) == folder:
                self.flag=1
                break
        for direc in dirs:
            if direc==normname:
                self.flag=1
                break
        if self.flag==1:
            return False
        else:
            return True

    def listdir(self):
        '''Returns a list of files and directories in path'''
        self.source=os.listdir(self.path)
        return self.source

#File Sorter Class
class FileSorter(object):

    def __init__(self,file):
        self.file=file
        self.base,self.ext=os.path.splitext(self.file)
        #rep=report.report() #Report generator
        global checkupto

    def isMovie(self):
        '''If file is greater than 200MB, returns true
        NOTE: This function assumes file supplied is a video'''
        return (os.path.getsize('./'+self.file) > 200000000)

    def isdir(self):
        '''Returns 1 if directory exists, else returns 0'''
        if os.path.isdir(self.file):
            return 1
        else:
            return 0

    def isFormat(self,ls):
        '''Returns 1 if file extension is present in the supplied list'''
        for i in ls:
            if self.file.lower().endswith(i):
                return True
                break

    def moveto(self,filetype):
        '''Move the file to the folder named filetype
        This function will create the folder if it does not exist
        Returns new file name if renamed, else returns None'''
        os.makedirs(filetype,exist_ok=True)
        self.moveto='./'+filetype
        #Check whether file with same name is inside the folder already and rename accordingly
        if os.path.isfile(self.moveto+'/'+self.file):
          for indexcheck in range(1,checkupto):
              if not os.path.isfile(self.moveto+'/'+self.base+'_'+str(indexcheck)+self.ext):
                  finalindex=indexcheck
                  break
          shutil.move(('./'+self.file),(self.moveto+'/'+self.base+'_'+str(finalindex)+self.ext))
          print("Renamed "+self.file+" to "+self.base+"_"+str(finalindex)+self.ext+" and moved to "+filetype)
          return (self.base+"_"+str(finalindex)+self.ext)
        #Normal move if file does not exist already
        else:
            shutil.move(('./'+self.file),self.moveto)
            print("Moved",self.file,"to",filetype)
            return None


#Folder Sort App class
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

        self.root.wm_title("Folder Sort")
        self.root.configure(bg="#8BC34A")
        #self.root.iconbitmap(r'plainicon.ico')
        global version
        button_opt = {'fill': constants.BOTH, 'padx': 10, 'pady': 10}

        # Text
        self.l1 = tk.Label(self.root,text="Folder Sort",font=("Corbel", 25))
        self.l1.configure(fg="#ffffff",bg="#8BC34A")
        self.l1.pack(**button_opt)
        self.l2 = tk.Label(self.root,text="Version "+version,font=("Corbel", 15))
        self.l2.configure(fg="#ffffff",bg="#8BC34A")
        self.l2.pack(fill=constants.BOTH, pady=5,padx=10)

        # Browse Button
        self.browse=tk.Button(self.root, text='Select Directory', command=self.askdirectory)
        self.browse.configure(fg="#212121", bg="#ffffff",activebackground="#689F38",bd=-1,height='2',font=('Corbel',13))
        self.browse.pack(**button_opt)

        # Browse Button options
        self.dir_opt = options = {}
        options['initialdir'] = 'C:\\'
        options['mustexist'] = False
        options['parent'] = self.root
        options['title'] = 'Select Directory to Sort'

        # Quit Button
        self.button = tk.Button(self.root, text = 'Close', command=self.quit)
        self.button.configure(fg="#212121", bg="#ffffff",activebackground="#689F38",bd=-1,height='2',font=('Corbel',13))
        self.button.pack(**button_opt)

        # Text Widget
        self.txt = ScrolledTextOut(self.root, undo=True)
        self.txt['font'] = ('Corbel', '12')
        self.txt.configure(fg="#ffffff", bg="#212121",bd=-1)
        self.txt.pack(**button_opt)
        self.txt.insert(tk.INSERT, "Welcome to Folder Sort Version %s\nSelect a directory to Proceed...\n"%version)

        # Disable scrolledtext
        self.txt.configure(state='disabled')

        # Menu Bar
        menubar = tk.Menu(self.root)
        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label="About", command=self.onInfo)
        menubar.add_cascade(label="Help", menu=helpmenu)
        self.root.config(menu=menubar)

        #Start the frame
        self.root.mainloop()

    # Quit Application
    def quit(self):
        self.root.destroy()
        mainApp.main()

    #About InfoBox
    def onInfo(self):
        global displayinfo
        mbox.showinfo("About Folder Sort", displayinfo)

   #Directory Button Function
    def askdirectory(self): #open the file
        directory = filediag.askdirectory()
        self.FolderSort(directory)

   #Folder Sort Program
    def FolderSort(self,path):
        #Redirect all print statements to GUI
        sys.stdout = self.txt
        #Reenable scrolledtext
        self.txt.configure(state='normal')
        #Disable buttons to prevent accidental clicking
        self.browse.config(state="disabled")
        self.button.config(state="disabled")
        #Setting initial counter and flag variables
        direxists=0
        sortedfiles=0
        securityerror=0
        #Get the home directory of current user
        home = expanduser("~")
        #Create instance of Directory class
        folder=Directory(path)
        #Check is path is valid (will always be but just in case)
        direxists=folder.isdir()
        if direxists==1:
            print("\nDirectory Found")
        else:
            if path!='':
                print("Directory/Path/Library '%s' Not found"%path)
        #Check if it is safe to sort the selected folder
        allowed=folder.isAllowed()
        if not allowed:
            securityerror=1

        #Check conditions before sorting
        if direxists==1 and securityerror==0:
            #We are now sure that directory exists and it is ready to be sorted

            source=folder.listdir() #create a list of files in folder
            #Start sorting if directory is ready
            #Start Timer
            start_time = time.clock()

            self.savedPath = os.getcwd() #Save the current path
            os.chdir(path) #Change the current working directory to the one we will be sorting
            print("Sorting",os.getcwd()+"...")
            #Create instance for report generation (start generating report)
            rep=report.report()
            #Start sorting each file
            for file in source:
                current=FileSorter(file)
                try:
                    #Try sorting each file. if not, then throw a permission warning

                    #Video Files
                    if current.isFormat(['.mp4','.mkv','.avi']):
                        #Move to Movies if file is bigger than 200MB
                        if current.isMovie():
                          res=current.moveto('Movies')
                          rep.insert([file,os.getcwd(),(os.getcwd()+'\\'+'Movies')],res)
                        #Else Move to Videos
                        else:
                          res=current.moveto('Videos')
                          rep.insert([file,os.getcwd(),(os.getcwd()+'\\'+'Videos')],res)
                    #Images
                    elif current.isFormat(['.jpg','.jpeg','.png','.bmp','.svg','.ico','.gif','.tif','.tiff']):
                        res=current.moveto('Pictures')
                        rep.insert([file,os.getcwd(),(os.getcwd()+'\\'+'Pictures')],res)
                    #Songs
                    elif current.isFormat(['.mp3','.m4a','.ogg','.wav','.mpeg','.wma','.aac','.flac']):
                        res=current.moveto('Songs')
                        rep.insert([file,os.getcwd(),(os.getcwd()+'\\'+'Songs')],res)
                    #Documents
                    elif current.isFormat(['.pdf','.doc','.docx','.rtf','.odt','.lyx','.txt','.csv','.html','.htm','.php']):
                        res=current.moveto('Documents')
                        rep.insert([file,os.getcwd(),(os.getcwd()+'\\'+'Documents')],res)
                    #Spreadsheets
                    elif current.isFormat(['.xls','.xlsx','.ods','.xml']):
                        res=current.moveto('Spreadsheets')
                        rep.insert([file,os.getcwd(),(os.getcwd()+'\\'+'Spreadsheets')],res)
                    #Presentations
                    elif current.isFormat(['.ppt','.pptx','.odp']):
                        res=current.moveto('Presentations')
                        rep.insert([file,os.getcwd(),(os.getcwd()+'\\'+'Presentations')],res)
                    #Compressed
                    elif current.isFormat(['.zip','.rar','.tar.gz','.tar','.7z','.tgz','.xip']):
                        res=current.moveto('Compressed')
                        rep.insert([file,os.getcwd(),(os.getcwd()+'\\'+'Compressed')],res)
                    #Programs
                    elif current.isFormat(['.py','.c','.cpp','.java','.pyw']):
                        res=current.moveto('Programs')
                        rep.insert([file,os.getcwd(),(os.getcwd()+'\\'+'Programs')],res)
                    #Applications (Mac, Linux and Android)
                    elif current.isFormat(['.dmg','.app','.apk']):
                        res=current.moveto('Apps')
                        rep.insert([file,os.getcwd(),(os.getcwd()+'\\'+'Apps')],res)
                    #Softwares (exe files)
                    elif current.isFormat(['.exe','.msi','.run']):
                        res=current.moveto('Softwares')
                        rep.insert([file,os.getcwd(),(os.getcwd()+'\\'+'Softwares')],res)
                    #Others (except Directories)
                    else:
                      if not current.isdir() and not current.isFormat(['.ini','.lnk','.sys', '.dat','.dll']):
                          res=current.moveto('Others')
                          rep.insert([file,os.getcwd(),(os.getcwd()+'\\'+'Others')],res)
                    #Count the number of files sorted
                    if not current.isdir() and not current.isFormat(['.ini','.lnk','.sys', '.dat','.dll']):
                      sortedfiles+=1
              #Check for permission errors and display it accordingly
                except PermissionError:
                    print("403:Could not sort",file,"due to insufficient permissions.")
                except FileNotFoundError:
                    print("404:Could not sort",file,"due to insufficient permissions.")
            #Calculate total time elapsed
                elapsed=round((time.clock() - start_time),4)

            #Sorting is done, show success message
            print("\nSorting Complete.")
            print("Sorted",sortedfiles,"files in",elapsed,"seconds.")

            #This tells our report module to stop adding stuff to the report
            report_loc=rep.done()

            #If atleast one file was sorted, show success messagebox
            if sortedfiles!=0:
                #Ask if user wants the report
                result=mbox.askyesno("Sorting Complete", "Sorting Complete. Generate Report?",icon='info')
                if result==True:
                    print("Report successfully generated and saved in "+os.getcwd()+'\\'+report_loc)
                else:
                    rep.delete()

            #Come Back to the saved path directory
            '''The reason this is here is that we can only come back to savedpath when report is done'''
            os.chdir(self.savedPath)

            #Now that processing is done, disable scrolledtext again
            self.txt.configure(state='disabled')
            #Reenable buttons
            self.browse.config(state="normal")
            self.button.config(state="normal")
        #END OF FOLDER SORT FUNCTION
        #All the errors to print if the folder cannot be sorted
        else:
            if path != '':
                print("\nSorry, cannot sort",path)
                print("Reason: ",end='')
                if securityerror==1:
                    print("Security error. The directory you selected could be a system folder.")
                elif direxists==0:
                    print("Directory not found/program does not have permission to access directory")
                else:
                    print("Unknown error. Please contact developer.")
            #We are done printing. Now disable the ScrolledText
            self.txt.configure(state='disabled')
            #Reenable buttons
            self.browse.config(state="normal")
            self.button.config(state="normal")

#Call the app
if __name__ == '__main__':
    app = App()
def main():
    app = App()
