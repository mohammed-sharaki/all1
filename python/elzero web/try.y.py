'''
tuple1="mohamemd","aasem"
tuple2=("aasem",10)
print(type(tuple1))
print(type(tuple2))
tuple3=[1,2,3,4,5]
tuple3[0]="5"
print(tuple3)
mystrig="mohammed"
mylist=[1,2]
mytuple="mohammed","ahmed"
print(mystrig*2)
print(mytuple*2)
print(mylist *2)
'''
'''
print('___________________set___________________')
#set
#{}بتتفتح كده 
#كش مرتبه خالص
#مفيش فيها index
#مفيش فيها سليس
#ممكن تخزن فيها [numbers string  tuple ] #not list dic 
#بتحذف اي حاج مكرره 
mysetone={"mohamemd"}
print(mysetone)
mysettwo={"mohamemd",100}
print(mysettwo)
#set methods
#clear()
mysetthree={1,2,3}
mysetthree.clear()
print(mysetthree)
#union
a={1,2,3,4}
b={5,6,7}
print(a|b)
#add()
d={1,2,3,4,5}
d.add(5)
print(d)'''
'''
r={1,2,3}
m={1,5,6}
print(r.intersection_update(m))
print(r)
'''
'''
#diffrunt of issuperset issubset  
#issuperset start from back to face 
#issubset start from face to back
r={1,2,3,4,5,6,7}
t={1,4,5,7}
print(r.issuperset(t))

a={1,2,3,4}
m={1,2,3,4,5,6}
print(a.issubset(m))
'''
'''
thename=input("what is your name : ")
theemail=input("enter the your email : ")

print(f"hello {thename} your email {theemail} ")

'''
#================peractis age==============
#input age 
age=int(input("enter you age : "))

#get ag ein all time
mounth= age*12
week=mounth*4
day=age*365
hour=day*24
minetes=hour*60
sec=hour*60
print("you are live for : ")
print(f"{mounth} mounth.")
print(f"{week} week.")
print(f"{day:,} day.")
print(f"{hour:,} hour.")
print(f"{minetes:,} minetes.")
print(f"{sec:,} sec.")

