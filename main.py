import os.path
import tempfile
from cProfile import label
from tkinter import *
from tkinter import messagebox
import random,os,tempfile,subprocess, sys,smtplib
from unittest import result


billnumber=random.randint(500,1000)

def pin_enter():
    if pinentry.get() == '1234':
        passwordentry.insert(0,"wvxl xcef uhfk usdn")



def clear():
    bathsopeEntry.delete(0,END)
    bathsopeEntry.insert(0,0)
    FacecreamEntry.delete(0,END)
    FacecreamEntry.insert(0,0)
    FacewashEntry.delete(0,END)
    FacewashEntry.insert(0,0)
    HiresprayEntry.delete(0,END)
    HiresprayEntry.insert(0,0)
    HiregelEntry.delete(0, END)
    HiregelEntry.insert(0, 0)
    BodyLotionEntry.delete(0, END)
    BodyLotionEntry.insert(0, 0)

    RiceEntry.delete(0,END)
    RiceEntry.insert(0,0)
    OilEntry.delete(0,END)
    OilEntry.insert(0,0)
    DallEntry.delete(0,END)
    DallEntry.insert(0,0)
    WheatEntry.delete(0,END)
    WheatEntry.insert(0,0)
    SugerEntry.delete(0, END)
    SugerEntry.insert(0, 0)
    TeaEntry.delete(0, END)
    TeaEntry.insert(0, 0)


    MaazaEntry.delete(0,END)
    MaazaEntry.insert(0,0)
    DewEntry.delete(0,END)
    DewEntry.insert(0,0)
    pepsiEntry.delete(0,END)
    pepsiEntry.insert(0,0)
    FrootiEntry.delete(0,END)
    FrootiEntry.insert(0,0)
    CocacolaEntry.delete(0, END)
    CocacolaEntry.insert(0, 0)
    SpriteEntry.delete(0, END)
    SpriteEntry.insert(0, 0)

    nameEntry.delete(0,END)
    phoneEntry.delete(0,END)
    billEntry.delete(0,END)

    cosmaticspriceEntry.delete(0,END)
    cosmaticstaxEntry.delete(0, END)
    grocerypriceEntry.delete(0, END)
    grocerytaxEntry.delete(0, END)
    coolpriceEntry.delete(0, END)
    cooltaxEntry.delete(0, END)
    texerea.delete(1.0, END)


def sent_email():
    def send_gmail():
        try:
            ob=smtplib.SMTP('smtp.gmail.com',587)
            ob.starttls()
            ob.login(senderentry.get(),passwordentry.get())
            message=emailtextarea.get(1.0,END)
            ob.sendmail(senderentry.get(),reseverentry.get(),message)
            ob.quit()
            messagebox.showinfo('success','Bill is succsessfuly send')
            root1.destroy()
        except:
            messagebox.showerror('error','wrong')
    if texerea.get(1.0,END)=='\n':
        messagebox.showerror('error','bill is empty')
    else:
        root1 = Toplevel()
        root1.grab_set()
        root1.title('send gmail')
        root1.config(bg='gray20')
        root1.resizable(0,0)

        global pinentry,passwordentry

        senderframe=LabelFrame(root1,text='sender',font=('arial',16,'bold'),bd=8,bg='gray20',fg='white')
        senderframe.grid(row=0,column=0, padx=40,pady=20)

        senderlable=Label(senderframe, text='Sender Email',font=('arial',14,'bold'),bd=8,bg='gray20',fg='white')
        senderlable.grid(row=0, column=0,padx=40,pady=8)

        senderentry = Entry(senderframe,font=('arial', 14, 'bold'), bd=8, bg='gray20', fg='white')
        senderentry.grid(row=0, column=1, padx=40,pady=8 )
        senderentry.insert(0, "chamishkadkulasinghe@gmail.com")

        pinlable = Label(senderframe, text='Pin', font=('arial', 14, 'bold'), bd=8, bg='gray20', fg='white')
        pinlable.grid(row=1, column=0, padx=40, pady=8)

        pinentry = Entry(senderframe, font=('arial', 14, 'bold'), bd=8, bg='gray20', fg='white', show='*')
        pinentry.grid(row=1, column=1, padx=40, pady=8)

        pinbutton=Button(senderframe,text='submit',font=('arial',16,'bold'), width=15 ,command=pin_enter)
        pinbutton.grid(row=2,column=1,pady=20)

        passwordlable = Label(senderframe, text='Password', font=('arial', 14, 'bold'), bd=8, bg='gray20', fg='white')
        passwordlable.grid(row=3, column=0, padx=40, pady=8)

        passwordentry = Entry(senderframe, font=('arial', 14, 'bold'), bd=8, bg='gray20', fg='white',show='*')
        passwordentry.grid(row=3, column=1, padx=40, pady=8)

        resipientframe = LabelFrame(root1, text='Resipient', font=('arial', 16, 'bold'), bd=8, bg='gray20', fg='white')
        resipientframe.grid(row=1, column=0, padx=40, pady=20)

        reseverlable = Label(resipientframe, text='Email address', font=('arial', 14, 'bold'), bd=8, bg='gray20', fg='white')
        reseverlable.grid(row=0, column=0, padx=40, pady=8)

        reseverentry = Entry(resipientframe, font=('arial', 14, 'bold'), bd=8, bg='gray20', fg='white')
        reseverentry.grid(row=0, column=1, padx=40, pady=8)

        massagelable = Label(resipientframe, text='Message', font=('arial', 14, 'bold'), bd=8, bg='gray20',fg='white')
        massagelable.grid(row=1, column=0, padx=40, pady=8)

        emailtextarea = Text(resipientframe, font=('arial', 14, 'bold'), bd=2,relief=SUNKEN,width=42,height=11 )
        emailtextarea.grid(row=2, column=0, columnspan=2)

        emailtextarea.delete(1.0,END)
        emailtextarea.insert(END,texerea.get(1.0,END).replace('=','').replace('-','').replace('\t\t\t','\t\t'))

        sendbutton=Button(root1,text='SEND',font=('arial',16,'bold'), width=15 ,command=send_gmail)
        sendbutton.grid(row=2,column=0,pady=20)

        root1.mainloop()

