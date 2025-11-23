import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np

def plot_trajectory():
    try:

        initial_velocity = float(entry_velocity.get())
        angle_degrees = float(entry_angle.get())
        gravity = float(entry_gravity.get())

        if initial_velocity <= 0 or angle_degrees <= 0 or gravity <= 0:
            raise ValueError("One from all vars is not positive.")


        angle_radians = np.radians(angle_degrees)

        v_x = initial_velocity * np.cos(angle_radians)  
        v_y = initial_velocity * np.sin(angle_radians) 

       
        time_of_flight = (2 * v_y) / gravity

       
        t = np.linspace(0, time_of_flight, num=500)

       
        x = v_x * t
        y = v_y * t - 0.5 * gravity * t**2

     
        plt.figure(figsize=(8, 6))
        plt.plot(x, y, label="Trajectory of movement")
        plt.title("Schedule of movement a object an at angel")
        plt.xlabel("S (x)")
        plt.ylabel("h (y)")
        plt.grid(True)
        plt.legend()
        plt.show()

    except ValueError as e:
        messagebox.showerror("Ошибка", str(e))


root = tk.Tk()
root.title("Modelling of movement a object at an angel")


label_velocity = tk.Label(root, text="First speed (m/s):")
label_velocity.grid(row=0, column=0, padx=10, pady=5, sticky="w")
entry_velocity = tk.Entry(root)
entry_velocity.grid(row=0, column=1, padx=10, pady=5)

label_angle = tk.Label(root, text="Throw angle:")
label_angle.grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_angle = tk.Entry(root)
entry_angle.grid(row=1, column=1, padx=10, pady=5)

label_gravity = tk.Label(root, text="Acceleration of gravity (m/s²):")
label_gravity.grid(row=2, column=0, padx=10, pady=5, sticky="w")
entry_gravity = tk.Entry(root)
entry_gravity.grid(row=2, column=1, padx=10, pady=5)

button_plot = tk.Button(root, text="Build...", command=plot_trajectory)
button_plot.grid(row=3, column=0, columnspan=2, pady=10)


root.mainloop()
