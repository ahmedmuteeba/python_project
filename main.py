# importing modules
from tkinter.ttk import *
import time
from tkinter import *
import pypyodbc
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter.ttk import Combobox
import textblob
import googletrans
import pyttsx3
from tkinter import ttk
from random import *


def loading():
    global load
    # this is splash screen
    load = Tk()
    load.geometry("600x350+300+150")
    load.config(bg="black")

    load.overrideredirect(True)
    logo = ImageTk.PhotoImage(
        Image.open(("D:/NED 1st semester/PL/project/images/loading.jpeg"))
    )
    name1 = Label(load, text="----A COLLABORATIVE PROJECT BY----")
    name = Label(load, text="MUTEEBA AHMED")
    name1.config(background="Black", foreground="white")
    name.config(background="Black", foreground="white")
    name1.place(x=180, y=70)
    name.place(x=230, y=100)
    # progress=Progressbar(length=200,orient=HORIZONTAL,mode="determinate")
    # progress.place(x=50,y=230)
    Label(load, image=logo).place(x=245, y=140)
    s = Style()
    s.theme_use("clam")
    s.configure(
        "orange.Horizontal.TProgressbar", foreground="orange", background="orange"
    )
    # Create a progressbar widget
    progress_bar = Progressbar(
        load,
        style="orange.Horizontal.TProgressbar",
        orient="horizontal",
        length=200,
        mode="determinate",
        maximum=100,
        value=0,
    )
    progress_bar.place(x=185, y=300)

    number = Label(load, text="", font="arial 15 bold")
    number.place(x=260, y=260)
    number.config(background="black", foreground="red")
    for i in range(1, 101, 1):
        progress_bar["value"] = i
        load.update()
        number.config(text=str(i) + "%")
        time.sleep(0.01)
    # m.after(time in millisecond, function name)
    load.after(200, delete_loading)  # jis window pe jana uskanaaam,mainwindow))

    load.mainloop()


def delete_loading():
    load.destroy()
    startPage()


# the screen that displays our apps name
def startPage():
    global f
    f = Tk()
    f.title("quiz application")
    f.geometry("920x600+180+20")

    f.resizable(False, False)
    img = Image.open("D:/NED 1st semester/PL/project/images/xoxo.png")
    resize = img.resize((920, 600), Image.ANTIALIAS)
    np = ImageTk.PhotoImage(resize)
    l = Label(f, image=np)
    l.place(x=0, y=0, relwidth=1, relheight=1)

    b = Button(
        f,
        text="start",
        bg="light blue",
        fg="white",
        font=("courier", 20),
        command=delete_start,
    )
    b.pack(padx=40, pady=20, side=BOTTOM)

    f.mainloop()


def delete_start():
    f.destroy()
    main_screen()


# now login page
global main_screen


def main_screen():
    global window

    window = Tk()
    window.geometry("920x600+180+20")
    window.resizable(False, False)
    window.title("L O G I N ")
    background = Image.open("D:/NED 1st semester/PL/project/images/menu (2).png")
    # antialias removes the structural padding from the image
    resizedbackg = background.resize((920, 600), Image.ANTIALIAS)
    newbbackg = ImageTk.PhotoImage(resizedbackg)

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global name_entry
    global password_entry

    l = Label(window, image=newbbackg)
    l.place(x=0, y=0, relwidth=1, relheight=1)

    # lable login at top
    Label(
        window,
        text="LOGIN FORM",
        font=("courier", 35),
        bg="white",
        width=10,
        fg="black",
    ).place(x=270, y=60)

    # creating label username
    Label(
        window, text="Username :", font=("courier", 20), bg="white", fg="black"
    ).place(x=250, y=150)
    # creating entry username
    name_entry = Entry(
        window,
        font=("courier", 20),
        bg="white",
        fg="blue",
        width=25,
        textvariable=username_verify,
    )
    name_entry.place(x=250, y=200)

    # creating lable passsword
    Label(window, text="Password :", font=("courier", 20), bg="white").place(
        x=250, y=250
    )
    # creating entry Password
    password_entry = Entry(
        window,
        font=("courier", 20),
        bg="white",
        fg="blue",
        width=25,
        textvariable=password_verify,
        show="*",
    )
    password_entry.place(x=250, y=300)
    # login Button
    Button(
        window, text="LOGIN", width=20, height=2, bg="light grey", command=loginVerify
    ).place(x=360, y=360)
    # creating lable for registration
    Label(
        window,
        text="Haven't registered yet??",
        font=("Comic Sans MS", 10, "bold"),
        fg="red",
        bg="#e3e3e3",
    ).place(x=350, y=450)
    # REGISTRATION BUTTON
    Button(
        window,
        text=" Click here to register  ",
        width=42,
        height=2,
        bg="light grey",
        command=register,
    ).place(x=290, y=480)
    window.mainloop()


def loginVerify():
    global username1

    username1 = username_verify.get()
    password1 = password_verify.get()

    if username1 == "" or password1 == "":
        messagebox.showerror("Error!", "FILL ALL FIELDS")
        name_entry.delete(0, END)
        password_entry.delete(0, END)
    else:
        con = pypyodbc.connect(
            r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};"
            r"DBQ=D:/NED 1st semester/PL/project/PL PROJECT (1).accdb;"
        )
        cur1 = con.cursor()
        cur1.execute("select username,password from trial")
        data = cur1.fetchall()
        # Now converting my data which was initially in list into the dictionary so that
        # we can verify username and password
        final = dict(data)
        if username1 in final.keys():
            if password1 == final[username1]:
                loginSuccessful()
            else:
                messagebox.showerror(
                    "Invalid Password",
                    "Incorrect password ! \nPlease enter correct password.",
                )
                password_entry.delete(0, END)
        else:
            messagebox.showerror(
                "Invalid Username!", "USER NOT FOUND ! \nPlease enter correct Username."
            )
            name_entry.delete(0, END)
            password_entry.delete(0, END)

        con.close()


def loginSuccessful():
    window.destroy()
    new()


