#https://ithelp.ithome.com.tw/users/20111961/ironman/1795

print("//------------------------------------------------------")
# age=21 # 定義一個變數值為20

# if age>=20 : # 判斷變數值是否大於20
#     print("can vote") # 若大於20印出can vote
# else : # 變數值沒有大於20就執行else區塊
#     print("can't vote") # 進入else區塊後印出can't vote


# names=["bonny","jack","rose"] # 建立一個names串列
# for name in names : # 告知python從names串列中取出名字，並將取出的名字存到name變數中
#     if name=="bonny" : # 判斷如果name等於bonny
#         print(name.upper()) #等於bonny就把bonny變全部大寫 
#     else : # 如果name不等於bonny
#         print(name) #不等於bonny就直接把name印出
print("//Array------------------------------------------------------")

# fruits=["apple","banana","grape","pineapple"] # 建立一個fruits串列
# print(fruits) # 印出原本的fruits串列
# fruits.append("mango") # 新增一個"mango"元素到fruits串列尾端
# print(fruits) # 再印出新增元素後的fruits串列


# letters=["a","b","c","d"] # 建立一個letters串列
# letters.insert(0,"e") # 將"e"元素插入letters串列中的第一個位置
# print(letters) # 印出letters串列

# colors=["red","orange","yellow","green","blue"]
# print(colors[0:3]) # 印出索引足標0,1,2對應的元素
# print(colors[1:4]) # 印出索引足標1,2,3對應的元素
# print(colors[:2]) # 印出從索引足標0到1的元素
# print(colors[2:]) # 印出從索引足標2到最後的元素
# print(colors[-2:]) # 印出從索引足標-2(也就是倒數第二個)到最後的元素

# colors=["red","orange","yellow","green","blue"]
# for color in colors[1:3] : # 印出colors串列中索引足標1和2的元素
#     print(color)

print("//判斷式------------------------------------------------------")

# a = 5
# b = 6
# c = 4

# if a>c and b>a : # a>c和b>a都是正確敘述，所以會跳到下一行印出句子
#     print("Both conditions are True")

# if a>c or b<a :  # a>c是正確敘述，b<a是錯誤敘述，但因為or只要其中一個條件正確就可以通過，所以會跳到下一行印出句子
#     print("At least one of the conditions are True")       

# if True and True:
#     print(" True and True")

# if False and True:
#     print(" False and True")   

# if False or True:
#     print(" False or True")

print("//字典------------------------------------------------------")
# car = {
#     "color":"black",
#     "brand":"Toyota"
# } # 建立一個car字典裡面包含兩個鍵值對
# color = car["color"] # 將car字典中color鍵對應的值存到color變數內
# print("The car's color is "+color) # 印出color
# car["mileage"] = 10 # 新增一個鍵為"mileage"值為10到car字典
# print(car) # 印出新增鍵值對後的car字典

# del car["color"] # 刪除car字典中color鍵和它對應的值
# print(car) # 印出新增鍵值對後的car字典

print("//if else------------------------------------------------------")

# age = input("how old are you ?") # 使用者輸入的東西都算是字串  Readline

# number = int(age) # 將age變數轉成int的型態再傳回age變數中
# if number % 2 ==0 : # 判斷是否除2會整除
#     print("It's even") # 如果整除2就是偶數
# else :
#     print("It's odd") # 如果們有整除2就是奇數

# text = "apple banana apple grape apple apple watermelon" # 建立一個text字串
# find = input("which word do you want to find ?") # 輸入一個值存到find變數中

# print(text.count(find)) # 用count()方法來找find變數的值在text字串裡出現幾次

# scores=[] # 建立一個空的scores串列

# if scores : # 如果串列裡有東西
#     for score in scores : # 將scores串列裡的值一一存取到score變數內
#         print(score) # 一一印出score變數的值
#     print("completed!!") # 最後印出completed!!
# else :
#     print("list is empty") # 若串列是空的就跳到else區塊然後印出這行


print("//while------------------------------------------------------")

# text = "enter your name or enter 'quit' to leave the program : "
# while True : # 讓迴圈一直執行
#     name = input(text) # 印出text字串將輸入的值存到name變數中
    
#     if name == "quit" : # 當輸入quit時進入if區塊
#         break # 跳出迴圈
#     else :
#         print("Hello,"+name)  


# order=["hamburger","french fries","cola"]
# already_cooked=[]

# while order : # 如果order串列有東西while迴圈就會繼續執行
#     cooking=order.pop() # 將order串列的值一一彈出來存到cooking變數中
#     print("cooking :"+cooking)
#     already_cooked.append(cooking) # 將cooking變數的值新增到already_cooked串列中

# print("Finished :")
# for cooked in already_cooked : # 告知python從already_cooked串列中取出值，並將取出的值存到cooked變數中

#     print(cooked)

# text = ["apple", "banana", "apple", "grape", "apple", "apple", "watermelon"]