def print_bill():
    if texerea.get(1.0,END)=='\n':
        messagebox.showerror('error','bill is empty')
    else:
        file=tempfile.mktemp('.txt')
        open(file,'w').write(texerea.get(1.0,END))
        os.startfile(file,'print')

def search_bill():
    for i in os.listdir('bills/'):
        if i.split('.')[0]==billEntry.get():
            f=open(f'bills/{i}','r')
            texerea.delete(1.0,END)
            for data in f:
                texerea.insert(END,data)
            f.close()
            break
    else:
        messagebox.showerror('error','invalid bill number')


if not os.path.exists('bills'):
    os.mkdir('bills')
#funtionality port


def save_bill():
    result = messagebox.askyesno('Confirm','Do you want to save bill')
    if result:
        bill_contant= texerea.get(1.0,END)
        file= open(f"bills/{billnumber}.txt.","w")
        file.write(bill_contant)
        file.close()
        messagebox.showinfo("success",f"{billnumber} is saved succesfully")
def bill_area():
    if nameEntry.get()=='' or phoneEntry.get()=='':
        messagebox.showerror("error","customer detsils are requird")

    elif cosmaticspriceEntry.get()=='' or grocerypriceEntry.get()=='' or coolpriceEntry.get()=='':
        messagebox.showerror("error","no product are selected")

    elif cosmaticspriceEntry.get() =="Rs. 0" and grocerypriceEntry.get() =="Rs. 0" and coolpriceEntry.get()=="Rs. 0":
        messagebox.showerror("error", "no product are selected")

    else:
        texerea.delete(1.0,END)
        texerea.insert(END,"\t\t\t\t **welcome customer**\n\n")
        texerea.insert(END,f"Bill Number:{billnumber}\n")
        texerea.insert(END,f"\ncustomer Name:{nameEntry.get()}\n")
        texerea.insert(END, f"\nPhone Number:{phoneEntry.get()}\n\n")
        texerea.insert(END, "==================================================================================\n")
        texerea.insert(END,"product \t\t\t\t Quantity \t\t\t\t Price\n")
        texerea.insert(END, "==================================================================================\n")
        if bathsopeEntry.get()!='0':
            texerea.insert(END,f"Bath Sope     \t\t\t\t {bathsopeEntry.get()}\t\t\t\tRs. {sopeprice}\n")
        if FacecreamEntry.get()!='0':
            texerea.insert(END,f"Face cream     \t\t\t\t {FacecreamEntry.get()}\t\t\t\tRs. {creamprice}\n")
        if FacewashEntry.get()!='0':
            texerea.insert(END,f"Face Wash    \t\t\t\t {FacewashEntry.get()}\t\t\t\tRs. {Facewashprice}\n")
        if HiresprayEntry.get()!='0':
            texerea.insert(END,f"Hire Spray    \t\t\t\t {HiresprayEntry.get()}\t\t\t\tRs. {Hiresprayprice}\n")
        if HiregelEntry.get() != '0':
            texerea.insert(END, f"Hire Gel    \t\t\t\t {HiresprayEntry.get()}\t\t\t\tRs. {Hiregelprice}\n")
        if BodyLotionEntry.get() != '0':
            texerea.insert(END, f"Body Lotion    \t\t\t\t {BodyLotionEntry.get()}\t\t\t\tRs. {BodyLotionprice}\n")

        if RiceEntry.get() != '0':
            texerea.insert(END, f"Rice   \t\t\t\t {RiceEntry.get()}\t\t\t\tRs. {riceprice}\n")
        if DallEntry.get() != '0':
            texerea.insert(END, f"Dall   \t\t\t\t {DallEntry.get()}\t\t\t\tRs. {Dallprice}\n")
        if OilEntry.get() != '0':
            texerea.insert(END, f"Oil   \t\t\t\t {OilEntry.get()}\t\t\t\tRs. {Oilprice}\n")
        if SugerEntry.get() != '0':
            texerea.insert(END, f"Suger   \t\t\t\t {SugerEntry.get()}\t\t\t\tRs. {Sugerprice}\n")
        if TeaEntry.get() != '0':
            texerea.insert(END, f"Tea   \t\t\t\t {TeaEntry.get()}\t\t\t\tRs. {Teaprice}\n")
        if WheatEntry.get() != '0':
            texerea.insert(END, f"Wheat   \t\t\t\t {WheatEntry.get()}\t\t\t\tRs. {Wheatprice}\n")

        if MaazaEntry.get() != '0':
            texerea.insert(END, f"Maaza  \t\t\t\t {MaazaEntry.get()}\t\t\t\tRs. {Maazaprice}\n")
        if pepsiEntry.get() != '0':
            texerea.insert(END, f"Pepsi \t\t\t\t {pepsiEntry.get()}\t\t\t\tRs. {Pepsiprice}\n")
        if DewEntry.get() != '0':
            texerea.insert(END, f"Dew \t\t\t\t {DewEntry.get()}\t\t\t\tRs. {Dewprice}\n")
        if FrootiEntry.get() != '0':
            texerea.insert(END, f"Frooti \t\t\t\t {FrootiEntry.get()}\t\t\t\tRs. {Frootiprice}\n")
        if CocacolaEntry.get() != '0':
            texerea.insert(END, f"Coca Cola \t\t\t\t {CocacolaEntry.get()}\t\t\t\tRs. {cocacolaprice}\n")
        if SpriteEntry.get() != '0':
            texerea.insert(END, f"Sprite \t\t\t\t {SpriteEntry.get()}\t\t\t\tRs. {Spriteprice}\n")

        texerea.insert(END, "----------------------------------------------------------------------------------\n")

        if cosmaticstaxEntry.get()!="Rs. 0.0":
            texerea.insert(END,f"Cosmatics Tax   \t\t\t\t\t\t\t\t{cosmaticstaxEntry.get()}\n")
        if grocerytaxEntry.get() != "Rs. 0.0":
            texerea.insert(END, f"Grocary Tax   \t\t\t\t\t\t\t\t{grocerytaxEntry.get()}\n")
        if cooltaxEntry.get()!="Rs. 0.0":
            texerea.insert(END,f"Cool Drink Tax   \t\t\t\t\t\t\t\t{cooltaxEntry.get()}\n\n")

        texerea.insert(END, "----------------------------------------------------------------------------------\n")
        texerea.insert(END,f"Total Bill \t\t\t\t\t\t\t\tRs. {TotalBill}\n" )
        texerea.insert(END, "----------------------------------------------------------------------------------\n")
        save_bill()
