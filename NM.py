import imp
from tkinter import *
from tkinter import messagebox
from tkinter.font import BOLD
from turtle import back
from tkinter import ttk
import mysql.connector
  

stations = ['Majestic, Kempegowda Station', 'Mantri Square, Sampige Road', 'Srirampura', 'Mahakavi Kuvempu Road', 'Rajajinagar',
'Mahalakhsmi' ,'Sandal Soap Factory', 'Yeshwantpur', 'Goraguntepalya' , 'Peenya','Peenya Industry', 'Jalahalli','Dasarahalli',
'Nagasandra', 'Chikpete', 'Krishna Rajendra Nagar', 'National College', 'Lalbagh', 'South End Circle', 'Jayanagar', 
'Rashtreeya Vidyalaya Road', 'Banashankari', 'Jaya Prakash Nagar', 'Yelachenahalli', 'Konanakunte Cross', 'Doddakallasandra', 'Vajrahalli',
 'Thalaghattapura', 'Silk Institute' , 'Sir Viswesaraya Station, Central College', 'Vidhan Soudha','Cubbon Park',
 'MG Road', 'Trinity', 'Halasuru','Indiranagar', 'Swami Vivekananda Road', 'Baiyappanahalli', 'KSR Railway Station', 'Magadi Road', 'Hosahalli','Vijayanagar', 'Attiguppe',
 'Gitanjali Nagar', 'Mysore Road','Nayadanahalli', 'Rajarajeshwari',  'Jnanabharathi', 'Pattanagere', 'Kengeri Bus Terminal', 
 'Kengeri']

g1 = ['Majestic, Kempegowda Station', 'Mantri Square, Sampige Road', 'Srirampura', 'Mahakavi Kuvempu Road', 'Rajajinagar',
'Mahalakhsmi' ,'Sandal Soap Factory', 'Yeshwantpur', 'Goraguntepalya' , 'Peenya','Peenya Industry', 'Jalahalli','Dasarahalli',
'Nagasandra' ]

g2 = ['Majestic, Kempegowda Station', 'Chikpete', 'Krishna Rajendra Nagar', 'National College', 'Lalbagh', 'South End Circle', 'Jayanagar', 
'Rashtreeya Vidyalaya Road', 'Banashankari', 'Jaya Prakash Nagar', 'Yelachenahalli', 'Konanakunte Cross', 'Doddakallasandra', 'Vajrahalli',
 'Thalaghattapura', 'Silk Institute' ]

p1 = ['Majestic, Kempegowda Station', 'Sir Viswesaraya Station, Central College', 'Vidhan Soudha','Cubbon Park',
 'MG Road', 'Trinity', 'Halasuru','Indiranagar', 'Swami Vivekananda Road', 'Baiyappanahalli']

p2 = ['Majestic, Kempegowda Station', 'KSR Railway Station', 'Magadi Road', 'Hosahalli','Vijayanagar', 'Attiguppe',
 'Gitanjali Nagar', 'Mysore Road','Nayadanahalli', 'Rajarajeshwari',  'Jnanabharathi', 'Pattanagere', 'Kengeri Bus Terminal', 
 'Kengeri' ]
print("Green Line 1", g1,"\n")
print("Green Line 2", g2,"\n")

print("Purple Line 1", p1,"\n")
print("Purple Line 1", p2,"\n")

maintainance_list =[]
extraPrice_dict ={}

lines = {'Green 1':g1 , 'Green 2':g2, 'Purple 1':p1, 'Purple 2':p2}
route = []
boarding_list = []
destination_list = []
BD = {}

window = Tk()
window.title("Welcome to Namma Metro")
window.geometry('500x500+300+200')
window.configure(bg='#FFF')
window.resizable(False, False)


title1 = Label(window, text = "Namma Metro Fair Calculator",font=('Microsoft yahei UI Light', 25, 'bold'),bg="white", fg="#153462")
title1.pack(pady = 10)


# title = Label(window,text = "Namma Metro Fare Calculator", bg="Purple", fg="White")
# title.pack(pady = 10)



boarding_variable = StringVar(window)
destination_variable = StringVar(window)