# now designing a window for registration
def register():
    global register_screen
    window.destroy()
    register_screen = Tk()
    register_screen.title("R E G I S T E R")
    register_screen.geometry("920x600+180+20")
    ##

    background = Image.open("D:/NED 1st semester/PL/project/images/menu (3).png")
    # antialias removes the structural padding from the image
    resizedbackg2 = background.resize((920, 600), Image.ANTIALIAS)
    newbbackg2 = ImageTk.PhotoImage(resizedbackg2)
    l = Label(register_screen, image=newbbackg2)
    l.place(x=0, y=0, relwidth=1, relheight=1)

    # register_screen.config(bg="white")
    # setting global variables
    global fullname
    global username
    global password
    global continame
    global fullname_entry
    global username_entry
    global password_entry
    global continame_entry

    # setting text variables
    fullname = StringVar()
    username = StringVar()
    password = StringVar()
    continame = StringVar()

    Label(register_screen, bg="yellow").grid(row=0, column=0)

    Frame(register_screen, width=489, height=620, bg="white").place(x=220, y=0)
    # heading
    Label(
        register_screen,
        text="Sign Up",
        font=("courier", 25),
        width=23,
        height=2,
        bg="light grey",
    ).place(x=220, y=0)
    # set label for instruction
    Label(
        register_screen,
        text="Please enter your details below",
        bg="white",
        fg="grey",
        font=10,
    ).place(x=340, y=100)
    # now creating entry fields label
    fullname_lable = Label(
        register_screen, text="Full Name : ", bg="white", font=("courier", 15)
    )
    fullname_lable.place(x=250, y=200)

    username_lable = Label(
        register_screen, text="Username : ", bg="white", font=("courier", 15)
    )
    username_lable.place(x=250, y=270)

    password_lable = Label(
        register_screen, text="Password :", bg="white", font=("courier", 15)
    )
    password_lable.place(x=250, y=340)

    continame_label = Label(
        register_screen, text="Continent : ", bg="white", font=("courier", 15)
    )
    continame_label.place(x=250, y=410)
    # creating entry boxes
    fullname_entry = Entry(
        register_screen,
        font=("courier", 15),
        width=25,
        textvariable=fullname,
        bg="#C4A484",
    )
    fullname_entry.place(x=390, y=200)

    username_entry = Entry(
        register_screen,
        font=("courier", 15),
        width=25,
        textvariable=username,
        bg="#C4A484",
    )
    username_entry.place(x=390, y=270)

    password_entry = Entry(
        register_screen,
        font=("courier", 15),
        width=25,
        textvariable=password,
        bg="#C4A484",
    )
    password_entry.place(x=390, y=340)

    options = [
        "Asia",
        "Australia",
        "Antarctica",
        "Africa",
        "North America",
        "South America",
        "Europe",
    ]

    continame.set(".....Click to select Your Continent...")
    # Create Dropdown menu
    continame_entry = OptionMenu(register_screen, continame, *options)
    continame_entry.config(
        width=28,
        font=("courier", 12),
        bg="#C4A484",
        fg="blue",
        activebackground="yellow",
    )
    continame_entry.place(x=390, y=410)

    # buttons
    Button(
        register_screen,
        text="Register",
        font=("courier ", 12),
        width=10,
        bg="#C4A484",
        fg="blue",
        command=register_user,
    ).place(x=415, y=500)
    # a button for going back after logging in
    Button(register_screen, text="Back", bg="white", fg="blue", command=back).place(
        x=220, y=550
    )

    register_screen.mainloop()


# back button's command
def back():
    register_screen.destroy()
    main_screen()


# register button command
def register_user():
    global register_screen

    if (
        fullname.get() == ""
        or username.get() == ""
        or password.get() == ""
        or continame.get() == ".....Click to select Your Continent..."
    ):
        messagebox.showerror("F I E L D S", "Fill all fields !")
    else:
        con = pypyodbc.connect(
            r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};"
            r"DBQ=D:/NED 1st semester/PL/project/PL PROJECT (1).accdb;"
        )
        cur2 = con.cursor()
        cur2.execute("select username from trial")
        data = cur2.fetchall()
        list = []
        for i in data:
            for j in i:
                list.append(j)

        if username.get() in list:
            messagebox.showerror("username", "username already taken!")
            con.commit()
            con.close()
        else:
            cur1 = con.cursor()
            cur1.execute(
                f"INSERT INTO trial(name,username,password,continent) values('{fullname.get()}','{username.get()}','{password.get()}','{continame.get()}')"
            )
            con.commit()
            messagebox.showinfo("SUCCESS", "You have been registered")
            con.close()
            # set a label for showing success information on screen
            Label(
                register_screen,
                text="Registration Success click on back to login",
                fg="green",
                bg="white",
                font=("calibri", 11),
            ).place(x=350, y=550)

            fullname_entry.delete(0, END)
            password_entry.delete(0, END)
            continame.set("Click to select Your Continent")

            con1 = pypyodbc.connect(
                r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};"
                r"DBQ=D:/NED 1st semester/PL/project/PL PROJECT (1).accdb;"
            )
            cur2 = con1.cursor()
            cur2.execute(f"INSERT INTO Score(username) values('{username.get()}')")
            con1.commit()

        username_entry.delete(0, END)


# menu page which has all buttons
def new():
    global roott
    roott = Tk()
    roott.title("M E N U -P A G E")
    roott.geometry("920x600+180+20")
    roott.resizable(False, False)

    img = Image.open("D:/NED 1st semester/PL/project/images/menu1.png")
    resize = img.resize((920, 600), Image.ANTIALIAS)
    np = ImageTk.PhotoImage(resize)
    l = Label(roott, image=np)
    l.place(x=0, y=0, relwidth=1, relheight=1)

    l1 = Label(roott, text="MENU", font=("courier 20 bold"), bg="white")
    l1.place(x=400, y=20)

    b = Button(
        roott, text="accent training", font=("courier 16"), bg="pink", command=accentt
    )
    b.place(x=410, y=110)
    b1 = Button(
        roott,
        text="stroop effect",
        font=("courier 16"),
        bg="pink",
        width=16,
        command=cgame,
    )
    b1.place(x=637, y=110)
    b2 = Button(
        roott,
        text="tile matching",
        font=("courier 16"),
        bg="pink",
        width=16,
        command=game,
    )
    b2.place(x=410, y=210)
    b3 = Button(
        roott,
        text="linguistics",
        font=("courier 16"),
        bg="pink",
        width=16,
        command=ling,
    )
    b3.place(x=637, y=210)
    b4 = Button(
        roott,
        text="islamic questions",
        font=("courier 16"),
        bg="pink",
        width=16,
        command=dbisl,
    )
    b4.place(x=410, y=320)
    b5 = Button(
        roott,
        text="Genernal Knowledge",
        font=("courier 15"),
        bg="pink",
        width=17,
        command=dbGK,
    )
    b5.place(x=637, y=320)
    b6 = Button(
        roott, text="Logical", font=("courier 16"), bg="pink", width=16, command=dblogic
    )
    b6.place(x=410, y=420)
    b7 = Button(
        roott,
        text="magic box",
        font=("courier 16"),
        bg="pink",
        width=16,
        command=magicgame,
    )
    b7.place(x=637, y=420)
    b8 = Button(
        roott,
        text="Score Board",
        font=("courier 16"),
        bg="pink",
        width=13,
        command=scard,
        wraplength=100,
    )
    b8.place(x=170, y=100)
    roott.mainloop()


##back buttons
def back10():
    nw.destroy()
    new()


def back9():
    magic.destroy()
    new()


def back8():
    lg.destroy()
    new()


def back7():
    gk.destroy()
    new()


def back6():
    isl.destroy()
    new()


def back5():
    gamescreen.destroy()
    new()


def back4():
    g.destroy()
    new()


def back3():
    p.destroy()
    new()


def back2():
    m.destroy()
    new()


