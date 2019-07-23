
import tkinter.ttk


main = tkinter.Tk()
main.geometry('800x600+550+200')
def quit_program():
    main.destroy()



frame = tkinter.Frame(main)
frame2 = tkinter.Frame(main)

def create_main_menu():
    l = tkinter.Label(frame, fg = 'red', width=20, text='MindLuck',font=("Helvetica",36),height= 4).pack()
    play_button = tkinter.Button(frame,text='Start',font=("Helvetica",20),bd=5,width=10).pack()
    conf_button = tkinter.Button(frame,text='Configs',font=("Helvetica",20),bd=5,width=10).pack()
    authors_button = tkinter.Button(frame,text='Authors',font=("Helvetica",20),bd=5,width=10).pack()
    rules_button = tkinter.Button(frame,text='Rules',font=("Helvetica",20),bd=5,width=10).pack()
    quit_button = tkinter.Button(frame, text='Quit', font=("Helvetica", 20), bd=5, width=10,command=quit_program).pack()


def create_rules_menu():
    rules = tkinter.Button(frame2, fg='red', width=20, text='Rules', font=("Helvetica", 36), height=4).pack()

create_main_menu()
create_rules_menu()





main.mainloop()