boarding_label = Label(window, text= 'Boarding from', font=('Microsoft yahei UI Light', 15), bg='white', fg= 'black').place(x=30,y=80)
drop1 = OptionMenu(window, boarding_variable, *stations)
drop1.place(x=200,y=80)
drop1.config(bg="#FBFBFB", fg="black", width=20)

destination_label = Label(window, text= 'Going to', font=('Microsoft yahei UI Light', 15), bg='white', fg= 'black').place(x=30,y=180)
drop2 = OptionMenu(window, destination_variable, *stations)
drop2.place(x=200,y=180)
drop2.config(bg="#FBFBFB", fg="black", width=20)

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "sharwin123",
    database = "metro_ticket_system"
)
mycursor = mydb.cursor()

sql_command = "INSERT INTO ticket_history(boarding_station, destination_station) values (%s, %s)"
sql_values = [boarding_variable.get(), destination_variable.get()]
mycursor.execute(sql_command,sql_values)

mydb.commit()


def priceCalc():
    global boarding_variable, destination_variable, station, g1,g2,p1,p2, lines, route, destination_list,boarding_list, BD, maintainance_list, extraPrice_dict
    new_window = Toplevel()
    new_window.geometry("700x550")
    new_window.config(bg="#F6F6C9")
    new_window.title("Namma Metro Fair Calculator")
    title1 = Label(new_window, text = "Namma Metro Fair Estimation",font=('Microsoft yahei UI Light', 25),bg="#F6F6C9", fg="#153462")
    title1.pack(pady = 10)
    boarding = boarding_variable.get()
    destination = destination_variable.get()
    if (boarding == destination):
        stops = 0
        messagebox.showerror('Invalid', "Boarding and Destination Stations cannot be the same. ")
        new_window.destroy()
    elif(boarding =="" or destination ==""):
        stops = 0
        messagebox.showerror('Invalid', "Boarding or Destination cannot be empty dumbass.")
        new_window.destroy()
    elif(boarding in maintainance_list):
        stops = 0
        messagebox.showerror('Invalid', "The boarding station that you have selected is under maintainance.")
        new_window.destroy()
    elif(destination in maintainance_list):
        stops = 0
        messagebox.showerror('Invalid', "The destination station that you have selected is under maintainance.")
        new_window.destroy()
    else:
        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "sharwin123",
            database = "metro_ticket_system"
        )
        mycursor = mydb.cursor()

        sql_command = "INSERT INTO ticket_history(boarding_station, destination_station) values (%s, %s)"
        sql_values = [boarding_variable.get(), destination_variable.get()]
        mycursor.execute(sql_command,sql_values)

        mydb.commit()



        for k,v in lines.items():
            if boarding in v:
                BD[boarding] = k
                boarding_list = v[v.index(boarding)::-1]
            if destination in v:
                BD[destination] = k
                destination_list = v[v.index(destination)::-1]
                print(BD)
        if destination in boarding_list:
            route = boarding_list[0:boarding_list.index(destination)+1]

        elif boarding in destination_list:
            route = destination_list[destination_list.index(boarding)::-1]
        else:
            route = boarding_list + destination_list[-2::-1]
        print("Boarding Station" , boarding)
        print("Destination Station" , destination)

        print("Route: ",route,"\n")
        stops = len(route)-1 # excluding boarding station and including destination station
        if stops == 0:
             price = 0
        elif stops == 1:
            price = 9
        elif stops == 2:
            price = 14
        elif stops == 3:
            price = 18
        elif stops > 3:
            price = 18 + (stops - 3)*2
        if destination == "Majestic, Kempegowda Station":
            price = price + 1

        if boarding in extraPrice_dict.keys():
            price+=extraPrice_dict[boarding]
        if destination in extraPrice_dict.keys():
            price+=extraPrice_dict[destination]
        print("Price: ", price)
        


        title_route = Label(new_window, text = "Route Details",font=('Microsoft yahei UI Light', 15,'bold'),bg="#F6F6C9", fg="#153462")
        title_route.pack()

        style=ttk.Style()
        style.theme_use('clam')
        style.configure('Treeview', rowheight=30)
        my_tree = ttk.Treeview(new_window)
        # Define Our Columns
        my_tree['columns']= ("Stop No.", "Station Name", "Stage")

        #Formate Our Columns
        my_tree.column('#0', width =0, stretch=NO)
        my_tree.column("Stop No.", anchor =CENTER, width =80, stretch=False)
        my_tree.column("Station Name",  anchor=CENTER, width=250, stretch=False)
        my_tree.column("Stage", anchor=CENTER, width=100, stretch= NO)

        # Create Headings
        my_tree.heading('#0', text='')
        my_tree.heading("Stop No.", text="Stop No.", anchor =CENTER)
        my_tree.heading("Station Name", text='Station Name' , anchor=CENTER)
        my_tree.heading("Stage",text='Type' ,anchor=CENTER)

        # Add Data
        # my_tree.insert(parent='', index='end', iid = 0, text='', values=(0, 'S0', 'Boarding'))
        # my_tree.insert(parent='', index='end', iid = 1, text='', values=(1, 'S1', ''))
        # my_tree.insert(parent='', index='end', iid = 2, text='', values=(2, 'S2', ''))
        count = 0
        for x in route:
            if route.index(x) == 0:
                my_tree.insert(parent='', index='end', iid = count, text='', values=(count, x, 'Boarding'))
            elif route.index(x) == len(route)-1:
                my_tree.insert(parent='', index='end', iid = count, text='', values=(count, x, 'Destination'))
            else:
                my_tree.insert(parent='', index='end', iid = count, text='', values=(count, x, ''))
            
            count+=1
        my_tree.pack(pady=10)
        def handle_click(event):
            if my_tree.identify_region(event.x, event.y) == "separator":
             return "break"
        my_tree.bind('<Button-1>', handle_click)
        title_pricelabel = Label(new_window, text = "Total Price",font=('Microsoft yahei UI Light', 15,'bold'),bg="#F6F6C9", fg="#153462")
        title_pricelabel.pack()
        title_price = Label(new_window, text = f"₹{price}",font=('Microsoft yahei UI Light', 20),bg="#F6F6C9", fg="#4FA095")
        title_price.pack()
        back_Btn = Button(new_window, text="Go Back", command=new_window.destroy, bg= "#FFF", fg="black",border=0, highlightthickness=0, font=("Microsoft yahei UI Light", 15))
        back_Btn.pack(pady=10)