def accentt():
    global m
    roott.destroy()
    engine = pyttsx3.init()

    def speaknow():
        # using 1,END becz we want the input to be read from the 1st line to the very last line
        text = text_area.get(1.0, END)
        gender = gender_combobox.get()
        speed = speed_combobox.get()
        # using getproperty to add different voices
        voices = engine.getProperty("voices")

        def setvoice():
            if gender == "Male":
                # here we want to imply the property
                # inside parenthesis 1st we write our property name
                # than we will set that specific property 0 is for males
                # where id is the string identifier of the voice
                engine.setProperty("voice", voices[0].id)
                # after initiliazing we will make the program to speak the text by using say() function
                engine.say(text)
                # to run the speech we use Run&Wait only say function wont be said unless the interpreter encounters RAW
                engine.runAndWait()
            else:
                engine.setProperty("voice", voices[1].id)
                engine.say(text)
                engine.runAndWait()

        if text:
            if speed == "fast":
                engine.setProperty("rate", 250)
                setvoice()
            elif speed == "normal":
                engine.setProperty("rate", 150)
                setvoice()
            else:
                engine.setProperty("rate", 80)
                setvoice()

    def clear():
        text_area.delete(1.0, END)

    m = Tk()
    m.title("A C C E N T-T R A I N E R")
    m.geometry("920x600+180+20")
    m.resizable(False, False)

    # Image.open() Opens and identifies the given image file.
    background = Image.open("D:/NED 1st semester/PL/project/images/accent3.png")
    # antialias removes the structural padding from the image
    resizedbackg = background.resize((920, 600), Image.ANTIALIAS)
    newbbackg = ImageTk.PhotoImage(resizedbackg)

    l = Label(m, image=newbbackg)
    l.place(x=0, y=0, relwidth=1, relheight=1)

    ##adding frame top frame
    top_frame = Frame(m, bg="white", width=1000, height=75)
    top_frame.place(x=0, y=0)
    # adding pic to the top frame
    my_pic = Image.open("D:/NED 1st semester/PL/project/images/mike.png")
    resized = my_pic.resize((70, 70), Image.ANTIALIAS)
    new = ImageTk.PhotoImage(resized)
    Label(top_frame, image=new, bg="white").place(x=10, y=5)
    Label(
        top_frame,
        text="Accent Training",
        font=("courier", 20, "bold"),
        fg="black",
        bg="white",
    ).place(x=100, y=30)

    ####
    text_area = Text(m, font="Robote 20", bg="white")
    text_area.place(x=10, y=150, width=500, height=250)

    Label(m, text="VOICE", font="courier 15 bold", bg="blue", fg="black").place(
        x=580, y=160
    )
    Label(m, text="SPEED", font="courier 15 bold", bg="blue", fg="black").place(
        x=760, y=160
    )
    # A combobox is a combination of an Entry widget and a Listbox widget
    # here from preventing user to enter input we use state method=r(readonly)
    gender_combobox = Combobox(
        m, values=["Male", "Female"], font="courier 14 ", state="r", width=10
    )
    gender_combobox.place(x=550, y=200)
    # using set to initialze the default voice
    gender_combobox.set("Male")

    speed_combobox = Combobox(
        m, values=["fast", "normal", "Slow"], font="courier 14", state="r", width=10
    )
    speed_combobox.place(x=730, y=200)
    speed_combobox.set("normal")

    imageicon = Image.open("D:/NED 1st semester/PL/project/images/speek.png")
    resizedic = imageicon.resize((35, 35), Image.ANTIALIAS)
    newpic = ImageTk.PhotoImage(resizedic)
    ##if we want to use image and text together in button we use compound
    ##as given below image will be at the left corner
    btn = Button(
        m,
        text="speak",
        compound=LEFT,
        image=newpic,
        width=130,
        font="courier 14 ",
        command=speaknow,
    )
    btn.place(x=550, y=280)

    ####ADDING CLEAR BUTTON
    clear_button = Button(
        m, text="clear", width=10, height=1, font="courier 15 ", command=clear
    )
    clear_button.place(x=740, y=280)
    homebtn = Button(
        m, text="home", width=10, height=1, font="courier 15 ", command=back2
    )
    homebtn.place(x=100, y=530)

    m.mainloop()


def ling():
    roott.destroy()
    global p
    p = Tk()
    p.title(" Translator")

    p.geometry("920x600+180+20")
    p.resizable(False, False)

    background = Image.open("D:/NED 1st semester/PL/project/images/speakbg3.png")
    # antialias removes the structural padding from the image
    resizedbackg = background.resize((920, 600), Image.ANTIALIAS)
    newbbackg = ImageTk.PhotoImage(resizedbackg)

    l = Label(p, image=newbbackg)
    l.place(x=0, y=0, relwidth=1, relheight=1)

    def translate_it():
        # Delete Any Previous Translations
        translated_text.delete(1.0, END)

        try:
            # Get Languages From Dictionary Keys
            # Get the From Langauage Key
            for key, value in languages.items():
                if value == original_combo.get():
                    from_language_key = key

            # Get the To Language Key
            for key, value in languages.items():
                if value == translated_combo.get():
                    to_language_key = key

            # Turn Original Text into a TextBlob
            words = textblob.TextBlob(original_text.get(1.0, END))

            # Translate Text
            words = words.translate(from_lang=from_language_key, to=to_language_key)

            # Output translated text to screen
            translated_text.insert(1.0, words)

            # Initialize the speech engine
            engine = pyttsx3.init()

            # Play with Voices
            voices = engine.getProperty("voices")
            # for voice in voices:
            # 	engine.setProperty('voice', voice.id)
            # 	engine.say(words)

            # Pass text to speech engine
            engine.say(words)

            # Run to the engine
            engine.runAndWait()

        except Exception as e:
            messagebox.showerror("Translator", e)

    def clear():
        # Clear the text boxes
        original_text.delete(1.0, END)
        translated_text.delete(1.0, END)

    # language_list = (1,2,3,4,5,6,7,8,9,0,11,12,13,14,15,16,16,1,1,1,1,1,1,1,1,1,1,1,1,1)

    # Grab Language List From GoogleTrans
    languages = googletrans.LANGUAGES

    # Convert to list
    language_list = list(languages.values())

    l = Label(p, text="LINGUISTIC", font=("courier", 20), padx=20, pady=10)
    l.grid(row=1, column=1)

    # Text Boxes
    original_text = Text(p, height=10, width=40)
    original_text.grid(row=2, column=0, pady=20, padx=10)

    translate_button = Button(
        p, text="Translate!", font=("courier", 16), width=10, command=translate_it
    )
    translate_button.grid(row=2, column=1, padx=10)

    translated_text = Text(p, height=10, width=40)
    translated_text.grid(row=2, column=2, padx=10)

    # Combo boxes
    original_combo = ttk.Combobox(p, width=50, value=language_list)
    original_combo.current(21)
    original_combo.grid(row=3, column=0)

    translated_combo = ttk.Combobox(p, width=50, value=language_list)
    translated_combo.current(26)
    translated_combo.grid(row=3, column=2)

    # Clear button
    clear_button = Button(
        p, text="Clear", font=("courier", 16), width=10, command=clear
    )
    clear_button.grid(row=4, column=1, pady=10)
    ##homebutton
    homebtn2 = Button(
        p, text="home", width=10, height=1, font="courier 15 ", command=back3
    )
    homebtn2.place(x=100, y=530)

    p.mainloop()