def total():
    global Maazaprice,TotalBill
    global Pepsiprice
    global Dewprice
    global Frootiprice
    global cocacolaprice
    global Spriteprice

    global sopeprice
    global creamprice
    global Facewashprice
    global Hiresprayprice
    global Hiregelprice
    global BodyLotionprice

    global riceprice
    global Dallprice
    global Oilprice
    global Sugerprice
    global Teaprice
    global Wheatprice

    sopeprice= int(bathsopeEntry.get())*10
    creamprice= int(FacecreamEntry.get())*10
    Facewashprice= int(FacewashEntry.get())*10
    Hiresprayprice = int(HiresprayEntry.get()) * 10
    Hiregelprice = int(HiregelEntry.get()) * 10
    BodyLotionprice = int( BodyLotionEntry.get()) * 10

    totalcosmaticsprice=(sopeprice+creamprice+Facewashprice+Hiresprayprice+Hiregelprice+BodyLotionprice)
    cosmaticspriceEntry.delete(0,END)
    cosmaticspriceEntry.insert(0,"Rs. "+str(totalcosmaticsprice))
    cosmaticstax=totalcosmaticsprice*0.05
    cosmaticstaxEntry.delete(0,END)
    cosmaticstaxEntry.insert(0,"Rs. "+str(cosmaticstax))

    #grocery price calculation
    riceprice=int(RiceEntry.get())*10
    Dallprice=int(DallEntry.get())*10
    Oilprice=int(OilEntry.get())*10
    Sugerprice=int(SugerEntry.get())*10
    Teaprice=int(TeaEntry.get())*10
    Wheatprice=int(WheatEntry.get())*10

    totalgrocaryprice = (riceprice + Dallprice + Oilprice + Sugerprice + Teaprice + Wheatprice)
    grocerypriceEntry.delete(0,END)
    grocerypriceEntry.insert(0, "Rs. " + str(totalgrocaryprice))
    grocerytax = totalgrocaryprice * 0.05
    grocerytaxEntry.delete(0, END)
    grocerytaxEntry.insert(0, "Rs. " + str(grocerytax))

    # Drinks price calculation

    Maazaprice = int(MaazaEntry.get()) * 10
    Pepsiprice = int(pepsiEntry.get()) * 10
    Dewprice = int(DewEntry.get()) * 10
    Frootiprice = int(FrootiEntry.get()) * 10
    cocacolaprice = int(CocacolaEntry.get()) * 10
    Spriteprice = int(SpriteEntry.get()) * 10

    totalcoolprice = (Maazaprice + Pepsiprice + Dewprice + Frootiprice + cocacolaprice + Spriteprice)
    coolpriceEntry.delete(0,END)
    coolpriceEntry.insert(0, "Rs. " + str(totalcoolprice))

    coolpricetax = totalcoolprice * 0.05
    cooltaxEntry.delete(0, END)
    cooltaxEntry.insert(0, "Rs. " + str(coolpricetax))

    TotalBill= totalcosmaticsprice+totalgrocaryprice+totalcoolprice+coolpricetax+cosmaticstax+grocerytax

