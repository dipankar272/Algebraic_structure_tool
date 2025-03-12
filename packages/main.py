from tkinter import *
import itertools
import Ring as r
import Group as g
#a=r.is_ring([0,1,2,3,4,5,6],'+','*',7,7)
#print(a)
def gmatrixset():
    gm1 = Tk()
    gm1.geometry("800x300")
    gm1.title("Group Matrix Set")
    Label(gm1, text="Size of matrix:").place(x=20, y=40)
    Label(gm1, text="Modulo for elements:").place(x=20, y=80)
    Label(gm1, text="Enter the operation:").place(x=20, y=120)
    Label(gm1, text="Enter the mod value for operation:").place(x=20, y=160)
    Label(gm1,text="(Optinal)").place(x=240,y=160)
    n1 = Entry(gm1)  
    n1.place(x=180, y=40)
    n2 = Entry(gm1)
    n2.place(x=180, y=80)
    n3 = Entry(gm1)
    n3.place(x=180, y=120)
    n4 = Entry(gm1)
    n4.place(x=230, y=160)
    def submitf():
        try:
            mod_op=1
            size = int(n1.get())
            mod = int(n2.get())
            operation = str(n3.get())
            mod_op = int(n4.get())
            sets=[]
            mat=[]
            tmat=[]
            for row1 in itertools.product(range(mod), repeat=size):
                for row2 in itertools.product(range(mod), repeat=size):
                  matrix = [[row1[0], row1[1]], [row2[0], row2[1]]]
                  sets.append(list(list(row) for row in matrix))
            result = g.groupabout(sets, operation, mod_op)
            #messagebox.showinfo("Group Check Result", result)
        except ValueError:
            messagebox.showerror("Error", "Please enter valid integer values.")
    # Create submit button
    submit_button = Button(gm1, text="Submit", command=submitf)
    submit_button.place(x=100, y=200)

    gm1.mainloop()
def gcustommatrix():
    gm1 = Tk()
    gm1.geometry("800x300")
    gm1.title("Group Matrix Set")
    Label(gm1, text="Enter the set:").place(x=20, y=40)
    Label(gm1, text="Enter the operation:").place(x=20, y=80)
    Label(gm1, text="Enter the mod value for operation:").place(x=20, y=120)
    Label(gm1,text="(Optinal)").place(x=385,y=120)
    n1 = Entry(gm1)  
    n1.place(x=180, y=40)
    n2 = Entry(gm1)
    n2.place(x=180, y=80)
    n3 = Entry(gm1)
    n3.place(x=230, y=120)
    def submitf():
        try:
            mod_op=1
            sets = list(n1.get())
            operation = str(n2.get())
            mod_op = int(n3.get())
            
        except TypeError:
            messagebox.showerror("Error", "Please renter input.")
    submit_button = Button(gm1, text="Submit", command=submitf)
    submit_button.place(x=100, y=200)
def gset():
    gm1=Tk()
    gm1.geometry("800x300")
    
    Label(gm1, text="start value:").place(x=20, y=40)
    Label(gm1, text="end value:").place(x=20, y=80)
    Label(gm1, text="differnce in value:").place(x=20, y=120)
    Label(gm1, text="Enter the operation:").place(x=20, y=160)
    Label(gm1, text="Enter the mod value for operation:").place(x=20, y=200)
    n1 = Entry(gm1)  
    n1.place(x=180, y=40)
    n2 = Entry(gm1)
    n2.place(x=180, y=80)
    n3 = Entry(gm1)
    n3.place(x=180, y=120)
    n4 = Entry(gm1)
    n4.place(x=180, y=160)
    n5 = Entry(gm1)
    n5.place(x=230, y=200)
    def submitf():
        try:
            mod_op=1
            start= int(n1.get())
            end=int(n2.get())
            diff=int(n3.get())
            operation = str(n4.get())
            mod_op = int(n5.get())
            sets=[]
            for i in range(start,end+1,diff):
                sets.append(i)
            result = g.groupabout(sets, operation, mod_op)
        except TypeError:
            messagebox.showerror("Error", "Please renter input.")
    submit_button = Button(gm1, text="Submit", command=submitf)
    submit_button.place(x=100, y=240)