# color game aka stroop effect
def cgame():
    global color_game
    roott.destroy()

    def colour_game():
        global timeleft
        global score
        # list of possible colour.
        colours = [
            "Red",
            "Blue",
            "Green",
            "Pink",
            "Black",
            "Yellow",
            "Orange",
            "Purple",
            "Brown",
        ]
        # scores and timeleft initially
        score = 0
        timeleft = 30

        def startGame(event):
            if timeleft == 30:
                # start the countdown timer.
                countdown()

            # run the function to
            # choose the next colour.
            nextColour()

        # Function to choose and
        # display the next colour.
        def nextColour():
            # use the globally declared 'score'
            # and 'play' variables above.
            global timeleft
            global score

            if timeleft > 0:
                e.focus_set()

                # if the colour typed is equal to the colour of the text
                if e.get().lower() == colours[1].lower():
                    score += 1

                # clear the text entry box.
                e.delete(0, END)
                shuffle(colours)
                # change the colour to type, by changing the
                # text and the colour to a random colour value
                label.config(fg=str(colours[1]), text=str(colours[0]))
                # print(colours,colours[1],colours[2])
                # update the score.
                scoreLabel.config(text="Score: " + str(score))

        # Countdown timer function
        def countdown():
            global timeleft

            # if a game is in play
            if timeleft > 0:
                # decrement the timer.
                timeleft -= 1

                # update the time left label
                timerLabel.config(text="Time left: " + str(timeleft))
                if timeleft == 0:
                    timerLabel.config(text="Time Over!", fg="red")

                # run the function again after 1 second.
                timerLabel.after(1000, countdown)

        global gamescreen
        gamescreen = Tk()
        gamescreen.title("Colour Game")
        gamescreen.geometry("600x300+180+20")

        # antialias removes the structural padding from the image
        gamebg = Image.open("D:/NED 1st semester/PL/project/images/white.png")
        resizedbackg = gamebg.resize((600, 300), Image.ANTIALIAS)
        newbackg = ImageTk.PhotoImage(resizedbackg)

        l = Label(gamescreen, image=newbackg)
        l.place(x=0, y=0, relwidth=1, relheight=1)

        # the instruction lable
        instruction = Label(
            gamescreen,
            text="Type in the COLOUR of the words not the WORD!",
            bg="white",
            fg="black",
            font=("courier", 15),
        )
        instruction.place(x=40, y=0)
        instruction.config(fg="grey")
        #  a score label
        keyLabel = Label(
            gamescreen, text="Press Enter to start", bg="white", font=("courier", 15)
        )
        keyLabel.place(x=200, y=40)
        scoreLabel = Label(
            gamescreen, text="Score = 0", bg="white", font=("cooper black", 15)
        )
        scoreLabel.place(x=238, y=65)

        # a time left label
        timerLabel = Label(
            gamescreen,
            text="Time left: " + str(timeleft),
            bg="white",
            font=("courier", 15),
        )
        timerLabel.place(x=225, y=90)

        # a label for displaying the colours
        label = Label(gamescreen, bg="white", font=("courier Bold", 50))
        label.place(x=190, y=120)

        # add a text entry box for
        # typing in colours
        e = Entry(gamescreen, bg="light blue", width=30, border=5)
        e.place(x=200, y=210)
        # set focus on the entry box
        e.focus_set()

        # run the 'startGame' function
        # when the enter key is pressed
        gamescreen.bind("<Return>", startGame)

        def stroop():
            messagebox.showinfo(
                "INFORMATION",
                "The Stroop effect is the delay in reaction time between congruent and incongruent stimuli.A basic task that demonstrates this effect occurs when there is a mismatch between the name of a color (e.g., 'blue', 'green', or 'red') and the color it is printed on (i.e., the word 'red' printed in blue ink instead of red ink). When asked to name the color of the word it takes longer and is more prone to errors when the color of the ink does not match the name of the color.This simple finding plays a huge role in psychological research and clinical psychology.\n\n        CHALLENGE:TRY TO SCORE 20+",
            )

        def reset_button():
            gamescreen.destroy()
            colour_game()

        info_button = Button(
            gamescreen,
            text="Information",
            bg="light blue",
            fg="black",
            font=("courier", 11),
            command=stroop,
        )
        info_button.place(x=0, y=270)

        cbg = Button(
            gamescreen,
            text="Home",
            bg="blue",
            fg="white",
            font=("courier", 15),
            command=back5,
        )
        cbg.place(x=250, y=260)

        resetButton = Button(
            gamescreen,
            text="Reset",
            bg="light blue",
            fg="black",
            font=("courier", 11),
            command=reset_button,
        )
        resetButton.place(x=547, y=270)
        gamescreen.mainloop()

    colour_game()


