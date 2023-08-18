import tkinter as tk
from threading import Thread
from modules.main import main

class IRCClientGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Cliente IRC")
        self.root.geometry("800x600")

        self.text_box = tk.Text(root, state=tk.DISABLED)
        self.text_box.pack(fill=tk.BOTH, expand=True)

        self.input_field = tk.Entry(root)
        self.input_field.pack(fill=tk.BOTH)

        self.send_button = tk.Button(root, text="Enviar", command=self.send_message)
        self.send_button.pack(fill=tk.BOTH)

        self.thread = Thread(target=main)

    def send_message(self):
        message = self.input_field.get()
        self.text_box.config(state=tk.NORMAL)
        self.text_box.insert(tk.END, f"Você: {message}\n")
        self.text_box.config(state=tk.DISABLED)
        self.input_field.delete(0, tk.END)
        # Enviar a mensagem usando a lógica do cliente IRC aqui

    def start(self):
        self.thread.start()
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    gui = IRCClientGUI(root)
    gui.start()
