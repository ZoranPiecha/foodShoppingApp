from tkinter import *
from PIL import ImageTk, Image

color = ["black", "white", "#D6D3F0", "#0B3142", "#001011", "#D8D4DA"]

root = Tk()

root.title("FoodApp by ZP")
root.geometry("470x677+780+60")
root.resizable(False, False)
root.configure(bg=color[2])
calc = ""
add_list = []
ban_price = []
rap_price = []
pea_price = []
sta_price = []
gra_price = []
kiw_price = []
lem_price = []
che_price = []
gap_price = []
price_list = []
price_list1 = []
w_length = 470
l_length = 120
w_p_length = 780
l_p_length = 60
all_amount = 0
price_amount = 0
price_amount1 = 0
price_amount_check = 0
price_amount_check1 = 0
ban_amount, rap_amount, pea_amount = 0, 0, 0
sta_amount, gra_amount, kiw_amount = 0, 0, 0
lem_amount, che_amount, gap_amount = 0, 0, 0
ban_amount_check, rap_amount_check, pea_amount_check = 0, 0, 0
sta_amount_check, gra_amount_check, kiw_amount_check = 0, 0, 0
lem_amount_check, che_amount_check, gap_amount_check = 0, 0, 0
ban_list, rap_list, pea_list, sta_list, gra_list, kiw_list, lem_list, che_list, gap_list = 0, 0, 0, 0, 0, 0, 0, 0, 0


food_nr = ["0", "1", "2",
           "3", "4", "5",
           "6", "7", "8"]


food_icon = ["🍌", "🍎", "🍐",
             "🍓", "🍇", "🥝",
             "🍋", "🍒", "🍏"]


food_name = ["banana", "red apple", "pear",
             "strawberry", "grapes", "kiwi",
             "lemon", "cherries", "green apple"]

food_price = ["1.50", "0.50", "1.25",
              "2.25", "1.75", "0.50",
              "0.50", "1.25", "1.00"]


class Banana:
    name = "banana"
    food_icon = "🍌"
    food_img = "food_img0"
    food_nr = "0"
    food_price = "1.50"


class RedApple:
    name = "red apple"
    food_icon = "🍎"
    food_img = "food_img1"
    food_nr = "1"
    food_price = "0.85"


class Pear:
    name = "pear"
    food_icon = "🍐"
    food_img = "food_img2"
    food_nr = "2"
    food_price = "1.25"


class Strawberries:
    name = "strawberries"
    food_icon = "🍓"
    food_img = "food_img3"
    food_nr = "3"
    food_price = "2.25"


class Grapes:
    name = "grapes"
    food_icon = "🍇"
    food_img = "food_img4"
    food_nr = "4"
    food_price = "1.15"


class Kiwi:
    name = "kiwi"
    food_icon = "🥝"
    food_img = "food_img5"
    food_nr = "5"
    food_price = "0.55"


class Lemon:
    name = "lemon"
    food_icon = "🍋"
    food_img = "food_img6"
    food_nr = "6"
    food_price = "0.35"


class Cherries:
    name = "cherries"
    food_icon = "🍒"
    food_img = "food_img7"
    food_nr = "7"
    food_price = "1.20"


class GreenApple:
    name = "green apple"
    food_icon = "🍏"
    food_img = "food_img8"
    food_nr = "8"
    food_price = "0.90"


# QUIT APPLICATION
def qui():
    root.quit()


# CONTINUE SHOPPING
def conti():
    clear()
    root.deiconify()
    top1.withdraw()


# PURCHASE
def purchase():
    clear()
    global top1
    top.withdraw()
    root.withdraw()
    top1 = Toplevel()
    top1.title("FoodApp by ZP - Purchased Successfully!")
    top1.geometry("470x226+780+280")
    top1.resizable(False, False)
    top1.focus()
    input_result25 = Label(top1, width=29, height=1,
                           fg=color[2], bg=color[4],
                           text="", font=("Arial", 25))
    input_result25.pack()
    input_result26 = Label(top1, width=29, height=1,
                           fg="yellow", bg=color[4],
                           text="Purchased Successfully!", font=("Arial", 25))
    input_result26.pack()
    input_result27 = Label(top1, width=29, height=1,
                           fg=color[2], bg=color[4],
                           text="", font=("Arial", 25))
    input_result27.pack()
    input_result28 = Button(top1, width=45, height=1,
                            fg=color[2], bg=color[4], command=lambda: conti(),
                            text="Continue Shopping", font=("Arial", 18))
    input_result28.pack()
    input_result29 = Button(top1, width=45, height=1,
                            fg=color[2], bg=color[4], command=lambda: qui(),
                            text="End Shopping", font=("Arial", 18))
    input_result29.pack()