# the tile matching game
def game():
    global g
    roott.destroy()
    g = Tk()
    g.geometry("920x600+180+20")
    g.resizable(False, False)
    g.title("Tile Matching Game")

    img1 = Image.open("D:/NED 1st semester/PL/project/images/tile.png")
    res_img = img1.resize((920, 600), Image.ANTIALIAS)

    img2 = ImageTk.PhotoImage(res_img)

    bg_l = Label(g, image=img2)
    bg_l.place(x=0, y=0, relwidth=1, relheight=1)

    global matches
    global count, l_ans, d_ans, win

    # what goes on the tiles, 4x3 game
    global matches
    matches = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]
    shuffle(matches)

    Game_label = Label(
        g, text="Tile Matching", font=("Courier", 30, "bold"), bg="#df7961"
    )
    Game_label.pack(side=TOP, pady=15)

    # create frame for buttons
    f1 = Frame(g)
    f1.pack(pady=15)

    # counter for how many tiles matched
    global win
    win = 0

    # create function to show that you have won game
    def winner():
        l1.config(text="Congratulations!! You won!")

        # Change colour of buttons when you win through loop(to make code smaller)
        b_list = [b0, b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11]
        for button in b_list:
            button.config(bg="#df7961")

    # Create function to show number on tile
    count = 0
    l_ans = []
    d_ans = {}

    def show(button, match_index):
        global count, l_ans, d_ans, win

        if button["text"] == " " and count < 2:
            button["text"] = matches[match_index]

            # add what tile was clicked to the list
            l_ans.append(match_index)
            # add which index of shuffled match list into the dictionary
            d_ans[button] = matches[match_index]
            count = count + 1

        # Determine whether answer is correct
        if len(l_ans) == 2:
            # if the answers match
            if matches[l_ans[0]] == matches[l_ans[1]]:
                l1.config(text="It's a match!", bg="#df7961")
                # make the buttons that have already been clicked to be disabled
                for key in d_ans:
                    key["state"] = "disabled"
                count = 0
                l_ans = []
                d_ans = {}

                # Increment win counter every time a tile is matched
                win = win + 1
                if win == 6:
                    winner()
            # if the answer doesn't match
            else:
                l1.config(text="Uh oh! Not a match", bg="#df7961")
                count = 0
                l_ans = []
                # optional pop up box
                messagebox.showinfo("Incorrect!", "Wrong answer!!")

                # reset the clicked buttons when answers don't match
                for key in d_ans:
                    key["text"] = " "

                d_ans = {}

    # Define our buttons
    b0 = Button(
        f1,
        text=" ",
        font=("Courier", 20),
        bg="beige",
        height=3,
        width=6,
        command=lambda: show(b0, 0),
        relief=RAISED,
        bd=4,
    )
    b1 = Button(
        f1,
        text=" ",
        font=("Courier", 20),
        bg="beige",
        height=3,
        width=6,
        command=lambda: show(b1, 1),
        relief=RAISED,
        bd=4,
    )
    b2 = Button(
        f1,
        text=" ",
        font=("Courier", 20),
        bg="beige",
        height=3,
        width=6,
        command=lambda: show(b2, 2),
        relief=RAISED,
        bd=4,
    )
    b3 = Button(
        f1,
        text=" ",
        font=("Courier", 20),
        bg="beige",
        height=3,
        width=6,
        command=lambda: show(b3, 3),
        relief=RAISED,
        bd=4,
    )
    b4 = Button(
        f1,
        text=" ",
        font=("Courier", 20),
        bg="beige",
        height=3,
        width=6,
        command=lambda: show(b4, 4),
        relief=RAISED,
        bd=4,
    )
    b5 = Button(
        f1,
        text=" ",
        font=("Courier", 20),
        bg="beige",
        height=3,
        width=6,
        command=lambda: show(b5, 5),
        relief=RAISED,
        bd=4,
    )
    b6 = Button(
        f1,
        text=" ",
        font=("Courier", 20),
        bg="beige",
        height=3,
        width=6,
        command=lambda: show(b6, 6),
        relief=RAISED,
        bd=4,
    )
    b7 = Button(
        f1,
        text=" ",
        font=("Courier", 20),
        bg="beige",
        height=3,
        width=6,
        command=lambda: show(b7, 7),
        relief=RAISED,
        bd=4,
    )
    b8 = Button(
        f1,
        text=" ",
        font=("Courier", 20),
        bg="beige",
        height=3,
        width=6,
        command=lambda: show(b8, 8),
        relief=RAISED,
        bd=4,
    )
    b9 = Button(
        f1,
        text=" ",
        font=("Courier", 20),
        bg="beige",
        height=3,
        width=6,
        command=lambda: show(b9, 9),
        relief=RAISED,
        bd=4,
    )
    b10 = Button(
        f1,
        text=" ",
        font=("Courier", 20),
        bg="beige",
        height=3,
        width=6,
        command=lambda: show(b10, 10),
        relief=RAISED,
        bd=4,
    )
    b11 = Button(
        f1,
        text=" ",
        font=("Courier", 20),
        bg="beige",
        height=3,
        width=6,
        command=lambda: show(b11, 11),
        relief=RAISED,
        bd=4,
    )

    # Create grid for each button
    b0.grid(row=0, column=0)
    b1.grid(row=0, column=1)
    b2.grid(row=0, column=2)
    b3.grid(row=0, column=3)

    b4.grid(row=1, column=0)
    b5.grid(row=1, column=1)
    b6.grid(row=1, column=2)
    b7.grid(row=1, column=3)

    b8.grid(row=2, column=0)
    b9.grid(row=2, column=1)
    b10.grid(row=2, column=2)
    b11.grid(row=2, column=3)

    # Create Label to display if answer was correct
    l1 = Label(g, text="", font="Courier")
    l1.pack(pady=20)

    # Home Button
    bhome = Button(
        g,
        font=("Courier", 15),
        text="Home",
        height=2,
        width=8,
        relief=RAISED,
        command=back4,
        bg="#df7961",
    )
    bhome.place(x=80, y=500)

    g.mainloop()


def scard():
    global nw
    roott.destroy()
    nw = Tk()
    nw.title("S C O R E - C A R D")
    nw.geometry("920x600+180+20")
    nw.resizable(False, False)

    scbg = Image.open("D:/NED 1st semester/PL/project/images/score1.png")
    scr = scbg.resize((920, 600), Image.ANTIALIAS)
    scimg = ImageTk.PhotoImage(scr)
    ll = Label(nw, image=scimg)
    ll.place(x=0, y=0, relwidth=1, relheight=1)

    sl = Label(nw, text="SCORE RECORDS", font=("courier 20 bold"), bg="white")
    sl.place(x=350, y=20)

    f = Frame(nw)
    f.place(x=220,y=90)
    display = ttk.Style(f)
    display.theme_use("classic")
    display.configure(".", font=("Courier", 17))
    display.configure("sctable.heading", foreground="pink", font=("Courier", 25))
    sctable = ttk.Treeview(
        f, columns=("sno", "username", "G_K", "LOGICAL", "ISLAMIC", "TOTAL")
    )
    sctable.pack()
    sctable["show"] = "headings"

    sctable.column("sno", width=50, minwidth=50, anchor=CENTER)
    sctable.column("username", width=120, minwidth=50, anchor=CENTER)
    sctable.column("G_K", width=80, minwidth=50, anchor=CENTER)
    sctable.column("LOGICAL", width=80, minwidth=50, anchor=CENTER)
    sctable.column("ISLAMIC", width=80, minwidth=50, anchor=CENTER)
    sctable.column("TOTAL", width=80, minwidth=50, anchor=CENTER)

    sctable.heading("sno", text="S.", anchor=CENTER)
    sctable.heading("username", text="USERNAME", anchor=CENTER)
    sctable.heading("G_K", text="G.KNOW", anchor=CENTER)
    sctable.heading("LOGICAL", text="LOGICAL", anchor=CENTER)
    sctable.heading("ISLAMIC", text="ISLAMIC", anchor=CENTER)
    sctable.heading("TOTAL", text="TOTAL", anchor=CENTER)
    con = pypyodbc.connect(
        r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};"
        r"DBQ=D:/NED 1st semester/PL/project/PL PROJECT (1).accdb;"
    )
    cur1 = con.cursor()
    cur1.execute("SELECT * FROM Score ORDER by sno")
    data = cur1.fetchall()
    for i in data:
        sctable.insert("", END, values=i)
    con.close()

    hmbtn = Button(nw, text="HOME", font=("Courier", 20), command=back10)
    hmbtn.place(x=600, y=530, anchor=E)
    nw.mainloop()


