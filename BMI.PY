from tkinter import Tk, Frame, Label, Entry, Button, SOLID


colors = {"co0": "#444466", "co1": "#ADD8E6", "co2": "#6856FF"}


window = Tk()
window.title('BMI Calculator')
window.geometry('295x230')
window.resizable(height=False, width=False)
window.configure(bg=colors["co1"])

frames = {name: Frame(window, width=295, height=50, bg=colors["co1"], pady=0, padx=0) for name in ["top", "down"]}
frames["top"].grid(row=0, column=0)
frames["down"].grid(row=1, column=0)


labels = {
    "app_name": Label(frames["top"], text = "BMI Calculator", width=23, height=1, padx=0, anchor="center", font=("Helvetica", 16, "bold"), bg=colors["co1"], fg=colors["co0"]),
    "app_line": Label(frames["top"], text = "", width=400, height=1, padx=0, anchor="center", font=("Arial", 1), bg=colors["co2"], fg=colors["co0"])
}
labels["app_name"].place(x=0, y=2)
labels["app_line"].place(x=0, y=35)


def calculate():
    weight = float(entries["weight"].get())
    height = float(entries["height"].get()) ** 2
    result = weight / height

    if result < 18.4:
        labels["result_text"]['text'] = "Your BMI is: Underweight"
    elif result >= 18.5 and result < 24.9:
         labels["result_text"]['text'] = "Your BMI is: Normal"
    elif result >=25 and result <29.9:
         labels["result_text"]['text'] = "Your BMI is: Overweight"
    else:
         labels["result_text"]['text'] = "Your BMI is: Obesity"

    labels["result"]['text'] = "{:.{}f}".format(result, 2)


entries = {
    "weight": Entry(frames["down"], width=5, font=("Helvetica", 10, "bold"), justify="center", relief=SOLID),
    "height": Entry(frames["down"], width=5, font=("Helvetica", 10, "bold"), justify="center", relief=SOLID)
}
for i, key in enumerate(entries):
    Label(frames["down"], text = f"Enter your {key}", height=1, padx=0, anchor="center", font=("Helvetica", 10, "bold"), bg=colors["co1"], fg=colors["co0"]).grid(row=i, column=0, columnspan=1, pady=10, padx=3)
    entries[key].grid(row=i, column=1, columnspan=1, pady=10, padx=3)


labels["result"] = Label(frames["down"], width=5, text="---", height=1, padx=6, pady=12, relief="flat", anchor="center", font=('Helvetica', 24, 'bold'), bg=colors["co2"], fg=colors["co1"])
labels["result"].place(x=175, y=10)

labels["result_text"] = Label(frames["down"], width=37, text="", height=1, padx=6, pady=12, relief="flat", anchor="center", font=('Helvetica', 10, 'bold'), bg=colors["co1"], fg=colors["co0"])
labels["result_text"].place(x=0, y=85)


Button(frames["down"], text="Calculate", width=34, height=1, bg=colors["co2"], fg=colors["co1"], font=("Helvetica", 10, "bold"), anchor="center", command=calculate).grid(row=4, column=0, pady=60, padx=5, columnspan=30)


window.mainloop()