root = Tk()
root.title('Billing System')
root.geometry('1270x685')
root.iconbitmap('icon.ico')

headinglabel = Label(root, text="billing system", font=("times new roman",30,"bold"), bg="gray45",fg="gold" ,bd=12,relief=GROOVE)
headinglabel.pack(fill=X,pady=10)

customer_detail_frame= LabelFrame(root,text="Customer Details",font=("times new romen",15,"bold"),bg="gray45", fg="gold",bd=8, relief=GROOVE)
customer_detail_frame.pack(fill=X)

nameLable= Label(customer_detail_frame,text="Name",font=("times new romen",15,"bold"),bg="gray45",fg="white",bd=8,relief=GROOVE)
nameLable.grid(row=0,column=0,padx=20,pady=2)

nameEntry= Entry(customer_detail_frame,font=("arial",15),bd=7, width=18 ,validatecommand=str)
nameEntry.grid(row=0,column=1,padx=8,pady=2)

phoneLable= Label(customer_detail_frame,text="Telephone Number",font=("times new romen",15,"bold"),bg="gray45",fg="white",bd=8,relief=GROOVE)
phoneLable.grid(row=0,column=2,padx=20,pady=2)

phoneEntry= Entry(customer_detail_frame,font=("arial",15),bd=7, width=18)
phoneEntry.grid(row=0,column=3,padx=8,pady=2)

