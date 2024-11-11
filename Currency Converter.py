from tkinter import *
from tkinter import ttk

def convert_currency():
    try:
        amount = float(amount_entry.get())
        from_curr = from_currency.get()
        to_curr = to_currency.get()
        conversion_rate = conversion_rates[from_curr][to_curr]
        converted_amount = amount * conversion_rate
        result_label.config(text=f"{amount} {from_curr} = {converted_amount:.2f} {to_curr}")
    except ValueError:
        result_label.config(text="Please enter a valid amount")

# Conversion rates
conversion_rates = {
    'USD': {'INR': 74.85, 'EUR': 0.85, 'GBP': 0.75},
    'INR': {'USD': 0.013, 'EUR': 0.011, 'GBP': 0.010},
    'EUR': {'USD': 1.18, 'INR': 88.32, 'GBP': 0.88},
    'GBP': {'USD': 1.34, 'INR': 100.16, 'EUR': 1.14},
}

# Set up GUI
converter = Tk()
converter.geometry("400x300")
converter.title("Currency Converter")

# Adding amount input and dropdowns for currency selection
amount_label = Label(converter, text="Amount:")
amount_label.grid(column=0, row=1)
amount_entry = Entry(converter)
amount_entry.grid(column=1, row=1)

from_label = Label(converter, text="From:")
from_label.grid(column=0, row=2)
from_currency = ttk.Combobox(converter, values=list(conversion_rates.keys()))
from_currency.grid(column=1, row=2)

to_label = Label(converter, text="To:")
to_label.grid(column=0, row=3)
to_currency = ttk.Combobox(converter, values=list(conversion_rates.keys()))
to_currency.grid(column=1, row=3)

convert_button = Button(converter, text="Convert", command=convert_currency)
convert_button.grid(column=0, row=4, columnspan=2)

result_label = Label(converter, text="")
result_label.grid(column=0, row=5, columnspan=2)

mainloop()