# SHOW VALUES
def show(value):
    global calc, ban_list, rap_list, pea_list, sta_list, gra_list, kiw_list, lem_list, che_list, gap_list, all_amount
    add_list.append(value)
    calc += value
    input_result.config(text=calc)

    if value == "🍌":
        ban_list += 1
        all_amount += 1
        ban_price.append(food_price[0])
        price_list.append(food_price[0])
        price_list1.append(f"£{food_price[0]}")

    elif value == "🍎":
        rap_list += 1
        all_amount += 1
        rap_price.append(food_price[1])
        price_list.append(food_price[1])
        price_list1.append(f"£{food_price[1]}")

    elif value == "🍐":
        pea_list += 1
        all_amount += 1
        pea_price.append(food_price[2])
        price_list.append(food_price[2])
        price_list1.append(f"£{food_price[2]}")

    elif value == "🍓":
        sta_list += 1
        all_amount += 1
        sta_price.append(food_price[3])
        price_list.append(food_price[3])
        price_list1.append(f"£{food_price[3]}")

    elif value == "🍇":
        gra_list += 1
        all_amount += 1
        gra_price.append(food_price[4])
        price_list.append(food_price[4])
        price_list1.append(f"£{food_price[4]}")

    elif value == "🥝":
        kiw_list += 1
        all_amount += 1
        kiw_price.append(food_price[5])
        price_list.append(food_price[5])
        price_list1.append(f"£{food_price[5]}")

    elif value == "🍋":
        lem_list += 1
        all_amount += 1
        lem_price.append(food_price[6])
        price_list.append(food_price[6])
        price_list1.append(f"£{food_price[6]}")

    elif value == "🍒":
        che_list += 1
        all_amount += 1
        che_price.append(food_price[7])
        price_list.append(food_price[7])
        price_list1.append(f"£{food_price[7]}")

    elif value == "🍏":
        gap_list += 1
        all_amount += 1
        gap_price.append(food_price[8])
        price_list.append(food_price[8])
        price_list1.append(f"£{food_price[8]}")

    global price_amount_check1
    price_amount_check1 = price_amount1
    for item in price_list:
        price_amount_check1 += float(price_amount1) + float(item)
    round(price_amount_check1, 2)
    input_result2.config(text=f"£{price_amount_check1}")


# SHOW VALUES / TESTING
def show_cart():
    input_result.config(text="")
    input_result2.config(text="")
    # print(add_list)
    # print(ban_price)
    # print(price_list)
    # print(price_amount)
    # print(price_amount_check)


