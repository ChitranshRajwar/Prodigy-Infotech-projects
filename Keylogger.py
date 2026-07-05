import tkinter as tk
from datetime import datetime

LOG_FILE = "key_log.txt"

def log_key(event):
    key = event.keysym
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_file.write(f"[{timestamp}] {key}\n")
    log_file.flush()
    status.config(text=f"Last Key Pressed: {key}")

def clear_log():
    log_file.seek(0)
    log_file.truncate()
    status.config(text="Log cleared.")

def on_close():
    log_file.close()
    root.destroy()

# Open the log file once, keep it open for the app's lifetime
log_file = open(LOG_FILE, "a")

root = tk.Tk()
root.title("Keyboard Event Logger")
root.geometry("400x220")

label = tk.Label(
    root,
    text="Click inside this window and press keys.",
    font=("Arial", 12)
)
label.pack(pady=20)

status = tk.Label(root, text="Waiting for input...", font=("Arial", 11))
status.pack()

clear_btn = tk.Button(root, text="Clear Log", command=clear_log)
clear_btn.pack(pady=10)

root.bind("<Key>", log_key)
root.protocol("WM_DELETE_WINDOW", on_close)
root.mainloop()
