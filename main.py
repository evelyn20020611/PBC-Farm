from PIL import ImageTk
from PIL import Image   # 如果要用resize的話
import tkinter as tk
import tkinter.font as tkFont
from PIL import Image
import tkinter.messagebox #這個是訊息框，對話方塊的關鍵
import time


class Farm(tk.Frame):  # try
    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()  # 產生網格
        self.createImages()
        self.createWidgets()
        self.init_grid()
        self.level = 0
        self.pas = "no"
        self.target = ""
        self.seeded = False
        self.Timer_ended = True
        self.amount = {'coriander':0,'eggplant':0,'pepper':0}

    # 計時器
    def Timer(self):
        self.Timer_ended = False
        self.start_time = time.time()
        self.end_time = self.start_time + 30
        self.update_clock()

    # 每秒更新計時器
    def update_clock(self):
        now = int(self.end_time - time.time())
        if now < 0:
            self.Timer_ended = True
            return
        self.timer_label.configure(text=now)
        self.after(1000, self.update_clock)

    def createImages(self):
    	# 匯入圖片的部分寫這邊self.image_ = ImageTk.PhotoImage(file = 'graph/.png')  # 
        self.image_bg = ImageTk.PhotoImage(file = 'graph/rug2.PNG')  # 背景圖片
        self.image_waterer = ImageTk.PhotoImage(file = 'graph/waterer.PNG')  # waterer
        self.image_small_pepper = ImageTk.PhotoImage(file = 'graph/small_pepper.PNG')  # small_pepper
        self.image_small_eggplant = ImageTk.PhotoImage(file = 'graph/small_eggplant.PNG')  # small_eggplant
        self.image_small_coriander = ImageTk.PhotoImage(file = 'graph/small_coriander.PNG')  # small_coriander
        self.image_seedstore_icon = ImageTk.PhotoImage(file = 'graph/seedstore_icon.png')  # seedstore_icon
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
        self.image_book_icon = ImageTk.PhotoImage(file = 'graph/book_icon.png')  # book_icon
        self.image_book = ImageTk.PhotoImage(file = 'graph/book.png')  # book
        self.image_big_eggplant = ImageTk.PhotoImage(file = 'graph/big_eggplant.PNG')  # big_eggplant
        self.image_big_pepper = ImageTk.PhotoImage(file = 'graph/big_pepper.PNG')  # big_pepper
        self.image_big_coriander = ImageTk.PhotoImage(file = 'graph/big_coriander.PNG')  # big_coriander
        self.image_back_icon_name = ImageTk.PhotoImage(file = 'graph/back_icon_name.png')  # back_icon_name
        self.image_back_icon = ImageTk.PhotoImage(file = 'graph/back_icon.png')  # back_icon
        self.image_conversation = ImageTk.PhotoImage(file = 'graph/conversation.PNG')  # conversation 種子對話框
        self.image_pot_with_seed = ImageTk.PhotoImage(file = 'graph/pot_with_seed.jpg')  # pot_with_seed
        self.image_big_coriander_ill = ImageTk.PhotoImage(file = 'graph/big_coriander_ill.png')
        self.image_big_pepper_ill = ImageTk.PhotoImage(file = 'graph/big_pepper_ill.png')
        self.image_big_eggplant_ill = ImageTk.PhotoImage(file = 'graph/big_eggplant_ill.png')
        self.image_hoe = ImageTk.PhotoImage(file = 'graph/hoe.png')  # hoe 鋤頭

    def createWidgets(self):
        self.background_label = tk.Label(self, image=self.image_bg)  # 產生背景圖片
        self.empty_pot_label = tk.Label(self,image=self.image_empty_pot)  #產生空盆栽
        self.small_coriander_label = tk.Label(self,image=self.image_small_coriander)  #產生small_coriander盆栽
        self.mid_coriander_label = tk.Label(self,image=self.image_mid_coriander)  #產生mid_coriander盆栽
        self.big_coriander_label = tk.Label(self,image=self.image_big_coriander)  #產生big_coriander盆栽
        
        self.small_pepper_label = tk.Label(self,image=self.image_small_pepper)  #產生small_pepper盆栽
        self.mid_pepper_label = tk.Label(self,image=self.image_mid_pepper)  #產生mid_pepper盆栽
        self.big_pepper_label = tk.Label(self,image=self.image_big_pepper)  #產生big_pepper盆栽
        
        self.small_eggplant_label = tk.Label(self,image=self.image_small_eggplant)  #產生small_eggplant盆栽
        self.mid_eggplant_label = tk.Label(self,image=self.image_mid_eggplant)  #產生mid_eggplant盆栽
        self.big_eggplant_label = tk.Label(self,image=self.image_big_eggplant)  #產生big_eggplant盆栽
        
        self.image_pot_with_seed_label = tk.Label(self,image=self.image_pot_with_seed)  # 產生pot_with_seed

        self.timer_label = tk.Label(text="0", font=('Helvetica', 48), fg='black')

        # 產生button 的部分寫這邊
        self.button_book = tk.Button(self, image=self.image_book_icon, command = self.click_button_book)
        self.button_seedstore = tk.Button(self, image=self.image_seedstore_icon, command = self.open_store)
        self.button_waterer = tk.Button(self, image = self.image_waterer, command = self.click_button_waterer)
        self.button_harvest = tk.Button(self, image = self.image_hoe, command = self.click_button_harvest)

    def init_grid(self):
        # 初始grid 的部分寫這邊
        self.empty_pot_label.grid(row = 0, column = 0, columnspan = 5)
        self.button_seedstore.grid(row = 1, column = 0)
        self.button_waterer.grid(row = 1, column = 2)
        self.button_book.grid(row = 1, column = 4)
        self.timer_label.grid(row = 2, column = 0, columnspan = 5)


 
        
    # 種子商店功能
    def open_store(self): # 點了種子商店按鈕後的function
        r1 = tk.Toplevel()
        r1.title('Seed Store')
        r1.geometry('1000x800')

        # 產生button
        self.button_seed_package_pepper = tk.Button(r1, image = self.image_seed_package_pepper , command = self.put_peppersd)
        self.button_seed_package_eggplant = tk.Button(r1, image = self.image_seed_package_eggplant, command = self.put_eggplantsd)
        self.button_seed_package_coriander = tk.Button(r1, image = self.image_seed_package_coriander, command = self.put_coriandersd)

        # grid 上去
        #sticky = tk.N+tk.S
        # columnspan = 2, rowspan = 2,
        self.button_seed_package_pepper.grid(row = 5, column = 1, columnspan = 2, rowspan = 2, sticky = tk.NE + tk.SW, padx = 50, pady = 50)
        self.button_seed_package_eggplant.grid(row = 5, column = 3, columnspan = 2, rowspan = 2, sticky = tk.NE + tk.SW, padx = 50, pady = 50)
        self.button_seed_package_coriander.grid(row = 5, column = 5, columnspan = 2, rowspan = 2, sticky = tk.NE + tk.SW, padx = 50, pady = 50)
        lab1 = tk.Label(r1, text='青椒種子', height=1, width=15, bg='white', fg='black')
        lab1.grid(row=7, column=1, sticky = tk.NE + tk.SW, padx = 50, pady = 10)
        lab2 = tk.Label(r1, text='茄子種子', height=1, width=15, bg='white', fg='black')
        lab2.grid(row=7, column=3, sticky = tk.NE + tk.SW, padx = 50, pady = 10)
        lab3 = tk.Label(r1, text='香菜種子', height=1, width=15, bg='white', fg='black')
        lab3.grid(row=7, column=5, sticky = tk.NE + tk.SW, padx = 50, pady = 10)


    # 種子商店功能-青椒種子
    def put_peppersd(self):
        self.seeded  = True
        self.Timer()
        self.target = "pepper"  
        self.empty_pot_label.destroy()
        self.image_pot_with_seed_label.grid(row = 0,column = 0,columnspan = 5)

    # 種子商店功能-茄子種子
    def put_eggplantsd(self): 
        self.seeded = True
        self.Timer()
        self.target = "eggplant"
        self.empty_pot_label.destroy()
        self.image_pot_with_seed_label.grid(row = 0,column = 0,columnspan = 5)

    # 種子商店功能-香菜種子
    def put_coriandersd(self):
        self.seeded = True
        self.Timer()
        self.target = "coriander"  # 設立target
        self.empty_pot_label.destroy()
        self.image_pot_with_seed_label.grid(row = 0,column = 0,columnspan = 5)
     
    # 圖鑑功能
    def click_button_book(self):
        # 產生視窗
        illustrated_book = tk.Toplevel()
        illustrated_book.title('illustration_book')
        illustrated_book.geometry('800x600')

        # 產生label
        big_coriander_label = tk.Label(illustrated_book, image = self.image_big_coriander_ill)
        big_pepper_label = tk.Label(illustrated_book, image = self.image_big_pepper_ill)
        big_eggplant_label = tk.Label(illustrated_book, image = self.image_big_eggplant_ill)
        amount_coriander_label = tk.Label(illustrated_book, text = self.amount['coriander'], font=('TkDefaultFont', 20))
        amount_pepper_label = tk.Label(illustrated_book, text = self.amount['pepper'], font=('TkDefaultFont', 20))
        amount_eggplant_label = tk.Label(illustrated_book, text = self.amount['eggplant'], font=('TkDefaultFont', 20))

        # grid
        big_coriander_label.grid(row = 1, column = 3)
        big_pepper_label.grid(row = 1, column = 1)
        big_eggplant_label.grid(row = 1, column = 2)
        amount_coriander_label.grid(row = 3, column = 3)
        amount_pepper_label.grid(row = 3, column = 1)
        amount_eggplant_label.grid(row = 3, column = 2)
        
        # 標示圖片下文字說明
        lab11 = tk.Label(illustrated_book, text='青椒', height=1, width=15, bg='white', fg='black')
        lab11.grid(row=2, column=1)
        lab22 = tk.Label(illustrated_book, text='茄子', height=1, width=15, bg='white', fg='black')
        lab22.grid(row=2, column=2)
        lab33 = tk.Label(illustrated_book, text='香菜', height=1, width=15, bg='white', fg='black')
        lab33.grid(row=2, column=3)

    # 採收功能
    def click_button_harvest(self):
        # 產生澆水鍵，消除採收鍵     
        self.button_harvest.destroy()
        self.button_harvest = tk.Button(self, image = self.image_hoe, command = self.click_button_harvest)


        # destroy 大植物
        if self.target == "coriander":
            self.big_coriander_label.destroy()        
        if self.target == "eggplant":
            self.big_eggplant_label.destroy()               
        if self.target == "pepper":
            self.big_pepper_label.destroy()

        self.createWidgets()
        self.button_waterer.grid(row = 1, column = 2)

        self.amount[self.target] += 1
        self.empty_pot_label.grid(row = 0, column = 0, columnspan = 5)
        self.level = 0
        self.seeded = False



    # 澆水器功能（完成）
    def click_button_waterer(self):
        if not self.seeded:
            tk.messagebox.showerror('尚未選擇種子','你的盆栽是空的....\n去種子商店選一種種子吧！')
            return
        if not self.Timer_ended:
            tk.messagebox.showerror('大哥你別急','下次澆水的時間還沒到喔...\n再耐心等等吧！')
            return
        a = ""
        target = self.target
        self.pas = "no"
        if self.level == 0:
            #   小問題請改以下三行
            a = tk.messagebox.askquestion("確認","捷運中有哪一條線有經過台北車站？(答案:紅線)")
            print("a", a)
            if a == "yes":
                self.Timer()
            
                if target == "coriander":
                    self.image_pot_with_seed_label.destroy()
                    self.small_coriander_label.grid(row = 0,column = 0,columnspan = 5)
                    
                if target == "eggplant":
                    self.image_pot_with_seed_label.destroy()
                    self.small_eggplant_label.grid(row = 0,column = 0,columnspan = 5)
                       
                if target == "pepper":
                    self.image_pot_with_seed_label.destroy()
                    self.small_pepper_label.grid(row = 0,column = 0,columnspan = 5)
                    
                self.pas = "yes"

        if self.level == 1:
            # 小問題請改以下三行
            a = tk.messagebox.askquestion("確認","哪一個不是韓國三大經紀公司？(答案：Woollim)")
            print("a", a)
            if a == "yes":
                self.Timer()
            
                if target == "coriander":
                    self.small_coriander_label.destroy()
                    self.mid_coriander_label.grid(row = 0,column = 0,columnspan = 5)
                    
                if target == "eggplant":
                    self.small_eggplant_label.destroy()
                    self.mid_eggplant_label.grid(row = 0,column = 0,columnspan = 5)
                       
                if target == "pepper":
                    self.small_pepper_label.destroy()
                    self.mid_pepper_label.grid(row = 0,column = 0,columnspan = 5)
                    
                self.pas = "yes"
            
        
        if self.level == 2:
            #   小問題請改以下三行
            a = tk.messagebox.askquestion("確認","3 x 5 = 15 ?")
            print("a", a)
            if a == "yes":
                if target == "coriander":
                    self.mid_coriander_label.destroy()
                    self.big_coriander_label.grid(row = 0, column = 0,columnspan = 5)
                    
                if target == "eggplant":
                    self.mid_eggplant_label.destroy()
                    self.big_eggplant_label.grid(row = 0, column = 0,columnspan = 5)
                       
                if target == "pepper":
                    self.mid_pepper_label.destroy()
                    self.big_pepper_label.grid(row = 0, column = 0,columnspan = 5)
                    
                self.pas = "yes"
                self.button_waterer.destroy()   # 澆水器消失，看要不要改
                self.button_harvest.grid(row = 1, column = 2)

                
        if self.pas == "yes":
            self.level += 1




