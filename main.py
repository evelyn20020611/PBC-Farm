from PIL import ImageTk
import tkinter as tk
import tkinter.font as tkFont

class Farm(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()  # 產生網格
        self.createWidgets()

    def createWidgets(self):
    	# 匯入圖片的部分寫這邊
    	self.image_bg = ImageTk.PhotoImage(file = 'graph/rug2.PNG')  # 背景圖片

    	# 產生label的部分寫這邊
    	self.background_label = tk.Label(self, image=self.image_bg)  # 產生背景圖片

    	# 產生button 的部分寫這邊

    	# grid 的部分寫這邊
    	self.background_label.grid(row = 0, column = 0, columnspan = 6)

print()
game = Farm()
game.master.title("PBC Farm")
game.mainloop()
