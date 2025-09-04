import socket
import threading
import tkinter as tk
from tkinter import simpledialog, scrolledtext, messagebox

# Client setup
HOST = "titokhehehehehehe"  # same as server
PORT = 0      # same as server

nickname = None
client = socket.socket(socket.AF_INET6, socket.SOCK_STREAM) #ipv6 if u want v4 use AF_INET

def receive():
    while True:
        try:
            message = client.recv(1234).decode("utf-8")
            if message == "NICK":
                client.send(nickname.encode("utf-8"))
            else:
                chat_area.config(state=tk.NORMAL)
                chat_area.insert(tk.END, message + "\n")
                chat_area.config(state=tk.DISABLED)
                chat_area.yview(tk.END)
        except:
            messagebox.showerror("Error", "Disconnected from server")
            client.close()
            break

def send_message():
    match msg_entry.get():
        case "":
            return
        case "/quit":
            client.close()
            root.destroy()
            return

    message = f"{nickname}: {msg_entry.get()}"
    chat_area.config(state=tk.NORMAL)
    chat_area.insert(tk.END, f"you: {msg_entry.get()}\n")
    chat_area.config(state=tk.DISABLED)
    chat_area.yview(tk.END)
    client.send(message.encode("utf-8"))
    msg_entry.delete(0, tk.END)

"""
cat-es telóhoz:
    w40 h33 
    w30 
    yp30
samsung galaxy telóhoz:
    w80 h40 xp10 yp10
    w65 xp10 yp10
    xp10 xp10
"""

# Tkinter UI
root = tk.Tk()
root.title("Chat Client")

chat_area = scrolledtext.ScrolledText(root, state=tk.DISABLED, width=100, height=20)
chat_area.pack(padx=10, pady=10)

msg_entry = tk.Entry(root, width=90)
msg_entry.pack(side=tk.LEFT, padx=10, pady=10)

send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(side=tk.LEFT, padx=10, pady=10)

# Ask nickname before connecting
nickname = simpledialog.askstring("Nickname", "Choose a nickname:", parent=root)

# Connect to server
try:
    client.connect((HOST, PORT))
    thread = threading.Thread(target=receive)
    thread.start()
except:
    messagebox.showerror("Connection Error", "Unable to connect to server")
    root.destroy()

root.mainloop()
