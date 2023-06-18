# Program to make a simple 
# login screen  
 

import math
from tkinter import *
from cgitb import text
import tkinter as tk
from tkinter import Frame, Label, font
from turtle import bgcolor

  

root=tk.Tk()

root.title("Cost Evaluation Of Transformer")
# setting the windows size

root.geometry("1200x730")

frame1= Frame(root,highlightbackground="red",highlightthickness=2)

  
# declaring string variable
# for storing name and password

HPY_var=tk.DoubleVar()

Avf_var=tk.DoubleVar()

annual_escalation_rate = tk.DoubleVar()

Fixed_cost_rate = tk.DoubleVar()

efficiency_of_transmission= tk.DoubleVar()

discount_rate= tk.DoubleVar()

increase_factor= tk.DoubleVar()

no_load_loss= tk.DoubleVar()

load_loss= tk.DoubleVar()

LIC= tk.DoubleVar()

load_loss_of_ref_transformer= tk.DoubleVar()

no_load_loss_of_ref_transformer= tk.DoubleVar()

current_year_energy_price= tk.DoubleVar()

life_span= tk.DoubleVar()

#annual_escalation_rate= tk.IntVar()

peak_per_unit_transformer_load= tk.DoubleVar()

peak_responsibility_factor= tk.DoubleVar()

current_year_emission_cost_factor= tk.DoubleVar()

load_factor= tk.DoubleVar()

bid_price= tk.DoubleVar()

no_load_loss_factor_A = tk.DoubleVar()

load_loss_factor_B= tk.DoubleVar()

LECN = tk.DoubleVar()

LECL = tk.DoubleVar()

CRF = tk.DoubleVar()

no_load_loss_cost= tk.DoubleVar()

load_loss_cost= tk.DoubleVar()

cost_of_losses= tk.DoubleVar()

total_owing_cost= tk.DoubleVar()

tp=tk.DoubleVar()


 
  
# defining a function that will
# get the name and password and 
# print them on the screen