# while "apple" in text : # 當text串列中含有apple字串時，迴圈就會一直執行
#     # text.remove("apple") # 將text串列中的apple字串移除
#     a=text.index("apple")
#     print("apple in index :" + str(a))
#     del text[a]

# print(text)

# response={} # 建立一個空字典

# while True:
#     name=input("What's your name?")#console.write
#     place=input("Where would you want to go?")#console.write
#     response[name]=place # 建立name為鍵place為值的鍵-值對然後存到response字典中

#     continue_prompt = input("Would you like to let someone else respond? (yes/no)")
#     if continue_prompt=="no": # 如果continue_prompt=="no"就跳出迴圈
#         break
    
# for name,place in response.items(): # items()方法會讓for迴圈將每個鍵-值對分別存到name和place的變數中
#     print(name+" would like to go "+place)
    
print("//函式-------------------")

# def greet(name): # 在greet函式放入name去接收任意值，在這裡是接收到"Weiting"
#     print("hello,"+name)
    
# greet("Weiting") # 呼叫greet()函式

# # def pets(pet_name,pet_type): # 定義pets函式需要兩個引數
# #     print("I have a "+pet_type+" and its name is "+pet_name)
# def pets(pet_name,pet_type="dog"): 
#     print("I have a "+pet_type+" and its name is "+pet_name)
# #以下是函式的多次呼叫，只要在呼叫一次函式它就會印出對應的值
# pets("dog","tony") # 將dog引數放入pet_type參數中、tony引數放入pet_name參數中
# pets("cat","candy")
# pets("cat")
# pets(pet_type="dog",pet_name="tony") # 明確的指出pet_type對應dog、pet_name對應tony 
# pets(pet_name="tony") # 預設pet_type是dog所以只要傳入pet_name就好
# pets(pet_name="candy",pet_type="cat") # 如果不是dog的話就傳入新的pet_type它就不會使用預設值

# print("//函式  傳入陣列-------------------")

# def get_name(names):
#     for name in names:
#         print("hello,"+name)
        
# usernames=["bonny","steven","jack","rose"]
# get_name(usernames) # 將usernames串列傳入get_name函式中

# print("//函式  傳入陣列特別用法-------------------")

# def get_name(*names): # *names參數中的星號會讓python建立一個名字為names的空多元組
#     for name in names:
#         print("hello,"+name)
    
# get_name("bonny","steven")
# get_name("jack")
# get_name("rose","john","jane")

# def users(first_name,last_name,**user_info): # **user_info參數中的星號會讓python建立一個名字為user_info的空字典
#     user={}  
#     user["first"]=first_name # 將first_name新增至user字典
#     user["last"]=last_name # 將last_name新增至user字典
#     for key,value in user_info.items(): # 用迴圈遍訪user_info裡的鍵值對並將其新增至user字典
#         user[key]=value
#     return user
    
# user1=users("bonny","chang",city="taipei")
# print(user1)
# user2=users("steven","chang",city="taoyuan")
# print(user2)

# def users(*first_name,**user_info): # **user_info參數中的星號會讓python建立一個名字為user_info的空字典
#     user={}  
#     for aa in first_name:
#         print(aa)
#     for key,value in user_info.items(): # 用迴圈遍訪user_info裡的鍵值對並將其新增至user字典
#         user[key]=value
#     return user
    
# user1=users("bonny","chang",city="taipei",city2="taipei2")
# print(user1)
# user2=users("steven","chang",city="taoyuan")
# print(user2)

# car = {
#     "color":"black",
#     "brand":"Toyota"
# } # 建立一個car字典裡面包含兩個鍵值對
# color = car["color"] # 將car字典中color鍵對應的值存到color變數內
# print("The car's color is "+color) # 印出color
# car["mileage"] = "10" # 新增一個鍵為"mileage"值為10到car字典
# print(car) # 印出新增鍵值對後的car字典

# def get_dic(names):
#     for value ,a in names.items():
#         print("hello,"+a)
# get_dic(car) # 將usernames串列傳入get_name函式中


print("//import -------------------")
# import name

# name.get_name("bonny")
# name.get_city("taipei")

# from name import get_name as gn

# gn("bonny")
# gn("taipei")

# from name import *

# get_name("bonny")
# get_city("taipei")

print("//Clase -------------------")

# class Dog(): # 建立一個Dog類別 self 相當tihs
#     def __init__(self,name,age): 
#         self.name=name # 取得name參數中的值並將其存入name變數中
#         self.age=age # 取得age參數中的值並將其存入age變數中
#         self.age2=age # 取得age參數中的值並將其存入age2變數中
#         self.age3=0
#         self.sex="male"
#     def eat(self): # 定義一個eat方法
#         print(self.name + " is eating")
        
#     def sleep(self): # 定義一個sleep方法
#         print(self.name + " is sleeping")

#     def reage(self): # 定義一個run方法
#         self.age3=self.age2
        
