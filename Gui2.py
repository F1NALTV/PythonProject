#Remaking the Gui trying to do it better doing this project alone isn't easy tho
import tkinter as tk
from tkinter import ttk
#from SQLHandler import *
import sqlite3
conn = sqlite3.connect('bidcalc.db') #creates db called bidcalc
c = conn.cursor() #creates db at same location as py file   

c.execute('''CREATE TABLE IF NOT EXISTS JOB
            (JobKind VARCHAR(30)    NOT NULL,
            JobAddress VARCHAR(50)    NOT NULL,
            JobTime    VARCHAR(50)    NOT NULL,
            JobPNumber    VARCHAR(50)    NOT NULL,
            JobContractor    VARCHAR(50) NOT NULL,
            JobDate    VARCHAR(30)    NOT NULL,
            JobExp    VARCAR(5),
            JobName    VARCHAR(30)    NOT NULL,
            JobID    INTEGER    PRIMARY KEY AUTOINCREMENT);''')
conn.commit()
class MainMenu(tk.Frame):
    def __init__ (self, parent):
        tk.Frame.__init__(self, parent)
        
        createJobButton = ttk.Button(self, text="Create Job", command=self.createJob)
        createJobButton.grid(row = 0, column = 0)
        

        
        viewJobButton = ttk.Button(self, text="View Jobs", command= self.viewJob)
        viewJobButton.grid(row = 0, column = 1)
    def createJob(self):
        new = tk.Toplevel(self)
        CreateJob(new).grid(row = 0, column = 0)
    def editJob(self):
        new = tk.Toplevel(self)
        EditJob(new).grid(row = 0, column = 0)
    def viewJob(self):
        new = tk.Toplevel(self)
        ViewJob(new).grid(row=0,column=0)
