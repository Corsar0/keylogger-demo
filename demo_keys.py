import tkinter as tk
from datetime import datetime

LOGFILE = "key_demo_log.txt"

def format_key(event):
    # Se è un carattere stampabile (lettere/numeri/simboli), usiamo event.char
    if event.char and event.char.isprintable():
        return event.char
    # Altrimenti è un tasto speciale tipo Enter/Shift/BackSpace
    return f"[{event.keysym}]"

def on_key(event):
    key = format_key(event)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"{timestamp} {key}\n"

    # Salviamo su file
    with open(LOGFILE, "a", encoding="utf-8") as f:
        f.write(line)

    # Mostriamo in finestra
    output.insert("end", line)
    output.see("end")

# Creiamo la finestra
root = tk.Tk()
root.title("Key Capture Demo - SOLO QUESTA FINESTRA")
root.geometry("800x400")

# Banner informativo (consenso/trasparenza)
info = tk.Label(
    root,
    text="DEMO EDUCATIVA\n"
         "Registra i tasti SOLO quando questa finestra è attiva.\n"
         "Premi ESC per uscire.",
    justify="left"
)
info.pack(anchor="w", padx=10, pady=10)

# Area di testo dove stampiamo il log live
output = tk.Text(root, wrap="word")
output.pack(expand=True, fill="both", padx=10, pady=10)

# Colleghiamo l'evento 'tasto premuto' alla funzione on_key
root.bind("<KeyPress>", on_key)

# ESC chiude l'app
root.bind("<Escape>", lambda e: root.destroy())

# Loop degli eventi della GUI (la finestra resta “viva” e ascolta)
root.mainloop()