# dog1=Dog("tony",3) # 建立一個dog1實例
# dog1.name="QOOO"
# print("My dog's name is "+dog1.name+" and it's "+str(dog1.age2)+" years old.")
# print("My dog's sex is "+dog1.sex)
# dog1.eat() # 呼叫eat方法
# dog1.sleep() # 呼叫sleep方法
# print("My dog's age is "+str(dog1.age3))
# dog1.reage()
# print("My dog's age is "+str(dog1.age3))

print("//Clase 繼承 -------------------")

# # from car import Car # import陳述句會讓python開啟car模組並匯入Car類別
# from car import Car,ElectricCar # import陳述句會讓python開啟car模組並匯入Car和Electric類別
# ecar1 = ElectricCar(2018,"toyota","black")
# ecar1.get_name()
# ecar1.miles=90
# ecar1.money=30
# ecar1.spendmoney()
# ecar=Car(2018,"toyota","black")
# ecar.fill_gas()
# ecar1.fill_gas()

# import car 
# ecar2 = car.ElectricCar(2019,"toyota","black")
# ecar2.miles=10
# ecar2.money=20
# ecar2.spendmoney()

print("//read file and write file-------------------")

# #如果檔案不釋放在同個資料夾中的話記得要給完整路徑才能讀取喔!
# #原本内容
# #123
# #456
# #789
# with open("number.txt") as file_object: # 開啟number.txt檔並將其存到file_object中
#     content=file_object.read() # 讀取file_object的所有內容
#     print(content.rstrip()) # 將印出的檔案刪除read()返回的一行空白

# with open("C://Python//number.txt") as file_object: # 開啟number.txt檔並將其存到file_object中
#     for line in file_object: #可用回圈處理
#         print(line)
# with open("C://Python//number.txt") as file_object: # 開啟number.txt檔並將其存到file_object中       
#     for line2 in file_object: #可用回圈處理
#         print(line2.rstrip())    

# # w	 讀取模式	r寫入模式 	a附加檔案 	r+可讀取寫入模式		

# filename="number.txt" 

# with open(filename,"w") as file_object: # 以寫入模式開啟number.txt檔
#     file_object.write("9487") # 寫入第一行
#     file_object.write("666") # 寫入第二行         

# filename="number.txt"

# with open(filename,"a") as file_object: # 以附加模式開啟number.txt檔
#     file_object.write("01234")
#     file_object.write("56789")    

 
print("//catch-------------------")   
# while True:
#     first=input("First number :")
#     second=input("Second number :")
#     try:
#         ans=int(first)/int(second) # 因為input都是字串所以要轉int才能相除
#     except ZeroDivisionError:
#         print("You can't divide by zero")
#     else:
#         print(ans) # 若沒有出錯就印出兩個值相除
#         break # 跳出迴圈
# filename="alice.txt"

# try:
#     with open(filename) as file:
#         contents=file.read()
# except FileNotFoundError: # 如果找不到檔案會執行這個區塊
#     pass # 出錯時直接略過這個區塊
#     msg="Sorry,the file "+filename+" does not exist"
#     print(msg)
# else: # 找到檔案會執行這個區塊
#     find=input("find the word :")
#     print(contents.count(find))     
#    
print("//儲存資料-------------------")   

# import json

# numbers=[1,2,3,4,5,6] 

# filename="number.json" # 指定要把numbers串列存到number.json檔中
# with open(filename,"w") as file: # 以寫入模式開啟檔案才可以將資料儲存進去
#     json.dump(numbers,file) # 將numbers串列存到number.json檔    

# filename="number.json" # 這行我們要確定是不是跟前面的讀取檔案名稱相同
# with open(filename) as file: # 以讀取模式開啟檔案(若沒有第二個參數都是預設成讀取模式)
#     numbers=json.load(file) # 用json.load()載入放在number.json檔裡面的資料，然後將它存到numbers變數中

# print(numbers)    

print("//Django-------------------")   
# mkdir learning_log
# cd learning_log
# python -m venv learning_log
# learning_log\Scripts\activate
# 之後就會出現 (learning_log) C:\Users\ASUS\learning_log> 這個東西
# pip install Django
# django-admin.py startproject learning_log .
# dir learning_log
# python manage.py migrate
# dir 出現 db.sqlite3
# python manage.py runserver
# Starting development server at http://127.0.0.1:8000/ 為專案位置
# python manage.py startapp learning_logs
# learning_logs/models.py 新增
#--------------
# from django.db import models
# #Create your models here.

# class Topic(models.Model):
#     text=models.CharField(max_length=100)
#     date_added=models.DateTimeField(auto_now_add=True)
    
#     def __str__(self):
#         return self.text # 返回儲存在text屬性中的字串
#-----------------------
#learning_log/setting.py檔，然後找到INSTALLED_APPS 新增
#INSTALLED_APPS = [
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#     'learning_logs', # 新增區塊
# ]
# python manage.py makemigrations learning_logs
# python manage.py migrate
# python manage.py 