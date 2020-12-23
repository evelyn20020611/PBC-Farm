from PIL import ImageTk
import tkinter as tk
import tkinter.font as tkFont

class Farm(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()  # 產生網格
        self.createWidgets()

    def createWidgets(self):
    	# 匯入圖片的部分寫這邊self.image_ = ImageTk.PhotoImage(file = 'graph/.PNG')  # 
        self.image_bg = ImageTk.PhotoImage(file = 'graph/rug2.PNG')  # 背景圖片
        self.image_waterer = ImageTk.PhotoImage(file = 'graph/waterer.PNG')  # waterer
        self.image_small_pepper = ImageTk.PhotoImage(file = 'graph/small_pepper.PNG')  # small_pepper
        self.image_small_eggplant = ImageTk.PhotoImage(file = 'graph/small_eggplant.PNG')  # small_eggplant
        self.image_small_coriander = ImageTk.PhotoImage(file = 'graph/small_coriander.PNG')  # small_coriander
        self.image_seedstore_icon = ImageTk.PhotoImage(file = 'graph/seedstore_icon.PNG')  # seedstore_icon
        self.image_seed_pepper = ImageTk.PhotoImage(file = 'graph/seed_pepper.PNG')  # seed_pepper
        self.image_seed_package_pepper = ImageTk.PhotoImage(file = 'graph/seed_package_pepper.PNG')  # seed_package_pepper
        self.image_seed_package_eggplant = ImageTk.PhotoImage(file = 'graph/seed_package_eggplant.PNG')  # seed_package_eggplant
        self.image_seed_package_coriander = ImageTk.PhotoImage(file = 'graph/seed_package_coriander.PNG')  # seed_package_coriander
        self.image_seed_eggplant = ImageTk.PhotoImage(file = 'graph/seed_eggplant.PNG')  # seed_eggplant
        self.image_seed_coriander = ImageTk.PhotoImage(file = 'graph/seed_coriander.PNG')  # seed_coriander
    	self.image_mid_pepper = ImageTk.PhotoImage(file = 'graph/mid_pepper.PNG')  # mid_pepper
        self.image_mid_eggplant = ImageTk.PhotoImage(file = 'graph/mid_eggplant.PNG')  # mid_eggplant
        self.image_mid_coriander = ImageTk.PhotoImage(file = 'graph/mid_coriander.PNG')  # mid_coriander
        self.image_empty_pot = ImageTk.PhotoImage(file = 'graph/empty_pot.PNG')  # empty_pot
        self.image_book_icon = ImageTk.PhotoImage(file = 'graph/book_icon.PNG')  # book_icon
        self.image_book = ImageTk.PhotoImage(file = 'graph/book.PNG')  # book
        self.image_big_eggplant = ImageTk.PhotoImage(file = 'graph/big_eggplant.PNG')  # big_eggplant
        self.image_big_pepper = ImageTk.PhotoImage(file = 'graph/big_pepper.PNG')  # big_pepper
        self.image_big_coriander = ImageTk.PhotoImage(file = 'graph/big_coriander.PNG')  # big_coriander
        self.image_back_icon_name = ImageTk.PhotoImage(file = 'graph/back_icon_name.PNG')  # back_icon_name
        self.image_back_icon = ImageTk.PhotoImage(file = 'graph/back_icon.PNG')  # back_icon
        self.image_conversation = ImageTk.PhotoImage(file = 'graph/conversation.PNG')  # conversation 種子對話框

    	# 產生label的部分寫這邊
    	self.background_label = tk.Label(self, image=self.image_bg)  # 產生背景圖片

    	# 產生button 的部分寫這邊
        self.button_book = tk.Button(self, image=self.image_book_icon)
        self.button_seedstore = tk.Button(self, image=self.image_seedstore_icon)
        self.button_seed_pepper = tk.Button(self, image=self.image_seed_pepper)
        self.button_seed_eggplan = tk.Button(self, image=self.image_seed_eggplant)
        self.button_seed_coriander = tk.Button(self, image=self.image_seed_coriander)
        self.button_back = tk.Button(self, image=self.image_back_icon)
        self.button_waterer = tk.Button(self, image = self.image_waterer, command=self.click_button_waterer, height=1, width=2)

        # grid 的部分寫這邊
    	self.background_label.grid(row = 0, column = 0, columnspan = 10)
        self.back.grid(row = 1, column = 0, columnspan = 10)
        self.book.grid(row = 8, column = 0, columnspan = 10)
        self.seedstore.grid(row = 9, column = 0, columnspan = 10)
        self.waterer.grid(row = 10, column = 5, columnspan = 10)
        
    # 種子商店
    def open_store(): # 點了種子商店按鈕後的function
        global open_store  # 不確定這行要不要
        seed_store = tk.Tk()
        seed_store.title('Seed Store')
        seed_store.geometry('500x300')
        self.havesd = 0
        self.button_seed_package_pepper.grid(row = 0, column = 1, columnspan = 10)
        self.button_seed_package_eggplant.grid(row = 0, column = 2, columnspan = 10)
        self.button_seed_package_coriander.grid(row = 0, column = 3, columnspan = 10)

    def put_peppersd(self):
        self.havesd = 1
        self.Label_peppersd = tk.Label(seed_store, image = self.image_seed_pepper)
        self.peppersd.grid(row = 5.5, column = 5, columnspan = 10)
        if self.havesd == 1:
            self.button_exit = tk.Button(text = "Click and Quit", command = seed_store.destroy)
            self.button_exit.grid(row = 1, column = 2, columnspan = 10)

    def put_eggplantsd(self): 
        self.havesd = 1
        self.Label_eggplantsd = tk.Label(seed_store, image = self.image_seed_eggplant)
        self.eggplantsd.grid(row = 5.5 , column = 5, columnspan = 10)
        if self.havesd == 1:
            self.button_exit = tk.Button(text = "Click and Quit", command = seed_store.destroy)
            self.button_exit.grid(row = 1, column = 2, columnspan = 10)

    def put_coriandersd(self):
        self.havesd = 1
        self.Label_coriandersd = tk.Label(seed_store, image = self.image_seed_coriander)
        self.coriandersd.grid(row = 5.5 , column = 5, columnspan = 10)
        if self.havesd == 1:
            self.button_exit = tk.Button(text = "Click and Quit", command = seed_store.destroy)
            self.button_exit.grid(row = 1, column = 2, columnspan = 10)

    def cclick_button_waterer(self):
        self.lb1Num.configure("")  # 配置，回傳文字1


game = Farm()
game.master.title("PBC Farm")
game.mainloop()