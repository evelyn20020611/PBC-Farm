from PIL import ImageTk
from PIL import Image   # 如果要用resize的話
import tkinter as tk
import tkinter.font as tkFont
from PIL import Image
import tkinter.messagebox #這個是訊息框，對話方塊的關鍵

class Farm(tk.Frame):  # try
    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()  # 產生網格
        self.createWidgets()
        self.level = 0
        self.pas = "no"
        self.target = ""

    def createWidgets(self):
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


        #self.image_seedstore_icon = self.image_seedstore_icon.resize((80,60),Image.ANTIALIAS)
        ''' 如果要用resize的話，路徑再改，還有size再變動
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
        

        # 產生label的部分寫這邊
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

        # 產生button 的部分寫這邊
        self.button_book = tk.Button(self, image=self.image_book_icon, command = self.click_button_book)
        self.button_seedstore = tk.Button(self, image=self.image_seedstore_icon, command = self.open_store)
        self.button_waterer = tk.Button(self, image = self.image_waterer, command = self.click_button_waterer)

        
        # 初始grid 的部分寫這邊
        self.empty_pot_label.grid(row = 0, column = 0, columnspan = 3)


        # grid 的部分寫這邊
        self.button_seedstore.grid(row = 1, column = 0)
        self.button_waterer.grid(row = 1, column = 1)
        self.button_book.grid(row = 1, column = 2)

 
        '''
        # grid 的部分寫這邊_修改後的
        self.background_label.grid(row = 0, column = 0, columnspan = 10, rowspan = 11)
        self.button_back.grid(row = 1, column = 0)
        self.button_book.grid(row = 8, column = 0)
        self.button_seedstore.grid(row = 9, column = 0)
        self.button_waterer.grid(row = 10, column = 5)
        '''
 
        
    # 種子商店
    def open_store(self): # 點了種子商店按鈕後的function
        # 產生視窗
        seed_store = tk.Tk()
        seed_store.title('Seed Store')
        seed_store.geometry('500x300')

        # 產生button
        button_seed_pepper = tk.Button(master = seed_store, image = self.image_seed_package_pepper , command = self.put_peppersd)
        button_seed_eggplant = tk.Button(master = seed_store, text = '2', command = self.put_eggplantsd)
        button_seed_coriander = tk.Button(master = seed_store, text = '3', command = self.put_eggplantsd)

        # grid 上去
        button_seed_pepper.grid(row = 0, column = 0)
        button_seed_eggplant.grid(row = 0, column = 1)
        button_seed_coriander.grid(row = 0, column = 2)


    def put_peppersd(self):
        self.target = "pepper"  # 設立target
                                # 放置pot with seed

    def put_eggplantsd(self): 
        self.target = "eggplant"

    def put_coriandersd(self):
        self.target = "coriander"


                

    # 圖鑑功能
    def click_button_book(self):
        illustrated_book = tk.Tk()
        illustrated_book.title('illustrated_book')
        illustrated_book.geometry('500x300')

        self.image_big_coriander.grid(row = 1, column = 0)
        self.image_big_eggplant.grid(row = 1, column = 1)
        self.image_big_pepper.grid(row = 1, column = 2)



    # 澆水器功能
    def click_button_waterer(self):
        a = ""
        target = "coriander"
        self.pas = "no"
        if self.level == 0:
            #   小問題請改以下三行
            a = tk.messagebox.askquestion("確認","捷運中有哪一條線有經過台北車站？(答案:紅線)")
            print("a", a)
            if a == "yes":
            
                if target == "coriander":
                    self.background_label.destroy()
                    self.small_coriander_label.grid(row = 0,column = 0,columnspan = 5)
                    
                if target == "eggplant":
                    self.empty_pot_label.destroy()
                    self.small_eggplant_label.grid(row = 0,column = 0,columnspan = 5)
                       
                if target == "pepper":
                    self.empty_pot_label.destroy()
                    self.small_pepper_label.grid(row = 0,column = 0,columnspan = 5)
                    
                self.pas = "yes"

        if self.level == 1:
            #   小問題請改以下三行
            a = tk.messagebox.askquestion("確認","哪一個不是韓國三大經紀公司？(答案：Woollim)")
            print("a", a)
            if a == "yes":
            
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
                    self.big_coriander_label.grid(row = 0,column = 0,columnspan = 5)
                    
                if target == "eggplant":
                    self.mid_eggplant_label.destroy()
                    self.big_eggplant_label.grid(row = 0,column = 0,columnspan = 5)
                       
                if target == "pepper":
                    self.mid_pepper_label.destroy()
                    self.big_pepper_label.grid(row = 0,column = 0,columnspan = 5)
                    
                self.pas = "yes"
                self.button_waterer.destroy()   # 澆水器消失，看要不要改
                
                
        if self.pas == "yes":
            self.level += 1


game = Farm()
game.master.title("PBC Farm")
game.mainloop()