billLable= Label(customer_detail_frame,text="Bill Number",font=("times new romen",15,"bold"),bg="gray45",fg="white",bd=8,relief=GROOVE)
billLable.grid(row=0,column=4,padx=20,pady=2)

billEntry= Entry(customer_detail_frame,font=("arial",15),bd=7, width=18)
billEntry.grid(row=0,column=5,padx=8,pady=2)
searchButon=Button(customer_detail_frame,text="SEARCH",font=("arial",15,"bold"),bg="gray45",bd=8,relief=GROOVE, command=search_bill)
searchButon.grid(row=0,column=6,padx=10,pady=8)

productFrame=Frame(root)
productFrame.pack(fill=X)
cosmaticsFrame=LabelFrame(productFrame,text="cosmetics",font=("times new romen",15,"bold"),bg="gray45", fg="gold")
cosmaticsFrame.grid(row=0,column=0)

bathsopeLabel=Label(cosmaticsFrame,text="Bath sope",font=("times new romen",15,"bold"),bg="gray45",fg="white")
bathsopeLabel.grid(row = 0,column=0)

bathsopeEntry=Entry(cosmaticsFrame,font=("times new romen",15,"bold"),width=10,bd=5)
bathsopeEntry.grid(row=0,column=1)
bathsopeEntry.insert(0,0)

FacecreamLabel=Label(cosmaticsFrame,text="Face cream",font=("times new romen",15,"bold"),bg="gray45",fg="white")
FacecreamLabel.grid(row = 1,column=0)

FacecreamEntry=Entry(cosmaticsFrame,font=("times new romen",15,"bold"),width=10,bd=5)
FacecreamEntry.grid(row=1,column=1)
FacecreamEntry.insert(0,0)

FacewashLabel=Label(cosmaticsFrame,text="Facewash",font=("times new romen",15,"bold"),bg="gray45",fg="white")
FacewashLabel.grid(row = 2,column=0)

FacewashEntry=Entry(cosmaticsFrame,font=("times new romen",15,"bold"),width=10,bd=5)
FacewashEntry.grid(row=2,column=1)
FacewashEntry.insert(0,0)

HiresprayLabel=Label(cosmaticsFrame,text="Hire spray",font=("times new romen",15,"bold"),bg="gray45",fg="white")
HiresprayLabel.grid(row = 3,column=0)

HiresprayEntry=Entry(cosmaticsFrame,font=("times new romen",15,"bold"),width=10,bd=5)
HiresprayEntry.grid(row=3,column=1)
HiresprayEntry.insert(0,0)

HiregelLabel=Label(cosmaticsFrame,text="Hire gel",font=("times new romen",15,"bold"),bg="gray45",fg="white")
HiregelLabel.grid(row =4,column=0)

HiregelEntry=Entry(cosmaticsFrame,font=("times new romen",15,"bold"),width=10,bd=5)
HiregelEntry.grid(row=4,column=1)
HiregelEntry.insert(0,0)

BodyLotionLabel=Label(cosmaticsFrame,text="Body Lotion",font=("times new romen",15,"bold"),bg="gray45",fg="white")
BodyLotionLabel.grid(row = 5,column=0)

BodyLotionEntry=Entry(cosmaticsFrame,font=("times new romen",15,"bold"),width=10,bd=5)
BodyLotionEntry.grid(row=5,column=1)
BodyLotionEntry.insert(0,0)

GrocaryFrame=LabelFrame(productFrame,text="Grocary",font=("times new romen",15,"bold"),bg="gray45", fg="gold")
GrocaryFrame.grid(row=0,column=1)

RiceLabel=Label(GrocaryFrame,text="Rice",font=("times new romen",15,"bold"),bg="gray45",fg="white")
RiceLabel.grid(row = 0,column=0)

RiceEntry=Entry(GrocaryFrame,font=("times new romen",15,"bold"),width=10,bd=5)
RiceEntry.grid(row=0,column=1)
RiceEntry.insert(0,0)

OilLabel=Label(GrocaryFrame,text="Oil",font=("times new romen",15,"bold"),bg="gray45",fg="white")
OilLabel.grid(row = 1,column=0)

