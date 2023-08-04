import tkinter as tk

body = tk.Tk()
body.title("LOVEMETER")
body.geometry("300x150")
body.configure(bg="black")

def remove_widgets():
    for widget in body.winfo_children():
        widget.destroy()
def page1():
    remove_widgets()
#    tk.Label(text=" Welcome ", bg="white").place(relx=.5,rely=.4,anchor="s",relheight=.3,relwidth=.4)
    tk.Label(text=" Welcome\n\nLoveMeter ", bg="white").place(relx=.5, rely=.5, anchor="s", relheight=.4, relwidth=.4)
    tk.Label(text=" ♡ ", bg="white", fg="red").place(relx=.5, rely=.3, anchor="center", relheight=.1, relwidth=.4)
    tk.Button(body,text="Start", bg="white",command=page2).place(relx=.5,rely=.7,anchor="center",relheight=.2,relwidth=.8)


def page2():
    remove_widgets()
    tk.Button(body,text="Meter", bg="white", command=page1).place(relx=.5,rely=.7,anchor="center",relheight=.2,relwidth=.2)



page1()
body.mainloop()