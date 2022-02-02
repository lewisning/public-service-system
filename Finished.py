from tkinter import *
import datetime
import random
import sqlite3


connection = None
cursor = None

class SQL:
    def __init__(self, root):

        self.path="./original.db"

        self.connect()
        
        self.drop_tables()
        self.define_tables()
        
        self.filename = input("请输入文件名称:")
        self.insert_data(self.filename)
        
        connection.commit()
        connection.close()
        

        
        self.root = root
        self.root.title("DATABASE")
        self.root.geometry("500x500")
        self.isLogOut = False
        self.login_screen()
        self.root.mainloop()


    def login_screen(self):
        self.remove_menu()
        if self.isLogOut == True:
            self.logout.place_forget()
        
        self.isLogOut = False
        self.uidLabel = Label(self.root, text="用户名")
        self.uidLabel.grid(row=0, column=0)
        self.pwdLabel = Label(self.root, text="密码")
        self.pwdLabel.grid(row=1, column=0)

        
        self.uid = Entry(self.root)
        self.pwd = Entry(self.root, show ="*")
        
        self.uid.grid(row=0, column=1)
        self.pwd.grid(row=1, column=1)
        self.login = Button(self.root, text="登陆", command =self.login_determine)
        self.login.place(relx = 0.5, rely = 0.8, anchor = CENTER)        
        self.exit = Button(self.root, text="退出程序", command =self.root.destroy)
        self.exit.place(relx = 0.2, rely = 0.8, anchor = CENTER)


    def login_determine(self):
        global connection, cursor
        connection = sqlite3.connect(self.path)
        cursor = connection.cursor()
        self.user = self.uid.get()
        cursor.execute("SELECT pwd FROM users WHERE uid=?",(self.user,))
        b = cursor.fetchall()
        c = self.pwd.get()
        
        if([(c,)] == b):
            self.login_successfull()
            cursor.execute("SELECT utype FROM users WHERE uid=?",(self.user,))
            d = cursor.fetchall()
            if(d == [('a',)]):
                self.registry_main_menu()
            else:
                self.traffic_main_menu()
        else:
            self.login_fail()


    def login_successfull(self):
        self.login.place_forget()
        self.uid.grid_remove()
        self.pwd.grid_remove()
        self.pwdLabel.grid_forget()
        self.uidLabel.grid_forget()
        self.isLogOut = True
        self.logout = Button(self.root, text="退出登陆", command= self.logout_procedure)
        self.logout.place(relx = 0.8, rely = 0.8, anchor = CENTER)


    def login_fail(self):
        self.uid.grid_remove()
        self.pwd.grid_remove()
        self.pwdLabel.grid_forget()
        self.uidLabel.grid_forget()
        self.login.place_forget()
        self.login_screen()
        print("无法登陆")


    def remove_menu(self):
        emptyMenu = Menu(self.root)
        self.root.config(menu=emptyMenu)


    def logout_procedure(self):
        _list = self.root.winfo_children()

        for item in _list :
            if item.winfo_children() :
                _list.extend(item.winfo_children())
                
        for item in _list:
            item.grid_forget()
            item.pack_forget()
            item.place_forget()
        self.login_screen()

        
    def registry_main_menu(self):
        menubar = Menu(self.root)
          
        birth = Menu(menubar, tearoff = 0)
        birth.add_command(label = "注册新生儿", command = self.birthRegister)
        menubar.add_cascade(label = "注册新生儿", menu = birth)
        
        marriage = Menu(menubar, tearoff = 0)
        marriage.add_command(label = "结婚登记", command = self.marriageRegister)
        menubar.add_cascade(label = "结婚登记", menu = marriage)
        
        vehicle = Menu(menubar, tearoff = 0)
        vehicle.add_command(label = "更新车辆信息", command = self.vehicleRenew)
        menubar.add_cascade(label = "更新车辆信息", menu = vehicle)
        
        bill = Menu(menubar, tearoff = 0)
        bill.add_command(label = "查看账单", command = self.processBill)
        menubar.add_cascade(label = "查看账单", menu = bill)
        
        payment = Menu(menubar, tearoff = 0)
        payment.add_command(label = "支付罚单", command = self.processPayment)
        menubar.add_cascade(label = "支付罚单", menu = payment)
        
        abstract = Menu(menubar, tearoff = 0)
        abstract.add_command(label = "查看罚单信息", command = self.getAbstract)
        menubar.add_cascade(label = "查看罚单信息", menu = abstract)
        self.root.config(menu=menubar)
    
        
    def birthRegister(self):
        self.remove_menu()
        global connection, cursor
        
        d = datetime.datetime.today()
        self.bfname = Entry(self.root)
        self.blname = Entry(self.root)
        self.gender = Entry(self.root)
        self.birthdate = Entry(self.root)
        self.birthplace = Entry(self.root)
        self.fnamep1 = Entry(self.root)
        self.lnamep1 = Entry(self.root)
        self.fnamep2 = Entry(self.root)
        self.lnamep2 = Entry(self.root)
        
        self.bfname.grid(row=0, column=1)
        self.blname.grid(row=1, column=1)
        self.gender.grid(row=2, column=1)
        self.birthdate.grid(row=3, column=1)
        self.birthplace.grid(row=4, column=1)
        self.fnamep1.grid(row=5, column=1)
        self.lnamep1.grid(row=6, column=1)
        self.fnamep2.grid(row=7, column=1)
        self.lnamep2.grid(row=8, column=1)
        
        self.lbfname = Label(self.root, text="名")
        self.lblname = Label(self.root, text="姓")
        self.lgender = Label(self.root, text="性别")
        self.lbirthdate = Label(self.root, text="出生日期(xxxx-xx-xx)")
        self.lbirthplace = Label(self.root, text="出生地")
        self.lfnamep1 = Label(self.root, text="母亲名")
        self.llnamep1 = Label(self.root, text="母亲姓")
        self.lfnamep2 = Label(self.root, text="父亲名")
        self.llnamep2 = Label(self.root, text="父亲姓")
        
        self.lbfname.grid(row=0, column=0)
        self.lblname.grid(row=1, column=0)
        self.lgender.grid(row=2, column=0)
        self.lbirthdate.grid(row=3, column=0)
        self.lbirthplace.grid(row=4, column=0)
        self.lfnamep1.grid(row=5, column=0)
        self.llnamep1.grid(row=6, column=0)
        self.lfnamep2.grid(row=7, column=0)
        self.llnamep2.grid(row=8, column=0)
        
        
        
        self.birthSubmit = Button(self.root, text="提交", command= self.submit_births)
        self.birthSubmit.place(relx = 0.5, rely = 0.8, anchor = CENTER)
        
        self.today = datetime.datetime(d.year,d.month, d.day)
        cursor.execute("SELECT city FROM users WHERE uid=?",(self.user,))

        self.registrationPlace = cursor.fetchall()   
        self.regnum = random.randint(0,999)
        cursor.execute("SELECT regno FROM births")
        self.regno = cursor.fetchall()
        for no in self.regno:
            while no[0] == self.regnum:
                self.renum = random.randint(0,999)
                
    
    def submit_births(self):
        global connection, cursor

        birthData = (self.regnum, (str(self.bfname.get())).capitalize(), (str(self.blname.get())).capitalize(), self.today, (str(self.registrationPlace[0][0])).capitalize(), (str(self.gender.get())).capitalize(), str(self.fnamep2.get()), (str(self.lnamep2.get())).capitalize(), (str(self.fnamep1.get())).capitalize(), (str(self.lnamep1.get())).capitalize())
        try:
            cursor.execute('INSERT INTO births(regno, fname, lname, regdate, regplace, gender, f_fname, f_lname, m_fname, m_lname) VALUES(?,?,?,?,?,?,?,?,?,?)',birthData)
            connection.commit()
            self.create_person()
        
        except ValueError:
            print('无法录入')
            self.remove_birth_grid()
            self.registry_main_menu()
        
        except sqlite3.IntegrityError:
            print('录入的信息已存在')
            self.remove_birth_grid()
            self.registry_main_menu()
        

    def create_person(self):
        global connection, cursor
        self.registry_main_menu()
        bdate = datetime.datetime.strptime(str(self.birthdate.get()), '%Y-%m-%d')
        momf_name = str(self.fnamep1.get()).capitalize()
        moml_name = str(self.lnamep1.get()).capitalize()
        dadf_name = str(self.fnamep2.get()).capitalize()
        dadl_name = str(self.lnamep2.get()).capitalize()
        momData = (momf_name, moml_name,)
        dadData = (dadf_name, dadl_name,)
        
        cursor.execute("SELECT * FROM persons WHERE fname=? AND lname=?",momData)
        hasMom = cursor.fetchall()
        cursor.execute("SELECT * FROM persons WHERE fname=? AND lname=?",dadData)
        self.remove_birth_grid()
        hasDad = cursor.fetchall()
        if len(str(hasDad)) == 2:
            self.get_person_info(dadf_name, dadl_name, '父亲')
            
        if len(str(hasMom)) == 2:
            self.get_person_info(momf_name, moml_name, '母亲')
        else:
            cursor.execute("SELECT address FROM persons WHERE fname=? AND lname=?",momData)
            address = cursor.fetchall()
            cursor.execute("SELECT phone FROM persons WHERE fname=? AND lname=?",momData)
            phone = cursor.fetchall()
            personData = (str(self.bfname.get()), str(self.blname.get()),bdate, str(self.birthplace.get()), str(address[0][0]), str(phone[0][0]))
            cursor.execute('INSERT INTO persons(fname, lname, bdate, bplace, address, phone) VALUES (?,?,?,?,?,?)',personData)
        connection.commit()
        

    def get_person_info(self, fname, lname, person):
        global connection, cursor
        self.remove_menu()
        
        self.person_first_name = fname
        self.person_last_name = lname
        self.bdate = Entry(self.root)
        self.bplace = Entry(self.root)
        self.address = Entry(self.root)
        self.phone = Entry(self.root)
        
        self.bdate.grid(row=0, column=1)
        self.bplace.grid(row=1, column=1)
        self.address.grid(row=2, column=1)
        self.phone.grid(row=3, column=1)
        
        self.lbdate = Label(self.root, text="Birthday of "+person)
        self.lbplace = Label(self.root, text="Birth Place of "+person)
        self.laddress = Label(self.root, text="Address of "+person)
        self.lphone = Label(self.root, text="Phone of "+person)
        
        self.lbdate.grid(row=0, column=0)
        self.lbplace.grid(row=1, column=0)
        self.laddress.grid(row=2, column=0)
        self.lphone.grid(row=3, column=0)
        
        self.personSubmit = Button(self.root, text="提交", command= self.submit_person)
        self.personSubmit.place(relx = 0.5, rely = 0.8, anchor = CENTER)


    def submit_person(self):        
        global connection, cursor
        
        if (str(self.bdate.get())) == '':
            bdate = '0000-00-0'
        else:
            bdate = datetime.datetime.strptime(str(self.bdate.get()), '%Y-%m-%d')

        if (str(self.bplace.get())) == '':
            bplace = '无'
        else:
            bplace = str(self.bplace.get()).capitalize()
        
        if(str(self.address.get())) == '':
            address = '无'
        else:
            address = str(self.address.get()).capitalize()
        
        if (str(self.phone.get())) == '':
            phone = '无'
        else:
            phone = str(self.phone.get())
        self.personsData = (self.person_first_name, self.person_last_name, bdate, bplace, address, phone)
        print(self.personsData)
        cursor.execute('INSERT INTO persons(fname, lname, bdate, bplace, address, phone) VALUES (?,?,?,?,?,?)',self.personsData)
        connection.commit()

        self.personSubmit.place_forget()
        self.remove_person_grid()
        self.registry_main_menu()
        

    def remove_person_grid(self):
        self.bdate.grid_remove()
        self.bplace.grid_remove()
        self.address.grid_remove()
        self.phone.grid_remove()
        
        self.lbdate.grid_forget()
        self.lbplace.grid_forget()
        self.laddress.grid_forget()
        self.lphone.grid_forget()

        
    def remove_birth_grid(self):
        self.bfname.grid_remove()
        self.blname.grid_remove()
        self.gender.grid_remove()
        self.birthdate.grid_remove()
        self.birthplace.grid_remove()
        self.fnamep1.grid_remove()
        self.lnamep1.grid_remove()
        self.fnamep2.grid_remove()
        self.lnamep2.grid_remove()
        self.birthSubmit.place_forget()
        
        self.lbfname.grid_forget()
        self.lblname.grid_forget()
        self.lgender.grid_forget()
        self.lbirthdate.grid_forget()
        self.lbirthplace.grid_forget()
        self.lfnamep1.grid_forget()
        self.llnamep1.grid_forget()
        self.lfnamep2.grid_forget()
        self.llnamep2.grid_forget()


    def marriageRegister(self):
        global connection, cursor
        self.remove_menu()
        
        self.fpartner1 = Entry(self.root)
        self.fpartner1.grid(row=0, column=1)
        self.fp_partner1 = Label(self.root, text="请输入男方名:")
        self.fp_partner1.grid(row=0, column=0)    
        self.fpartner2 = Entry(self.root)
        self.fpartner2.grid(row=1, column=1)
        self.fp_partner2 = Label(self.root, text="请输入男方姓:")
        self.fp_partner2.grid(row=1, column=0)  
        
        self.spartner1 = Entry(self.root)
        self.spartner1.grid(row=2, column=1)
        self.sp_partner1 = Label(self.root, text="请输入女方名:")
        self.sp_partner1.grid(row=2, column=0)    
        self.spartner2 = Entry(self.root)
        self.spartner2.grid(row=3, column=1)
        self.sp_partner2 = Label(self.root, text="请输入女方姓:")
        self.sp_partner2.grid(row=3, column=0)        
        
        self.p_details = Button(self.root, text="提交", command= self.m_Details)
        self.p_details.place(relx = 0.5, rely = 0.8, anchor = CENTER)  
        
        cursor.execute("SELECT city FROM users WHERE uid=?",(self.user,))

        self.regisPlace = cursor.fetchall()   
        self.regNum = random.randint(0,999)
        cursor.execute("SELECT regno FROM marriages")
        self.m_regno = cursor.fetchall()
        for no in self.m_regno:
            while no[0] == self.regNum:
                self.regNum = random.randint(0,999)        


    def m_Details(self):
        global connection, cursor

        self.remove_marriageRegister()
        self.p_details.place_forget()
        
        d = datetime.datetime.today()
        self.today = datetime.datetime(d.year,d.month, d.day)
        
        marriageData = (self.regNum, self.today, str(self.regisPlace[0][0]).capitalize(), str(self.fpartner1.get()).capitalize(), str(self.fpartner2.get()).capitalize(), str(self.spartner1.get()).capitalize(), str(self.spartner2.get()).capitalize(),)
        cursor.execute('INSERT INTO marriages(regno, regdate, regplace, p1_fname, p1_lname, p2_fname, p2_lname) VALUES(?,?,?,?,?,?,?)',marriageData)
        connection.commit()
        
        cursor.execute('select fname, lname from persons')
        personList = cursor.fetchall()
        self.registry_main_menu()
        for i in range(len(personList)):
            if (personList[i][0]==str(self.fpartner1.get())).capitalize() and (personList[i][1]==str(self.fpartner2.get())).capitalize():
                break
            elif i==(len(personList)-1):
               self.get_person_info( str(self.fpartner1.get()).capitalize(), str(self.fpartner2.get()).capitalize(), '男方')
        
        for j in range(len(personList)):
            if (personList[j][0]==str(self.spartner1.get()).capitalize()) and (personList[j][1]==str(self.spartner2.get()).capitalize()):
                break
            elif j==(len(personList)-1):
                self.get_person_info( str(self.spartner1.get()).capitalize(), str(self.spartner2.get()).capitalize(), '女方')
        

    def remove_marriageRegister(self):
        self.fpartner1.grid_remove()
        self.fp_partner1.grid_forget()   
        
        self.fpartner2.grid_remove()
        self.fp_partner2.grid_forget() 
        
        self.spartner1.grid_remove()
        self.sp_partner1.grid_forget()  
        
        self.spartner2.grid_remove()
        self.sp_partner2.grid_forget()        


    def vehicleRenew(self):
        self.remove_menu()
        global connection, cursor
        
        self.regisNum = Entry(self.root)     
        self.regisNum.grid(row=0, column=1)
        self.lregno = Label(self.root, text="已经存在的注册编号:")
        self.lregno.grid(row=0, column=0)
        
        self.renewReg = Button(self.root, text="提交", command= self.renew_registration)
        self.renewReg.place(relx = 0.5, rely = 0.8, anchor = CENTER)
        

    def renew_registration(self):
        global connection, cursor
        
        d = datetime.datetime.today()
        self.today = datetime.datetime(d.year,d.month, d.day)
        try:
            cursor.execute('select regno from registrations;')
            regno_table = cursor.fetchall()
            
            self.new_regno = random.randint(0,2000)
            for no in regno_table:
                while no[:-1] == self.new_regno:
                    self.new_regno = random.randint(0,2000)        
            
            cursor.execute('select expiry from registrations where regno=?', (self.regisNum.get(),))
            expiry_table = cursor.fetchall()
            
            expiry_date = datetime.datetime.strptime(expiry_table[0][0], '%Y-%m-%d')
            
            if expiry_date <= d:
                new_edate = d.replace(d.year+1)
            else:
                
                new_edate = expiry_date.replace(expiry_date.year + 1)
                
            cursor.execute('update registrations set regno=?, expiry=? where regno=?', (self.new_regno, new_edate, self.regisNum.get()))
            connection.commit()
        except:
            print('无法登记')
        
        self.remove_renew_registry()
        self.renewReg.place_forget()
        self.registry_main_menu()
        
    
    def remove_renew_registry(self):
        self.regisNum.grid_remove()
        self.lregno.grid_forget()


    def processBill(self):
        global connection, cursor
        self.remove_menu()
        
        self.p_vin = Entry(self.root)
        self.p_vin.grid(row=0, column=1)
        self.p_pvin = Label(self.root, text="请输入车辆注册编号:")
        self.p_pvin.grid(row=0, column=0)        
        
        self.p_cfname = Entry(self.root)
        self.p_cfname.grid(row=1, column=1)
        self.p_pcfname = Label(self.root, text="请输入现拥有者名:")
        self.p_pcfname.grid(row=1, column=0)      
        
        self.p_clname = Entry(self.root)
        self.p_clname.grid(row=2, column=1)
        self.p_pclname = Label(self.root, text="请输入现拥有者姓:")
        self.p_pclname.grid(row=2, column=0) 
        
        self.p_nfname = Entry(self.root)
        self.p_nfname.grid(row=3, column=1)
        self.p_pnfname = Label(self.root, text="请输入新拥有者名:")
        self.p_pnfname.grid(row=3, column=0)
        
        self.p_nlname = Entry(self.root)
        self.p_nlname.grid(row=4, column=1)
        self.p_pnlname = Label(self.root, text="请输入新拥有者姓:")
        self.p_pnlname.grid(row=4, column=0) 
        
        self.newplate = Entry(self.root)
        self.newplate.grid(row=5, column=1)
        self.p_newplate = Label(self.root, text="请输入新车牌号:")
        self.p_newplate.grid(row=5, column=0)              
        
        self.bill_details = Button(self.root, text="提交", command= self.bill_Details)
        self.bill_details.place(relx = 0.5, rely = 0.8, anchor = CENTER)        


    def bill_Details(self):
        global connection, cursor

        try:
            cursor.execute('select expiry from registrations where vin=?', (str(self.p_vin.get()),))
            e_table=cursor.fetchall()
            
            eDate = e_table[0][0]
            for i in range(len(e_table)):
                if eDate < e_table[i][0]:
                    eDate = e_table[i][0]
            cursor.execute('select fname, lname from registrations where expiry=?',(eDate,))
            names = cursor.fetchall()
            
            d = datetime.datetime.today()
            self.today = datetime.datetime(d.year,d.month, d.day)        
            
            if names[0][0]!= str(self.p_cfname.get()).capitalize() or names[0][1]!=str(self.p_clname.get()).capitalize():
                print('交易失败')
            else:
                cursor.execute('select fname, lname from persons')
                persons_list = cursor.fetchall()
                for i in range(len(persons_list)):
                    if persons_list[i][0] == str(self.p_nfname.get()).capitalize() or persons_list[i][1]==str(self.p_nlname.get()).capitalize():    
                        cursor.execute('select regno from registrations;')
                        regno_table = cursor.fetchall()
                        
                        new_regno = random.randint(0,2000)
                        for no in regno_table:
                            while no[:-1] == new_regno:
                                new_regno = random.randint(0,2000)                     
                        
                        cursor.execute('select plate from registrations where vin=? and expiry=?', ( str(self.p_vin.get()), eDate,))
                        plate = cursor.fetchall()
                        cursor.execute('update registrations set expiry=? where vin=? and expiry=?',( self.today, str(self.p_vin.get()), eDate,))
                        cursor.execute('insert into registrations values (?,?,?,?,?,?,?)', ( new_regno, self.today, self.today.replace(self.today.year+1), self.newplate.get(), self.p_vin.get(), str(self.p_nfname.get()).capitalize(), str(self.p_nlname.get()).capitalize(),))
                        
                        connection.commit()
                        break
                    elif i == (len(persons_list)-1):
                        print('交易失败')
        except:
            print('无法输入')
            
        self.remove_bill_Details()
        self.bill_details.place_forget()
        self.registry_main_menu()
        connection.commit()


    def remove_bill_Details(self):
        self.p_vin.grid_remove()
        self.p_pvin.grid_forget()
        
        self.p_cfname.grid_remove()
        self.p_pcfname.grid_forget() 
        
        self.p_clname.grid_remove()
        self.p_pclname.grid_forget()
        
        self.p_nfname.grid_remove()
        self.p_pnfname.grid_forget() 
        
        self.p_nlname.grid_remove()
        self.p_pnlname.grid_forget()    
        
        self.newplate.grid_remove()
        self.p_newplate.grid_forget()        
        

    def processPayment(self):
        global connection, cursor
        self.remove_menu()
        
        self.p_tno = Entry(self.root)
        self.p_tno.grid(row=0, column=1)
        self.p_ptno = Label(self.root, text="请输入罚单编号:")
        self.p_ptno.grid(row=0, column=0)    
        self.p_amount = Entry(self.root)
        self.p_amount.grid(row=1, column=1)
        self.p_pAmount = Label(self.root, text="请输入总金额:")
        self.p_pAmount.grid(row=1, column=0)        
        
        self.p_details = Button(self.root, text="提交", command= self.p_Details)
        self.p_details.place(relx = 0.5, rely = 0.8, anchor = CENTER)  

    
    def p_Details(self):
        global connection, cursor

        cursor.execute('SELECT tno FROM tickets;')
        tnumber = cursor.fetchall()
        try:
            cursor.execute('SELECT fine FROM tickets WHERE tno = ?;', (self.p_tno.get(),))
            fine = cursor.fetchall()
            userAmount = self.p_amount.get()
            userInput = self.p_tno.get()

            if ((int(userInput),)) not in tnumber:
                print("罚单编号无效，请重试")
            elif ((int(userAmount),)) > fine[0]:
                print("金额无效，请重试")
            else:
                cursor.execute('INSERT INTO payments values(?, date("now"), ?);', (str(userInput), str(userAmount)))
                cursor.execute('UPDATE tickets SET fine = fine - ? WHERE tno = ?;', (userAmount, userInput))
        except ValueError:
            print('无法录入')
        except sqlite3.IntegrityError:
            print('每日只能支付一次账单')
        finally:
            connection.commit()
            self.remove_processPayment()
            self.p_details.place_forget()
            self.registry_main_menu()
        

    def remove_processPayment(self):
        
        self.p_tno.grid_remove()
        self.p_ptno.grid_forget()
        
        self.p_amount.grid_remove()
        self.p_pAmount.grid_forget() 
      

    def getAbstract(self):
        global connection, cursor
        self.remove_menu()
        
        self.d_fname = Entry(self.root)
        self.d_fname.grid(row=0, column=1)
        self.dd_fname = Label(self.root, text="请输入名:")
        self.dd_fname.grid(row=0, column=0)

        self.d_lname = Entry(self.root)
        self.d_lname.grid(row=1, column=1)
        self.dd_lname = Label(self.root, text="请输入姓:")
        self.dd_lname.grid(row=1, column=0)


        self.d_details = Button(self.root, text="提交", command= self.d_Details)
        self.d_details.place(relx = 0.5, rely = 0.8, anchor = CENTER) 


    def d_Details(self):
        global connection, cursor
        try:
            d_Person = (str(self.d_fname.get()).capitalize(), str(self.d_lname.get()).capitalize())
            cursor.execute("SELECT COUNT(t.tno) FROM tickets t, registrations r WHERE r.regno = t.regno AND r.fname = ? AND r.lname = ? AND 2>(CURRENT_TIMESTAMP-t.vdate)",(d_Person))
            self.ticket_num = cursor.fetchall()
            cursor.execute("SELECT COUNT(*), SUM(d.points) FROM demeritNotices d WHERE d.fname = ? AND d.lname = ? AND 2>(CURRENT_TIMESTAMP-d.ddate)",(d_Person))
            self.demirit_Amount = cursor.fetchall()
            self.two_result = self.ticket_num[0] + self.demirit_Amount[0]
            
            cursor.execute("SELECT t.tno FROM tickets t, registrations r WHERE r.regno = t.regno AND r.fname = ? AND r.lname = ? ORDER BY t.vdate DESC",(d_Person))
            self.tickNo_ordered = cursor.fetchall()
            
            cursor.execute("SELECT COUNT(t.tno) FROM tickets t, registrations r WHERE r.regno = t.regno AND r.fname = ? AND r.lname = ?",(d_Person))
            self.life_time_tick_num = cursor.fetchall()
            cursor.execute("SELECT COUNT(*), SUM(d.points) FROM demeritNotices d WHERE d.fname = ? AND d.lname = ?",(d_Person))
            self.life_time_demerit_Amount = cursor.fetchall()
            self.lifetime_result = self.life_time_tick_num[0] + self.life_time_demerit_Amount[0]
    
            self.show_first_results()
        except IndexError:
            print('无法录入')

            self.d_details.place_forget()
            self.remove_getAbstract()
            self.registry_main_menu() 


    def show_first_results(self):
        self.d_details.place_forget()
        self.remove_getAbstract()

        
        self.two_fname = Label(self.root, text="2年内的罚单以及处分:\n\n"+'\t罚单数量: '+str(self.two_result[0])+'\n'+'\t处分数量: '+str(self.two_result[1])+'\n'+'\t扣分: '+str(self.two_result[2]))
        self.two_fname.grid(row=0, column=0)
        self.life_fname = Label(self.root, text="永久罚单以及处分:\n\n"+'\t罚单数量: '+str(self.lifetime_result[0])+'\n'+'\t处分数量: '+str(self.lifetime_result[1])+'\n'+'\t扣分: '+str(self.lifetime_result[2]))
        self.life_fname.grid(row=1, column=0)
        self.first_continue = Button(self.root, text="查看罚单", command= self.ordered_Tick)
        self.first_continue.place(relx = 0.5, rely = 0.8, anchor = CENTER)


    def ordered_Tick(self):
        global connection, cursor
        self.two_fname.grid_remove()
        self.life_fname.grid_remove()
        self.first_continue.place_forget()
        alpha = 0
        if(len(self.tickNo_ordered)>=5):
            for self.alpha in range(5):

                tick_str = ''
                cursor.execute('SELECT t.tno, t.vdate, t.violation, t.fine, t.regno, v.make, v.model FROM tickets t, registrations r, vehicles v WHERE t.tno = ? AND t.regno = r.regno AND r.vin = v.vin',self.tickNo_ordered[0])
                disp_tick = cursor.fetchall()
                for stuff in disp_tick:
                    for i in range(7):
                        tick_str += str(stuff[i])
                        tick_str += ' '
                 
                if self.alpha ==0:
                    self.first = Label(self.root, text=tick_str)
                    self.first.grid(row=self.alpha, column = 1)
                if self.alpha ==1:
                    self.second = Label(self.root, text=tick_str)
                    self.second.grid(row=self.alpha, column = 1)
                if self.alpha == 2:
                    self.third = Label(self.root, text=tick_str)
                    self.third.grid(row=self.alpha, column = 1)
                if self.alpha == 3:
                    self.forth = Label(self.root, text=tick_str)
                    self.forth.grid(row=self.alpha, column = 1)
                if self.alpha == 4:
                    self.fifth = Label(self.root, text=tick_str)
                    self.fifth.grid(row=self.alpha, column = 1)
                
                self.tickNo_ordered.remove(self.tickNo_ordered[0])
                self.alpha+=1
            self.see_more_tick = Button(self.root, text = '更多', command = self.see_more)
            self.see_more_tick.place(relx =0.6, rely = 0.8, anchor = CENTER)
            
            self.return_to_main = Button(self.root, text = '返回主菜单', command = self.final)
            self.return_to_main.place(relx =0.4, rely = 0.8, anchor = CENTER)

        else:
            for self.alpha in range (len(self.tickNo_ordered)):
                tick_str = ''
                cursor.execute('SELECT t.tno, t.vdate, t.violation, t.fine, t.regno, v.make, v.model FROM tickets t, registrations r, vehicles v WHERE t.tno = ? AND t.regno = r.regno AND r.vin = v.vin',self.tickNo_ordered[0])
                disp_tick = cursor.fetchall()
                for stuff in disp_tick:
                    for i in range(7):
                        tick_str += str(stuff[i])
                        tick_str += ' '
                 
                if self.alpha ==0:
                    self.first = Label(self.root, text=tick_str)
                    self.first.grid(row=self.alpha, column = 1)
                if self.alpha ==1:
                    self.second = Label(self.root, text=tick_str)
                    self.second.grid(row=self.alpha, column = 1)
                if self.alpha == 2:
                    self.third = Label(self.root, text=tick_str)
                    self.third.grid(row=self.alpha, column = 1)
                if self.alpha == 3:
                    self.forth = Label(self.root, text=tick_str)
                    self.forth.grid(row=self.alpha, column = 1)
                
                self.tickNo_ordered.remove(self.tickNo_ordered[0])
                self.alpha+=1
                self.return_to_main = Button(self.root, text = '返回主菜单', command = self.final)
                self.return_to_main.place(relx =0.5, rely = 0.8, anchor = CENTER)


    def see_more(self):
        self.first.grid_remove()
        self.second.grid_remove()
        self.third.grid_remove()
        self.forth.grid_remove()
        self.fifth.grid_remove()
        self.see_more_tick.place_forget()
        self.return_to_main.place_forget()
        self.ordered_Tick()


    def final(self):
        self.first.grid_remove()
        self.second.grid_remove()
        self.third.grid_remove()
        self.forth.grid_remove()
        self.fifth.grid_remove()
        self.see_more_tick.place_forget()
        self.return_to_main.place_forget()
        self.registry_main_menu()


    def remove_getAbstract(self):
        self.d_fname.grid_remove()
        self.dd_fname.grid_forget()     
        self.d_lname.grid_remove()
        self.dd_lname.grid_forget()       


    def traffic_main_menu(self):
        tmenubar = Menu(self.root)
        
        ticket = Menu(tmenubar, tearoff=0)
        ticket.add_command(label = "开罚单", command = self.issueTicket)
        tmenubar.add_cascade(label = "开罚单", menu = ticket)
        
        car = Menu(tmenubar, tearoff = 0)
        car.add_command(label = "查找车主", command = self.carOwner)
        tmenubar.add_cascade(label = "查找车主", menu = car)
        
        self.root.config(menu=tmenubar)

        
    def issueTicket(self):
        global connection, cursor
        self.remove_menu()
        self.v_regno = Entry(self.root)
        self.v_regno.grid(row=0, column=1)
        self.l_regno = Label(self.root, text="注册编号:")
        self.l_regno.grid(row=0, column=0)   
        
        self.t_details = Button(self.root, text="提交", command= self.getDetails)
        self.t_details.place(relx = 0.5, rely = 0.8, anchor = CENTER)


    def getDetails(self):
        global connection, cursor
        try:
            cursor.execute('SELECT p.fname, p.lname, v.make, v.model, v.year, v.color FROM persons p, registrations r, vehicles v WHERE p.fname=r.fname AND p.lname=r.lname AND r.vin=v.vin AND r.regno=(?);',(self.v_regno.get(),))
            details = cursor.fetchall()
            self.t_details.place_forget()
            self.v_regno.grid_remove()
            self.l_regno.grid_forget()
            self.tick_fname = details[0][0]
            self.tick_lname = details[0][1]
            self.tick_vmake = details[0][2]
            self.tick_vmodel = details[0][3]
            self.tick_vyear = details[0][4]
            self.tick_vcolor = details[0][5]
            
            self.ltick_fname = Label(self.root, text=self.tick_fname)
            self.ltick_fname.grid(row =0, column=0)
            self.ltick_lname = Label(self.root, text=self.tick_lname)
            self.ltick_lname.grid(row =0, column=1)
            self.ltick_vmake = Label(self.root, text=self.tick_vmake)
            self.ltick_vmake.grid(row =0, column=2)
            self.ltick_vmodel = Label(self.root, text=self.tick_vmodel)
            self.ltick_vmodel.grid(row =0, column=3)
            self.ltick_vyear = Label(self.root, text=str(self.tick_vyear))
            self.ltick_vyear.grid(row =0, column=4)
            self.ltick_vcolor = Label(self.root, text=self.tick_vcolor)
            self.ltick_vcolor.grid(row =0, column=5)

            self.is_info_correct()
        except IndexError:
            print('无法录入')
            self.l_regno.grid_remove()
            self.v_regno.grid_forget()
            self.t_details.place_forget()
            self.traffic_main_menu()
        

    def is_info_correct(self):
        self.correct = Button(self.root, text="正确", command= self.correctSub)
        self.correct.place(relx = 0.5, rely = 0.8, anchor = CENTER)
        self.incorrect = Button(self.root, text="错误", command= self.incorrectSub)
        self.incorrect.place(relx = 0.5, rely = 0.6, anchor = CENTER)
        #self.registry_main_menu()    


    def incorrectSub(self):
        self.ltick_fname.grid_forget()
        self.ltick_lname.grid_forget()
        self.ltick_vmake.grid_forget()
        self.ltick_vmodel.grid_forget()
        self.ltick_vyear.grid_forget()
        self.ltick_vcolor.grid_forget()

        self.correct.place_forget()
        self.incorrect.place_forget()
        self.issueTicket()


    def correctSub(self):
        global connection, cursor
        self.ltick_fname.grid_forget()
        self.ltick_lname.grid_forget()
        self.ltick_vmake.grid_forget()
        self.ltick_vmodel.grid_forget()
        self.ltick_vyear.grid_forget()
        self.ltick_vcolor.grid_forget()
        self.correct.place_forget()
        self.incorrect.place_forget()
        d = datetime.datetime.today()
        self.vtoday = datetime.datetime(d.year,d.month, d.day)
        cursor.execute('SELECT tno FROM tickets')
        alltickNum = cursor.fetchall()
        self.tickNo = random.randint(0,2000)
        for no in alltickNum:
            if self.tickNo == no:
                self.tickNo = random.randint(0,2000)
        
            
        
        self.violation_Date = Entry(self.root)
        self.violation_Date.grid(row=0, column=1)
        self.l_violation_Date = Label(self.root, text="事故日期:")
        self.l_violation_Date.grid(row=0, column=0)   
        
        if self.violation_Date == '':
            self.violation_Date = self.vtoday
        
        
        self.violation_Desc = Entry(self.root)
        self.violation_Desc.grid(row=1, column=1)
        self.l_violation_Desc = Label(self.root, text="事故描述:")
        self.l_violation_Desc.grid(row=1, column=0)   
        
        
        self.fine_amt = Entry(self.root)
        self.fine_amt.grid(row=2, column=1)
        self.l_fine_amt = Label(self.root, text="罚款总额:")
        self.l_fine_amt.grid(row=2, column=0)   
        
        tickValues = (self.tickNo, self.v_regno.get(), self.fine_amt.get(), self.violation_Desc.get(), self.vtoday)
        
        cursor.execute('INSERT INTO tickets VALUES (?,?,?,?,?)', tickValues)
        connection.commit()
                
        self.subTick = Button(self.root, text="提交", command= self.submit_tick)
        self.subTick.place(relx = 0.5, rely = 0.8, anchor = CENTER)


    def submit_tick(self):
        self.subTick.place_forget()
        self.violation_Date.grid_forget()
        self.l_violation_Date.grid_remove()
        self.violation_Desc.grid_forget()
        self.l_violation_Desc.grid_remove()
        self.fine_amt.grid_forget()
        self.l_fine_amt.grid_remove()
        self.traffic_main_menu()
        

    def carOwner(self):
        global connection, cursor
        
        self.cmake = Entry(self.root)
        self.cmake.grid(row=0, column=1)
        self.c_cmake = Label(self.root, text="车辆制造商:")
        self.c_cmake.grid(row=0, column=0)    
        
        self.cmodel = Entry(self.root)
        self.cmodel.grid(row=1, column=1)
        self.c_cmodel = Label(self.root, text="车辆型号:")
        self.c_cmodel.grid(row=1, column=0)  
        
        self.cyear = Entry(self.root)
        self.cyear.grid(row=2, column=1)
        self.c_cyear = Label(self.root, text="制造年份:")
        self.c_cyear.grid(row=2, column=0)        
        
        self.color = Entry(self.root)
        self.color.grid(row=3, column=1)
        self.c_color = Label(self.root, text="车辆颜色:")
        self.c_color.grid(row=3, column=0)       
        
        self.cplate = Entry(self.root)
        self.cplate.grid(row=4, column=1)
        self.c_cplate = Label(self.root, text="请输入车牌号:")
        self.c_cplate.grid(row=4, column=0) 
        
        self.t_details = Button(self.root, text="提交", command= self.car_ownerDetails)
        self.t_details.place(relx = 0.5, rely = 0.8, anchor = CENTER)     


    def car_ownerDetails(self):
        global connection, cursor
        
        self.remove_menu()
        if self.cmake.get() == '' and self.cmodel.get() == '' and self.cyear.get() == '' and self.color.get() == '' and self.cplate.get() == '':
            print("无法输入")
            
            self.cmake.grid_forget()
            self.c_cmake.grid_remove()   
            self.cmodel.grid_forget()
            self.c_cmodel.grid_remove()          
            self.cyear.grid_forget()
            self.c_cyear.grid_remove()      
            self.color.grid_forget()
            self.c_color.grid_remove()
            self.cplate.grid_forget()
            self.c_cplate.grid_remove()
            self.t_details.place_forget()               
            self.traffic_main_menu()
            
        else:
            self.cmake.grid_forget()
            self.c_cmake.grid_remove()   
            self.cmodel.grid_forget()
            self.c_cmodel.grid_remove()          
            self.cyear.grid_forget()
            self.c_cyear.grid_remove()      
            self.color.grid_forget()
            self.c_color.grid_remove()
            self.cplate.grid_forget()
            self.c_cplate.grid_remove()
            self.t_details.place_forget()   
            carsel = 'SELECT v.vin FROM vehicles v, registrations r WHERE v.vin = r.vin AND v.make =? AND v.model=? AND v.year=? AND v.color=? AND r.plate=?'
            amountCar = (str(self.cmake.get()).capitalize(), str(self.cmodel.get()).capitalize(), str(self.cyear.get()), str(self.color.get()).lower(), str(self.cplate.get()).capitalize())
            carAmount = ()
            if self.cmake.get() == '':
                carsel = carsel.replace('AND v.make =?','')
            if self.cmodel.get() == '':
                carsel = carsel.replace('AND v.model=?','')
            if self.cyear.get() == '':
                carsel = carsel.replace('AND v.year=?','')
            if self.color.get() == '':
                carsel = carsel.replace('AND v.color=?','')
            if self.cplate.get() == '':
                carsel = carsel.replace('AND r.plate=?','')
            
            for val in amountCar:
                if val != '':
                    carAmount += (val,)
                
            cursor.execute(carsel,carAmount)
            carlist = cursor.fetchall()
            carOwnersList = ''
            j = 0
            self.ownerButtons = []
            if (len(carlist))<4:
                for i in carlist:
                    a = str(i)
                    cursor.execute('SELECT v.make, v.model, v.year, v.color, r.plate, r.regdate, r.expiry, r.fname, r.lname FROM vehicles v, registrations r WHERE v.vin = r.vin AND r.vin = ?', i)
                    ad = cursor.fetchall()
                    for b in ad:
                        for stuff in b:
                            carOwnersList += str(stuff)
                            carOwnersList += ' '
                    Label(self.root, text=carOwnersList).grid(row = j,column = 1)
                    carOwnersList = ''
                    j+=1
            else:
                for i in carlist:
                    a = str(i)
                    cursor.execute('SELECT v.make, v.model, v.year, v.color, r.plate FROM vehicles v, registrations r WHERE v.vin = r.vin AND r.vin = ?', i)
                    ad = cursor.fetchall()
                    for b in ad:
                        for stuff in b:
                            carOwnersList += str(stuff)
                            carOwnersList += ' '
                    self.ownerButtons.append(Button(self.root, text=carOwnersList, command= lambda i1 = i: self.display_owner(i1,len(carlist))))
                    self.ownerButtons[j].place(relx = 0.5, rely =(j+1)/15 , anchor = CENTER) 
                    j+=1
                    carOwnersList = ''


    def display_owner(self,vin, numberOfButtons):
        global connection, cursor
        for cars in range(numberOfButtons):
            self.ownerButtons[cars].place_forget()
        display_owner_List = ''
        cursor.execute('SELECT v.make, v.model, v.year, v.color, r.plate, r.regdate, r.expiry, r.fname, r.lname FROM vehicles v, registrations r WHERE v.vin = r.vin AND r.vin = ?', vin)
        ad = cursor.fetchall()
        for b in ad:
            for stuff in b:
                display_owner_List += str(stuff)
                display_owner_List += ' '
        self.driver_details_traffic = Label(self.root, text=display_owner_List)
        self.driver_details_traffic.grid(row = 1,column = 1)
        display_owner_List = ''

        self.ttt_details = Button(self.root, text = "返回主菜单", command = self.ttt_details_finish)
        self.ttt_details.place(relx = 0.5, rely = 0.8, anchor = CENTER)


    def ttt_details_finish(self):
        self.driver_details_traffic.grid_remove()
        self.ttt_details.place_forget()
        self.traffic_main_menu()
        

    def insert_data(self, filename):
        global connection, cursor
        f = open(filename, 'r')
        f = f.readlines()
        for line in f:
            line = line.strip('\n')
            cursor.execute(line)
            connection.commit()


    def connect(self):
        global connection, cursor
        connection = sqlite3.connect(self.path)
        cursor = connection.cursor()
        cursor.execute(' PRAGMA forteign_keys=ON; ')
        connection.commit()
        return


    def drop_tables(self):
        global connection, cursor
        tables = ['demeritNotices', 'tickets', 'registrations', 'vehicles', 'marriages', 'births', 'persons', 'payments', 'users']
        for i in tables:
            cursor.execute('drop table if exists '+i+';')    
        
        connection.commit()
    
        
    def define_tables(self):
        global connection, cursor
        persons_query=   '''
                            create table persons (
                                        fname char(12),
                                        lname char(12),
                                        bdate date,
                                        bplace char(20), 
                                        address char(30),
                                        phone char(12),
                                        primary key (fname, lname)
                                        );
                        '''
    
        births_query=  '''
                            create table births (
                                        regno int,
                                        fname char(12),
                                        lname char(12),
                                        regdate	date,
                                        regplace char(20),
                                        gender char(1),
                                        f_fname char(12),
                                        f_lname	char(12),
                                        m_fname	char(12),
                                        m_lname	char(12),
                                        primary key (regno),
                                        foreign key (fname,lname) references persons,
                                        foreign key (f_fname,f_lname) references persons,
                                        foreign key (m_fname,m_lname) references persons
                                        );
                        '''
    
        marriages_query= '''
                        create table marriages (
                                    regno int,
                                    regdate date,
                                    regplace char(20),
                                    p1_fname char(12),
                                    p1_lname char(12),
                                    p2_fname char(12),
                                    p2_lname char(12),
                                    primary key (regno),
                                    foreign key (p1_fname,p1_lname) references persons,
                                    foreign key (p2_fname,p2_lname) references persons
                                    );
                    '''
        
        vehicles_query= '''
                       create table vehicles (
                                   vin char(5),
                                   make char(10),
                                   model char(10),
                                   year int,
                                   color char(10),
                                   primary key (vin)
                                   );
                        '''
        
        registrations_query= '''
                      create table registrations (
                                  regno int,
                                  regdate date,
                                  expiry date,
                                  plate char(7),
                                  vin char(5), 
                                  fname char(12),
                                  lname char(12),
                                  primary key (regno),
                                  foreign key (vin) references vehicles,
                                  foreign key (fname,lname) references persons
                                  );
                              '''
        
        tickets_query= '''
                      create table tickets (
                                  tno int,
                                  regno int,
                                  fine int,
                                  violation text,
                                  vdate date,
                                  primary key (tno),
                                  foreign key (regno) references registrations
                                  );
                        '''
        
        demeritNotices_query= '''
                     create table demeritNotices (
                                 ddate date, 
                                 fname char(12), 
                                 lname char(12), 
                                 points	int, 
                                 desc text,
                                 primary key (ddate,fname,lname),
                                 foreign key (fname,lname) references persons
                                 );
                               '''
        
        payments_query= '''
                           create table payments (
                                       tno int,
                                       pdate date,
                                       amount int,
                                       primary key (tno, pdate),
                                       foreign key (tno) references tickets
                                       );
                         '''
        
        users_query= '''
                        create table users (
                                    uid char(8),
                                    pwd char(8),
                                    utype char(1),
                                    fname char(12),
                                    lname char(12), 
                                    city char(15),
                                    primary key(uid),
                                    foreign key (fname,lname) references persons
                                    );
                      '''
        
        cursor.execute(persons_query)
        cursor.execute(births_query)
        cursor.execute(marriages_query)
        cursor.execute(vehicles_query)
        cursor.execute(registrations_query)
        cursor.execute(tickets_query)
        cursor.execute(demeritNotices_query)
        cursor.execute(payments_query)
        cursor.execute(users_query)
        connection.commit()
    
        return


def main():

    window = SQL(Tk())
    
main()