def submit():
 
    #Get 
    HPY_c=HPY_var.get()

    Avf_c=Avf_var.get()

    life_span_c=life_span.get()

    discount_rate_c = discount_rate.get()

    peak_per_unit_transformer_load_c =peak_per_unit_transformer_load.get()

    current_year_energy_price_c = current_year_energy_price.get()

    load_factor_c = load_factor.get()

    annual_escalation_rate_c =annual_escalation_rate.get()

    increase_factor_c = increase_factor.get()

    no_load_loss_c = no_load_loss.get()

    load_loss_c = load_loss.get()

    load_factor_c=load_factor.get()

    bid_price_c=bid_price.get()
    

    
     
    
    ET =0.7912
    FCR= 0.1886
    PRF= 0.735

    CRF_c=(float) ((discount_rate_c*(1+discount_rate_c)**life_span_c) /( ((1+discount_rate_c)**life_span_c)-1))
    #loss factor (lf)
    lf =(float)( (0.3*load_factor_c)+(0.7*(load_factor_c*load_factor_c)))
    TLF =(float) (math.sqrt((lf* (peak_per_unit_transformer_load_c * peak_per_unit_transformer_load_c) )))


    # d=0.10
    #AF = 
    #BL=Life of the transformer
    #LECN_var = 0.10608 * HPY * Avf* (1+EIR/d-EIR) * ((1-(1+EIR/1+d)**ls)) 
    #tp1=0.10608 * 8760 *0.95* (1+0.05/0.10-0.05)   * ((1-(1+0.05/1+0.10)**30))

    #LECN=load_factor*bid_price

    #print("The name is : " , HPY)

    #Calulation

    peak_per_unit_transformer_load_c =peak_per_unit_transformer_load.get()
    # For no_load_loss_factor_A

    LIC_c = LIC.get()
    #LECN_c = 1241.2738
    LECN_c =(float)( CRF_c * HPY_c * current_year_energy_price_c*Avf_c *((1+annual_escalation_rate_c)/(discount_rate_c-annual_escalation_rate_c) )* ((1-((1+annual_escalation_rate_c)/(1+discount_rate_c))**life_span_c)))
    
    no_load_loss_factor_A_c= (float)((LIC_c + LECN_c) / (ET * FCR * increase_factor_c ))

    #no_load_loss_factor_B
    
    
    LECL_c = (float)(CRF_c * HPY_c * current_year_energy_price_c *((1+annual_escalation_rate_c)/(discount_rate_c-annual_escalation_rate_c)) * ((1-((1+annual_escalation_rate_c)/(1+discount_rate_c))**life_span_c)))
    load_loss_factor_B_c =(float)(( (LIC_c * (PRF*PRF) * (peak_per_unit_transformer_load_c * peak_per_unit_transformer_load_c) + ( LECL_c *(TLF*TLF)))) / (ET * FCR * increase_factor_c))
    #no_load_loss_cost(CNLL) = A*NLL

    no_load_loss_cost_c = (float)(no_load_loss_factor_A_c  *  no_load_loss_c)

    #load_loss_cost(CLL) = B*LL

    load_loss_cost_c = (float)(load_loss_factor_B_c * load_loss_c)

    #cost_of_losses(CL) = CL + CNLL

    cost_of_losses_c = (float)(no_load_loss_cost_c + load_loss_cost_c) 

    #total_owing_cost(TOC)

    total_owing_cost_c =(float) (bid_price_c +( no_load_loss_factor_A_c * no_load_loss_c )+ (load_loss_factor_B_c * load_loss_c))

    


    #print("The password is : " , Avf)
    space_label = tk.Label(root, text ="           ").grid(row=4,column=8)
    space_label = tk.Label(root, text ="           ").grid(row=4,column=7)
    space_label = tk.Label(root, text ="           ").grid(row=4,column=6)
    space_label = tk.Label(root, text ="           ").grid(row=4,column=5)
    no_load_loss_factor_A_label = tk.Label(root,text="No Load Loss Factor(A)",font="calibre 12 bold").grid(row=4,column=9)
    space_label = tk.Label(root, text ="      ").grid(row=4,column=10)
    no_load_loss_factor_A_label = tk.Label(root,text=no_load_loss_factor_A_c,font="Rockwell 10 bold",width=20,height=2,borderwidth=3,relief="ridge",bg="beige").grid(row=4,column=11)


    space_label = tk.Label(root, text ="           ").grid(row=6,column=8)
    space_label = tk.Label(root, text ="           ").grid(row=6,column=7)
    space_label = tk.Label(root, text ="           ").grid(row=6,column=6)
    space_label = tk.Label(root, text ="           ").grid(row=6,column=5)
    load_loss_factor_B_label = tk.Label(root,text="Load Loss Factor(B)",font="calibre 12 bold").grid(row=6,column=9)
    space_label = tk.Label(root, text ="      ").grid(row=6,column=10)
    load_loss_factor_B_label = tk.Label(root,text=load_loss_factor_B_c,font="Rockwell 10 bold",width=20,height=2,borderwidth=3,relief="ridge",bg="beige").grid(row=6,column=11)


    space_label = tk.Label(root, text ="           ").grid(row=8,column=8)
    space_label = tk.Label(root, text ="           ").grid(row=8,column=7)
    space_label = tk.Label(root, text ="           ").grid(row=8,column=6)
    space_label = tk.Label(root, text ="           ").grid(row=8,column=5)
    LECN_label = tk.Label(root,text="LECN",font="calibre 12 bold").grid(row=8,column=9)
    space_label = tk.Label(root, text ="      ").grid(row=8,column=10)
    LECN_label = tk.Label(root,text=LECN_c,font="Rockwell 10 bold",width=20,height=2,borderwidth=3,relief="ridge",bg="beige").grid(row=8,column=11)


    space_label = tk.Label(root, text ="           ").grid(row=10,column=8)
    space_label = tk.Label(root, text ="           ").grid(row=10,column=7)
    space_label = tk.Label(root, text ="           ").grid(row=10,column=6)
    space_label = tk.Label(root, text ="           ").grid(row=10,column=5)
    LECL_label = tk.Label(root,text="LECL",font="calibre 12 bold").grid(row=10,column=9)
    space_label = tk.Label(root, text ="      ").grid(row=10,column=10)
    LECL_label = tk.Label(root,text=LECL_c,font="Rockwell 10 bold",width=20,height=2,borderwidth=3,relief="ridge",bg="beige").grid(row=10,column=11)


    space_label = tk.Label(root, text ="           ").grid(row=12,column=8)
    space_label = tk.Label(root, text ="           ").grid(row=12,column=7)
    space_label = tk.Label(root, text ="           ").grid(row=12,column=6)
    space_label = tk.Label(root, text ="           ").grid(row=12,column=5)
    CRF_label = tk.Label(root,text="CRF",font="calibre 12 bold").grid(row=12,column=9)
    space_label = tk.Label(root, text ="      ").grid(row=12,column=10)
    CRF_label = tk.Label(root,text=CRF_c,font="Rockwell 10 bold",width=20,height=2,borderwidth=3,relief="ridge",bg="beige").grid(row=12,column=11)


    space_label = tk.Label(root, text ="           ").grid(row=14,column=8)
    space_label = tk.Label(root, text ="           ").grid(row=14,column=7)
    space_label = tk.Label(root, text ="           ").grid(row=14,column=6)
    space_label = tk.Label(root, text ="           ").grid(row=14,column=5)
    no_load_loss_cost_label = tk.Label(root,text="No Load Loss Cost(CNLL)",font="calibre 12 bold").grid(row=14,column=9)
    space_label = tk.Label(root, text ="      ").grid(row=14,column=10)
    no_load_loss_cost_label = tk.Label(root,text=no_load_loss_cost_c,font="Rockwell 10 bold",width=20,height=2,borderwidth=3,relief="ridge",bg="beige").grid(row=14,column=11)


    space_label = tk.Label(root, text ="           ").grid(row=16,column=8)
    space_label = tk.Label(root, text ="           ").grid(row=16,column=7)
    space_label = tk.Label(root, text ="           ").grid(row=16,column=6)
    space_label = tk.Label(root, text ="           ").grid(row=16,column=5)
    load_loss_cost_label = tk.Label(root,text="Load Loss Cost(CLL)",font="Rockwell 12 bold").grid(row=16,column=9)
    space_label = tk.Label(root, text ="      ").grid(row=16,column=10)
    load_loss_cost_label = tk.Label(root,text=load_loss_cost_c,font="Rockwell 10 bold",width=20,height=2,borderwidth=3,relief="ridge",bg="beige").grid(row=16,column=11)



    space_label = tk.Label(root, text ="           ").grid(row=18,column=8)
    space_label = tk.Label(root, text ="           ").grid(row=18,column=7)
    space_label = tk.Label(root, text ="           ").grid(row=18,column=6)
    space_label = tk.Label(root, text ="           ").grid(row=18,column=5)
    cost_of_losses_label = tk.Label(root,text="Cost Of Losses(CL)",font="calibre 12 bold").grid(row=18,column=9)
    space_label = tk.Label(root, text ="      ").grid(row=18,column=10)
    cost_of_losses_label = tk.Label(root,text=cost_of_losses_c,font="Rockwell 10 bold",width=20,height=2,borderwidth=3,relief="ridge",bg="beige").grid(row=18,column=11)



    space_label = tk.Label(root, text ="           ").grid(row=20,column=8)
    space_label = tk.Label(root, text ="           ").grid(row=20,column=7)
    space_label = tk.Label(root, text ="           ").grid(row=20,column=6)
    space_label = tk.Label(root, text ="           ").grid(row=20,column=5)
    total_owing_cost_label = tk.Label(root,text="TOTAL OWING COST(TOC)",font="calibre 12 bold").grid(row=20,column=9)
    space_label = tk.Label(root, text ="      ").grid(row=20,column=10)
    total_owing_cost_label = tk.Label(root,text=total_owing_cost_c,font="Rockwell 10 bold",width=20,height=2,borderwidth=3,relief="ridge",bg="beige").grid(row=20,column=11)

    



     
   #Set
    HPY_var.set(HPY_c)

    Avf_var.set(Avf_c)

    life_span.set("")
    no_load_loss_factor_A.set(no_load_loss_factor_A_c)

    load_loss_factor_B.set(load_loss_factor_B_c)

    LECN.set(LECN_c)

    LECL.set(LECL_c)

    CRF.set(CRF_c)

    no_load_loss_cost.set(no_load_loss_cost_c)

    load_loss_cost.set(load_loss_cost_c)

    cost_of_losses.set(cost_of_losses_c)

    total_owing_cost.set(total_owing_cost_c)
    


    

     
     