def dbisl():
    global isl
    global ID
    roott.destroy()

    isl = Tk()
    isl.geometry("920x600+180+20")
    isl.resizable(False, False)
    isl.title("I S L A M I C ")

    ibg = Image.open("D:/NED 1st semester/PL/project/images/db2.png")
    # antialias removes the structural padding from the image
    ir = ibg.resize((920, 600), Image.ANTIALIAS)
    newir = ImageTk.PhotoImage(ir)

    li = Label(isl, image=newir)
    li.place(x=0, y=0, relwidth=1, relheight=1)

    con = pypyodbc.connect(
        r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};"
        r"DBQ=D:/NED 1st semester/PL/project/PL PROJECT (1).accdb;"
    )
    cur1 = con.cursor()
    cur1.execute("SELECT * FROM [ISLAMIC] ORDER By ID")
    data = cur1.fetchall()
    ID = [1, 2, 3, 4]
    Q = [1, 2, 3, 4]
    QUESTION = []
    OptA = []
    OptB = []
    OptC = []
    OptD = []
    ANSWER = []
    for i in range(0, 5):
        QUESTION.append(data[i][1])
        OptA.append(data[i][2])
        OptB.append(data[i][3])
        OptC.append(data[i][4])
        OptD.append(data[i][5])
        ANSWER.append(data[i][6])

    correct = set()

    def presss():
        global score, scoredisplay
        if radiovar.get() in ANSWER:
            correct.add(radiovar.get())
        score = len(correct)
        if score > 3:
            scoredisplay = (
                "CONGRATULATIONS!! \n \n YOUR SCORE IS " + str(score) + " / " + "5 "
            )
        else:
            scoredisplay = (
                "KEEP ON TRYING! \n \n YOUR SCORE IS " + str(score) + " / " + "5 "
            )

    def submit():
        messagebox.showinfo("END!", "You are going to submit.")
        qno.destroy()
        l2.destroy()
        opt1.destroy()
        opt2.destroy()
        opt3.destroy()
        opt4.destroy()
        bfinish.destroy()
        resultlab = Label(
            isl,
            text=scoredisplay,
            font=("courier", 40, "bold"),
            bg="#f9bfbc",
            fg="dark blue",
        )
        resultlab.place(x=120, y=200)
        hmbtn = Button(isl, text="HOME", font=("Courier", 20), command=back6)
        hmbtn.place(x=600, y=530, anchor=E)

        con2 = pypyodbc.connect(
            r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};"
            r"DBQ=D:/NED 1st semester/PL/project/PL PROJECT (1).accdb;"
        )
        cur2 = con2.cursor()
        cur2.execute("SELECT * FROM [Score] ")
        data2 = cur2.fetchall()
        for i in data2:
            if username1 in i:
                nscore = i[4] + score

        cur2.execute(
            f"UPDATE Score SET [ISLAMIC] ='{nscore}' WHERE username = '{username1}'"
        )
        con2.commit()
        con2.close()

    def nextq():
        global ID, n, q
        q = choice(Q)
        n = ID[0]
        qno.destroy()
        l2.destroy()
        opt1.destroy()
        opt2.destroy()
        opt3.destroy()
        opt4.destroy()
        bnext.destroy()
        ID.remove(n)
        Q.remove(q)
        screen(n, q)

    def screen(t, x):
        global l2, bck, opt1, opt2, opt3, opt4, radiovar, bnext, bfinish, qno
        qno = Label(isl, bg="#f9bfbc", text=(str(t + 1), "#"), font=("Courier", 22))
        qno.place(x=80, y=25)
        l2 = Label(
            isl,
            bg="#f9bfbc",
            fg="black",
            text=QUESTION[x],
            font=("Courier", 18),
            wraplength=800,
        )
        l2.place(x=80, y=80)
        radiovar = StringVar()
        radiovar.set(-1)
        opt1 = Radiobutton(
            isl,
            bg="#f9bfbc",
            text=OptA[x],
            font=("Courier", 17),
            variable=radiovar,
            value=OptA[x],
            command=presss,
        )
        opt1.place(x=80, y=90, rely=0.12)
        opt2 = Radiobutton(
            isl,
            bg="#f9bfbc",
            text=OptB[x],
            font=("Courier", 17),
            variable=radiovar,
            value=OptB[x],
            command=presss,
        )
        opt2.place(x=80, y=105, rely=0.2)
        opt3 = Radiobutton(
            isl,
            bg="#f9bfbc",
            text=OptC[x],
            font=("Courier", 17),
            variable=radiovar,
            value=OptC[x],
            command=presss,
        )
        opt3.place(x=80, y=120, rely=0.3)
        opt4 = Radiobutton(
            isl,
            bg="#f9bfbc",
            text=OptD[x],
            font=("Courier", 17),
            variable=radiovar,
            value=OptD[x],
            command=presss,
        )
        opt4.place(x=80, y=135, rely=0.4)
        if len(ID) == 0:
            bfinish = Button(
                isl,
                text="FINISH",
                font=("Courier", 20),
                bg="blue",
                fg="white",
                command=submit,
            )
            bfinish.place(x=600, y=530, anchor=E)
        else:
            bnext = Button(
                isl, text="NEXT", font=("Courier", 20), bg="light blue", command=nextq
            )
            bnext.place(x=600, y=530, anchor=E)

    screen(0, 0)
    con.close()
    isl.mainloop()


