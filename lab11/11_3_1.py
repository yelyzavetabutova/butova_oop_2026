import tkinter as tk

def solve_equation():

    a1 = float(entry_a1.get())
    b1 = float(entry_b1.get())
    c1 = float(entry_c1.get())
    a2 = float(entry_a2.get())
    b2 = float(entry_b2.get())
    c2 = float(entry_c2.get())
    D = a1 * b2 - b1 * a2
    Dx = c1 * b2 - b1 * c2
    Dy = a1 * c2 - c1 * a2
    x = Dx / D
    y = Dy / D
    label_result.config(text=f"x = {round(x, 2)}     y = {round(y, 2)}")

root = tk.Tk()

entry_a1 = tk.Entry(root, width=5)
entry_a1.grid(row=0, column=0, padx=5, pady=5)
lbl_x1 = tk.Label(root, text="x +")
lbl_x1.grid(row=0, column=1)
entry_b1 = tk.Entry(root, width=5)
entry_b1.grid(row=0, column=2, padx=5, pady=5)
lbl_y1 = tk.Label(root, text="y =")
lbl_y1.grid(row=0, column=3)
entry_c1 = tk.Entry(root, width=5)
entry_c1.grid(row=0, column=4, padx=5, pady=5)

entry_a2 = tk.Entry(root, width=5)
entry_a2.grid(row=1, column=0, padx=5, pady=5)
lbl_x2 = tk.Label(root, text="x +")
lbl_x2.grid(row=1, column=1)
entry_b2 = tk.Entry(root, width=5)
entry_b2.grid(row=1, column=2, padx=5, pady=5)
lbl_y2 = tk.Label(root, text="y =")
lbl_y2.grid(row=1, column=3)
entry_c2 = tk.Entry(root, width=5)
entry_c2.grid(row=1, column=4, padx=5, pady=5)

label_result = tk.Label(root, text="x =                 y = ")
label_result.grid(row=2, column=0, columnspan=5, pady=10)
btn_calc = tk.Button(root, text="Solve", command=solve_equation)
btn_calc.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()