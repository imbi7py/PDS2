import tkinter as tk

'''
	Matrix with text to calculator
'''
buttonText = [
	["", "", "", "", "", "limpar"],
	["raizq", "x2", "**", "(", ")", "/"],
	["sin", "cos", "7", "8", "9", "+"],
	["sin-x", "cos-x", "4", "5", "6", "-"],
	["tan", "tan-x", "1", "2", "3", "*"],
	["n!", "pi", ".", "0", "=", "C"]
]

'''
	Adds text to GUI element
'''

'''
	Creates the elements for the GUI
'''
def createElement(frame, tipo, i, j, columnspan=1, label=None):
	element = None
	if tipo == "button":
		element = tk.Button(
			frame, text=buttonText[i][j], bd=3, padx=1, pady=1, width=8, height=2, highlightbackground="blue")
	elif tipo == "label":
		element = tk.Label(
			frame, text=buttonText[i][j], highlightbackground="blue", bg="blue")

	element.grid(row=i, column=j, columnspan=columnspan)
	return element

'''
	Generates the Screen
'''
class Screen:
	def __init__(self, master):
		self.texto = ""
		self.mainScreen = master
		self.mainScreen.title("Scientific Calculator")

		self.num1 = tk.DoubleVar
		self.num2 = tk.DoubleVar
		self.operator = tk.StringVar

		self.fr = tk.Frame(self.mainScreen, highlightbackground="blue", bg="blue")
		self.fr.pack()

		self.lb = createElement(self.fr, "label", 0, 0, 5)
		self.btn05 = createElement(self.fr, "button", 0, 5, 1)

		def addText(self, newtexto, label):
			self.texto += newtexto
			label.config(text=newtexto)

		for i in range(1, len(buttonText)):
			for j in range(0, len(buttonText[i])):
				self.element = createElement(self.fr, "button", i, j, 1, self.lb)
				self.element.config(command=addText(buttonText[i][j], self.lb))


'''
	Main function
'''
def main():
	rootWindow = tk.Tk()
	Screen(rootWindow)
	rootWindow.mainloop()

main()