# creating a label for 
# name using widget Label
Head_label = tk.Label(root,text="TRANSFORMER  COST  EVALUATION", font="Bookman 30 bold",fg="crimson").grid(row=0,column=1,columnspan=11)
space_label = tk.Label(root, text =" ").grid(row=1,column=0)

HPY_var_label = tk.Label(root, text = 'Hour per year(HPY)', font=('calibre',10, 'bold')).grid(row=4,column=0)

space_label = tk.Label(root, text =" ").grid(row=3,column=0)

Avf_var_label=tk.Label(root, text = 'Availability Factor', font=('calibre',10, 'bold')).grid(row=6,column=0)

space_label = tk.Label(root, text =" ").grid(row=5,column=0)

annual_escalation_rate_label=tk.Label(root, text = 'Annual escalation rate', font=('calibre',10, 'bold')).grid(row=8,column=0)

space_label = tk.Label(root, text =" ").grid(row=7,column=0)

Fixed_cost_rate_label=tk.Label(root, text = 'Fixed Cost Rate ^_^', font=('calibre',10, 'bold')).grid(row=10,column=0)

space_label = tk.Label(root, text =" ").grid(row=9,column=0)

efficiency_of_transmission_label=tk.Label(root, text = 'Efficiency of Transmission', font=('calibre',10, 'bold')).grid(row=12,column=0)

