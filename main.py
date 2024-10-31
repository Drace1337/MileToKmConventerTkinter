import tkinter

def calculate():
    input_text = input.get()
    kilometers = int(input_text)*1.6
    convert_label.config(text=f"{kilometers}")

window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)

input = tkinter.Entry(width=10)
input.grid(column=1, row=0)

miles_label = tkinter.Label(text="Miles")
miles_label.grid(column=2, row=0)

equal_label = tkinter.Label(text="is equal to")
equal_label.grid(column=0, row=1)

convert_label = tkinter.Label(text="0")
convert_label.grid(column=1, row=1)

km_label = tkinter.Label(text="Km")
km_label.grid(column=2, row=1)


calculate_button = tkinter.Button(text="Calculate", command=calculate)
calculate_button.grid(column=1, row=2)





window.mainloop()