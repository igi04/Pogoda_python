import requests
import tkinter as tk


def daj_pogode_lebork():
    lebork_api = "https://danepubliczne.imgw.pl/api/data/synop/station/lebork"
    lebork_api_data = requests.get(lebork_api).json()

    return lebork_api_data

    # print(lebork_api_data)
    # print("Znajdujemy sie w stacji "+lebork_api_data['stacja'])
    # print("O godzinie "+lebork_api_data["godzina_pomiaru"]+" bylo "+lebork_api_data['temperatura']+" stopni celsjusza")
    #
    # if float(lebork_api_data['cisnienie']) <= 1050:
    #     print("Cisnienie niskie, na poziomie " + lebork_api_data['cisnienie'])
    # else:
    #     print("Cisnienie wyokie, na poziomie "+lebork_api_data['cisnienie'])


# TODO: Ma zwracać dane o lęborku
def wpisz_dane_o_leborku():
    pass
    textbox.insert(tk.END, f"Id stacji: {daj_pogode_lebork()['id_stacji']}    Stacja: {daj_pogode_lebork()['stacja']}"
                           f"Data: {daj_pogode_lebork()['data_pomiaru']}   Temperatura:  {daj_pogode_lebork()['temperatura']}   Godzina:  {daj_pogode_lebork()['godzina_pomiaru']} "
                           f"Predkosc wiatru:  {daj_pogode_lebork()['predkosc_wiatru']}  Kierunek wiatru:  {daj_pogode_lebork()['kierunek_wiatru']}"
                           f"Wilgotnosc wzgledna:  {daj_pogode_lebork()['wilgotnosc_wzgledna']}")


root =  tk.Tk()
root.geometry("500x500")
root.title("Pogoda GUI")

label = tk.Label(root, text="Hello World!", font=("Arial", 18))
label.pack(padx=20, pady=20)

textbox = tk.Text(root, height=3 , font=('Arial', 16), )

textbox.pack(padx=10, pady=10)

button = tk.Button(root, text="Wyświetl", font=('Arial', 18))
button.pack(padx=10, pady=10)

buttonFrame = tk.Frame(root)
buttonFrame.columnconfigure(0, weight=1)
buttonFrame.columnconfigure(1, weight=1)
buttonFrame.columnconfigure(2, weight=1)

btn1 = tk.Button(buttonFrame, text='Lębork', font=('Arial', 18), command=wpisz_dane_o_leborku)
btn1.grid(row=0, column=0, sticky=tk.W+tk.E)

btn2 = tk.Button(buttonFrame, text='1', font=('Arial', 18))
btn2.grid(row=0, column=1, sticky=tk.W+tk.E)

btn3 = tk.Button(buttonFrame, text='1', font=('Arial', 18))
btn3.grid(row=0, column=2, sticky=tk.W+tk.E)

btn4 = tk.Button(buttonFrame, text='1', font=('Arial', 18))
btn4.grid(row=1, column=0, sticky=tk.W+tk.E)

btn5 = tk.Button(buttonFrame, text='1', font=('Arial', 18))
btn5.grid(row=1, column=1, sticky=tk.W+tk.E)

btn6 = tk.Button(buttonFrame, text='1', font=('Arial', 18))
btn6.grid(row=1, column=2, sticky=tk.W+tk.E)

buttonFrame.pack(fill='x')


# anotherButton = tk.Button(root, text="TEST")
# anotherButton.place(x=200, y=200, height=100, width=100)
# wejscie = tk.Entry(root)
# wejscie.pack()
root.mainloop()