class ViewJob(tk.Frame):
    def editJob(self):
        new = tk.Toplevel(self)
        EditJob(new).grid(row = 0, column = 0)
    
    def __init__(self, parent):
        tk.Frame.__init__(self,parent)
        
        # page two table that displays the entries
        # frame for table so we can put a scrollbar on it
        frame2 = tk.Frame(self)
        frame2.grid(row=3, column=0, sticky=tk.NW, padx=25)
        canvas = tk.Canvas(frame2)
        canvas.grid(row=0, column=0)
        #scrollbar
        vsbar = tk.Scrollbar(frame2, orient=tk.VERTICAL, command=canvas.yview)
        vsbar.grid(row=0, column=1, sticky=tk.NS)
        canvas.configure(yscrollcommand=vsbar.set)
        tableFrame = tk.Frame(canvas)
        
        # this populates the table with headings
        headings = ["JobKind", "JobAddress", "JobTime", "JobPNumber", "JobContractor", "JobDate", "JobExp", "JobName", "JobID"]
        headingRow = 1
        headingColumn = 9
        for z in range(headingColumn):
            for y in range(headingRow):
                for x in range(9):
                    headingLabel = ttk.Label(tableFrame, background = "gray90", borderwidth = 1, width = 30, relief = "ridge", text=headings[z])
                    headingLabel.grid(row=y, column=z, sticky=tk.NSEW)
       
        # this gets the count of entries and then creates the number of rows in the table accordingly
        c.execute("SELECT COUNT (*) FROM JOB;")
        entries = c.fetchall()
        print(entries[0][0])
        tableheight = entries[0][0]
        tablewidth = 9
       
        # this fills the table with the entries saved in the db
        c.execute("SELECT * FROM JOB;")
        items = c.fetchall()
        print(items)
        for i in range(tablewidth): #columns
            for j in range(tableheight): #rows
                itemEntry = ttk.Label(tableFrame, borderwidth = 1, width = 30, relief="ridge", text=items[j][i])
                itemEntry.grid(row=j+1, column=i)

        # Creating canvas window to hold the tableFrame
        canvas.create_window((0,0), window=tableFrame, anchor=tk.NW)
        tableFrame.update_idletasks()  # Needed to make bbox info available
        bbox = canvas.bbox(tk.ALL)  # Get bounding box of canvas

        # Defining the scrollable region as entire canvas with only the desired
        w, h = bbox[2]-bbox[1], bbox[3]-bbox[1]
        dw, dh = int((w/tablewidth) * 9), int((h/(tableheight + 1)) * 6)
        canvas.configure(scrollregion=bbox, width=dw, height=dh)
       
        ttk.Label(self, text="All Jobs").grid(row=0, column=0, sticky=tk.N,)
        
        f1 = tk.Frame(self)
        f1.grid(row=15,column=0)
        ttk.Button(f1, text="back", command = lambda: self.master.destroy()).grid(row = 0, column=0)#,padx =75, pady=25)
        ttk.Button(f1, text="Edit Jobs", command= lambda: self.editJob()).grid(row=0,column=1)
        ttk.Button(f1, text="Refresh Table",command=self.refreshTable).grid(row=0,column=2)
        ttk.Button(f1, text="Delete Entry",command = self.deleteJob).grid(row=0,column=3)
    def refreshTable(self):
        frame2 = tk.Frame(self)
        frame2.grid(row=3, column=0, sticky=tk.NW, padx=25)
        canvas = tk.Canvas(frame2)
        canvas.grid(row=0, column=0)
        #scrollbar
        vsbar = tk.Scrollbar(frame2, orient=tk.VERTICAL, command=canvas.yview)
        vsbar.grid(row=0, column=1, sticky=tk.NS)
        canvas.configure(yscrollcommand=vsbar.set)
        tableFrame = tk.Frame(canvas)
        
        # this populates the table with headings
        headings = ["JobKind", "JobAddress", "JobTime", "JobPNumber", "JobContractor", "JobDate", "JobExp", "JobName", "JobID"]
        headingRow = 1
        headingColumn = 9
        for z in range(headingColumn):
            for y in range(headingRow):
                for x in range(9):
                    headingLabel = ttk.Label(tableFrame, background = "gray90", borderwidth = 1, width = 30, relief = "ridge", text=headings[z])
                    headingLabel.grid(row=y, column=z, sticky=tk.NSEW)
       
        # this gets the count of entries and then creates the number of rows in the table accordingly
        c.execute("SELECT COUNT (*) FROM JOB;")
        entries = c.fetchall()
        print(entries[0][0])
        tableheight = entries[0][0]
        tablewidth = 9
       
        # this fills the table with the entries saved in the db
        c.execute("SELECT * FROM JOB;")
        items = c.fetchall()
        print(items)
        for i in range(tablewidth): #columns
            for j in range(tableheight): #rows
                itemEntry = ttk.Label(tableFrame, borderwidth = 1, width = 30, relief="ridge", text=items[j][i])
                itemEntry.grid(row=j+1, column=i)

        # Creating canvas window to hold the tableFrame
        canvas.create_window((0,0), window=tableFrame, anchor=tk.NW)
        tableFrame.update_idletasks()  # Needed to make bbox info available
        bbox = canvas.bbox(tk.ALL)  # Get bounding box of canvas

        # Defining the scrollable region as entire canvas with only the desired
        w, h = bbox[2]-bbox[1], bbox[3]-bbox[1]
        dw, dh = int((w/tablewidth) * 9), int((h/(tableheight + 1)) * 6)
        canvas.configure(scrollregion=bbox, width=dw, height=dh)
    def deleteJob(self):
        new = tk.Toplevel(self)
        DeleteJob(new).grid(row=0,column=0)
