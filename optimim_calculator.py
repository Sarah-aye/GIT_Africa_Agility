from tkinter import *

root = Tk()
root.title("Optimum calculator")
root.geometry("450x500")
root.configure(bg="#873e23")
root.resizable(False, False)

font_properties = ("Arial", 14)
btn_bg = "#442510"
btn_fg = "#eab676"

# the best part. the functions that will run the calculator... handles button clicked and updates the entry field

def on_button_click(value):
    current = entry_var.get() # .get() function gets whatever you put in the entry
    entry_var.set(current + value)
    if value =="C":
        entry_var.set("")
    elif value=="X":
        entry_var.set(current[:-1]) #get the last value and delete it
    elif value=="=":
        try:
            result = eval(current) # eval() function is built in function that evaluate all current value
            entry_var.set(result)
        except ValueError as e:
            entry_var.set(e)
    else:
        entry_var.set(str(value))
   

entry_var = StringVar()
calc_entry = Entry(root, textvariable=entry_var, font=("Arial", 20), bg="#442510", fg="#eab676", justify="left", bd=5)
calc_entry.grid(row=0, column=0, ipadx=8, ipady=8, columnspan=7)

#row 1 (c-x-())

clear_btn = Button(root, text="C", width=6, height=2, font=font_properties, bg="black", fg=btn_fg, command=lambda:on_button_click("C"))
clear_btn.grid(row=1, column=0, padx=4, pady=4)

delete_btn = Button(root, text="X", width=6, height=2, font=font_properties, bg="black", fg=btn_fg,command=lambda:on_button_click("X"))
delete_btn.grid(row=1, column=1, padx=4, pady=4)

opening_br_btn = Button(root, text="(", width=6, height=2, font=font_properties, bg="black", fg=btn_fg,command=lambda:on_button_click("("))
opening_br_btn.grid(row=1, column=2, padx=4, pady=4)

closing_br_btn = Button(root, text=")", width=6, height=2, font=font_properties, bg="black", fg=btn_fg,command=lambda:on_button_click(")"))
closing_br_btn.grid(row=1, column=3, padx=4, pady=4)

#row 2 (7-8-9-/)
btn_7 = Button(root, text="7", width=6, height=2, font=font_properties, bg="black", fg=btn_fg,command=lambda:on_button_click("7"))
btn_7.grid(row=2, column=0, padx=4, pady=2)

btn_8 = Button(root, text="8", width=6, height=2, font=font_properties, bg="black", fg=btn_fg,command=lambda:on_button_click("8"))
btn_8.grid(row=2, column=1, padx=4, pady=2)

btn_9 = Button(root, text="9", width=6, height=2, font=font_properties, bg="black", fg=btn_fg,command=lambda:on_button_click("9"))
btn_9.grid(row=2, column=2, padx=4, pady=2)

btn_bkslash = Button(root, text="/", width=6, height=2, font=font_properties, bg="black", fg=btn_fg,command=lambda:on_button_click("/"))
btn_bkslash.grid(row=2, column=3, padx=4, pady=2)

#row 3 (4-5-6-*)
btn_4 = Button(root, text="4", width=6, height=2, font=font_properties, bg="black", fg=btn_fg,command=lambda:on_button_click("4"))
btn_4.grid(row=3, column=0, padx=4, pady=2)

btn_5 = Button(root, text="5", width=6, height=2, font=font_properties, bg="black", fg=btn_fg,command=lambda:on_button_click("5"))
btn_5.grid(row=3, column=1, padx=4, pady=2)

btn_6 = Button(root, text="6", width=6, height=2, font=font_properties, bg="black", fg=btn_fg,command=lambda:on_button_click("6"))
btn_6.grid(row=3, column=2, padx=4, pady=2)

btn_multiply = Button(root, text="*", width=6, height=2, font=font_properties, bg="black", fg=btn_fg,command=lambda:on_button_click("*"))
btn_multiply.grid(row=3, column=3, padx=4, pady=2)

# row 4 (1-2-3-+)

btn_1 = Button(root, text="1", width=6, height=2, font=font_properties, bg="black", fg=btn_fg, command=lambda:on_button_click("1"))
btn_1.grid(row=4, column=0, padx=4, pady=2)

btn_2 = Button(root, text="2", width=6, height=2, font=font_properties, bg="black", fg=btn_fg, command=lambda:on_button_click("2"))
btn_2.grid(row=4, column=1, padx=4, pady=2)

btn_3 = Button(root, text="3", width=6, height=2, font=font_properties, bg="black", fg=btn_fg, command=lambda:on_button_click("3"))
btn_3.grid(row=4, column=2, padx=4, pady=2)

btn_multiply = Button(root, text="+", width=6, height=2, font=font_properties, bg="black", fg=btn_fg, command=lambda:on_button_click("+"))
btn_multiply.grid(row=4, column=3, padx=4, pady=2)

# row 5 (0-.---=)
btn_0 = Button(root, text="0", width=6, height=2, font=font_properties, bg="black", fg=btn_fg, command=lambda:on_button_click("0"))
btn_0.grid(row=5, column=0, padx=4, pady=2)

btn_dot = Button(root, text=".", width=6, height=2, font=font_properties, bg="black", fg=btn_fg, command=lambda:on_button_click("."))
btn_dot.grid(row=5, column=1, padx=4, pady=2)

btn_minus = Button(root, text="-", width=6, height=2, font=font_properties, bg="black", fg=btn_fg, command=lambda:on_button_click("-"))
btn_minus.grid(row=5, column=2, padx=4, pady=2)

btn_equal = Button(root, text="=", width=6, height=2, font=font_properties, bg="black", fg=btn_fg, command=lambda:on_button_click("="))
btn_equal.grid(row=5, column=3, padx=4, pady=2)

root.mainloop()