# CALCULATE PRICE AMOUNT
def calc_price():
    if calc != "":
        global price_amount_check, w_length, l_length, w_p_length, l_p_length, top
        price_amount_check = price_amount
        for item in price_list:
            price_amount_check += float(price_amount) + float(item)
        round(price_amount_check, 2)
        input_result2.config(text=f"£{price_amount_check}")
        top = Toplevel()
        top.title("FoodApp by ZP - Cart")
        w_length = 470
        l_length = 120
        w_p_length = 780
        l_p_length = 60

        # CART MENU
        input_result0 = Label(top, width=29, height=1,
                              fg="yellow", bg=color[4],
                              text=f"Total Price: £{price_amount_check}", font=("Arial", 25))
        input_result0.pack()

        input_result3 = Label(top, width=600, height=1,
                              fg="yellow", bg=color[4],
                              text="", font=("Arial", 1))
        input_result3.pack()

        input_result4 = Label(top, width=280, height=0,
                              fg=color[1], bg=color[4],
                              text="Summary", font=("Arial", 22))
        input_result4.pack()

        if ban_list > 0:
            global ban_amount_check
            global ban_amount
            l_length += 86
            ban_amount_check = int(ban_list) * float(food_price[0])
            input_result6 = Label(top, width=110, height=0,
                                  fg=color[3], bg=color[2],
                                  text="Banana 🍌", font=("Arial", 16))
            input_result6.pack()
            input_result7 = Label(top, width=110, height=0,
                                  fg=color[3], bg=color[2],
                                  text=f"Quantity: {ban_list} // Price: £{ban_amount_check}\n", font=("Arial", 16))
            input_result7.pack()

        if rap_list > 0:
            global rap_amount_check
            global rap_amount
            l_length += 86
            rap_amount_check = int(rap_list) * float(food_price[1])
            input_result8 = Label(top, width=110, height=0,
                                  fg=color[3], bg=color[2],
                                  text="Red Apple 🍎", font=("Arial", 16))
            input_result8.pack()
            input_result9 = Label(top, width=110, height=0,
                                  fg=color[3], bg=color[2],
                                  text=f"Quantity: {rap_list} // Price: £{rap_amount_check}\n", font=("Arial", 16))
            input_result9.pack()

        if pea_list > 0:
            global pea_amount_check
            global pea_amount
            l_length += 86
            pea_amount_check = int(pea_list) * float(food_price[2])
            input_result10 = Label(top, width=110, height=0,
                                   fg=color[3], bg=color[2],
                                   text="Pear 🍐", font=("Arial", 16))
            input_result10.pack()
            input_result11 = Label(top, width=110, height=0,
                                   fg=color[3], bg=color[2],
                                   text=f"Quantity: {pea_list} // Price: £{pea_amount_check}\n", font=("Arial", 16))
            input_result11.pack()

        if sta_list > 0:
            global sta_amount_check
            global sta_amount
            l_length += 86
            sta_amount_check = int(sta_list) * float(food_price[3])
            input_result12 = Label(top, width=110, height=0,
                                   fg=color[3], bg=color[2],
                                   text="Strawberries 🍓", font=("Arial", 16))
            input_result12.pack()
            input_result13 = Label(top, width=110, height=0,
                                   fg=color[3], bg=color[2],
                                   text=f"Quantity: {sta_list} // Price: £{sta_amount_check}\n", font=("Arial", 16))
            input_result13.pack()

        if gra_list > 0:
            global gra_amount_check
            global gra_amount
            l_length += 86
            gra_amount_check = int(gra_list) * float(food_price[4])
            input_result14 = Label(top, width=110, height=0,
                                   fg=color[3], bg=color[2],
                                   text="Grapes 🍇", font=("Arial", 16))
            input_result14.pack()
            input_result15 = Label(top, width=110, height=0,
                                   fg=color[3], bg=color[2],
                                   text=f"Quantity: {gra_list} // Price: £{gra_amount_check}\n", font=("Arial", 16))
            input_result15.pack()

        if kiw_list > 0:
            global kiw_amount_check
            global kiw_amount
            l_length += 86
            kiw_amount_check = int(kiw_list) * float(food_price[5])
            input_result16 = Label(top, width=110, height=0,
                                   fg=color[3], bg=color[2],
                                   text="Kiwi 🥝", font=("Arial", 16))
            input_result16.pack()
            input_result17 = Label(top, width=110, height=0,
                                   fg=color[3], bg=color[2],
                                   text=f"Quantity: {kiw_list} // Price: £{kiw_amount_check}\n", font=("Arial", 16))
            input_result17.pack()

        if lem_list > 0:
            global lem_amount_check
            global lem_amount
            l_length += 86
            lem_amount_check = int(lem_list) * float(food_price[6])
            input_result18 = Label(top, width=110, height=0,
                                   fg=color[3], bg=color[2],
                                   text="Lemon 🍋", font=("Arial", 16))
            input_result18.pack()
            input_result19 = Label(top, width=110, height=0,
                                   fg=color[3], bg=color[2],
                                   text=f"Quantity: {lem_list} // Price: £{lem_amount_check}\n", font=("Arial", 16))
            input_result19.pack()

        if che_list > 0:
            global che_amount_check
            global che_amount
            l_length += 86
            che_amount_check = int(che_list) * float(food_price[7])
            input_result20 = Label(top, width=110, height=0,
                                   fg=color[3], bg=color[2],
                                   text="Cherries 🍒", font=("Arial", 16))
            input_result20.pack()
            input_result21 = Label(top, width=110, height=0,
                                   fg=color[3], bg=color[2],
                                   text=f"Quantity: {che_list} // Price: £{che_amount_check}\n", font=("Arial", 16))
            input_result21.pack()

        if gap_list > 0:
            global gap_amount_check
            global gap_amount
            l_length += 86
            gap_amount_check = int(gap_list) * float(food_price[8])
            input_result22 = Label(top, width=110, height=0,
                                   fg=color[3], bg=color[2],
                                   text="Green Apple 🍏", font=("Arial", 16))
            input_result22.pack()
            input_result23 = Label(top, width=110, height=0,
                                   fg=color[3], bg=color[2],
                                   text=f"Quantity: {gap_list} // Price: £{gap_amount_check}\n", font=("Arial", 16))
            input_result23.pack()

        input_result24 = Button(top, width=110, height=1, command=lambda: purchase(),
                                fg=color[2], bg=color[4], text="COMPLETE PURCHASE",
                                font=("Arial", 18))
        input_result24.pack()
        top.geometry(f"{w_length}x{l_length}+{w_p_length}+{l_p_length}")
        top.resizable(False, False)
        top.focus()

    else:
        input_result.config(text="Choose your Product First")