space_label = tk.Label(root, text =" ").grid(row=11,column=0)

discount_rate_label=tk.Label(root, text = 'Discount Rate', font=('calibre',10, 'bold')).grid(row=14,column=0)

space_label = tk.Label(root, text =" ").grid(row=13,column=0)

increase_factor_label=tk.Label(root, text = 'Increase Factor(IF)', font=('calibre',10, 'bold')).grid(row=16,column=0)

space_label = tk.Label(root, text =" ").grid(row=15,column=0)

no_load_loss_label=tk.Label(root, text = 'No Load Loss(NLL)', font=('calibre',10, 'bold')).grid(row=18,column=0)

space_label = tk.Label(root, text =" ").grid(row=17,column=0)

load_loss_label=tk.Label(root, text = 'Load Loss(LL)', font=('calibre',10, 'bold')).grid(row=20,column=0)

space_label = tk.Label(root, text =" ").grid(row=19,column=0)

LIC_label=tk.Label(root, text = 'LIC', font=('calibre',10, 'bold')).grid(row=22,column=0)

space_label = tk.Label(root, text =" ").grid(row=21,column=0)


#Second Row
load_loss_of_ref_transformer_label=tk.Label(root, text = 'Load Loss of Ref Trns ^_^', font=('calibre',10, 'bold')).grid(row=4,column=3)