def gcustomset():
    gm1=Tk()
    gm1.geometry("800x300")
    Label(gm1, text="Enter the set:").place(x=20, y=40)
    Label(gm1, text="Enter the operation:").place(x=20, y=80)
    Label(gm1, text="Enter the mod value for operation:").place(x=20, y=120)
    Label(gm1,text="(Optinal)").place(x=385,y=120)
    n1 = Entry(gm1)  
    n1.place(x=180, y=40)
    n2 = Entry(gm1)
    n2.place(x=180, y=80)
    n3 = Entry(gm1)
    n3.place(x=230, y=120)
    def submitf():
        try:
            mod_op=1
            sets=[]
            tsets=(n1.get().split(","))
            for i in range(0,len(tsets)):
                t=int(tsets[i])
                sets.insert(i,t)
            operation = str(n2.get())
            mod_op = int(n3.get())
            result = g.groupabout(sets, operation, mod_op)
        except ValueError:
            messagebox.showerror("Error", "Please renter input.")
    submit_button = Button(gm1, text="Submit", command=submitf)
    submit_button.place(x=100, y=200)
def gbuttons():
    g1=Tk()
    g1.geometry("1920x1080")
    gb1=Button(g1,text="matrix sets",bg="green",width=10,command=gmatrixset)
    gb1.pack()
    gb2=Button(g1,text="custom matrix",bg="green",width=10,command=gcustommatrix)
    gb2.pack()
    gb3=Button(g1,text="numerical sets",bg="green",width=10,command=gset)
    gb3.pack()
    gb4=Button(g1,text="custom sets",bg="green",width=10,command=gcustomset)
    gb4.pack()
def rmatrixset():
    rm1 = Tk()
    rm1.geometry("800x300")
    rm1.title("Group Matrix Set")
    Label(rm1, text="Size of matrix:").place(x=20, y=40)
    Label(rm1, text="Modulo for elements:").place(x=20, y=80)
    Label(rm1, text="Enter the operation1:").place(x=20, y=120)
    Label(rm1, text="Enter the operation2:").place(x=20, y=160)
    Label(rm1, text="Enter the mod value for operation1:").place(x=20, y=200)
    Label(rm1, text="Enter the mod value for operation2:").place(x=20, y=240)
    Label(rm1,text="(Optinal)").place(x=385,y=240)
    Label(rm1,text="(Optinal)").place(x=385,y=240)
    n1 = Entry(rm1)  
    n1.place(x=180, y=40)
    n2 = Entry(rm1)
    n2.place(x=180, y=80)
    n3 = Entry(rm1)
    n3.place(x=180, y=120)
    n4 = Entry(rm1)
    n4.place(x=180,y=160)
    n5= Entry(rm1)
    n5.place(x=230,y=200)
    n6= Entry(rm1)
    n6.place(x=230,y=240)
    def submitf():
        try:
            mod_op=1
            size = int(n1.get())
            mod = int(n2.get())
            operation1 = str(n3.get())
            operation2 = str(n4.get())
            mod_op1 = int(n5.get())
            mod_op2 = int(n6.get())
            sets=[]
            mat=[]
            tmat=[]
            for row1 in itertools.product(range(mod), repeat=size):
                for row2 in itertools.product(range(mod), repeat=size):
                  matrix = [[row1[0], row1[1]], [row2[0], row2[1]]]
                  sets.append(list(list(row) for row in matrix))
            result = r.is_ring(sets, operation, mod_op)
            messagebox.showinfo("Ring Check Result", result)
        except ValueError:
            messagebox.showerror("Error", "Please enter valid integer values.")
    submit_button = Button(gm1, text="Submit", command=submitf)
    submit_button.place(x=100, y=200)
    rm1.mainloop()
def rcustommatrix():
    rm1 = Tk()
    rm1.geometry("800x300")
    rm1.title("Group Matrix Set")
    Label(rm1, text="Enter the set:").place(x=20, y=40)
    Label(rm1, text="Enter the operation1:").place(x=20, y=80)
    Label(rm1, text="Enter the operation2:").place(x=20, y=120)
    Label(rm1, text="Enter the mod value for operation1:").place(x=20, y=160)
    Label(rm1, text="Enter the mod value for operation2:").place(x=20, y=200)
    Label(rm1,text="(Optinal)").place(x=385,y=160)
    Label(rm1,text="(Optinal)").place(x=385,y=200)
    n1 = Entry(rm1)  
    n1.place(x=180, y=40)
    n2 = Entry(rm1)
    n2.place(x=180, y=80)
    n3 = Entry(rm1)
    n3.place(x=180, y=120)
    n4 = Entry(rm1)
    n4.place(x=180, y=160)
    n5= Entry(rm1)
    n5.place(x=230,y=200)
    def submitf():
        try:
            mod_op=1
            sets = list(n1.get())
            operation1 = str(n2.get())
            operation2 = str(n3.get())
            mod_op1 = int(n4.get())
            mod_op2 = int(n5.get())
        except TypeError:
            messagebox.showerror("Error", "Please renter input.")
    submit_button = Button(gm1, text="Submit", command=submitf)
    submit_button.place(x=100, y=200)