OilEntry=Entry(GrocaryFrame,font=("times new romen",15,"bold"),width=10,bd=5)
OilEntry.grid(row=1,column=1)
OilEntry.insert(0,0)

DallLabel=Label(GrocaryFrame,text="Dall",font=("times new romen",15,"bold"),bg="gray45",fg="white")
DallLabel.grid(row = 2,column=0)

DallEntry=Entry(GrocaryFrame,font=("times new romen",15,"bold"),width=10,bd=5)
DallEntry.grid(row=2,column=1)
DallEntry.insert(0,0)

WheatLabel=Label(GrocaryFrame,text="Wheat",font=("times new romen",15,"bold"),bg="gray45",fg="white")
WheatLabel.grid(row = 3,column=0)

WheatEntry=Entry(GrocaryFrame,font=("times new romen",15,"bold"),width=10,bd=5)
WheatEntry.grid(row=3,column=1)
WheatEntry.insert(0,0)

SugerLabel=Label(GrocaryFrame,text="Suger",font=("times new romen",15,"bold"),bg="gray45",fg="white")
SugerLabel.grid(row = 4,column=0)

SugerEntry=Entry(GrocaryFrame,font=("times new romen",15,"bold"),width=10,bd=5)
SugerEntry.grid(row=4,column=1)
SugerEntry.insert(0,0)

TeaLabel=Label(GrocaryFrame,text="Tea",font=("times new romen",15,"bold"),bg="gray45",fg="white")
TeaLabel.grid(row = 5,column=0)

TeaEntry=Entry(GrocaryFrame,font=("times new romen",15,"bold"),width=10,bd=5)
TeaEntry.grid(row=5,column=1)
TeaEntry.insert(0,0)

ColdFrame=LabelFrame(productFrame,text="Cold Drink",font=("times new romen",15,"bold"),bg="gray45", fg="gold")
ColdFrame.grid(row=0,column=2)

MaazaLabel=Label(ColdFrame,text="Maaza",font=("times new romen",15,"bold"),bg="gray45",fg="white")
MaazaLabel.grid(row = 0,column=0)

MaazaEntry=Entry(ColdFrame,font=("times new romen",15,"bold"),width=10,bd=5)
MaazaEntry.grid(row=0,column=1)
MaazaEntry.insert(0,0)

pepsiLabel=Label(ColdFrame,text="Pepsi",font=("times new romen",15,"bold"),bg="gray45",fg="white")
pepsiLabel.grid(row = 1,column=0)

pepsiEntry=Entry(ColdFrame,font=("times new romen",15,"bold"),width=10,bd=5)
pepsiEntry.grid(row=1,column=1)
pepsiEntry.insert(0,0)

DewLabel=Label(ColdFrame,text="Dew",font=("times new romen",15,"bold"),bg="gray45",fg="white")
DewLabel.grid(row = 2,column=0)

DewEntry=Entry(ColdFrame,font=("times new romen",15,"bold"),width=10,bd=5)
DewEntry.grid(row=2,column=1)
DewEntry.insert(0,0)

FrootiLabel=Label(ColdFrame,text="Frooti",font=("times new romen",15,"bold"),bg="gray45",fg="white")
FrootiLabel.grid(row = 3,column=0)

FrootiEntry=Entry(ColdFrame,font=("times new romen",15,"bold"),width=10,bd=5)
FrootiEntry.grid(row=3,column=1)
FrootiEntry.insert(0,0)

CocacolaLabel=Label(ColdFrame,text="Coca cola",font=("times new romen",15,"bold"),bg="gray45",fg="white")
CocacolaLabel.grid(row = 4,column=0)

CocacolaEntry=Entry(ColdFrame,font=("times new romen",15,"bold"),width=10,bd=5)
CocacolaEntry.grid(row=4,column=1)
CocacolaEntry.insert(0,0)

SpriteLabel=Label(ColdFrame,text="Sprite",font=("times new romen",15,"bold"),bg="gray45",fg="white")
SpriteLabel.grid(row = 5,column=0)


SpriteEntry=Entry(ColdFrame,font=("times new romen",15,"bold"),width=10,bd=5)
SpriteEntry.grid(row=5,column=1)
SpriteEntry.insert(0,0)

billframe = Frame(productFrame,bd=8,relief=GROOVE)
billframe.grid(row=0,column=3,padx=20)

