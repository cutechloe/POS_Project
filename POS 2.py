from tkinter import *
import csv

def check(): 
    Meatpie = MeatpieVar.get()
    MeatpiePri = Meatpie[-3:]
    
    Chickenpie = ChickenpieVar.get() 
    ChickenpiePri = Chickenpie[-3:]
    
    Fishpie = FishpieVar.get()
    print(Fishpie)
    FishpiePri = Fishpie[-3:]
    
    Chips = ChipsVar.get()
    ChipsPri = Chips[-3:]
    
    Water = WaterVar.get()
    WaterPri = Water[-3:]
    
    Softdrinks = SoftdrinksVar.get()
    SoftdrinksPri = Softdrinks[-3:]
    
    Pizza = PizzaVar.get()
    PizzaPri = Pizza[-3:]
    
    Sharwarma = SharwarmaVar.get()
    SharwarmaPri = Sharwarma[-3:]
    
    Icecream = IcecreamVar.get()
    IcecreamPri = Icecream[-3:]
    
    total = 5000#int(IcecreamPri) #+ int(ChickenpiePri) #+ int(FishpiePri)
    #total = int(MeatpiePri) + int(FishpiePri) + int(ChickenpiePri) + int(ChipsPri) + int(WaterPri) + int(SoftdrinksPri) + int(PizzaPri) + int(SharwarmaPri) + int(IcecreamPri)

    
    Item = "My purchases are:\n" + Meatpie + "\n" + Chickenpie + "\n" + Fishpie + "\n" + Chips + "\n"+ Water + "\n" + Softdrinks + "\n" + Pizza + "\n" + Sharwarma + "\n" + Icecream + "Total Cost:" + str(total)
    print(Item)  
    result = Label(w,text = Item, bg= "Yellow").place(x=15, y=20)
    
    MoneyVar = StringVar()
    MoneyVar.set("Cash")
    
    EatingVar = StringVar()
    EatingVar.set("Takeout")
    
    store = "Lovely Tasty Snacks"
    data = [store + "\n" + Item]
    with open("Snacks_sales.csv", "a", encoding="UTF-8", newline='') as f:
        writer = csv.writer(f)
        #writer.writerow(header)
        writer.writerow(data)
    
    
    
    print(data)
        
    
def calculate_change():
    Amount_paid = Amount_paidVar.get()
    Item_cost = Item_costVar.get()
    change = int(Amount_paid) - int(Item_cost)
    
    Label(w,text = change, bg = "Green",fg= "white", width = "12").place(x="120",y="250")
    
    header = ["change", "Item_cost", "Amount_paid"]
    data = [[Amount_paid, Item_cost,change ]]  
    
    with open("Snacks_sales.csv", "a", encoding="UTF-8", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(data)
    
    







w = Tk()
w.title("POS")
w.geometry("700x400")
w.configure(bg = "grey")

MeatpieVar = StringVar()
ChickenpieVar = StringVar()
FishpieVar = StringVar()
ChipsVar = StringVar()
WaterVar = StringVar()
SoftdrinksVar = StringVar()
PizzaVar = StringVar()
SharwarmaVar = StringVar()
IcecreamVar = StringVar()
DisplayVar = StringVar()
Amount_paidVar = IntVar()
Item_costVar = IntVar()
MoneyVar = StringVar()
EatingVar = StringVar()

#Display_entry = Entry(w, textvariable = DisplayVar, width = "30",  = "60").place(x="100",y="20")
Label(w,text = "", bg = "yellow",fg= "white", width = "50", height = "10").place(x="12",y="20")
Item_cost = Label(w,text = "Item_cost", bg = "Blue",fg= "white", width = "12").place(x="12",y="190")
Item_cost_entry = Entry(w,textvariable = Item_costVar ,width = "15").place(x="120",y="190")
Amount_paid = Label(w,text = "Amount_paid", bg = "Blue",fg= "white", width = "12").place(x="12",y="220")
Amount_paid_entry = Entry(w,textvariable = Amount_paidVar, width = "15").place(x="120",y="220")

Change = Label(w,text = "Change", bg = "Blue",fg= "white", width = "12").place(x="12",y="250")
Label(w,text = "", bg= "white", width = "12").place(x="120",y="250")

# This is the code
submit = Button(w, text = "Calculate change", width = "20",command = calculate_change).place(x="120",y="280")
Print_receipt = Label(w,text = "Print_receipt", bg = "Blue",fg= "white", width = "50").place(x="12",y="320")
Check = Checkbutton(w,text = "Meatpie", variable = MeatpieVar, onvalue = "Meatpie-100", offvalue = "", bg = "white").place(x="400",y="20")
Check = Checkbutton(w,text = "Fishpie", variable = FishpieVar, onvalue = "Fishpie-180", offvalue = "", bg = "white").place(x="500",y="20")
Check = Checkbutton(w,text = "Chickenpie", variable = ChickenpieVar, onvalue = "Chickenpie-380", offvalue = "", bg = "white").place(x="600",y="20")
Check = Checkbutton(w,text = "Chips", variable = ChipsVar, onvalue = "Chips-250", offvalue = "", bg = "white").place(x="400",y="60")
Check = Checkbutton(w,text = "Water", variable = WaterVar, onvalue = "Water-120", offvalue = "", bg = "white").place(x="500",y="60")
Check = Checkbutton(w,text = "Softdrinks", variable = SoftdrinksVar, onvalue = "Softdrinks-220", offvalue = "", bg = "white").place(x="600",y="60")
Check = Checkbutton(w,text = "Pizza", variable = PizzaVar, onvalue = "Pizza-950", offvalue = "", bg = "white").place(x="400",y="100")
Check = Checkbutton(w,text = "Sharwarma", variable = SharwarmaVar, onvalue = "Sharwarma-700", offvalue = "", bg = "white").place(x="500",y="100")
Check = Checkbutton(w,text = "Icecream", variable = IcecreamVar, onvalue = "Icecream-500", offvalue = "", bg = "white").place(x="600",y="100")
Radiobutton(w,text = "Cash", variable = MoneyVar, bg= "white", value = "Cash").place(x="400",y="140")
Labeldivid = Label(w,width = 3,text ="/",bg="white").place(x="500",y="140")
Radiobutton(w,text = "POS", variable = MoneyVar, bg= "white", value = "POS").place(x="600",y="140")
Radiobutton(w,text = "Takeout", variable = EatingVar, bg= "white", value = "Takeout").place(x="400",y="180")
Labeldivid = Label(w,width = 3,text ="/",bg="white").place(x="500",y="180")
Radiobutton(w,text = "Here", variable = EatingVar, bg= "white", value = "Here").place(x="600",y="180")


submit = Button(w, text = "Checkbutton", width = "20",command = check).place(x="400",y="240")

w.mainloop()