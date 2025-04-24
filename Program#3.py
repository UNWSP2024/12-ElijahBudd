# Elijah Budd
# 4/24/2025
# Program #3: Long-Distance Calls
import tkinter as tk
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        #Create main window
        self.window = tk.Tk()

        #Set up the canvas
        self.canvas = tk.Canvas(self.window, width=550, height=250)
        self.canvas.grid(rowspan=4, columnspan=3)

        #Create IntVar object for the Radiobuttons
        self.radioVar = tk.IntVar()

        #Set the IntVar object to 1
        self.radioVar.set(1)

        #Create the Label for the Rate Category
        rateLabel = tk.Label(self.window, text="Rate Category")
        rateLabel.grid(row=0, column=0)

        #Create the Radiobuttons
        self.rb1 = tk.Radiobutton(self.window, text="Daytime (6:00 A.M. through 5:59 P.M.)", variable=self.radioVar, value=1)
        self.rb1.grid(row=1, column=0)

        self.rb2 = tk.Radiobutton(self.window, text="Evening (6:00 P.M.  through 11:59 P.M.)", variable=self.radioVar, value=2)
        self.rb2.grid(row=2, column=0)

        self.rb3 = tk.Radiobutton(self.window, text="Off-Peak (midnight through 5:59 P.M.) ", variable=self.radioVar, value=3)
        self.rb3.grid(row=3, column=0)

        #Create the rates for each category
        self.perMinLabel = tk.Label(self.window, text="Rate per Minute")
        self.perMinLabel.grid(row=0, column=1)

        self.dayRateLabel = tk.Label(self.window, text="$0.02")
        self.dayRateLabel.grid(row=1, column=1)

        self.eveningRateLabel = tk.Label(self.window, text="$0.12")
        self.eveningRateLabel.grid(row=2, column=1)

        self.offpeakRateLabel = tk.Label(self.window, text="$0.05")
        self.offpeakRateLabel.grid(row=3, column=1)

        #Create and set up the number of minutes input
        self.callInput = tk.Entry(self.window, width=10)
        self.callInput.grid(row=2, column=2)

        self.callLabel = tk.Label(self.window, text="Enter number of minutes on call")
        self.callLabel.grid(row=1, column=2)

        def call_input(self):
            self.nMinutes = self.callInput.get()
            return self.nMinutes

        # Create the calculate button
        self.calculateButton = tk.Button(self.window, text="Calculate", command=self.calculate)
        self.calculateButton.grid(row=3, column=2)

        # Start the main loop
        self.window.mainloop()

    #Create the calculate function
    def calculate(self):
        rate = 0.0

        radioVar = self.radioVar.get()
        nMinutes = float(self.callInput.get())

        if radioVar == 1:
            rate = 0.02
        elif radioVar == 2:
            rate = 0.12
        elif radioVar == 3:
            rate = 0.05

        total = nMinutes * rate

        tk.messagebox.showinfo("Call Cost", f"The cost of the call is: ${total:.2f}")

#Create an instance of the MyGUI class
if __name__ == '__main__':
    my_gui = MyGUI()
