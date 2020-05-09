
#Note to self just wanna kill myself because this was put off to last minute because no one knew what was going on yay!
import tkinter as tk
from tkinter import ttk


#sqlite tingssss
import sqlite3
conn = sqlite3.connect('bidcalc.db') #creates db called bidcalc
c = conn.cursor() #creates db at same location as py file
c.execute('''CREATE TABLE IF NOT EXISTS MATERIALS
            (MaterialName    VARCHAR(30) PRIMARY KEY NOT NULL,
            MaterialPrice    INT NOT NULL,
            MaterialAmount    INT    NOT NULL);''')
c.execute('''CREATE TABLE IF NOT EXISTS EMPLOYEE
            (EmployeeName VARCHAR(30) PRIMARY KEY NOT NULL,
            EmployeeWage     INT    NOT NULL);''')
c.execute('''CREATE TABLE IF NOT EXISTS JOB
            (JobType    VARCHAR(30) PRIMARY KEY NOT NULL,
            JobAddress VARCHAR(50),
            JobTime    INT    NOT NULL);''')

class EmployeeClass:
    def __init__(self, name, wage):
        self.name = name
        self.wage = wage
  
def editEmpScreen():
    editEmpFrame = tk.Toplevel(root)
    addWorkerB = tk.Button(editEmpFrame, text ="Add Worker", command =lambda : addWorkerScreen(editEmpFrame))
    delWorkerB = tk.Button(editEmpFrame, text ="Delete Worker", command =lambda : delWorkerScreen(editEmpFrame))
    addWorkerB.pack()
    delWorkerB.pack()
    
def addWorkerScreen(frame):
    
    addWorkerFrame = tk.Toplevel(frame)
    
    name = ttk.Label(addWorkerFrame, text = "Name of Employee:")
    wage = ttk.Label(addWorkerFrame, text = "Wage of Employee:")
   
    employeeName = tk.StringVar()
    employeeWage = 0

    nameEntry = ttk.Entry(addWorkerFrame, width=60, textvariable = employeeName)
    #nameEntry.insert(0, "bob") yea just spent well over 20 mins to get this to work and I don't even need it for this section...
    
    wageEntry = ttk.Entry(addWorkerFrame, width=60, textvariable = employeeWage)
    name.grid(row = 0, column = 0,)
    wage.grid(row = 1, column = 0,)
    nameEntry.grid(row = 0, column = 1)
    wageEntry.grid(row = 1, column = 1)
    
    def confirmWorker(name, wage):
        sqlite_insert_with_param = '''INSERT INTO EMPLOYEE (EmployeeName, EmployeeWage)  VALUES (?,?)'''
        data_tuple = (name, wage)
        c.execute(sqlite_insert_with_param, data_tuple)
        conn.commit()
        
    confirmB = tk.Button(addWorkerFrame, text = "confirm", command = lambda: confirmWorker(nameEntry.get(), wageEntry.get())) #finish please :) 
    backB = tk.Button(addWorkerFrame, text = "back", command=addWorkerFrame.destroy)
    backB.grid(row = 3, column = 0, padx = 130)
    confirmB.grid(row = 3, column = 1, padx = 5)
def delWorkerScreen(frame):
    delWorkerFrame = tk.Toplevel(frame)
    ttk.Label(delWorkerFrame, text="Select employee you would like to remove from DataBase").pack()
        
    
def jScreen():
    jwindow = tk.Toplevel(root)
    ttk.Label(jwindow,text="Drywall:").pack()
    drywallText = tk.StringVar()
    drywallEntry = ttk.Entry(jwindow, width=60, textvariable = drywallText).pack()
    #dwallAmount = drywallText.get()

def revJobScreen():
    revJobFrame = tk.Toplevel(root)
    ttk.Button(revJobFrame, width=20, text = "open").pack()
    
def editJob():
    editJobFrame = tk.Toplevel(root)
    
root = tk.Tk()
root.title("Only read this if gay")
root.geometry("500x600")
startingframe = ttk.Frame(root, padding ="10 10 10 10")
startingframe.pack(fill=tk.BOTH, expand=True)

#Main Menu buttons probably temporary maybe not well see :)
editJobButt = tk.Button(startingframe, text="Edit Job", command = editJob)
createJButt = tk.Button(startingframe, text ="Create Job", command = jScreen)
editEmpButt = tk.Button(startingframe, text ="Edit Employee", command = editEmpScreen)
revJobButt = tk.Button(startingframe, text = "Review Jobs", command = revJobScreen)
editEmpButt.pack()
createJButt.pack()
revJobButt.pack()
editJobButt.pack()



root.mainloop()