# IMAGE SOURCE
food_img0 = Image.open("./img/banana.png")  # 🍌
food_img1 = Image.open("./img/red_apple.png")  # 🍎
food_img2 = Image.open("./img/pear.png")  # 🍐
food_img3 = Image.open("./img/strawberries.png")  # 🍓
food_img4 = Image.open("./img/grapes.png")  # 🍇
food_img5 = Image.open("./img/kiwi.png")  # 🥝
food_img6 = Image.open("./img/lemon.png")  # 🍋
food_img7 = Image.open("./img/cherries.png")  # 🍒
food_img8 = Image.open("./img/green_apple.png")  # 🍏
cart_img = Image.open("./img/cart.png")
clear_img = Image.open("./img/clear.png")


# IMAGE RESIZE
res_img0 = food_img0.resize((115, 115), Image.LANCZOS)
res_img1 = food_img1.resize((130, 130), Image.LANCZOS)
res_img2 = food_img2.resize((80, 130), Image.LANCZOS)
res_img3 = food_img3.resize((95, 95), Image.LANCZOS)
res_img4 = food_img4.resize((90, 90), Image.LANCZOS)
res_img5 = food_img5.resize((130, 130), Image.LANCZOS)
res_img6 = food_img6.resize((130, 130), Image.LANCZOS)
res_img7 = food_img7.resize((125, 125), Image.LANCZOS)
res_img8 = food_img8.resize((100, 125), Image.LANCZOS)
res_img9 = cart_img.resize((90, 90), Image.LANCZOS)
res_img10 = clear_img.resize((80, 70), Image.LANCZOS)


# NEW IMAGE VARIABLE
new_img0 = ImageTk.PhotoImage(res_img0)
new_img1 = ImageTk.PhotoImage(res_img1)
new_img2 = ImageTk.PhotoImage(res_img2)
new_img3 = ImageTk.PhotoImage(res_img3)
new_img4 = ImageTk.PhotoImage(res_img4)
new_img5 = ImageTk.PhotoImage(res_img5)
new_img6 = ImageTk.PhotoImage(res_img6)
new_img7 = ImageTk.PhotoImage(res_img7)
new_img8 = ImageTk.PhotoImage(res_img8)
new_img9 = ImageTk.PhotoImage(res_img9)
new_img10 = ImageTk.PhotoImage(res_img10)


