import tkinter as tk
from tkinter import messagebox
import subprocess

root = tk.Tk()
root.title("LariAMP")
root.geometry("800x600")

# Frame principal
main_frame = tk.Frame(root, bg="#f2f2f2")
main_frame.pack(padx=2, pady=2, fill=tk.BOTH, expand=True)
main_frame.pack_propagate(False) 

# Frame pentru terminale
terminal_frame1 = tk.Frame(main_frame, bg="#f2f2f2")
terminal_frame1.grid(row=0, column=0, padx=2, pady=2, sticky="nsew")

terminal_frame1.columnconfigure(0, weight=2)
terminal_frame1.rowconfigure(0, weight=2)

terminal_frame1.update()

terminal1 = tk.Text(terminal_frame1, wrap=tk.WORD, bg="#6E99A7")
terminal1.pack(fill=tk.BOTH, expand=True)

# Aici adaugam al doilea terminal
terminal_frame2 = tk.Frame(main_frame, bg="#f2f2f2")
terminal_frame2.grid(row=1, column=0, padx=2, pady=2, sticky="nsew") 

terminal_frame2.columnconfigure(0, weight=2)
terminal_frame2.rowconfigure(0, weight=2)

terminal_frame2.update()

terminal2 = tk.Text(terminal_frame2, wrap=tk.WORD, bg="#6E99A7")
terminal2.pack(fill=tk.BOTH, expand=True)

# Apoi definim functiile
def open_terminal(command, frame):
    command = f'xterm -into {frame.winfo_id()} -hold -geometry 800x600 -e "{command}"' 
    subprocess.Popen(command, shell=True)

def highlight_button(button):
    for btn in buttons:
        btn.config(relief=tk.RAISED, bg="#6c757d", fg="#ffffff")
    button.config(relief=tk.SUNKEN, bg="#d9e4f4", fg="#000000")

# Toate functiile ruleaza scripturi
def apachelogs():
    command = f'sh startresapache.sh'
    open_terminal(command, terminal_frame1)  
    highlight_button(button1)

def apachehtop():
    command = f'sh logsAp.sh'
    open_terminal(command, terminal_frame1)  
    highlight_button(button2)

def createApache():
    command = f'sh htops.sh'
    open_terminal(command, terminal_frame1)  
    highlight_button(button3)

def run_script4():
    command = f'minikube service apache'
    open_terminal(command, terminal_frame1)  
    highlight_button(button4)

def run_script5():
    command = f'sh  logsSQL.sh'
    open_terminal(command, terminal_frame2)  
    highlight_button(button5)

def run_script6():
    command = f'sh htopsql.sh'
    open_terminal(command, terminal_frame2)  
    highlight_button(button6)

def run_script7():
    command = f'sh startressql.sh'
    open_terminal(command, terminal_frame2)  
    highlight_button(button7)

def run_script8():
    command = f'kubectl exec -it mysql -- mysql -u root -p testpass'
    open_terminal(command, terminal_frame2)  
    highlight_button(button8)

# Frame pentru bara de butoane
button_frame = tk.Frame(main_frame, bg="#305966")
button_frame.pack(side=tk.RIGHT, )

# Adaugarea butoanelor in bara de butoane
button1 = tk.Button(button_frame, text="Start/Restart Apache", command=apachelogs,bg='#599CB1')
button1.pack(side=tk.TOP)

button2 = tk.Button(button_frame, text="Logs Apache", command=apachehtop,bg='#599CB1')
button2.pack(side=tk.TOP)

button3 = tk.Button(button_frame, text="Resources Apache", command=createApache,bg='#599CB1')
button3.pack(side=tk.TOP)

button4 = tk.Button(button_frame, text="Preview Site", command=run_script4,bg='#599CB1')
button4.pack(side=tk.TOP)

button5 = tk.Button(button_frame, text="Logs Mysql", command=run_script5,bg='#599CB1')
button5.pack(side=tk.TOP)

button6 = tk.Button(button_frame, text="Resources Mysql", command=run_script6,bg='#599CB1')
button6.pack(side=tk.TOP)

button7 = tk.Button(button_frame, text="Start/Restart Mysql", command=run_script7,bg='#599CB1')
button7.pack(side=tk.TOP)

#button8 = tk.Button(button_frame, text="Open SQL", command=run_script8,bg='#599CB1')
#button8.pack(side=tk.TOP)

buttons = [button1, button2, button3, button5, button6, button7] #button8] button4, #  add noile butoane in lista,  

# Adaugam cateva linii pentru a se asigura ca ambele frame-uri de terminal primesc spatiu egal in  grid
main_frame.rowconfigure(0, weight=1)
main_frame.rowconfigure(1, weight=1)
main_frame.columnconfigure(0, weight=1)

root.mainloop()
