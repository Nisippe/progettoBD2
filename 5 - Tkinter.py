import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
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

def clickDelete():
    collection.delete_one(entry_titolo.get())
    pulizia()
    messagebox.showinfo("Cancellato","Cancellamento effettato!")

def clickUpdate():
    filter_query = {"title": entry_titolo.get()}
    descrizione=text.get("1.0",tk.END)
    if descrizione!='':
        update_query = {"$set": {"description": descrizione}}
        collection.update_one(filter_query,update_query)

    appare=entry_appears_on.get()
    if appare!='Appare in' and appare!='':
        update_query = {"$set": {"appears on": appare}}
        collection.update_one(filter_query,update_query)

    artista=entry_artist.get()
    if artista!='Artista' and artista!='':
        update_query = {"$set": {"artist": artista}}
        collection.update_one(filter_query,update_query)

    scrittore=entry_writer.get()
    if scrittore!='Scrittore' and scrittore!='':
        update_query = {"$set": {"writers": scrittore}}
        collection.update_one(filter_query,update_query)

    produttore=entry_producer.get()
    if produttore!='Produttore' and produttore!='':
        update_query = {"$set": {"producer": produttore}}
        collection.update_one(filter_query,update_query)

    rilasciato=entry_released.get()
    if rilasciato!='Rilasciato' and rilasciato!='':
        update_query = {"$set": {"released": rilasciato}}
        collection.update_one(filter_query,update_query)

    streak=entry_streak.get()
    if streak!='Streak' and streak!='':
        update_query = {"$set": {"streak": streak}}
        collection.update_one(filter_query,update_query)

    position=entry_position.get()
    if position!='Posizione' and position!='':
        update_query = {"$set": {"position": position}}
        collection.update_one(filter_query,update_query)

    messagebox.showinfo("Aggiornato", "Aggiornamento effettato!")



# Crea una finestra principale
window = tk.Tk()
listbox_risultati=ttk.Treeview(window,show="headings")
# Imposta le dimensioni della finestra principale
window.geometry("1620x720")
window.configure(bg="green")


def clickFind():
    listbox_risultati.delete(*listbox_risultati.get_children())
    collection.create_index([("title", "text")])
    documents = collection.find({"title": {"$regex": entry_titolo.get(), "$options": "i"}},{"_id": 0, "description": 0})

    for document in documents:
        item = (document["title"], document["appears on"], document["artist"], document["writers"], document["producer"], document["released"], document["streak"], document["position"])
        listbox_risultati.insert("",tk.END,values=item)

# Crea un bottone
buttonInsert = tk.Button(window, text="Insert", command=clickInsert,width=5,height=2)
buttonDelete = tk.Button(window, text="Delete", command=clickDelete,width=5,height=2)
buttonFind = tk.Button(window, text="Find", command=clickFind,width=5,height=2)
buttonUpdate = tk.Button(window, text="Update", command=clickUpdate,width=5,height=2)
# Posiziona il bottone nella finestra
buttonInsert.place(x=10,y=600)
buttonDelete.place(x=60,y=600)
buttonFind.place(x=110,y=600)
buttonUpdate.place(x=160,y=600)

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

def sort_by_column(column):
    # Ottieni l'elenco dei dati nella ListBox
    items = list(listbox_risultati.get(0, tk.END))

    # Ordina gli elementi in base alla colonna selezionata
    if column == "Nome":
        items.sort(key=lambda x: x.split(',')[0])  # Ordina per il primo nome
    elif column == "Cognome":
        items.sort(key=lambda x: x.split(',')[1])  # Ordina per il cognome
    elif column == "Età":
        items.sort(key=lambda x: int(x.split(',')[2]))  # Ordina per l'età

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


listbox_risultati["columns"] = ("title", "appears on", "artist", "writers", "producer", "released", "streak", "position")
listbox_risultati.heading("title",text="Titolo", command=lambda: sort_by_column("title"))
listbox_risultati.heading("appears on",text="Appare", command=lambda: sort_by_column("appears on"))
listbox_risultati.heading("artist",text="Arista", command=lambda: sort_by_column("artist"))
listbox_risultati.heading("writers",text="Scrittori", command=lambda: sort_by_column("writers"))
listbox_risultati.heading("producer",text="Produttore", command=lambda: sort_by_column("producer"))
listbox_risultati.heading("released",text="Rilasciato", command=lambda: sort_by_column("released"))
listbox_risultati.heading("streak",text="Streak", command=lambda: sort_by_column("streak"))
listbox_risultati.heading("position",text="Posizione", command=lambda: sort_by_column("position"))