space_label = tk.Label(root, text ="  ").grid(row=3,column=2)

no_load_loss_of_ref_transformer_label=tk.Label(root, text = 'No Load Loss Ref trans ^_^', font=('calibre',10, 'bold')).grid(row=6,column=3)

space_label = tk.Label(root, text ="  ").grid(row=5,column=2)

current_year_energy_price_label=tk.Label(root, text = 'Current Year Energy price', font=('calibre',10, 'bold')).grid(row=8,column=3)

space_label = tk.Label(root, text ="  ").grid(row=7,column=2)

life_span_label=tk.Label(root, text = 'Life Span', font=('calibre',10, 'bold')).grid(row=10,column=3)

space_label = tk.Label(root, text ="  ").grid(row=9,column=2)

peak_per_unit_transformer_load_label=tk.Label(root, text = 'Peak Per Unit Tr Load', font=('calibre',10, 'bold')).grid(row=12,column=3)

space_label = tk.Label(root, text ="  ").grid(row=11,column=2)

peak_responsibility_factor_label=tk.Label(root, text = 'Peak Responsibilty Factor ^_^', font=('calibre',10, 'bold')).grid(row=14,column=3)

space_label = tk.Label(root, text ="  ").grid(row=13,column=2)

current_year_emission_cost_factor_label=tk.Label(root, text = 'Current Year Emission Cost Factor ^_^', font=('calibre',10, 'bold')).grid(row=16,column=3)
space_label = tk.Label(root, text ="      ").grid(row=16,column=2)
space_label = tk.Label(root, text ="  ").grid(row=15,column=2)

load_factor_label=tk.Label(root, text = 'Load Factor', font=('calibre',10, 'bold')).grid(row=18,column=3)

space_label = tk.Label(root, text ="  ").grid(row=17,column=2)

bid_price_label=tk.Label(root, text = 'Bid Price', font=('calibre',10, 'bold')).grid(row=20,column=3)

space_label = tk.Label(root, text ="  ").grid(row=19,column=2)

#Entry Attributes

HPY_var_Entery = tk.Entry(root,textvariable=HPY_var, width=10,borderwidth=5).grid(row=4,column=1)
space_label = tk.Label(root, text =" ").grid(row=1,column=1)

Avf_var_Entery = tk.Entry(root,textvariable=Avf_var,width=10,borderwidth=5).grid(row=6,column=1)
space_label = tk.Label(root, text =" ").grid(row=3,column=1)

annual_escalation_rate_Entery = tk.Entry(root,textvariable=annual_escalation_rate,width=10,borderwidth=5).grid(row=8,column=1)
space_label = tk.Label(root, text =" ").grid(row=5,column=1)

Fixed_cost_rate_Entery = tk.Entry(root,textvariable=Fixed_cost_rate,width=10,borderwidth=5).grid(row=10,column=1)
space_label = tk.Label(root, text =" ").grid(row=7,column=1)

efficiency_of_transmission_Entery = tk.Entry(root,textvariable=efficiency_of_transmission,width=10,borderwidth=5).grid(row=12,column=1)
space_label = tk.Label(root, text =" ").grid(row=9,column=1)

discount_rate_Entery = tk.Entry(root,textvariable=discount_rate,width=10,borderwidth=5).grid(row=14,column=1)
space_label = tk.Label(root, text =" ").grid(row=11,column=1)

increase_factor_Entery = tk.Entry(root,textvariable=increase_factor,width=10,borderwidth=5).grid(row=16,column=1)
space_label = tk.Label(root, text =" ").grid(row=13,column=1)

no_load_loss_Entery = tk.Entry(root,textvariable=no_load_loss,width=10,borderwidth=5).grid(row=18,column=1)
space_label = tk.Label(root, text =" ").grid(row=15,column=1)

load_loss_Entery = tk.Entry(root,textvariable=load_loss,width=10,borderwidth=5).grid(row=20,column=1)
space_label = tk.Label(root, text =" ").grid(row=17,column=1)