def dbGK():
    global gk
    global ID
    roott.destroy()
    gk = Tk()
    gk.geometry("920x600+180+20")
    gk.resizable(False, False)
    gk.title("G E N E R A L - K N O W L E D G E")

    gkbg = Image.open("D:/NED 1st semester/PL/project/images/db4.png")
    # antialias removes the structural padding from the image
    gkr = gkbg.resize((920, 600), Image.ANTIALIAS)
    gknew = ImageTk.PhotoImage(gkr)

    ll = Label(gk, image=gknew)
    ll.place(x=0, y=0, relwidth=1, relheight=1)

    con = pypyodbc.connect(
        r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};"
        r"DBQ=D:/NED 1st semester/PL/project/PL PROJECT (1).accdb;"
    )
    cur1 = con.cursor()
    cur1.execute("SELECT * FROM [G_K] ORDER By ID")
    data = cur1.fetchall()
    ID = [1, 2, 3, 4]
    Q = [1, 2, 3, 4]
    QUESTION = []
    OptA = []
    OptB = []
    OptC = []
    OptD = []
    ANSWER = []
    for i in range(0, 5):
        QUESTION.append(data[i][1])
        OptA.append(data[i][2])
        OptB.append(data[i][3])
        OptC.append(data[i][4])
        OptD.append(data[i][5])
        ANSWER.append(data[i][6])

    correct = set()

    def presss():
        global score, scoredisplay
        if radiovar.get() in ANSWER:
            correct.add(radiovar.get())
        score = len(correct)
        if score > 3:
            scoredisplay = (
                "CONGRATULATIONS!! \n \n YOUR SCORE IS " + str(score) + " / " + "5 "
            )
        else:
            scoredisplay = (
                "KEEP ON TRYING! \n \n YOUR SCORE IS " + str(score) + " / " + "5 "
            )

    def submit():
        messagebox.showinfo("END!", "You are going to submit.")
        qno.destroy()
        l2.destroy()
        opt1.destroy()
        opt2.destroy()
        opt3.destroy()
        opt4.destroy()
        bfinish.destroy()
        resultlab = Label(
            gk,
            text=scoredisplay,
            font=("courier", 40, "bold"),
            bg="#d5d5e1",
            fg="dark blue",
        )
        resultlab.place(x=120, y=200)
        hmbtn = Button(gk, text="HOME", font=("Courier", 20), command=back7)
        hmbtn.place(x=600, y=530, anchor=E)

        con2 = pypyodbc.connect(
            r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};"
            r"DBQ=D:/NED 1st semester/PL/project/PL PROJECT (1).accdb;"
        )
        cur2 = con2.cursor()
        cur2.execute("SELECT * FROM [Score] ")
        data2 = cur2.fetchall()
        for i in data2:
            if username1 in i:
                nscore = i[2] + score
        cur2.execute(
            f"UPDATE Score SET [G_K] ='{nscore}' WHERE username = '{username1}'"
        )
        con2.commit()
        con2.close()

    def nextq():
        global ID, n, q
        q = choice(Q)
        n = ID[0]
        qno.destroy()
        l2.destroy()
        opt1.destroy()
        opt2.destroy()
        opt3.destroy()
        opt4.destroy()
        bnext.destroy()
        ID.remove(n)
        Q.remove(q)
        screen(n, q)

    def screen(t, x):
        global l2, bck, opt1, opt2, opt3, opt4, radiovar, bnext, bfinish, qno
        qno = Label(gk, text=(str(t + 1), "#"), font=("Courier", 22), bg="#d5d5e1")
        qno.place(x=80, y=25)
        l2 = Label(
            gk,
            bg="#d5d5e1",
            fg="black",
            text=QUESTION[x],
            font=("Courier", 18),
            wraplength=800,
        )
        l2.place(x=80, y=80)
        radiovar = StringVar()
        radiovar.set(-1)
        opt1 = Radiobutton(
            gk,
            text=OptA[x],
            bg="#d5d5e1",
            font=("Courier", 17),
            variable=radiovar,
            value=OptA[x],
            command=presss,
        )
        opt1.place(x=80, y=90, rely=0.12)
        opt2 = Radiobutton(
            gk,
            text=OptB[x],
            bg="#d5d5e1",
            font=("Courier", 17),
            variable=radiovar,
            value=OptB[x],
            command=presss,
        )
        opt2.place(x=80, y=105, rely=0.2)
        opt3 = Radiobutton(
            gk,
            text=OptC[x],
            bg="#d5d5e1",
            font=("Courier", 17),
            variable=radiovar,
            value=OptC[x],
            command=presss,
        )
        opt3.place(x=80, y=120, rely=0.3)
        opt4 = Radiobutton(
            gk,
            text=OptD[x],
            bg="#d5d5e1",
            font=("Courier", 17),
            variable=radiovar,
            value=OptD[x],
            command=presss,
        )
        opt4.place(x=80, y=135, rely=0.4)
        if len(ID) == 0:
            bfinish = Button(
                gk,
                text="FINISH",
                font=("Courier", 20),
                bg="#d5d5e1",
                fg="white",
                command=submit,
            )
            bfinish.place(x=600, y=530, anchor=E)
        else:
            bnext = Button(
                gk, text="NEXT", font=("Courier", 20), bg="#d5d5e1", command=nextq
            )
            bnext.place(x=600, y=530, anchor=E)

    screen(0, 0)
    con.close()
    gk.mainloop()


def dblogic():
    global lg
    global ID
    roott.destroy()
    lg = Tk()
    lg.geometry("920x600+180+20")
    lg.resizable(False, False)
    lg.title("L O G I C A L")

    lbg = Image.open("D:/NED 1st semester/PL/project/images/db3.png")
    # antialias removes the structural padding from the image
    lr = lbg.resize((920, 600), Image.ANTIALIAS)
    lnew = ImageTk.PhotoImage(lr)

    ll = Label(lg, image=lnew)
    ll.place(x=0, y=0, relwidth=1, relheight=1)
    con = pypyodbc.connect(
        r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};"
        r"DBQ=D:/NED 1st semester/PL/project/PL PROJECT (1).accdb;"
    )
    cur1 = con.cursor()
    cur1.execute("SELECT * FROM [LOGICAL] ORDER By ID")
    data = cur1.fetchall()
    ID = [1, 2, 3, 4]
    Q = [1, 2, 3, 4]
    QUESTION = []
    OptA = []
    OptB = []
    OptC = []
    OptD = []
    ANSWER = []
    for i in range(0, 5):
        QUESTION.append(data[i][1])
        OptA.append(data[i][2])
        OptB.append(data[i][3])
        OptC.append(data[i][4])
        OptD.append(data[i][5])
        ANSWER.append(data[i][6])

    correct = set()

    def presss():
        global score, scoredisplay
        if radiovar.get() in ANSWER:
            correct.add(radiovar.get())
        score = len(correct)
        if score > 3:
            scoredisplay = (
                "CONGRATULATIONS!! \n \n YOUR SCORE IS " + str(score) + " / " + "5 "
            )
        else:
            scoredisplay = (
                "KEEP ON TRYING! \n \n YOUR SCORE IS " + str(score) + " / " + "5 "
            )

    def submit():
        messagebox.showinfo("END!", "You are going to submit.")
        qno.destroy()
        l2.destroy()
        opt1.destroy()
        opt2.destroy()
        opt3.destroy()
        opt4.destroy()
        bfinish.destroy()
        resultlab = Label(
            lg,
            text=scoredisplay,
            font=("courier", 40, "bold"),
            bg="#f7e8c1",
            fg="dark blue",
        )
        resultlab.place(x=120, y=200)
        hmbtn = Button(lg, text="HOME", font=("Courier", 20), command=back8)
        hmbtn.place(x=600, y=530, anchor=E)

        con2 = pypyodbc.connect(
            r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};"
            r"DBQ=D:/NED 1st semester/PL/project/PL PROJECT (1).accdb;"
        )
        cur2 = con2.cursor()
        cur2.execute("SELECT * FROM [Score] ")
        data2 = cur2.fetchall()
        for i in data2:
            if username1 in i:
                nscore = i[3] + score
        cur2.execute(
            f"UPDATE Score SET [LOGICAL] ='{nscore}' WHERE username = '{username1}'"
        )
        con2.commit()
        con2.close()

    def nextq():
        global ID, n, q
        q = choice(Q)
        n = ID[0]
        qno.destroy()
        l2.destroy()
        opt1.destroy()
        opt2.destroy()
        opt3.destroy()
        opt4.destroy()
        bnext.destroy()
        ID.remove(n)
        Q.remove(q)
        screen(n, q)

    def screen(t, x):
        global l2, bck, opt1, opt2, opt3, opt4, radiovar, bnext, bfinish, qno
        qno = Label(lg, text=(str(t + 1), "#"), font=("Courier", 22), bg="#f7e8c1")
        qno.place(x=80, y=25)
        l2 = Label(
            lg,
            bg="#f7e8c1",
            fg="black",
            text=QUESTION[x],
            font=("Courier", 18),
            wraplength=800,
        )
        l2.place(x=80, y=80)
        radiovar = StringVar()
        radiovar.set(-1)
        opt1 = Radiobutton(
            lg,
            text=OptA[x],
            font=("Courier", 17),
            bg="#f7e8c1",
            variable=radiovar,
            value=OptA[x],
            command=presss,
        )
        opt1.place(x=80, y=90, rely=0.12)
        opt2 = Radiobutton(
            lg,
            text=OptB[x],
            font=("Courier", 17),
            bg="#f7e8c1",
            variable=radiovar,
            value=OptB[x],
            command=presss,
        )
        opt2.place(x=80, y=105, rely=0.2)
        opt3 = Radiobutton(
            lg,
            text=OptC[x],
            font=("Courier", 17),
            bg="#f7e8c1",
            variable=radiovar,
            value=OptC[x],
            command=presss,
        )
        opt3.place(x=80, y=120, rely=0.3)
        opt4 = Radiobutton(
            lg,
            text=OptD[x],
            font=("Courier", 17),
            bg="#f7e8c1",
            variable=radiovar,
            value=OptD[x],
            command=presss,
        )
        opt4.place(x=80, y=135, rely=0.4)
        if len(ID) == 0:
            bfinish = Button(
                lg,
                text="FINISH",
                font=("Courier", 20),
                bg="#f7e8c1",
                fg="white",
                command=submit,
            )
            bfinish.place(x=600, y=530, anchor=E)
        else:
            bnext = Button(
                lg, text="NEXT", font=("Courier", 20), bg="#f7e8c1", command=nextq
            )
            bnext.place(x=600, y=530, anchor=E)

    screen(0, 0)
    con.close()
    lg.mainloop()