# 主程式
game = Farm()
game.master.title("PBC Farm")
game.mainloop()







''' 
如果要用resize的話，路徑再改，還有size再變動
def createWidgets(self):
# 匯入圖片的部分寫這邊self.image_ = ImageTk.PhotoImage(file = 'graph/.png')  # 

#image = Image.open('E:\\importan\\python\\202012_project_JULIA\\graph\\rug2.PNG')
#image = image.resize((250, 250), Image.ANTIALIAS) ## The (250, 250) is (height, width)
#self.image_bg = ImageTk.PhotoImage(image)  # 背景圖片
self.image_bg = ImageTk.PhotoImage(file = 'E:\\importan\\python\\202012_project_JULIA\\graph\\rug2.PNG')  # 背景圖片

image = Image.open('E:\\importan\\python\\202012_project_JULIA\\graph\\waterer.PNG')
image = image.resize((80, 60), Image.ANTIALIAS) ## The (250, 250) is (height, width)
self.image_waterer = ImageTk.PhotoImage(image)  # waterer

self.image_small_pepper = ImageTk.PhotoImage(file = 'E:\\importan\\python\\202012_project_JULIA\\graph\\small_pepper.PNG')  # small_pepper
self.image_small_eggplant = ImageTk.PhotoImage(file = 'E:\\importan\\python\\202012_project_JULIA\\graph\\small_eggplant.PNG')  # small_eggplant

image = Image.open('E:\\importan\\python\\202012_project_JULIA\\graph\\small_coriander.PNG')
image = image.resize((80, 60), Image.ANTIALIAS) ## The (250, 250) is (height, width)
self.image_small_coriander = ImageTk.PhotoImage(image)  # small_coriander

image = Image.open('E:\\importan\\python\\202012_project_JULIA\\graph\\seedstore_icon.png')
image = image.resize((80, 60), Image.ANTIALIAS) ## The (250, 250) is (height, width)
self.image_seedstore_icon = ImageTk.PhotoImage(image)  # seedstore_icon

self.image_seed_pepper = ImageTk.PhotoImage(file = 'E:\\importan\\python\\202012_project_JULIA\\graph\\seed_pepper.PNG')  # seed_pepper
self.image_seed_package_pepper = ImageTk.PhotoImage(file = 'E:\\importan\\python\\202012_project_JULIA\\graph\\seed_package_pepper.PNG')  # seed_package_pepper
self.image_seed_package_eggplant = ImageTk.PhotoImage(file = 'E:\\importan\\python\\202012_project_JULIA\\graph\\seed_package_eggplant.PNG')  # seed_package_eggplant
self.image_seed_package_coriander = ImageTk.PhotoImage(file = 'E:\\importan\\python\\202012_project_JULIA\\graph\\seed_package_coriander.PNG')  # seed_package_coriander
self.image_seed_eggplant = ImageTk.PhotoImage(file = 'E:\\importan\\python\\202012_project_JULIA\\graph\\seed_eggplant.PNG')  # seed_eggplant
self.image_seed_coriander = ImageTk.PhotoImage(file = 'E:\\importan\\python\\202012_project_JULIA\\graph\\seed_coriander.PNG')  # seed_coriander
self.image_mid_pepper = ImageTk.PhotoImage(file = 'E:\\importan\\python\\202012_project_JULIA\\graph\\mid_pepper.PNG')  # mid_pepper
self.image_mid_eggplant = ImageTk.PhotoImage(file = 'E:\\importan\\python\\202012_project_JULIA\\graph\\mid_eggplant.PNG')  # mid_eggplant

image = Image.open('E:\\importan\\python\\202012_project_JULIA\\graph\\mid_coriander.PNG')
image = image.resize((80, 60)) ## The (250, 250) is (height, width)
self.image_mid_coriander = ImageTk.PhotoImage(image)  # mid_coriander

image = Image.open('E:\\importan\\python\\202012_project_JULIA\\graph\\empty_pot.PNG')
image = image.resize((80, 60)) ## The (250, 250) is (height, width)
self.image_empty_pot = ImageTk.PhotoImage(image)  # empty_pot


image = Image.open('E:\\importan\\python\\202012_project_JULIA\\graph\\book_icon.png')
image = image.resize((80, 60), Image.ANTIALIAS) ## The (250, 250) is (height, width)
self.image_book_icon = ImageTk.PhotoImage(image)  # book_icon

self.image_book = ImageTk.PhotoImage(file = 'E:\\importan\\python\\202012_project_JULIA\\graph\\book.png')  # book
self.image_big_eggplant = ImageTk.PhotoImage(file = 'E:\\importan\\python\\202012_project_JULIA\\graph\\big_eggplant.PNG')  # big_eggplant
self.image_big_pepper = ImageTk.PhotoImage(file = 'E:\\importan\\python\\202012_project_JULIA\\graph\\big_pepper.PNG')  # big_pepper

image = Image.open('E:\\importan\\python\\202012_project_JULIA\\graph\\big_coriander.png')
image = image.resize((80, 60), Image.ANTIALIAS) ## The (250, 250) is (height, width)
self.image_big_coriander = ImageTk.PhotoImage(image)  # big_coriander

self.image_back_icon_name = ImageTk.PhotoImage(file = 'E:\\importan\\python\\202012_project_JULIA\\graph\\back_icon_name.png')  # back_icon_name

image = Image.open('E:\\importan\\python\\202012_project_JULIA\\graph\\back_icon.png')
image = image.resize((80, 60), Image.ANTIALIAS) ## The (250, 250) is (height, width)
self.image_back_icon = ImageTk.PhotoImage(image)  # back_icon

self.image_conversation = ImageTk.PhotoImage(file = 'E:\\importan\\python\\202012_project_JULIA\\graph\\conversation.PNG')  # conversation 種子對話框
'''