LIC_Entery = tk.Entry(root,textvariable=LIC,width=10,borderwidth=5).grid(row=22,column=1)
space_label = tk.Label(root, text =" ").grid(row=19,column=1)

#Second Row

load_loss_of_ref_transformer_Entery = tk.Entry(root,textvariable=load_loss_of_ref_transformer,width=10,borderwidth=5).grid(row=4,column=4)
space_label = tk.Label(root, text =" ").grid(row=3,column=1)

no_load_loss_of_ref_transformer_Entery = tk.Entry(root,textvariable=no_load_loss_of_ref_transformer,width=10,borderwidth=5).grid(row=6,column=4)
space_label = tk.Label(root, text =" ").grid(row=5,column=1)

current_year_energy_price_Entery = tk.Entry(root,textvariable=current_year_energy_price,width=10,borderwidth=5).grid(row=8,column=4)
space_label = tk.Label(root, text =" ").grid(row=7,column=1)

life_span_Entery = tk.Entry(root,textvariable=life_span,width=10,borderwidth=5).grid(row=10,column=4)
space_label = tk.Label(root, text =" ").grid(row=9,column=1)

peak_per_unit_transformer_load_Entery = tk.Entry(root,textvariable=peak_per_unit_transformer_load,width=10,borderwidth=5).grid(row=12,column=4)
space_label = tk.Label(root, text =" ").grid(row=11,column=1)

peak_responsibility_factor_Entery = tk.Entry(root,textvariable=peak_responsibility_factor,width=10,borderwidth=5).grid(row=14,column=4)
space_label = tk.Label(root, text =" ").grid(row=13,column=1)

current_year_emission_cost_factor_Entery = tk.Entry(root,textvariable=current_year_emission_cost_factor,width=10,borderwidth=5).grid(row=16,column=4)
space_label = tk.Label(root, text =" ").grid(row=15,column=1)

load_factor_Entery = tk.Entry(root,textvariable=load_factor,width=10,borderwidth=5).grid(row=18,column=4)
space_label = tk.Label(root, text =" ").grid(row=17,column=1)

bid_price_Entery = tk.Entry(root,textvariable=bid_price,width=10,borderwidth=5).grid(row=20,column=4)
space_label = tk.Label(root, text =" ").grid(row=19,column=1)




# space_label = tk.Label(root, text = '  ', font = ('calibre',10,'bold')).grid(row=0,column=1)

  
# # creating a entry for input
# # name using widget Entry

# HYP_entry = tk.Entry(root,textvariable = HYP_var,width=10,borderwidth=5, font=('calibre',10,'normal')).grid(row=0,column=2)

  
# # creating a label for password
# space_label = tk.Label(root, text = ' ', font = ('calibre',10,'bold')).grid(row=1,column=0)

# Avf_label = tk.Label(root, text = 'Availability factor', font = ('calibre',10,'bold')).grid(row=2,column=0)

  
# # creating a entry for password
# space_label = tk.Label(root, text = ' ', font = ('calibre',10,'bold')).grid(row=1,column=1)

# Avf_entry=tk.Entry(root, textvariable = Avf_var,width=10,borderwidth=5, font = ('calibre',10,'normal')).grid(row=2,column=2)# show = '*')

  
# # creating a button using the widget 
# # Button that will call the submit function 

sub_btn=tk.Button(root,text = 'Click For TOC', command = submit,fg="blue" ,bg="yellow",borderwidth=6,width=10,height=3).grid(row=22,column=4,rowspan=2)

  
# placing the label and entry in
# the required position using grid
# method


#HYP_entry

#passw_label.grid(row=1,column=0)

#passw_entry.grid(row=1,column=1)

#sub_btn.grid(row=40,column=0)

  
# performing an infinite loop 
# for the window to display
root.mainloop()
 
