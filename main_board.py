import tkinter as tk
from tkinter import ttk
import server
from tkinter import messagebox

wordfont= ('Arial', 12)
classfont=('Arial', 18, "bold")

class RecordBoard(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry('1000x600')
        self.title("記分板板")
        menu_frame = tk.Frame(self)
        menu_frame.pack(side=tk.TOP)
        object_frame = tk.Frame(self)
        object_frame.pack()
        object_frame2 = tk.Frame(self)
        object_frame2.pack()

        def page_playerdata(): #球員數據頁面 我打好了
            def clean_smallframe(): #清空小frame裡的物件
                for widget in playerinfo_frame1.winfo_children():
                    widget.destroy()
                for widget in playerinfo_frame2.winfo_children():
                    widget.destroy()
                for widget in playerinfo_frame3.winfo_children():
                    widget.destroy()

            def callbackFunc(event): #處理下拉式選單選取要顯示的資訊
                clean_smallframe() #清除原本的東西
                infomat=combo.get()
                infomat = infomat.split(' ') #擷取學號
                data1 = server.player_info(infomat[0])
                tk.Label(playerinfo_frame1,text="姓名", font=wordfont).grid(row=0,column=0)
                tk.Label(playerinfo_frame1,text="背號", font=wordfont).grid(row=0,column=1)
                tk.Label(playerinfo_frame1,text="入隊學年", font=wordfont).grid(row=0,column=2)
                tk.Label(playerinfo_frame1,text="退隊學年", font=wordfont).grid(row=0,column=3)
                tk.Label(playerinfo_frame1,text="隊長", font=wordfont).grid(row=0,column=4)
                tk.Label(playerinfo_frame1,text="上場次數", font=wordfont).grid(row=0,column=5)
                for i in range(1,7):
                    if(data1[0][i] == None):
                        tk.Label(playerinfo_frame1,text="無", font=wordfont).grid(row=1,column=i-1)
                    else:
                        tk.Label(playerinfo_frame1,text=data1[0][i], font=wordfont).grid(row=1,column=i-1)

                data2 = server.player_data_average(infomat[0])
                tk.Label(playerinfo_frame2,text="得分率", font=wordfont).grid(row=0,column=0)
                tk.Label(playerinfo_frame2,text="進攻籃板率", font=wordfont).grid(row=0,column=1)
                tk.Label(playerinfo_frame2,text="防守籃板率", font=wordfont).grid(row=0,column=2)
                tk.Label(playerinfo_frame2,text="助攻率", font=wordfont).grid(row=0,column=3)
                tk.Label(playerinfo_frame2,text="阻攻率", font=wordfont).grid(row=0,column=4)
                tk.Label(playerinfo_frame2,text="抄截率", font=wordfont).grid(row=0,column=5)
                tk.Label(playerinfo_frame2,text="犯規率", font=wordfont).grid(row=0,column=6)
                tk.Label(playerinfo_frame2,text="失誤率", font=wordfont).grid(row=0,column=7)
                if(data2 == ()): #還沒打好
                    tk.Label(playerinfo_frame2,text="還沒上場過", font=wordfont).grid(row=1,column=3)
                else:
                    for i in range(1,9):
                        if(data2[0][i+2]==None):
                            tk.Label(playerinfo_frame2,text="無", font=wordfont).grid(row=1,column=i-1)
                        else:
                            tk.Label(playerinfo_frame2,text=data2[0][i+2], font=wordfont).grid(row=1,column=i-1)

                data3 = server.player_hit_rate(infomat[0])
                tk.Label(playerinfo_frame3,text="三分球命中率", font=wordfont).grid(row=0,column=0)
                tk.Label(playerinfo_frame3,text="投籃命中率", font=wordfont).grid(row=0,column=1)
                tk.Label(playerinfo_frame3,text="罰球命中率", font=wordfont).grid(row=0,column=2)
                if(data3 == ()):
                    tk.Label(playerinfo_frame3,text="還沒上場過", font=wordfont).grid(row=1,column=1)
                else:
                    for i in range(1,4):
                        if(data3[0][i+2] == None):
                            tk.Label(playerinfo_frame3,text="目前還沒有表現", font=wordfont).grid(row=1,column=i-1)
                        else:
                            tk.Label(playerinfo_frame3,text=data3[0][i+2], font=wordfont).grid(row=1,column=i-1)
            
            tk.Label(object_frame,text="球員數據", font=classfont).grid(row=0, column=1)
            tk.Label(object_frame,text="                        ", font=(18)).grid(row=0, column=2) #排版用的
            tk.Label(object_frame,text="選擇要查詢的球員學號和姓名").grid(row=1,column=0)
            combo = ttk.Combobox(object_frame, values=server.show_all_player(), state="readonly")  #下拉式選單
            combo.grid(row=1,column=1)
            playerinfo_frame1 = tk.Frame(object_frame2)
            playerinfo_frame1.pack()
            playerinfo_frame2 = tk.Frame(object_frame2)
            playerinfo_frame2.pack()
            playerinfo_frame3 = tk.Frame(object_frame2)
            playerinfo_frame3.pack()
            combo.bind("<<ComboboxSelected>>", callbackFunc) #選取之後顯示球員資料

        def page_teamdata(): #球隊數據頁面 我打好了
            def clean_smallframe():
                for widget in team_frame1.winfo_children():
                    widget.destroy()
                for widget in team_frame2.winfo_children():
                    widget.destroy()
                for widget in team_frame3.winfo_children():
                    widget.destroy()

            tk.Label(object_frame,text="球隊數據頁面", font=classfont).grid(row=0)
            data1 = server.game_score()
            data2 = server.data_average()
            data3 = server.team_hit_rate()

            team_frame1 = tk.Frame(object_frame)
            team_frame1.grid(row=1)
            team_frame2 = tk.Frame(object_frame)
            team_frame2.grid(row=2)
            team_frame3 = tk.Frame(object_frame)
            team_frame3.grid(row=3)

            tk.Label(team_frame1, text="日期", font=wordfont).grid(row=0,column=0)
            tk.Label(team_frame1, text="盃賽名稱", font=wordfont).grid(row=0,column=1)
            tk.Label(team_frame1, text="對手學校", font=wordfont).grid(row=0,column=2)
            tk.Label(team_frame1, text="對手系名", font=wordfont).grid(row=0,column=3)
            tk.Label(team_frame1, text="我方得分", font=wordfont).grid(row=0,column=4)
            tk.Label(team_frame1, text="對手得分", font=wordfont).grid(row=0,column=5)
            for i in range(len(data1)):
                tk.Label(team_frame1, text=data1[i][0], font=wordfont).grid(row=i+1,column=0)
                tk.Label(team_frame1, text=data1[i][2], font=wordfont).grid(row=i+1,column=1)
                tk.Label(team_frame1, text=data1[i][3], font=wordfont).grid(row=i+1,column=2)
                tk.Label(team_frame1, text=data1[i][4], font=wordfont).grid(row=i+1,column=3)
                tk.Label(team_frame1, text=data1[i][1], font=wordfont).grid(row=i+1,column=4)
                tk.Label(team_frame1, text=data1[i][5], font=wordfont).grid(row=i+1,column=5)

            tk.Label(team_frame2, text="得分率", font=wordfont).grid(row=0,column=0)
            tk.Label(team_frame2, text="籃板率", font=wordfont).grid(row=0,column=1)
            tk.Label(team_frame2, text="助攻率", font=wordfont).grid(row=0,column=2)
            tk.Label(team_frame2, text="阻攻率", font=wordfont).grid(row=0,column=3)
            tk.Label(team_frame2, text="抄截率", font=wordfont).grid(row=0,column=4)
            tk.Label(team_frame2, text="犯規率", font=wordfont).grid(row=0,column=5)
            tk.Label(team_frame2, text="失誤率", font=wordfont).grid(row=0,column=6)
            tk.Label(team_frame2, text=data2[0][0], font=wordfont).grid(row=1,column=0)
            tk.Label(team_frame2, text=data2[0][1], font=wordfont).grid(row=1,column=1)
            tk.Label(team_frame2, text=data2[0][2], font=wordfont).grid(row=1,column=2)
            tk.Label(team_frame2, text=data2[0][3], font=wordfont).grid(row=1,column=3)
            tk.Label(team_frame2, text=data2[0][4], font=wordfont).grid(row=1,column=4)
            tk.Label(team_frame2, text=data2[0][5], font=wordfont).grid(row=1,column=5)
            tk.Label(team_frame2, text=data2[0][6], font=wordfont).grid(row=1,column=6)
            
            tk.Label(team_frame3, text="三分球命中率", font=wordfont).grid(row=0,column=0)
            tk.Label(team_frame3, text="投籃命中率", font=wordfont).grid(row=0,column=1)
            tk.Label(team_frame3, text="罰球命中率", font=wordfont).grid(row=0,column=2)
            tk.Label(team_frame3, text=data3[0][0], font=wordfont).grid(row=1,column=0)
            tk.Label(team_frame3, text=data3[0][1], font=wordfont).grid(row=1,column=1)
            tk.Label(team_frame3, text=data3[0][2], font=wordfont).grid(row=1,column=2)

        def page_recordtable():  #歷屆紀錄表 打好了但是有奇怪的東西
            def clean_smallframe(): #清空小frame裡的物件
                for widget in record_frame.winfo_children():
                    widget.destroy()

            def callbackFunc(event): #處理下拉式選單選取要顯示的資訊
                clean_smallframe() #清空
                infomat=combo.get()
                infomat = infomat.split(' ') #擷取資料除掉空白鍵
                data = server.show_record(infomat[0],infomat[1],infomat[2],infomat[3])
                tk.Label(record_frame,text="姓名", font=wordfont).grid(row=0,column=0)
                tk.Label(record_frame,text="背號", font=wordfont).grid(row=0,column=1)
                tk.Label(record_frame,text="二分球投", font=wordfont).grid(row=0,column=2)
                tk.Label(record_frame,text="二分球中", font=wordfont).grid(row=0,column=3)
                tk.Label(record_frame,text="三分球投", font=wordfont).grid(row=0,column=4)
                tk.Label(record_frame,text="三分球中", font=wordfont).grid(row=0,column=5)
                tk.Label(record_frame,text="罰球投", font=wordfont).grid(row=0,column=6)
                tk.Label(record_frame,text="罰球中", font=wordfont).grid(row=0,column=7)
                tk.Label(record_frame,text="防守籃板", font=wordfont).grid(row=0,column=8)
                tk.Label(record_frame,text="進攻籃板", font=wordfont).grid(row=0,column=9)
                tk.Label(record_frame,text="助攻", font=wordfont).grid(row=0,column=10)
                tk.Label(record_frame,text="阻攻", font=wordfont).grid(row=0,column=11)
                tk.Label(record_frame,text="抄截", font=wordfont).grid(row=0,column=12)
                tk.Label(record_frame,text="失誤", font=wordfont).grid(row=0,column=13)
                tk.Label(record_frame,text="犯規", font=wordfont).grid(row=0,column=14)
                tk.Label(record_frame,text="被犯", font=wordfont).grid(row=0,column=15)
                for i in range(len(data)):
                    tk.Label(record_frame,text=data[i][6], font=wordfont).grid(row=i+1,column=0) #姓名
                    tk.Label(record_frame,text=data[i][7], font=wordfont).grid(row=i+1,column=1) #背號
                    tk.Label(record_frame,text=data[i][9], font=wordfont).grid(row=i+1,column=2) #二分球投
                    tk.Label(record_frame,text=data[i][10], font=wordfont).grid(row=i+1,column=3) #二分球中
                    tk.Label(record_frame,text=data[i][11], font=wordfont).grid(row=i+1,column=4) #三分球投
                    tk.Label(record_frame,text=data[i][12], font=wordfont).grid(row=i+1,column=5) #三分球中
                    tk.Label(record_frame,text=data[i][13], font=wordfont).grid(row=i+1,column=6) #罰球投
                    tk.Label(record_frame,text=data[i][14], font=wordfont).grid(row=i+1,column=7) #罰球中
                    tk.Label(record_frame,text=data[i][15], font=wordfont).grid(row=i+1,column=8) #防守籃板
                    tk.Label(record_frame,text=data[i][16], font=wordfont).grid(row=i+1,column=9) #進攻籃板
                    tk.Label(record_frame,text=data[i][17], font=wordfont).grid(row=i+1,column=10) #助攻
                    tk.Label(record_frame,text=data[i][18], font=wordfont).grid(row=i+1,column=11) #阻攻
                    tk.Label(record_frame,text=data[i][19], font=wordfont).grid(row=i+1,column=12) #抄截
                    tk.Label(record_frame,text=data[i][20], font=wordfont).grid(row=i+1,column=13) #失誤
                    tk.Label(record_frame,text=data[i][21], font=wordfont).grid(row=i+1,column=14) #犯規
                    tk.Label(record_frame,text=data[i][22], font=wordfont).grid(row=i+1,column=15) #被犯
                
            tk.Label(object_frame,text="歷屆紀錄表", font=classfont).grid(row=0,column=1)
            tk.Label(object_frame,text="選擇要查詢的比賽").grid(row=1,column=0)
            tk.Label(object_frame,text="               ", font=(18)).grid(row=0, column=2) #排版用的
            combo = ttk.Combobox(object_frame, values=server.game_info(), state="readonly") #下拉式選單
            combo.grid(row=1,column=1)
            record_frame = tk.Frame(object_frame2)
            record_frame.pack()
            combo.bind("<<ComboboxSelected>>", callbackFunc) #選取之後顯示球員資料


        def page_getrank(): #得分排行 我打好了
            tk.Label(object_frame,text="得分KING", font=classfont).grid(row=0, column=1)
            data = server.score_mvp()
            tk.Label(object_frame,text="學號", font=wordfont).grid(row=1,column=0)
            tk.Label(object_frame,text="背號", font=wordfont).grid(row=1,column=1)
            tk.Label(object_frame,text="總得分", font=wordfont).grid(row=1,column=2)
            for i in range(0,3):
                tk.Label(object_frame,text=data[i][1], font=wordfont).grid(row=i+2,column=0)
                tk.Label(object_frame,text=data[i][2], font=wordfont).grid(row=i+2,column=1)
                tk.Label(object_frame,text=data[i][3], font=wordfont).grid(row=i+2,column=2)

        def page_basketrank():
            tk.Label(object_frame,text="籃板KING", font=classfont).grid(row=0, column=1)
            data = server.backboard_mvp()
            tk.Label(object_frame,text="學號", font=wordfont).grid(row=1,column=0)
            tk.Label(object_frame,text="背號", font=wordfont).grid(row=1,column=1)
            tk.Label(object_frame,text="總籃板數", font=wordfont).grid(row=1,column=2)
            for i in range(0,3):
                tk.Label(object_frame,text=data[i][1], font=wordfont).grid(row=i+2,column=0)
                tk.Label(object_frame,text=data[i][2], font=wordfont).grid(row=i+2,column=1)
                tk.Label(object_frame,text=data[i][3], font=wordfont).grid(row=i+2,column=2)
        
        def page_soporank():
            tk.Label(object_frame,text="助攻KING", font=classfont).grid(row=0, column=1)
            data = server.assist_mvp()
            tk.Label(object_frame,text="學號", font=wordfont).grid(row=1,column=0)
            tk.Label(object_frame,text="背號", font=wordfont).grid(row=1,column=1)
            tk.Label(object_frame,text="總助攻數", font=wordfont).grid(row=1,column=2)
            for i in range(0,3):
                tk.Label(object_frame,text=data[i][1], font=wordfont).grid(row=i+2,column=0)
                tk.Label(object_frame,text=data[i][2], font=wordfont).grid(row=i+2,column=1)
                tk.Label(object_frame,text=data[i][3], font=wordfont).grid(row=i+2,column=2)
        
        def page_blockrank():
            tk.Label(object_frame,text="阻攻KING", font=classfont).grid(row=0, column=1)
            data = server.block_mvp()
            tk.Label(object_frame,text="學號", font=wordfont).grid(row=1,column=0)
            tk.Label(object_frame,text="背號", font=wordfont).grid(row=1,column=1)
            tk.Label(object_frame,text="總阻攻數", font=wordfont).grid(row=1,column=2)
            for i in range(0,3):
                tk.Label(object_frame,text=data[i][1], font=wordfont).grid(row=i+2,column=0)
                tk.Label(object_frame,text=data[i][2], font=wordfont).grid(row=i+2,column=1)
                tk.Label(object_frame,text=data[i][3], font=wordfont).grid(row=i+2,column=2)

        def page_catchrank():
            tk.Label(object_frame,text="抄截KING", font=classfont).grid(row=0, column=1)
            data = server.intercept_mvp()
            tk.Label(object_frame,text="學號", font=wordfont).grid(row=1,column=0)
            tk.Label(object_frame,text="背號", font=wordfont).grid(row=1,column=1)
            tk.Label(object_frame,text="總抄截數", font=wordfont).grid(row=1,column=2)
            for i in range(0,3):
                tk.Label(object_frame,text=data[i][1], font=wordfont).grid(row=i+2,column=0)
                tk.Label(object_frame,text=data[i][2], font=wordfont).grid(row=i+2,column=1)
                tk.Label(object_frame,text=data[i][3], font=wordfont).grid(row=i+2,column=2)

        def page_thirdgraderank():
            tk.Label(object_frame,text="三分球KING", font=classfont).grid(row=0, column=1)
            data = server.three_point_rate()
            tk.Label(object_frame,text="學號", font=wordfont).grid(row=1,column=0)
            tk.Label(object_frame,text="背號", font=wordfont).grid(row=1,column=1)
            tk.Label(object_frame,text="三分球命中率", font=wordfont).grid(row=1,column=2)
            for i in range(0,3):
                tk.Label(object_frame,text=data[i][1], font=wordfont).grid(row=i+2,column=0)
                tk.Label(object_frame,text=data[i][2], font=wordfont).grid(row=i+2,column=1)
                tk.Label(object_frame,text=data[i][3], font=wordfont).grid(row=i+2,column=2)

        def page_throwrank():
            tk.Label(object_frame,text="投籃KING", font=classfont).grid(row=0, column=1)
            data = server.shoot_rate_mvp()
            tk.Label(object_frame,text="學號", font=wordfont).grid(row=1,column=0)
            tk.Label(object_frame,text="背號", font=wordfont).grid(row=1,column=1)
            tk.Label(object_frame,text="投球命中率", font=wordfont).grid(row=1,column=2)
            for i in range(0,3):
                tk.Label(object_frame,text=data[i][1], font=wordfont).grid(row=i+2,column=0)
                tk.Label(object_frame,text=data[i][2], font=wordfont).grid(row=i+2,column=1)
                tk.Label(object_frame,text=data[i][3], font=wordfont).grid(row=i+2,column=2)

        def page_punishrank(): #我打好了
            tk.Label(object_frame,text="罰球KING", font=classfont).grid(row=0, column=1)
            data = server.penalty_mvp()
            tk.Label(object_frame,text="學號", font=wordfont).grid(row=1,column=0)
            tk.Label(object_frame,text="背號", font=wordfont).grid(row=1,column=1)
            tk.Label(object_frame,text="罰球命中率", font=wordfont).grid(row=1,column=2)
            for i in range(0,3):
                tk.Label(object_frame,text=data[i][1], font=wordfont).grid(row=i+2,column=0)
                tk.Label(object_frame,text=data[i][2], font=wordfont).grid(row=i+2,column=1)
                tk.Label(object_frame,text=data[i][3], font=wordfont).grid(row=i+2,column=2)

        def pop_up(result):
            #我在這裡設計一個功能，也就是為了彈出視窗所設計的功能
                messagebox.showinfo(" ",result)
            #括號裡面的兩個字串分別代表彈出視窗的標題(title)與要顯示的文字(index)

        def page_newplayer():
            tk.Label(object_frame,text="新增球員", font=classfont).pack(side="top", fill="x", pady=5)
            result = ("新增成功 !")
            pop_up(result)
        
        def page_changedata():
            tk.Label(object_frame,text="修改資料", font=classfont).pack(side="top", fill="x", pady=5)
            result = ("修改成功 !")
            pop_up(result)

        def page_startboard():
            tk.Button(object_frame, text='開始記錄', width=20, height=10, command=lambda: [clean_frame(), page_boardgetgameinfo()]).pack()

        def page_boardgetgameinfo():
            def do_print():
                print('%s' %(dateString.get()))
                print('%s' %(gameString.get()))
                print('%s' %(oppschoolString.get()))
                print('%s' %(oppdepString.get()))
                
            tk.Label(object_frame, text="開始記錄", font=('Arial', 18, "bold")).grid(column=0, row=0, sticky=tk.W)
            #Label-文字標籤
            dateLabel = tk.Label(object_frame, text='日期:')
            gameLabel = tk.Label(object_frame, text='盃賽名稱:')
            oppschoolLabel = tk.Label(object_frame, text='對手學校')
            oppdepLabel = tk.Label(object_frame, text='對手系名')

            dateLabel.grid(column=0, row=1, sticky=tk.W)
            gameLabel.grid(column=0, row=2, sticky=tk.W)
            oppschoolLabel.grid(column=0, row=3, sticky=tk.W)
            oppdepLabel.grid(column=0, row=4, sticky=tk.W)
            #定義文字輸入框裡的文字物件
            dateString = tk.StringVar()
            gameString = tk.StringVar()
            oppschoolString = tk.StringVar()
            oppdepString = tk.StringVar()
            dateEntry = tk.Entry(object_frame, show=None, font=('Arial', 14), textvariable=dateString)
            gameEntry = tk.Entry(object_frame, show=None, font=('Arial', 14), textvariable=gameString)
            oppschoolEntry = tk.Entry(object_frame, show=None, font=('Arial', 14), textvariable=oppschoolString)
            oppdepEntry = tk.Entry(object_frame, show=None, font=('Arial', 14), textvariable=oppdepString)

            dateEntry.grid(column=1, row=1, padx=10)
            gameEntry.grid(column=1, row=2, padx=10)
            oppschoolEntry.grid(column=1, row=3, padx=10)
            oppdepEntry.grid(column=1, row=4, padx=10)

            tk.Button(object_frame, text='確定', command=lambda: [clean_frame(), do_print(), page_boardchoosplayer()]).grid(column=1, row=5, sticky=tk.N)
    
        def page_boardchoosplayer():
            data = server.online_player()
            #print(data)

        #清空object_frame裡面的東西
        def clean_frame():
            for widget in object_frame.winfo_children():
                widget.destroy()
            for widget in object_frame2.winfo_children():
                widget.destroy()

        menubar = tk.Menu(menu_frame) #宣告一個Menu的frame裡面有: 模式 設定 查詢 排行
        funcmenu = tk.Menu(menubar, tearoff=0) 
        menubar.add_cascade(label='模式', menu=funcmenu)
        setmenu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label='設定', menu=setmenu)
        querymenu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label='查詢', menu=querymenu)
        rankmenu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label='排行', menu=rankmenu)
        #查詢選項的下拉式選單
        querymenu.add_command(label='球員數據', command=lambda: [clean_frame(), page_playerdata()])
        querymenu.add_command(label='球隊數據', command=lambda: [clean_frame(), page_teamdata()])
        querymenu.add_separator() #分隔線
        querymenu.add_command(label='歷屆紀錄表', command=lambda: [clean_frame(), page_recordtable()])
        #排行選項的下拉式選單
        rankmenu.add_command(label='得分', command=lambda: [clean_frame(), page_getrank()])
        rankmenu.add_command(label='籃板', command=lambda: [clean_frame(), page_basketrank()])
        rankmenu.add_command(label='助攻', command=lambda: [clean_frame(), page_soporank()])
        rankmenu.add_command(label='阻攻', command=lambda: [clean_frame(), page_blockrank()])
        rankmenu.add_command(label='抄截', command=lambda: [clean_frame(), page_catchrank()])
        rankmenu.add_separator() #分隔線
        rankmenu.add_command(label='三分球%', command=lambda: [clean_frame(), page_thirdgraderank()])
        rankmenu.add_command(label='投籃%', command=lambda: [clean_frame(), page_throwrank()])
        rankmenu.add_command(label='罰球%', command=lambda: [clean_frame(), page_punishrank()])
        #設定選項的下拉式選單
        setmenu.add_command(label='新增球員', command=lambda: [clean_frame(), page_newplayer()])
        setmenu.add_command(label='修改球員資料', command=lambda: [clean_frame(), page_changedata()])
        #模式選項的下拉式選單
        funcmenu.add_command(label='記分板版', command=lambda: [clean_frame(), page_startboard()])

        self.config(menu=menubar)
    
if __name__ == "__main__":
    window = RecordBoard()
    window.iconbitmap('./board.ico')
    # window.configure(bg='Tan')
    window.mainloop()