def stats():
    stat_window = Toplevel()
    stat_window.geometry("500x400")
    stat_window.config(bg="#F6F6C9")
    stat_window.title("Admin Panel")
  
    
    title_route = Label(stat_window, text = "Admin Panel",font=('Microsoft yahei UI Light', 20,'bold'),bg="#F6F6C9", fg="#153462")
    title_route.pack(pady=20)

    def came_stats():
        came_stats_window = Toplevel()
        came_stats_window.geometry("500x600")
        came_stats_window.config(bg="#F6F6C9")
        came_stats_window.title("Namma Metro Fair Calculator")
       
        title_route = Label(came_stats_window, text = "Station as Destination",font=('Microsoft yahei UI Light', 20,'bold'),bg="#F6F6C9", fg="#153462")
        title_route.pack(pady=20)

        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "sharwin123",
            database = "metro_ticket_system"
        )
        mycursor = mydb.cursor()
        mycursor.execute("select destination_station, count(*) as count FROM ticket_history GROUP BY destination_station")
        
        style=ttk.Style()
        style.theme_use('clam')
        style.configure('Treeview', rowheight=30)
        my_tree = ttk.Treeview(came_stats_window)
        # Define Our Columns
        my_tree['columns']= ("Stop No.", "Station Name", "Total Passengers")

        #Formate Our Columns
        my_tree.column('#0', width =0, stretch=NO)
        my_tree.column("Stop No.", anchor =CENTER, width =80, stretch=False)
        my_tree.column("Station Name",  anchor=CENTER, width=250, stretch=False)
        my_tree.column("Total Passengers", anchor=CENTER, width=100, stretch= NO)

        # Create Headings
        my_tree.heading('#0', text='')
        my_tree.heading("Stop No.", text="No.", anchor =CENTER)
        my_tree.heading("Station Name", text='Station Name' , anchor=CENTER)
        my_tree.heading("Total Passengers",text='Total Passengers' ,anchor=CENTER)

        count = -1
        i= 0
        for no_of_people in mycursor: 
            for j in range(len(no_of_people)-1):
                    count+=1
                    if count == 0:
                        continue
                    my_tree.insert(parent='', index='end', iid = i, text='', values=(count, no_of_people[j], no_of_people[j+1]))
                    i+=1
        my_tree.pack(pady=10)
        btn = Button(came_stats_window, width=10, pady = 7, relief="ridge",text = 'Back',bg = '#FFF',background='white',highlightthickness=0, fg = '#153462', border =0, command=came_stats_window.destroy, font=("Microsoft yahei UI Light", 15))
        btn.pack()
    
    def left_stats():
        left_stats_window = Toplevel()
        left_stats_window.geometry("500x600")
        left_stats_window.config(bg="#F6F6C9")
        left_stats_window.title("Namma Metro Fair Calculator")
        
        title_route = Label(left_stats_window, text = "Station as Boarding",font=('Microsoft yahei UI Light', 20,'bold'),bg="#F6F6C9", fg="#153462")
        title_route.pack(pady=20)

        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "sharwin123",
            database = "metro_ticket_system"
        )
        mycursor = mydb.cursor()
        mycursor.execute("select boarding_station, count(*) as count FROM ticket_history GROUP BY boarding_station")
   
        style=ttk.Style()
        style.theme_use('clam')
        style.configure('Treeview', rowheight=30)
        my_tree = ttk.Treeview(left_stats_window)
        # Define Our Columns
        my_tree['columns']= ("Stop No.", "Station Name", "Total Passengers")

        #Formate Our Columns
        my_tree.column('#0', width =0, stretch=NO)
        my_tree.column("Stop No.", anchor =CENTER, width =80, stretch=False)
        my_tree.column("Station Name",  anchor=CENTER, width=250, stretch=False)
        my_tree.column("Total Passengers", anchor=CENTER, width=100, stretch= NO)

        # Create Headings
        my_tree.heading('#0', text='')
        my_tree.heading("Stop No.", text="No.", anchor =CENTER)
        my_tree.heading("Station Name", text='Station Name' , anchor=CENTER)
        my_tree.heading("Total Passengers",text='Total Passengers' ,anchor=CENTER)

        count = -1
        i= 0
        for no_of_people in mycursor: 
            for j in range(len(no_of_people)-1):
                    count+=1
                    if count == 0:
                        continue
                    print('asdfasdfasdf')

                    my_tree.insert(parent='', index='end', iid = i, text='', values=(count, no_of_people[j], no_of_people[j+1]))
                    i+=1
        my_tree.pack(pady=10)

        btn = Button(left_stats_window, width=10, pady = 7, relief="ridge",text = 'Back',bg = '#FFF',background='white',highlightthickness=0, fg = '#153462', border =0, command=left_stats_window.destroy, font=("Microsoft yahei UI Light", 15))
        btn.pack()

    def unavailable():
        global stations, maintainance_list
        unwindow = Toplevel()
        unwindow.geometry("500x600")
        unwindow.config(bg="#F6F6C9")
        unwindow.title("Namma Metro System")
        # image1 = ImageTk.PhotoImage(Image.open("C:/Users/sukes/Downloads/images.png"))
        # left_stats_window.iconphoto(False, image1)
        title_route = Label(unwindow, text = "Stations under maintainance",font=('Microsoft yahei UI Light', 20,'bold'),bg="#F6F6C9", fg="#153462")
        title_route.pack(pady=20)

        style=ttk.Style()
        style.theme_use('clam')
        style.configure('Treeview', rowheight=30)
        my_tree = ttk.Treeview(unwindow)
        # Define Our Columns
        my_tree['columns']= ("No.", "Station Name")

        #Formate Our Columns
        my_tree.column('#0', width =0, stretch=NO)
        my_tree.column("No.", anchor =CENTER, width =0, stretch=False)
        my_tree.column("Station Name",  anchor=CENTER, width=250, stretch=False)


        # Create Headings
        my_tree.heading('#0', text='')
        my_tree.heading("No.", text="No.", anchor =CENTER)
        my_tree.heading("Station Name", text='Station Name' , anchor=CENTER)

        count = 1
        for station_name in maintainance_list:
            my_tree.insert(parent='', index='end', iid = count, text='', values=(station_name))
            count+=1
        my_tree.pack(pady=10)





        title_route = Label(unwindow, text = "Select Station",font=('Microsoft yahei UI Light', 15,'bold'),bg="#F6F6C9", fg="#153462")
        title_route.pack(pady=2)
        
        maintainance_variable = StringVar(unwindow)
        drop1 = OptionMenu(unwindow, maintainance_variable, *stations)
        drop1.pack(pady=20)
        drop1.config(bg="#FBFBFB", fg="black", width=20)
        def add_maintainance():
            global maintainance_list
            if maintainance_variable.get() not in maintainance_list:
                maintainance_list.append(maintainance_variable.get())
        
                my_tree.insert(parent='', index='end', values=(maintainance_list.index(maintainance_list[-1])+1,maintainance_list[-1]))
            
            print(maintainance_list)
        def remove_maintainance():
            global maintainance_list
            if maintainance_variable.get() in maintainance_list:
                del_index = maintainance_list.index(maintainance_variable.get())+1
                maintainance_list.remove(maintainance_variable.get())
                my_tree.delete(f"I00{del_index}")
            print(maintainance_list)

        btn = Button(unwindow, width=5, pady = 7, relief="ridge",text = 'add',bg = '#FFF',background='white',highlightthickness=0, fg = '#153462', border =0, command=add_maintainance, font=("Microsoft yahei UI Light", 15))
        btn.pack(pady=5)
        btn1 = Button(unwindow, width=5, pady = 7, relief="ridge",text = 'remove',bg = '#FFF',background='white',highlightthickness=0, fg = '#153462', border =0, command=remove_maintainance, font=("Microsoft yahei UI Light", 15))
        btn1.pack()
    def extraFare():
        global extraPrice_dict, stations
        extraW = Toplevel()
        extraW.geometry("500x700")
        extraW.config(bg="#F6F6C9")
        extraW.title("Namma Metro System")
        extraW.resizable(False, False)
     
        title_route = Label(extraW, text = "Add or Remove extra are",font=('Microsoft yahei UI Light', 20,'bold'),bg="#F6F6C9", fg="#153462")
        title_route.pack(pady=20)

        style=ttk.Style()
        style.theme_use('clam')
        style.configure('Treeview', rowheight=30)
        my_tree = ttk.Treeview(extraW)
        # Define Our Columns
        my_tree['columns']= ("No.", "Station Name", "Extra Fare")

        #Formate Our Columns
        my_tree.column('#0', width =0, stretch=NO)
        my_tree.column("No.", anchor =CENTER, width =0, stretch=False)
        my_tree.column("Station Name",  anchor=CENTER, width=250, stretch=False)
        my_tree.column("Extra Fare",  anchor=W, width=100, stretch=False)



        # Create Headings
        my_tree.heading('#0', text='')
        my_tree.heading("No.", text="No.", anchor =CENTER)        
        my_tree.heading("Station Name", text='Station Name' , anchor=CENTER)
        my_tree.heading("Extra Fare", text='Extra Fare' , anchor=W)

        # count = 1
        # for station_name in maintainance_list:
        #     my_tree.insert(parent='', index='end', iid = count, text='', values=(station_name))
        #     count+=1
        my_tree.pack(pady=10)


        title_route = Label(extraW, text = "Select Station",font=('Microsoft yahei UI Light', 15,'bold'),bg="#F6F6C9", fg="#153462")
        title_route.pack(pady=2)
        
        extra_fare_station = StringVar(extraW)
        drop1 = OptionMenu(extraW, extra_fare_station, *stations)
        drop1.pack(pady=15)
        drop1.config(bg="#FBFBFB", fg="black", width=20)


        title_route = Label(extraW, text = "Select extra fare",font=('Microsoft yahei UI Light', 15,'bold'),bg="#F6F6C9", fg="#153462")
        title_route.pack(pady=10)
        

        extraFare_lis = [0,1,2,3,4,5,6,7,8,9,10]
        extra_fare_variable = IntVar(extraW)
        drop2 = OptionMenu(extraW, extra_fare_variable, *extraFare_lis)
        drop2.pack(pady=10)
        drop2.config(bg="#FBFBFB", fg="black", width=1)


        def add_fare():
            global extraPrice_dict
            if extra_fare_variable.get() == "":
                messagebox.showerror('Invalid', "The station is blank")
            else:
                if(extra_fare_variable.get() == 0 and (extra_fare_station.get() in extraPrice_dict.keys())):
                    del_index = list(extraPrice_dict.keys()).index(extra_fare_station.get())+1
                    del extraPrice_dict[extra_fare_station.get()]
                    my_tree.delete(f"I00{del_index}")
                if (extra_fare_station.get() not in extraPrice_dict) and (extra_fare_variable.get() != 0):
                    extraPrice_dict[extra_fare_station.get()] = extra_fare_variable.get()
                    my_tree.insert(parent='', index='end', values=("", extra_fare_station.get(), extra_fare_variable.get()))
            
            
    
        btn = Button(extraW, width=10, pady = 7, relief="ridge",text = 'Make changes',bg = '#FFF',background='white',highlightthickness=0, fg = '#153462', border =0, command=add_fare, font=("Microsoft yahei UI Light", 15))
        btn.pack(pady=5)

    
    btn = Button(stat_window, width=27, pady = 7, relief="ridge",text = 'Boarding Station Stats',bg = '#FFF',background='white',highlightthickness=0, fg = '#153462', border =0, command=came_stats, font=("Microsoft yahei UI Light", 15))
    btn.pack(pady=10)
    btn2 = Button(stat_window, width=27, pady = 7, relief="ridge",text = 'Destination Station Stats',bg = '#FFF',background='white',highlightthickness=0, fg = '#153462', border =0, command=left_stats, font=("Microsoft yahei UI Light", 15))
    btn2.pack(pady=10)
    btn3 = Button(stat_window, width=27, pady = 7, relief="ridge",text = 'Maintenance Function',bg = '#FFF',background='white',highlightthickness=0, fg = '#153462', border =0, command=unavailable, font=("Microsoft yahei UI Light", 15))
    btn3.pack(pady=10)
    btn4 = Button(stat_window, width=27, pady = 7, relief="ridge",text = 'Change Fare',bg = '#FFF',background='white',highlightthickness=0, fg = '#153462', border =0, command=extraFare, font=("Microsoft yahei UI Light", 15))
    btn4.pack(pady=10)
    btn5 = Button(stat_window, width=10, pady = 7, relief="ridge",text = 'Back',bg = '#FFF',background='white',highlightthickness=0, fg = '#153462', border =0, command=stat_window.destroy, font=("Microsoft yahei UI Light", 15))
    btn5.pack(pady=20)


    mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "sharwin123",
            database = "metro_ticket_system"
    )
    mycursor = mydb.cursor()
    mycursor.execute("select destination_station, count(*) as count FROM ticket_history GROUP BY destination_station")
        
        

print("Extra Fare:", extraPrice_dict)
print("Maintenance List", maintainance_list)

btn = Button(window, width=27, pady = 7, relief="ridge",text = 'Get Fare Estimation',bg = '#FFF',background='white',highlightthickness=0, fg = '#153462', border =0, command=priceCalc, font=("Microsoft yahei UI Light", 15))
btn.place(x=100, y=280)
btn2 = Button(window, width=10, height=4,pady = 7, relief="ridge",text = 'Admin Panel',bg = '#FFF',background='white',highlightthickness=0, fg = '#153462', border =0, command=stats, font=("Microsoft yahei UI Light", 15))
btn2.place(x=180, y=340)
btn3 = Button(window, width=10, pady = 7, relief="ridge",text = 'Back',bg = '#FFF',background='white',highlightthickness=0, fg = '#153462', border =0, command=window.destroy, font=("Microsoft yahei UI Light", 15))
btn3.place(x=180, y=450)

mainloop()
