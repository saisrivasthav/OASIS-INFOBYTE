import tkinter as tk
from tkinter import messagebox


def calculate_bmi():
    try:
        weight = float(entry_weight.get())
        height = float(entry_height.get()) / 100  
        bmi = weight / (height ** 2)
        result_text.set(f"BMI: {bmi:.2f}")
        
        
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obesity"
        
        result_text.set(f"BMI: {bmi:.2f} ({category})")
        
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers for weight and height.")


root = tk.Tk()
root.title("BMI Calculator")
root.geometry("300x200")


result_text = tk.StringVar()


tk.Label(root, text="Weight (kg):").grid(row=0, column=0, padx=10, pady=10)
entry_weight = tk.Entry(root)
entry_weight.grid(row=0, column=1)

tk.Label(root, text="Height (cm):").grid(row=1, column=0, padx=10, pady=10)
entry_height = tk.Entry(root)
entry_height.grid(row=1, column=1)

tk.Button(root, text="Calculate", command=calculate_bmi).grid(row=2, columnspan=2, pady=20)

tk.Label(root, textvariable=result_text).grid(row=3, columnspan=2)


root.mainloop()