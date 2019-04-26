import random
random.random()

list = []   #宣告list
count = 0   #計數器
arrayLength=random.randint(0,9)
while count < arrayLength:
    mun=random.randint(0,9)
    list.append(mun)    
    print ("塞入數字：",mun)
    count1 = 0   #計數器
    while count1 < len(list)-1:
        if(list[count1]==mun and count !=0):
            print("重複刪除：",list[count1])
            del list[count1]
            count=count-1
        count1 = count1 + 1   #更新計數器       
    count = count + 1   #更新計數器
    
print ("最後")
for iterating_var in list:
   print (iterating_var,end='')

def users(*first_name,**user_info): # **user_info參數中的星號會讓python建立一個名字為user_info的空字典
    user={}  
    for aa in first_name:
        print(aa)
    for key,value in user_info.items(): # 用迴圈遍訪user_info裡的鍵值對並將其新增至user字典
        user[key]=value
    return user
    
user1=users("bonny","chang",city="taipei",city2="taipei2")
print(user1)
user2=users("steven","chang",city="taoyuan")
print(user2)

