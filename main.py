from PIL import ImageTk
from PIL import Image   # 如果要用resize的話
import tkinter as tk
import tkinter.font as tkFont
from PIL import Image
import tkinter.messagebox #這個是訊息框，對話方塊的關鍵
import time
import json
import random

class Farm(tk.Frame):  # try
    def __init__(self):
        tk.Frame.__init__(self)
        self.amount = {}
        self.pas = "no"
        self.Timer_ended = True
        self.seeded = False
        self.amount = {'coriander':0,'eggplant':0,'pepper':0}
        self.level = 0
        self.target = ""
        self.timer_label = tk.Label(text="0", font=('Helvetica', 48), fg='black')
        self.grid()  # 產生網格
        self.createImages()
        self.createWidgets()
        self.init_grid()
        self.read_data()
        self.question_libary()


    def read_data(self):
        with open('init_data.json', 'r') as f:
            data = json.load(f)
        self.amount['coriander'] = data[0]
        self.amount['eggplant'] = data[1]
        self.amount['pepper'] = data[2]

    # 計時器
    def Timer(self):
        self.Timer_ended = False
        self.start_time = time.time()
        self.end_time = self.start_time + 8
        self.update_clock()

    # 每秒更新計時器
    def update_clock(self):
        self.now = int(self.end_time - time.time())
        if self.now < 0:
            self.Timer_ended = True
            return
        self.timer_label.configure(text=self.now)
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
        self.image_pot_with_seed = ImageTk.PhotoImage(file = 'graph/pot_with_seed.png')  # pot_with_seed
        self.image_big_coriander_ill = ImageTk.PhotoImage(file = 'graph/big_coriander_ill.png')
        self.image_big_pepper_ill = ImageTk.PhotoImage(file = 'graph/big_pepper_ill.png')
        self.image_big_eggplant_ill = ImageTk.PhotoImage(file = 'graph/big_eggplant_ill.png')
        self.image_hoe = ImageTk.PhotoImage(file = 'graph/hoe.png')  # hoe 鋤頭
        self.image_letschat = ImageTk.PhotoImage(file = 'graph/letschat.jpg')  # letschat
        self.image_1_eggplant = ImageTk.PhotoImage(file = 'graph/1_eggplant.jpg')  # 1.eggplant 
        self.image_2_eggplant = ImageTk.PhotoImage(file = 'graph/2_eggplant.jpg')  # 2.eggplant

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
        self.image_letschat_label = tk.Label(self,image=self.image_letschat)  # 產生self.image_letschat
        self.image_1_eggplant_label = tk.Label(self,image=self.image_1_eggplant)  # 產生self.image_1.eggplant
        self.image_2_eggplant_label = tk.Label(self,image=self.image_2_eggplant)  # 產生self.image_2.eggplant


        # 產生button 的部分寫這邊
        self.button_book = tk.Button(self, image=self.image_book_icon, command = self.click_button_book)
        self.button_seedstore = tk.Button(self, image=self.image_seedstore_icon, command = self.open_store)
        self.button_waterer = tk.Button(self, image = self.image_waterer, command = self.click_button_waterer)
        self.button_harvest = tk.Button(self, image = self.image_hoe, command = self.click_button_harvest)
        self.button_save = tk.Button(self, text = "儲存進度", command = self.click_button_save)
        
         # 標示圖片下文字說明
        labe1_button_seedstore = tk.Label(self, text='種子商店', height=1, width=15, bg='white', fg='black')
        labe1_button_seedstore.grid(row = 9, column = 1, sticky=(tk.S,tk.W))
        label_button_waterer = tk.Label(self, text='澆水器', height=1, width=15, bg='white', fg='black')
        label_button_waterer.grid(row = 9, column = 5, sticky=(tk.S,tk.W))
        label_button_book = tk.Label(self, text='蔬菜圖鑑', height=1, width=15, bg='white', fg='black')
        label_button_book.grid(row = 9, column = 9, sticky=(tk.S,tk.W))
        

    def init_grid(self):
        # 初始grid 的部分寫這邊
        self.button_seedstore.grid(row = 1, column = 0)
        self.button_waterer.grid(row = 1, column = 2)
        self.button_book.grid(row = 1, column = 4)
        self.timer_label.grid(row = 2, column = 0, columnspan = 5)
        self.button_save.grid(row = 3, column = 0, columnspan = 5)
        self.empty_pot_label.grid(row = 0, column = 0, columnspan = 5)

        self.button_seedstore.grid(row = 10, column = 1, sticky=(tk.W))
        self.button_waterer.grid(row = 10, column = 5, sticky=(tk.W))
        self.button_book.grid(row = 10, column = 9, sticky=(tk.W))
        self.timer_label.grid(row = 0, column = 0, sticky=(tk.W))
        self.button_save.grid(row = 0, column = 5)

        self.empty_pot_label.grid(row = 0, column = 0, rowspan = 10, columnspan = 11)



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
        self.button_seed_package_pepper.grid(row = 5, column = 1, padx = 50, pady = 90)
        self.button_seed_package_eggplant.grid(row = 5, column = 3, padx = 50, pady = 90)
        self.button_seed_package_coriander.grid(row = 5, column = 5, padx = 50, pady = 90)
        lab1 = tk.Label(r1, text='青椒種子', height=2, width=15, bg='white', fg='black')
        lab1.grid(row=7, column=1, padx = 90, ipadx = 10, ipady = 10)
        lab2 = tk.Label(r1, text='茄子種子', height=2, width=15, bg='white', fg='black')
        lab2.grid(row=7, column=3, padx = 90, ipadx = 10, ipady = 10)
        lab3 = tk.Label(r1, text='香菜種子', height=2, width=15, bg='white', fg='black')
        lab3.grid(row=7, column=5, padx = 90, ipadx = 10, ipady = 10)
        
        #if self.seeded is True:
            #r1.destroy()
        

    # 種子商店功能-青椒種子
    def put_peppersd(self):
        self.seeded  = True
        self.target = "pepper"  
        self.empty_pot_label.destroy()
        self.image_pot_with_seed_label.grid(row = 0,column = 0, rowspan = 10, columnspan = 11)
        tk.messagebox.showwarning('小提示','種植成功！\n記得關掉種子商店視窗唷')
        
    # 種子商店功能-茄子種子
    def put_eggplantsd(self): 
        self.seeded = True
        self.target = "eggplant"
        self.empty_pot_label.destroy()
        self.image_pot_with_seed_label.grid(row = 0,column = 0, rowspan = 10, columnspan = 11)
        tk.messagebox.showwarning('小提示','種植成功！\n記得關掉種子商店視窗唷')
         
    # 種子商店功能-香菜種子
    def put_coriandersd(self):
        self.seeded = True
        self.target = "coriander"  # 設立target
        self.empty_pot_label.destroy()
        self.image_pot_with_seed_label.grid(row = 0,column = 0, rowspan = 10, columnspan = 11)
        tk.messagebox.showwarning('小提示','種植成功！\n記得關掉種子商店視窗唷')
         
    # 圖鑑功能
    def click_button_book(self):
        # 產生視窗
        illustrated_book = tk.Toplevel()
        illustrated_book.title('蔬菜圖鑑')
        illustrated_book.geometry('800x600')

        # 產生label
        big_coriander_label = tk.Label(illustrated_book, image = self.image_big_coriander_ill)
        big_pepper_label = tk.Label(illustrated_book, image = self.image_big_pepper_ill)
        big_eggplant_label = tk.Label(illustrated_book, image = self.image_big_eggplant_ill)
        amount_coriander_label = tk.Label(illustrated_book, text = self.amount['coriander'], font=('TkDefaultFont', 20))
        amount_pepper_label = tk.Label(illustrated_book, text = self.amount['pepper'], font=('TkDefaultFont', 20))
        amount_eggplant_label = tk.Label(illustrated_book, text = self.amount['eggplant'], font=('TkDefaultFont', 20))

        # grid
        big_coriander_label.grid(row = 1, column = 3, padx = 25,pady = 30)
        big_pepper_label.grid(row = 1, column = 1, padx = 25,pady = 30)
        big_eggplant_label.grid(row = 1, column = 2, padx = 25,pady = 30)
        amount_coriander_label.grid(row = 3, column = 3, padx = 25,pady = 30)
        amount_pepper_label.grid(row = 3, column = 1, padx = 25,pady = 30)
        amount_eggplant_label.grid(row = 3, column = 2, padx = 25,pady = 30)
        
        # 標示圖片下文字說明
        lab11 = tk.Label(illustrated_book, text='青椒', height=1, width=15, bg='white', fg='black')
        lab11.grid(row=2, column=1)
        lab22 = tk.Label(illustrated_book, text='茄子', height=1, width=15, bg='white', fg='black')
        lab22.grid(row=2, column=2)
        lab33 = tk.Label(illustrated_book, text='香菜', height=1, width=15, bg='white', fg='black')
        lab33.grid(row=2, column=3)
                # 青椒
        easy_or_not1 = tk.Label(illustrated_book, text='噁心程度', height=1, width=15, bg='white', fg='black')
        easy_or_not1.grid(row=4, column=1)
        easy_or_not11 = tk.Label(illustrated_book, text='★\n', height=2, width=15, font=('TkDefaultFont', 20), fg='yellow')
        easy_or_not11.grid(row=5, column=1)
        characteristic1 = tk.Label(illustrated_book, text='特色', height=1, width=15, bg='white', fg='black')
        characteristic1.grid(row=6, column=1)
        characteristic11 = tk.Label(illustrated_book, text='小孩子都不會吃', height=1, width=15, bg='white', fg='black')
        characteristic11.grid(row=7, column=1)
        characteristic111 = tk.Label(illustrated_book, text='害羞又靦腆的Big Girl', height=1, width=15, bg='white', fg='black')
        characteristic111.grid(row=8, column=1)
        # 台詞:
        # 那個><不要害怕吃我嘛…我很營養健康的說！
        # 茄子
        easy_or_not2 = tk.Label(illustrated_book, text='噁心程度', height=1, width=15, bg='white', fg='black')
        easy_or_not2.grid(row=4, column=2)
        easy_or_not22 = tk.Label(illustrated_book, text='★★★\n', height=2, width=15, font=('TkDefaultFont', 20), fg='yellow')
        easy_or_not22.grid(row=5, column=2)
        characteristic2 = tk.Label(illustrated_book, text='特色', height=1, width=15, bg='white', fg='black')
        characteristic2.grid(row=6, column=2)
        characteristic22 = tk.Label(illustrated_book, text='食物界的恥辱', height=1, width=15, bg='white', fg='black')
        characteristic22.grid(row=7, column=2)
        characteristic222 = tk.Label(illustrated_book, text='講話結巴又台灣國語的小胖', height=1, width=20, bg='white', fg='black')
        characteristic222.grid(row=8, column=2)
        # 台詞:
        # 喂…那、那邊那個帥、帥哥，不要看我這樣，偶是本屆紫色食物PK中奪得「金拍甲」冠軍餒。

        # 香菜
        easy_or_not3 = tk.Label(illustrated_book, text='噁心程度', height=1, width=15, bg='white', fg='black')
        easy_or_not3.grid(row=4, column=3)
        easy_or_not33 = tk.Label(illustrated_book, text='★★★★★\n', height=2, width=15, font=('TkDefaultFont', 20), fg='yellow')
        easy_or_not33.grid(row=5, column=3)
        characteristic3 = tk.Label(illustrated_book, text='特色', height=1, width=15, bg='white', fg='black')
        characteristic3.grid(row=6, column=3)
        characteristic33 = tk.Label(illustrated_book, text='備受唾棄的噁心東東', height=1, width=15, bg='white', fg='black')
        characteristic33.grid(row=7, column=3)
        characteristic333 = tk.Label(illustrated_book, text='窈窕潑辣的大正妹', height=1, width=15, bg='white', fg='black')
        characteristic333.grid(row=8, column=3)
        # 台詞:
        # 是小鮮肉耶~~~姊姊偷偷告訴你，白飯佐香菜很讚啊嘶~快來跟姊姊炒飯~~/////

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
        self.button_waterer.grid(row = 10, column = 5, sticky=(tk.W))

        self.amount[self.target] += 1
        self.empty_pot_label.grid(row = 0, column = 0, rowspan = 10, columnspan = 11)
        self.level = 0
        self.seeded = False
        self.Timer_ended = True



    # 澆水器功能（完成）
    def click_button_waterer(self):
        ranQ = self.ran_question()
        if not self.seeded:
            tk.messagebox.showerror('尚未選擇種子','你的盆栽是空的....\n去種子商店選一種種子吧！')
            return
        if not self.Timer_ended:
            tk.messagebox.showerror('大哥你別急','下次澆水的時間還沒到喔...\n還有%s秒鐘，再等等吧！'%(self.now))
            return
        a = ""
        target = self.target
        self.pas = "no"
        if self.level == 0:
            a = tk.messagebox.askquestion("澆水小問題",ranQ)
            print("a", a)
            if a == self.question_libary[ranQ]:
                self.Timer()
            
                if target == "coriander":
                    self.image_pot_with_seed_label.destroy()
                    self.small_coriander_label.grid(row = 0,column = 0, rowspan = 10, columnspan = 11)
                    
                if target == "eggplant":
                    self.image_pot_with_seed_label.destroy()
                    self.small_eggplant_label.grid(row = 0,column = 0, rowspan = 10, columnspan = 11)
                       
                if target == "pepper":
                    self.image_pot_with_seed_label.destroy()
                    self.small_pepper_label.grid(row = 0,column = 0, rowspan = 10, columnspan = 11)
                    
                self.pas = "yes"
            else:
                tk.messagebox.showerror('答錯了','學海無涯，回頭是岸')

        if self.level == 1:
            a = tk.messagebox.askquestion("澆水小問題",ranQ)
            print("a", a)
            if a == self.question_libary[ranQ]:
                self.Timer()
                if target == "coriander":
                    self.small_coriander_label.destroy()
                    self.mid_coriander_label.grid(row = 0,column = 0, rowspan = 10, columnspan = 11)
                    
                if target == "eggplant":
                    self.small_eggplant_label.destroy()
                    self.mid_eggplant_label.grid(row = 0,column = 0, rowspan = 10, columnspan = 11)
                       
                if target == "pepper":
                    self.small_pepper_label.destroy()
                    self.mid_pepper_label.grid(row = 0,column = 0, rowspan = 10, columnspan = 11)
                    
                self.pas = "yes"
            else:
                tk.messagebox.showerror('答錯了','學海無涯，回頭是岸')
            
        
        if self.level == 2:
            #   小問題請改以下三行
            a = tk.messagebox.askquestion("澆水小問題",ranQ)
            if a == self.question_libary[ranQ]:
                if target == "coriander":
                    self.mid_coriander_label.destroy()
                    self.big_coriander_label.grid(row = 0, column = 0, rowspan = 10, columnspan = 11)
                    
                if target == "eggplant":
                    self.mid_eggplant_label.destroy()
                    self.big_eggplant_label.grid(row = 0, column = 0, rowspan = 10, columnspan = 11)
                       
                if target == "pepper":
                    self.mid_pepper_label.destroy()
                    self.big_pepper_label.grid(row = 0, column = 0, rowspan = 10, columnspan = 11)
                    
                self.pas = "yes"
                self.button_waterer.destroy()   # 澆水器消失，看要不要改
                self.button_harvest.grid(row = 10, column = 5, sticky=(tk.W))

            else:
                tk.messagebox.showerror('答錯了','學海無涯，回頭是岸')

                
        if self.pas == "yes":
            self.level += 1

    def click_button_save(self):
        a = tkinter.messagebox.askquestion(title="儲存遊戲", message="請問要儲存進度嗎？")
        with open("init_data.json","w") as f:
            json.dump([self.amount['coriander'],self.amount['eggplant'],self.amount['pepper'],self.level,self.target], f)


    def ran_question(self):
        ran_question = random.choice(list(self.question_libary))
        return ran_question

    def question_libary(self):
        self.question_libary = {"天空是藍色的": "yes","草是綠色的":"yes","在假設通貨膨脹的情況下，用Average cost這種算存貨的方法才能繳比較少的稅":"yes",
                    "捷運的綠線有經過台北車站":"no" ,"int是種可變的物件":"no",'香菜很好吃':'yes','孔令傑是商管程式設計這門課的老師':'yes','商管程式設計歷年來的平均停修率為20%':'yes',
                    '商管程助教影片常用(各位同學早安午安晚安)開頭':'yes','這個遊戲叫做傳說對決':'no','商管程每周作業都在周一早上9:00截止':'no',
                    '香菜可以治嘔吐':'yes','我吃麵一定會把香菜挑起來':'no','遛狗的英文為slide the dog':'no',
                    '香菜可以避免宿醉':'yes','達達主義盛於一次世界大戰期間':'yes','小說百年孤寂是描述中美洲的故事':'no',
                    '維克多·雨果是小說罪與罰的作者':'no','杜斯妥也夫斯基是小說戰爭與和平的作者':'no','俄國文豪托爾斯泰未曾得到諾貝爾獎':'yes',
                    '我去吃自助餐的時候一定會吃茄子':'yes','':'','查拉圖斯特拉如是說是華格納的作品':'no',
                    '西線無戰事是海明威的作品':'no','我每個禮拜都有認真寫商管程的作業':'yes','柏拉圖是亞里斯多德的學生':'no','希臘三哲包含柏拉圖、蘇格拉底、亞里斯多德':'yes',
                    '把香菜挑起來是一件好事':'no','神聖羅馬帝國的首都是羅馬':'no','銷貨成本的英文簡寫是COGS':'yes',
                    '美式咖啡是義式濃縮加水':'yes','吉利馬札羅是著名的咖啡產地':'yes'
        
                    }







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