##
def magicgame():
    global magic
    roott.destroy()
    magic = Tk()
    magic.geometry("920x600+180+20")
    magic.config(bg="#ff94cf")
    magic.title("M A G I C B O X")
    magic.resizable(False, False)

    mg = Image.open("D:/NED 1st semester/PL/project/images/magicbox.png")
    sizemg = mg.resize((920, 600), Image.ANTIALIAS)
    newmg = ImageTk.PhotoImage(sizemg)
    lmg = Label(magic, image=newmg)
    lmg.place(x=0, y=0, relheight=1, relwidth=1)
    heading_lable = Label(
        magic,
        bg="#afcf95",
        text="MAGIC BOX",
        font=("courier bold", 20),
        fg="black",
        width=10,
        height=2,
    ).place(x=350, y=0)

    e1 = Entry(magic, font=("Times new roman", 40), width=3)
    e1.config(background="#bbc0cd", foreground="blue")
    e1.place(x=200, y=120)
    e2 = Entry(magic, font=("Times new roman", 40), width=3)
    e2.config(background="#bbc0cd", foreground="blue")
    e2.place(x=290, y=120)
    e3 = Entry(magic, font=("Times new roman", 40), width=3)
    e3.config(background="#bbc0cd", foreground="blue")
    e3.place(x=380, y=120)
    e4 = Entry(magic, font=("Times new roman", 40), width=3)
    e4.config(background="#bbc0cd", foreground="blue")
    e4.place(x=200, y=200)
    e5 = Entry(magic, font=("Times new roman", 40), width=3)
    e5.config(background="#bbc0cd", foreground="blue")
    e5.place(x=290, y=200)
    e6 = Entry(magic, font=("Times new roman", 40), width=3)
    e6.config(background="#bbc0cd", foreground="blue")
    e6.place(x=380, y=200)
    e7 = Entry(magic, font=("Times new roman", 40), width=3)
    e7.config(background="#bbc0cd", foreground="blue")
    e7.place(x=200, y=280)
    e8 = Entry(magic, font=("Times new roman", 40), width=3)
    e8.config(background="#bbc0cd", foreground="blue")
    e8.place(x=290, y=280)
    e9 = Entry(magic, font=("Times new roman", 40), width=3)
    e9.config(background="#bbc0cd", foreground="blue")
    e9.place(x=380, y=280)

    instrctions = Label(
        magic,
        text="INSTRUCTIONS:\nEnter a number in each\nbox,the sum of all\nthe numbers in a\nrow must be equal,\nsimultaneously the sum\nof all the numbers\nin a column must\nbe equal, and the\nsum of diagonal numbers\nshould also be equal.",
    )
    instrctions.config(font=("courier", 17), bg="#c1daae", fg="blue")

    instrctions.place(x=500, y=120)

    def show():
        a = int(e3.get()) + int(e5.get()) + int(e7.get())
        b = int(e1.get()) + int(e4.get()) + int(e7.get())
        c = int(e2.get()) + int(e5.get()) + int(e8.get())
        d = int(e3.get()) + int(e6.get()) + int(e9.get())
        e = int(e4.get()) + int(e5.get()) + int(e6.get())
        f = int(e7.get()) + int(e8.get()) + int(e9.get())
        g = int(e1.get()) + int(e5.get()) + int(e9.get())
        h = int(e1.get()) + int(e2.get()) + int(e3.get())
        if a == b and b == c and c == d and d == e and e == f and f == g and g == h:
            results = "WELL DONE\n You're a GENIUS!"
        else:
            results = "KEEP TRYING!\nC'mon you can do it!"

        l1 = Label(
            magic,
            bg="#afcf95",
            text=h,
            fg="black",
            width=3,
            font=("Times new roman", 22),
        ).place(x=490, y=125)
        l2 = Label(
            magic, bg="#afcf95", text=e, width=3, font=("Times new roman", 22)
        ).place(x=490, y=205)
        l3 = Label(
            magic, bg="#afcf95", text=f, width=3, font=("Times new roman", 22)
        ).place(x=490, y=285)
        l4 = Label(
            magic, bg="#afcf95", text=g, width=4, font=("Times new roman", 22)
        ).place(x=490, y=360)
        l5 = Label(
            magic, bg="#afcf95", text=b, width=3, font=("Times new roman", 22)
        ).place(x=200, y=360)
        l6 = Label(
            magic, bg="#afcf95", text=c, width=3, font=("Times new roman", 22)
        ).place(x=290, y=360)
        l7 = Label(
            magic, bg="#afcf95", text=d, width=3, font=("Times new roman", 22)
        ).place(x=380, y=360)
        l8 = Label(
            magic, bg="#afcf95", text=a, width=4, font=("Times new roman", 22)
        ).place(x=100, y=360)
        scorez = Label(
            magic,
            text=results,
            bg="#afcf95",
            width=20,
            height=2,
            fg="black",
            font=("courier", 20),
        ).place(x=280, y=500)

    button = Button(
        magic,
        text="Show!",
        width=10,
        font=("courier bold", 20),
        height=1,
        bg="#afcf95",
        command=show,
    ).place(x=350, y=420)
    h_btn = Button(magic, text="HOME", width=10, height=1, bg="#afcf95", command=back9)
    h_btn.config(font=("courier", 15), fg="black")
    h_btn.place(x=100, y=550)
    magic.mainloop()


loading()