class DeleteJob(tk.Frame):
    def __init__ (self,parent):
        tk.Frame.__init__(self, parent)
        
        ttk.Label(self,text="Please enter ID of Job you want to Delete: ").grid(row = 0, column = 0)
        self.delID = ttk.Entry(self)
        self.delID.grid(row=0,column=1)
        ttk.Button(self, text="back", command = lambda: self.master.destroy()).grid(row = 1, column=0)#,padx =75, pady=25)
        ttk.Button(self, text="Delete Jobs",command = self.combineFuncs(lambda: self.confirmDel(), self.master.destroy)).grid(row=1,column=1)
    def confirmDel(self):
        sqldel = '''DELETE FROM JOB WHERE JobID = ?'''
        ID = self.delID.get()
        c.execute(sqldel, (ID, ))
        conn.commit()
    def combineFuncs(self, *funcs):
        def combinedFunc(*args, **kwargs):
            for f in funcs:
                f(*args, **kwargs)
        return combinedFunc     
class EditJob(tk.Frame):
    def getID(self):
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        rows = cursor.fetchall()
        c.execute("SELECT * FROM JOB")
        IDList = []
        for row in rows:
            data = (row["JobID"])
            IDList.append(data)
            print(IDList)
        '''
        counter = 0
        #cursor = c.execute(''select * FROM JOB;'')
        for i in range(len(cursor.fetchall())):
            return(counter)
            '''
    def __init__ (self, parent):
        tk.Frame.__init__(self, parent)
        
        ttk.Label(self, text="Job ID:").grid(column=0, row=0)
        self.jobID = ttk.Entry(self)
        self.jobID.grid(row=0,column=1)
        
        
        ttk.Label(self, text="Job Type:").grid(row = 1, column=0)
        self.jobKind = ttk.Entry(self, width=40)
        self.jobKind.grid(row=1, column=1)
        
        ttk.Label(self, text="Job Name:").grid(row = 2, column = 0)
        self.jobName = ttk.Entry(self, width=40,)
        self.jobName.grid(row = 2, column = 1)
        
        ttk.Label(self, text="Phone Number:",).grid(row = 3, column = 0)
        self.jobPhoneNumber = ttk.Entry(self, width = 40,)
        self.jobPhoneNumber.grid(row = 3, column = 1)
        
        ttk.Label(self, text="Job Address:",).grid(row = 4, column = 0)
        self.jobAddress = ttk.Entry(self, width = 40,)
        self.jobAddress.grid(row = 4, column = 1)
        
        ttk.Label(self, text="Contractor:",).grid(row = 5, column = 0)
        self.jobContractor = ttk.Entry(self, width = 40,)
        self.jobContractor.grid(row = 5, column = 1)
        
        ttk.Label(self, text="Date:",).grid(row = 6, column = 0)
        self.jobDate = ttk.Entry(self, width = 40,)
        self.jobDate.grid(row = 6, column = 1)
        
        ttk.Label(self, text="Days until Bid expires:",).grid(row = 7, column = 0)
        self.jobExp = ttk.Entry(self, width = 40,)
        self.jobExp.grid(row = 7, column = 1)
        
        ttk.Label(self, text="Hours to complete:").grid(row = 8, column = 0)
        self.jobTime = ttk.Entry(self, width=40)
        self.jobTime.grid(row=8,column=1)
        print(self.getID())
        
        
        ttk.Button(self, text="back", command = lambda: self.master.destroy()).grid(row = 9, column=0)
        ttk.Button(self, text="save", command= self.combineFuncs(lambda: self.editEntry(), self.master.destroy)).grid(row = 9, column=1)
    def editEntry(self):
        entryKind = self.jobKind.get()
        entryName = self.jobName.get()
        entryPNum = self.jobPhoneNumber.get()
        entryAddress = self.jobAddress.get()
        entryContractor = self.jobContractor.get()
        entryDate = self.jobDate.get()
        entryExp = self.jobExp.get()
        entryTime = self.jobTime.get()
        entryID = int(self.jobID.get())
        
        c.execute('''UPDATE JOB SET JobKind=(?), JobAddress=(?), JobTime=(?), JobPNumber=(?), JobContractor=(?),
                JobDate=(?), JobExp=(?), JobName=(?) WHERE JobID =(?);''',
                [entryKind,entryAddress,entryTime,entryPNum,entryContractor,
                entryDate, entryExp, entryName,entryID])
        conn.commit()
    def combineFuncs(self, *funcs):
        def combinedFunc(*args, **kwargs):
            for f in funcs:
                f(*args, **kwargs)
        return combinedFunc 