# CLEAR DATA FUNCTION
def clear():
    global w_length, l_length, w_p_length, l_p_length
    global ban_amount_check, rap_amount_check, pea_amount_check
    global sta_amount_check, gra_amount_check, kiw_amount_check
    global lem_amount_check, che_amount_check, gap_amount_check
    global calc, all_amount, price_amount, price_amount1, price_amount_check, price_amount_check1
    global ban_list, rap_list, pea_list, sta_list, gra_list, kiw_list, lem_list, che_list, gap_list
    global ban_amount, rap_amount, pea_amount, sta_amount, gra_amount, kiw_amount, lem_amount, che_amount, gap_amount
    input_result.config(text="")
    input_result2.config(text="")
    calc = ""
    w_length = 470
    l_length = 120
    w_p_length = 780
    l_p_length = 60
    all_amount = 0
    price_amount = 0
    price_amount1 = 0
    price_amount_check = 0
    price_amount_check1 = 0
    ban_amount, rap_amount, pea_amount = 0, 0, 0
    sta_amount, gra_amount, kiw_amount = 0, 0, 0
    lem_amount, che_amount, gap_amount = 0, 0, 0
    ban_amount_check, rap_amount_check, pea_amount_check = 0, 0, 0
    sta_amount_check, gra_amount_check, kiw_amount_check = 0, 0, 0
    lem_amount_check, che_amount_check, gap_amount_check = 0, 0, 0
    ban_list, rap_list, pea_list, sta_list, gra_list, kiw_list, lem_list, che_list, gap_list = 0, 0, 0, 0, 0, 0, 0, 0, 0
    add_list.clear()
    ban_price.clear()
    rap_price.clear()
    pea_price.clear()
    sta_price.clear()
    gra_price.clear()
    kiw_price.clear()
    lem_price.clear()
    che_price.clear()
    gap_price.clear()
    price_list.clear()
    price_list1.clear()


# MAIN INPUT
input_result = Label(root, width=23, height=1, fg=color[3], bg=color[2], text="", font=("Arial", 30))
input_result2 = Label(root, width=23, height=1, fg=color[3], bg=color[2], text="", font=("Arial", 30))
input_result.pack()
input_result2.pack()

# MAIN APPLICATION BUTTONS
btn_nr0 = Button(root, image=new_img0, width=150, height=150, bg=color[2],
                 font=("Arial", 15), bd=1, command=lambda: show(food_icon[0]))
btn_nr0.place(x=3, y=105)

btn_nr1 = Button(root, image=new_img1, width=150, height=150, bg=color[2],
                 font=("Arial", 15), bd=1, command=lambda: show(food_icon[1]))
btn_nr1.place(x=158, y=105)

btn_nr2 = Button(root, image=new_img2, width=150, height=150, bg=color[2],
                 font=("Arial", 15), bd=1, command=lambda: show(food_icon[2]))
btn_nr2.place(x=313, y=105)

btn_nr3 = Button(root, image=new_img3, width=150, height=150, bg=color[2],
                 font=("Arial", 15), bd=1, command=lambda: show(food_icon[3]))
btn_nr3.place(x=3, y=260)

btn_nr4 = Button(root, image=new_img4, width=150, height=150, bg=color[2],
                 font=("Arial", 15), bd=1, command=lambda: show(food_icon[4]))
btn_nr4.place(x=158, y=260)

btn_nr5 = Button(root, image=new_img5, width=150, height=150, bg=color[2],
                 font=("Arial", 15), bd=1, command=lambda: show(food_icon[5]))
btn_nr5.place(x=313, y=260)

btn_nr6 = Button(root, image=new_img6, width=150, height=150, bg=color[2],
                 font=("Arial", 15), bd=1, command=lambda: show(food_icon[6]))
btn_nr6.place(x=3, y=415)

btn_nr7 = Button(root, image=new_img7, width=150, height=150, bg=color[2],
                 font=("Arial", 15), bd=1, command=lambda: show(food_icon[7]))
btn_nr7.place(x=158, y=415)

btn_nr8 = Button(root, image=new_img8, width=150, height=150, bg=color[2],
                 font=("Arial", 15), bd=1, command=lambda: show(food_icon[8]))
btn_nr8.place(x=313, y=415)

btn_list = Button(root, image=new_img10, width=235, height=100, bg=color[2],
                  font=("Arial", 15), bd=1, command=lambda: clear())
btn_list.place(x=3, y=570)

btn_list1 = Button(root, image=new_img9, width=220, height=100, bg=color[2],
                   font=("Arial", 15), bd=1, command=lambda: calc_price())
btn_list1.place(x=243, y=570)

mainloop()