def sort_by_column(column):
    data = [(listbox_risultati.set(child, column), child) for child in listbox_risultati.get_children("")]
    data.sort(reverse=False)  # Ordinamento ascendente
    for index, (_, child) in enumerate(data):
        listbox_risultati.move(child, "", index)

scrollbarO=tk.Scrollbar(window,orient=tk.HORIZONTAL,command=listbox_risultati.xview)
scrollbarV=tk.Scrollbar(window,orient=tk.VERTICAL,command=listbox_risultati.yview)

listbox_risultati.configure(xscrollcommand=scrollbarO.set)
listbox_risultati.configure(yscrollcommand=scrollbarV.set)

listbox_risultati.grid(row=2, column=0, sticky="nsew")
scrollbarV.grid(row=2, column=1, sticky="ns")
scrollbarV.config(command=listbox_risultati.yview)
entry_titolo.place(x=10,y=270)
text.place(x=300,y=270)
entry_appears_on.place(x=10,y=310)
entry_artist.place(x=10,y=350)
entry_writer.place(x=10,y=390)
entry_producer.place(x=10,y=430)
entry_released.place(x=10,y=470)
entry_streak.place(x=10,y=510)
entry_position.place(x=10,y=550)



entry_parametrica=tk.Entry(font='Arial 18', fg='Grey',width=10)
entry_parametrica.place(x=850,y=270)

opzioniS=[">","<"]
combobox_val=ttk.Combobox(window,values=opzioniS,width=2,height=1)
def str_position(event):
    if combobox.get()=='streak' or combobox.get()=='position':
        combobox_val.place(x=1000,y=270)
    else:
        combobox_val.place_forget()

def seleziona_opzione():
    listbox_risultati.delete(*listbox_risultati.get_children())
    selected_option = combobox.get()
    control=combobox_val.get()
    val=entry_parametrica.get()
    listbox_risultati.delete(*listbox_risultati.get_children())
    if selected_option=='streak' or selected_option=='position':
        if control=='>':
            documents = collection.find({selected_option: {"$gt":int(val)}})
            for document in documents:
                item = (
                    document["title"], document["appears on"], document["artist"], document["writers"],
                    document["producer"],
                    document["released"], document["streak"], document["position"])
                print(item)
                listbox_risultati.insert("", tk.END, values=item)

        elif control=='<':
            documents = collection.find({selected_option: {"$lt": int(val)}})
            for document in documents:
                item = (
                    document["title"], document["appears on"], document["artist"], document["writers"],
                    document["producer"],
                    document["released"], document["streak"], document["position"])
                listbox_risultati.insert("", tk.END, values=item)
    else:
        documents = collection.find({selected_option: {"$regex": entry_parametrica.get(), "$options": "i"}},
                                    {"_id": 0, "description": 0})

        for document in documents:
            item = (
            document["title"], document["appears on"], document["artist"], document["writers"], document["producer"],
            document["released"], document["streak"], document["position"])
            listbox_risultati.insert("", tk.END, values=item)

opzioni=["title","appears on","artist","writers","producer","released","streak","position"]
combobox=ttk.Combobox(window,values=opzioni)
combobox.place(x=700,y=270)
combobox.bind("<<ComboboxSelected>>",str_position)
buttonF = tk.Button(window, text="Cerca per", command=seleziona_opzione)
buttonF.place(x=635,y=270)
entry_titolo_old=tk.Entry(font='Arial 18', fg='Grey',width=20)
entry_titolo_new=tk.Entry(font='Arial 18', fg='Grey',width=20)
entry_titolo_old.place(x=650,y=360)
entry_titolo_new.place(x=650,y=400)

def clickChange():
    titolo_vecchio=entry_titolo_old.get()
    titolo_nuovo=entry_titolo_new.get()
    filter_query = {"title": titolo_vecchio}
    if titolo_nuovo != '':
        update_query = {"$set": {"title": titolo_nuovo}}
        collection.update_many(filter_query, update_query)

buttonChange = tk.Button(window, text="Cambia Titolo", command=clickChange,width=20,height=2)
buttonChange.place(x=720,y=320)



# Esegui il ciclo principale degli eventi
window.mainloop()