billareaLabel= Label(billframe,text = "Bill area", font=("times new romen",15,"bold"))
billareaLabel.pack(fill=X)


scrollbar=Scrollbar(billframe,orient=VERTICAL)
scrollbar.pack(side=RIGHT,fill=Y)

texerea= Text(billframe,height=18,width=83,yscrollcommand=scrollbar.set)
texerea.pack()
scrollbar.config(command=texerea.yview())

billmanuFrame=LabelFrame(root,text="Bill Menu",font=("times new romen",15,"bold"),fg="gold",bd=8,relief=GROOVE,bg="gray20")
billmanuFrame.pack()

cosmaticspriceLabel=Label(billmanuFrame,text="cosmetics Price",font=("times new romen",15,"bold"),bg="gray45",fg="white")
cosmaticspriceLabel.grid(row=0,column=0,pady=9,padx=10,stick='w')

cosmaticspriceEntry=Entry(billmanuFrame,font=("times new romen",15,"bold"),width=10,bd=5)
cosmaticspriceEntry.grid(row=0,column=1)

grocerypriceLabel=Label(billmanuFrame,text="grocery Price",font=("times new romen",15,"bold"),bg="gray45",fg="white")
grocerypriceLabel.grid(row=1,column=0,pady=9,padx=10,stick='w')

grocerypriceEntry=Entry(billmanuFrame,font=("times new romen",15,"bold"),width=10,bd=5)
grocerypriceEntry.grid(row=1,column=1)

coolpriceLabel=Label(billmanuFrame,text="Cool Drinks Price",font=("times new romen",15,"bold"),bg="gray45",fg="white")
coolpriceLabel.grid(row=2,column=0,pady=9,padx=10,stick='w')

coolpriceEntry=Entry(billmanuFrame,font=("times new romen",15,"bold"),width=10,bd=5)
coolpriceEntry.grid(row=2,column=1)



cosmaticstaxLabel=Label(billmanuFrame,text="cosmetics Tax",font=("times new romen",15,"bold"),bg="gray45",fg="white")
cosmaticstaxLabel.grid(row=0,column=2,pady=9,padx=10,stick='w')

cosmaticstaxEntry=Entry(billmanuFrame,font=("times new romen",15,"bold"),width=10,bd=5)
cosmaticstaxEntry.grid(row=0,column=3)

grocerytaxLabel=Label(billmanuFrame,text="grocery Tax",font=("times new romen",15,"bold"),bg="gray45",fg="white")
grocerytaxLabel.grid(row=1,column=2,pady=9,padx=10,stick='w')

grocerytaxEntry=Entry(billmanuFrame,font=("times new romen",15,"bold"),width=10,bd=5)
grocerytaxEntry.grid(row=1,column=3)

cooltaxLabel=Label(billmanuFrame,text="Cool Drinks Tax",font=("times new romen",15,"bold"),bg="gray45",fg="white")
cooltaxLabel.grid(row=2,column=2,pady=9,padx=10,stick='w')

cooltaxEntry=Entry(billmanuFrame,font=("times new romen",15,"bold"),width=10,bd=5)
cooltaxEntry.grid(row=2,column=3)

buttonFrame=Frame(billmanuFrame,bd=8,relief=GROOVE)
buttonFrame.grid(row=0,column=4, rowspan=3)

totalButton=Button(buttonFrame, text="Total",font=("arial",16,"bold"),bg="gray20",bd=5,width=8,command=total)
totalButton.grid(row=0, column=0 ,pady=20 )

billButton=Button(buttonFrame, text="Bill",font=("arial",16,"bold"),bg="gray20",bd=5,width=8,command=bill_area)
billButton.grid(row=0, column=1 ,pady=20)

emailButton=Button(buttonFrame, text="Email",font=("arial",16,"bold"),bg="gray20",bd=5,width=8 ,command=sent_email)
emailButton.grid(row=0, column=2 ,pady=20)

printButton=Button(buttonFrame, text="print",font=("arial",16,"bold"),bg="gray20",bd=5,width=8,command=print_bill)
printButton.grid(row=0, column=3 ,pady=20)

clearlButton=Button(buttonFrame, text="Clear",font=("arial",16,"bold"),bg="gray20",bd=5,width=8,command=clear)
clearlButton.grid(row=0, column=4 ,pady=20)

root.mainloop()