class CreateJob(tk.Frame):
    def __init__ (self, parent):
        tk.Frame.__init__(self, parent)
        
        ttk.Label(self, text="Job Type:").grid(row = 0, column=0)
        self.jobKind = ttk.Entry(self, width=40)
        self.jobKind.grid(row=0, column=1)
        
        ttk.Label(self, text="Job Name:").grid(row = 1, column = 0)
        self.jobName = ttk.Entry(self, width=40,)
        self.jobName.grid(row = 1, column = 1)
        
        ttk.Label(self, text="Phone Number:",).grid(row = 2, column = 0)
        self.jobPhoneNumber = ttk.Entry(self, width = 40,)
        self.jobPhoneNumber.grid(row = 2, column = 1)
        
        ttk.Label(self, text="Job Address:",).grid(row = 3, column = 0)
        self.jobAddress = ttk.Entry(self, width = 40,)
        self.jobAddress.grid(row = 3, column = 1)
        
        ttk.Label(self, text="Contractor:",).grid(row = 4, column = 0)
        self.jobContractor = ttk.Entry(self, width = 40,)
        self.jobContractor.grid(row = 4, column = 1)
        
        ttk.Label(self, text="Date:",).grid(row = 5, column = 0)
        self.jobDate = ttk.Entry(self, width = 40,)
        self.jobDate.grid(row = 5, column = 1)
        
        ttk.Label(self, text="Days until Bid expires:",).grid(row = 6, column = 0)
        self.jobExp = ttk.Entry(self, width = 40,)
        self.jobExp.grid(row = 6, column = 1)
        
        ttk.Label(self, text="Hours to complete:").grid(row = 7, column = 0)
        self.jobTime = ttk.Entry(self, width=40)
        self.jobTime.grid(row=7,column=1)
        

        
        ttk.Button(self, text="Back", command = lambda: self.master.destroy()).grid(row = 8, column = 0)
        ttk.Button(self, text="Confirm", command=self.combineFuncs(self.dataEntry,lambda : self.master.destroy())).grid(row = 8, column = 1)
    
    def dataEntry(self):
        entryKind = self.jobKind.get()
        entryName = self.jobName.get()
        entryPNum = self.jobPhoneNumber.get()
        entryAddress = self.jobAddress.get()
        entryContractor = self.jobContractor.get()
        entryDate = self.jobDate.get()
        entryExp = self.jobExp.get()
        entryTime = self.jobTime.get()
        
        sql = '''INSERT INTO JOB
                (JobKind, JobAddress, JobTime, JobPNumber, JobContractor,
                JobDate, JobExp, JobName) VALUES (?,?,?,?,?,?,?,?)'''
        c.execute(sql,([entryKind,entryAddress,entryTime,entryPNum,entryContractor,
                entryDate, entryExp, entryName]))
        conn.commit()
        
            #allows for the save button to have multiple commands (saves and clears and goes to home screen all in one button)
    def combineFuncs(self, *funcs):
        def combinedFunc(*args, **kwargs):
            for f in funcs:
                f(*args, **kwargs)
        return combinedFunc  
    def clearEntry(self):
        self.jobKind.set("")
        self.datePur.set("")
        self.makeModel.set("")
        self.warrantyType.set("")
        self.warrantyExp.set("")
        self.comments.set("")
       
root = tk.Tk()
MainMenu(root).grid(row = 0, column = 0)
root.mainloop()
