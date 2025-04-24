# Elijah Budd
# 4/21/2025
# Program #2: MPG Calculator

#setup
import tkinter as tk

mainWindow = tk.Tk()

canvas = tk.Canvas(mainWindow, width=350, height=200)
canvas.grid(columnspan=2)
canvas.grid(rowspan=6)

# Gas input
gasInput = tk.Entry(mainWindow, width=10)
gasInput.grid(column=0, row=2)

gasLabel = tk.Label(mainWindow, text='Enter number of gallons of gas')
gasLabel.grid(column=0, row=1)

def gas_input():
    gasNumber = gasInput.get()
    print("Input", gasNumber)

    return gasNumber

# Miles input
milesInput = tk.Entry(mainWindow, width=10)
milesInput.grid(column=0, row=4)

milesLabel = tk.Label(mainWindow, text='Enter number of miles while on full tank')
milesLabel.grid(column=0, row=3)

def miles_input():
    maxMiles = milesInput.get()
    print("Input", maxMiles)

    return maxMiles

# Button calculation
def button_clicked():
    gallons = float(gasInput.get())
    miles = float(milesInput.get())

    mpg = miles/gallons

    mpgLabel = tk.Label(mainWindow, text=f'MPG = {mpg}')
    mpgLabel.grid(column=1, row=3)

calculateButton = tk.Button(mainWindow, text='Calculate MPG', command=button_clicked)
calculateButton.grid(column=1, row=2)

#end
mainWindow.mainloop()
