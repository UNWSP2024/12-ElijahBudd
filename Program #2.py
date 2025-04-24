# Elijah Budd
# 4/22/2025
# Program #3: Joe's Automotive

import tkinter as tk

def main():
    mainWindow = tk.Tk()

    # Create Var objects
    tireVar = tk.IntVar()
    mufflerVar = tk.IntVar()
    inspectionVar = tk.IntVar()
    transmissionVar = tk.IntVar()
    radiatorVar = tk.IntVar()
    lubeVar = tk.IntVar()
    oilVar = tk.IntVar()

    # Set the Var objects to 0
    tireVar.set(0)
    mufflerVar.set(0)
    inspectionVar.set(0)
    transmissionVar.set(0)
    radiatorVar.set(0)
    lubeVar.set(0)
    oilVar.set(0)

    # Setup canvas
    canvas = tk.Canvas(mainWindow, height=300, width=350)
    canvas.grid(rowspan=7, columnspan=3)

    # Oil
    oilBox = tk.Checkbutton(mainWindow, text="Oil Change - $30.00", variable=oilVar)
    oilBox.grid(column=0, row=0)

    # Lube
    lubeBox = tk.Checkbutton(mainWindow, text="Lube Job - $20.00", variable=lubeVar)
    lubeBox.grid(column=0, row=1)

    # Radiator
    radiatorBox = tk.Checkbutton(mainWindow, text="Radiator Flush - $40.00", variable=radiatorVar)
    radiatorBox.grid(column=0, row=2)

    # Transmission
    transmissionBox = tk.Checkbutton(mainWindow, text="Transmission Fluid - $100.00", variable=transmissionVar)
    transmissionBox.grid(column=0, row=3)

    # Inspection
    inspectionBox = tk.Checkbutton(mainWindow, text="Inspection - $35.00", variable=inspectionVar)
    inspectionBox.grid(column=0, row=4)

    # Muffler
    mufflerBox = tk.Checkbutton(mainWindow, text="Muffler Replacement - $200.00", variable=mufflerVar)
    mufflerBox.grid(column=0, row=5)

    # Tire
    tireBox = tk.Checkbutton(mainWindow, text=f"Tire Rotation - $20.00", variable=tireVar)
    tireBox.grid(column=0, row=6)

    # Calculate the total
    def calculate():
        total = 0
        if tireVar.get() == 1:
            total += 20.00
        if mufflerVar.get() == 1:
            total += 200.00
        if inspectionVar.get() == 1:
            total += 35.00
        if transmissionVar.get() == 1:
            total += 100.00
        if radiatorVar.get() == 1:
            total += 40.00
        if lubeVar.get() == 1:
            total += 20.00
        if oilVar.get() == 1:
            total += 30.00

        totalLabel = tk.Label(mainWindow, text=f"Total: {total}")
        totalLabel.grid(column=2, row=4)

    # Create total button
    totalBox = tk.Button(mainWindow, text="Total Charges", command=calculate)
    totalBox.grid(column=2, row=3)

    mainWindow.mainloop()

if __name__ == '__main__':
    main()
