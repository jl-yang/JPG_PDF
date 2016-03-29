# -*- coding: utf-8 -*-

from Tkinter import *
import tkFileDialog
import tkMessageBox
import img2pdf

import sys
class NullDevice():
    def write(self, s):
        pass

class Application(Frame):
	def __init__(self, master):
		Frame.__init__(self, master)
		self.grid()
		self.create_widgets()
		
		self.master = master
		
		sys.stdout = NullDevice()
		sys.stderr = NullDevice()
		
	def open_file(self):
		#Select multiple files
		#Convert them to a single pdf 
		self.fileName = tkFileDialog.askopenfilename(parent=self.master, multiple=True)
		
		if len(self.fileName) == 0:	
			return
			
			
		try:
			self.pdf = img2pdf.convert(sorted(self.fileName))
		except:
			tkMessageBox.showerror("转换失败", "选择的文件不是图像文件，请重新选择", parent=self.master)
			return
			
		with open("PDF.pdf", "wb") as f:			
			f.write(self.pdf)
		
		tkMessageBox.showinfo("转换成功", "已成功转换！转换后的pdf文件就在当前目录，文件名为PDF", parent=self.master)
		
	def create_widgets(self):
		self.label = Label(self, text="选择所有需要转换的jpg文件(或者其他图像文件)。 所选的所有文件将被转换为一个pdf文件")
		self.label.grid()
		
		self.button = Button(self, text = "选择", width = 20)
		self.button["command"] = self.open_file
		
		self.button.grid()
		
		
		
		
		
if __name__ == "__main__":	
	root = Tk()
	root.title("将jpg转换为pdf")

	w=500
	h=50
	ws = root.winfo_screenwidth()
	hs = root.winfo_screenheight()
	x = (ws/2) - (w/2)    
	y = (hs/2) - (h/2)
	root.geometry('%dx%d+%d+%d' % (w, h, x, y))
	
	app = Application(root)
	
	root.mainloop()

















 
#w = Label(root, text="Hello world!")
#w.pack()
 