def rset():
    gm1=Tk()
    gm1.geometry("800x300")
    Label(gm1, text="start value:").place(x=20, y=40)
    Label(gm1, text="end value:").place(x=20, y=80)
    Label(gm1, text="differnce in value:").place(x=20, y=120)
    Label(gm1, text="Enter the operation1:").place(x=20, y=160)
    Label(gm1, text="Enter the operation2:").place(x=20, y=200)
    Label(gm1, text="Enter the mod value for operation1:").place(x=20, y=240)
    Label(gm1, text="Enter the mod value for operation2:").place(x=20, y=280)
    Label(gm1,text="(Optinal)").place(x=385,y=240)
    Label(gm1,text="(Optinal)").place(x=385,y=280)
    n1 = Entry(gm1)  
    n1.place(x=180, y=40)
    n2 = Entry(gm1)
    n2.place(x=180, y=80)
    n3 = Entry(gm1)
    n3.place(x=180, y=120)
    n4 = Entry(gm1)
    n4.place(x=180, y=160)
    n5 = Entry(gm1)
    n5.place(x=180, y=200)
    n6 = Entry(gm1)
    n6.place(x=230, y=240)
    n7 = Entry(gm1)
    n7.place(x=230, y=280)
    def submitf():
        try:
            mod_op=1
            start= int(n1.get())
            end=int(n2.get())
            diff=int(n3.get())
            operation1 = str(n4.get())
            operation2=str(n5.get())
            mod_op1 = int(n6.get())
            mod_op2 = int(n7.get())
            sets=[]
            for i in range(start,end+1,diff):
                sets.append(i)
            result = r.ringabout(sets, operation1,operation2, mod_op1,mod_op2)
        except TypeError:
            messagebox.showerror("Error", "Please renter input.")
    submit_button = Button(gm1, text="Submit", command=submitf)
    submit_button.place(x=100, y=315)
def rcustomset():
    gm1=Tk()
    gm1.geometry("800x300")
    Label(gm1, text="Enter the set:").place(x=20, y=40)
    Label(gm1, text="Enter the operation1:").place(x=20, y=80)
    Label(gm1, text="Enter the operation2:").place(x=20, y=120)
    Label(gm1, text="Enter the mod value for operation1:").place(x=20, y=160)
    Label(gm1, text="Enter the mod value for operation2:").place(x=20, y=200)
    Label(gm1,text="(Optinal)").place(x=385,y=160)
    Label(gm1,text="(Optinal)").place(x=385,y=200)
    n1 = Entry(gm1)  
    n1.place(x=180, y=40)
    n2 = Entry(gm1)
    n2.place(x=180, y=80)
    n3 = Entry(gm1)
    n3.place(x=180, y=120)
    n4 =Entry(gm1)
    n4.place(x=230,y=160)
    n5 =Entry(gm1)
    n5.place(x=230,y=200)
    
    def submitf():
        try:
            mod_op=1
            sets=[]
            tsets=(n1.get().split(","))
            for i in range(0,len(tsets)):
                t=int(tsets[i])
                sets.insert(i,t)
            operation1 = str(n2.get())
            operation2 = str(n3.get())
            mod_op1 = int(n4.get())
            mod_op2 = int(n5.get())
            result = r.ringabout(sets, operation1,operation2, mod_op1,mod_op2)
        except ValueError:
            messagebox.showerror("Error", "Please renter input.")
    submit_button = Button(gm1, text="Submit", command=submitf)
    submit_button.place(x=100, y=240)
def rbuttons():
    r1=Tk()
    r1.geometry("1920x1080")
    gb1=Button(r1,text="matrix sets",bg="green",width=10,command=rmatrixset)
    gb1.pack()
    gb2=Button(r1,text="custom matrix",bg="green",width=10,command=rcustommatrix)
    gb2.pack()
    gb3=Button(r1,text="numerical sets",bg="green",width=10,command=rset)
    gb3.pack()
    gb4=Button(r1,text="custom sets",bg="green",width=10,command=rcustomset)
    gb4.pack()
win=Tk()
win.title("Abstract algebra")
win.geometry("1920x1080")
b1=Button(win,text="Groups",bg="green",width=10,command=gbuttons)
b1.pack()
b2=Button(win,text="Rings",bg="green",width=10,command=rbuttons)
b2.pack()
win.mainloop()