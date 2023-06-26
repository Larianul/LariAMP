import tkinter as tk
import subprocess

def open_terminal(command, frame):
    command = f'xterm -into {frame.winfo_id()} -hold -e "{command}"'
    subprocess.Popen(command, shell=True)

root = tk.Tk()
root.title("Aplicație cu terminale")
root.configure(bg="#a6bddb")

# Funcția pentru rularea în timp real a comenzii kubectl logs
def run_kubectl_logs():
    pod_name = "mysql"  # înlocuiește cu numele corect al pod-ului
    command = f'kubectl logs -f  {pod_name}'
    open_terminal(command, terminal1_frame)

# Funcția pentru instalarea și rularea automată a pachetului htop
def install_and_run_htop():
    command = 'apt-get update && apt-get install -y htop && htop '
    open_terminal(command, terminal2_frame)

# Frame-urile pentru terminale
terminal1_frame = tk.Frame(root, width=800, height=600, bg="#a6bddb")
terminal1_frame.pack(side=tk.LEFT)

terminal2_frame = tk.Frame(root, width=800, height=600, bg="#a6bddb")
terminal2_frame.pack(side=tk.LEFT)

# Butonul pentru rularea în timp real a comenzii kubectl logs
button1 = tk.Button(root, text="Run kubectl logs", command=run_kubectl_logs, bg="#d9e4f4", fg="#000000")
button1.pack(pady=10)

# Butonul pentru instalarea și rularea automată a pachetului htop
button2 = tk.Button(root, text="Install and run htop", command=install_and_run_htop, bg="#d9e4f4", fg="#000000")
button2.pack(pady=10)

root.mainloop()
