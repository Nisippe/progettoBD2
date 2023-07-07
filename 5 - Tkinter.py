import tkinter as tk
from tkinter import messagebox
from pymongo import MongoClient
# Connessione al server MongoDB
client = MongoClient('mongodb://localhost:27017')

# Seleziona il database
db = client['progettoBD2']

# Seleziona la collezione
collection = db['progettoBD2']

def clickInsert():
    document = {"title": entry_titolo.get(),
                "description": text.get("1.0", tk.END),
                "appears on": entry_appears_on.get(),
                "artist": entry_artist.get(),
                "writers": entry_writer.get(),
                "producer": entry_producer.get(),
                "released": entry_released.get(),
                "streak": entry_streak.get(),
                "position": entry_position.get()}
    collection.insert_one(document)
    pulizia()
    messagebox.showinfo("Inserito","Inserimento effettuato!")




# Crea una finestra principale
window = tk.Tk()

# Imposta le dimensioni della finestra principale
window.geometry("1280x720")
window.configure(bg="green")

# Crea un bottone
buttonInsert = tk.Button(window, text="Insert", command=clickInsert,width=5,height=2)
buttonDelete = tk.Button(window, text="Delete", command=clickInsert,width=5,height=2)
buttonFind = tk.Button(window, text="Find", command=clickInsert,width=5,height=2)
buttonUpdate = tk.Button(window, text="Update", command=clickInsert,width=5,height=2)
# Posiziona il bottone nella finestra
buttonInsert.place(x=10,y=10)
buttonDelete.place(x=60,y=10)
buttonFind.place(x=110,y=10)
buttonUpdate.place(x=160,y=10)

def focus_out_entry_box(widget, widget_text):
    if widget['fg'] == 'Black' and len(widget.get()) == 0:
        widget.delete(0, tk.END)
        widget['fg'] = 'Grey'
        widget.insert(0, widget_text)


def focus_in_entry_box(widget):
    if widget['fg'] == 'Grey':
        widget['fg'] = 'Black'
        widget.delete(0, tk.END)


def on_text_click(event):
    if text.get("1.0", "end-1c") == "Descrizione":
        text.delete("1.0", tk.END)
        text.config(fg='black')


def on_focusout(event):
    if text.get("1.0", "end-1c") == "":
        text.insert("1.0", "Descrizione")
        text.config(fg='gray')

def pulizia():
    entry_titolo.delete(0,tk.END)
    text.delete("1.0",tk.END)
    entry_appears_on.delete(0,tk.END)
    entry_artist.delete(0, tk.END)
    entry_writer.delete(0, tk.END)
    entry_producer.delete(0, tk.END)
    entry_released.delete(0, tk.END)
    entry_streak.delete(0, tk.END)
    entry_position.delete(0, tk.END)

entry_titolo = tk.Entry(font='Arial 18', fg='Grey',width=20)
entry_titolo.insert(0, "Titolo")
entry_titolo.bind("<FocusIn>", lambda args: focus_in_entry_box(entry_titolo))
entry_titolo.bind("<FocusOut>", lambda args: focus_out_entry_box(entry_titolo, "Titolo"))

text = tk.Text(font='Arial 18', fg='Grey',height=5,width=20)
text.insert("1.0","Descrizione")
text.bind("<FocusIn>", lambda args: on_text_click(text))
text.bind("<FocusOut>", lambda args: on_focusout(text))

entry_appears_on = tk.Entry(font='Arial 18', fg='Grey',width=20)
entry_appears_on.insert(0, "Appare in")
entry_appears_on.bind("<FocusIn>", lambda args: focus_in_entry_box(entry_appears_on))
entry_appears_on.bind("<FocusOut>", lambda args: focus_out_entry_box(entry_appears_on, "Appare in"))

entry_artist = tk.Entry(font='Arial 18', fg='Grey',width=20)
entry_artist.insert(0, "Artista")
entry_artist.bind("<FocusIn>", lambda args: focus_in_entry_box(entry_artist))
entry_artist.bind("<FocusOut>", lambda args: focus_out_entry_box(entry_artist, "Artista"))

entry_writer = tk.Entry(font='Arial 18', fg='Grey',width=20)
entry_writer.insert(0, "Scrittore")
entry_writer.bind("<FocusIn>", lambda args: focus_in_entry_box(entry_writer))
entry_writer.bind("<FocusOut>", lambda args: focus_out_entry_box(entry_writer, "Scrittore"))

entry_producer = tk.Entry(font='Arial 18', fg='Grey',width=20)
entry_producer.insert(0, "Produttore")
entry_producer.bind("<FocusIn>", lambda args: focus_in_entry_box(entry_producer))
entry_producer.bind("<FocusOut>", lambda args: focus_out_entry_box(entry_producer, "Produttore"))

entry_released = tk.Entry(font='Arial 18', fg='Grey',width=20)
entry_released.insert(0, "Rilasciato")
entry_released.bind("<FocusIn>", lambda args: focus_in_entry_box(entry_released))
entry_released.bind("<FocusOut>", lambda args: focus_out_entry_box(entry_released, "Rilasciato"))

entry_streak = tk.Entry(font='Arial 18', fg='Grey',width=20)
entry_streak.insert(0, "Streak")
entry_streak.bind("<FocusIn>", lambda args: focus_in_entry_box(entry_streak))
entry_streak.bind("<FocusOut>", lambda args: focus_out_entry_box(entry_streak, "Streak"))

entry_position = tk.Entry(font='Arial 18', fg='Grey',width=20)
entry_position.insert(0, "Posizione")
entry_position.bind("<FocusIn>", lambda args: focus_in_entry_box(entry_position))
entry_position.bind("<FocusOut>", lambda args: focus_out_entry_box(entry_position, "Posizione"))


entry_titolo.place(x=10,y=70)
text.place(x=300,y=70)
entry_appears_on.place(x=10,y=110)
entry_artist.place(x=10,y=150)
entry_writer.place(x=10,y=190)
entry_producer.place(x=10,y=230)
entry_released.place(x=10,y=270)
entry_streak.place(x=10,y=310)
entry_position.place(x=10,y=350)

# Esegui il ciclo principale degli eventi
window.mainloop()

