def max_num(num1, num2, num3):
    if num1 >=num2 and num1>=num3:
         return num1
    elif num2>=num1 and num2 >= num3:
         return num2 
    else:
         return num3
print(max_num(120, 400, 200))
print(max(2, 4, 2000))
#دي غير العك اليي فوق
def match_string(str1, str2):
    if str1 == str2:
        print("the string do match")
    else:
        print("the string dont match")
match_string("mohammed" , "mohammed")        
print ("bild a calculator")
print("_________________________________________")
operator = input("please enter the operator : ")
num1= float (input ("please enter the frist number : "))..





num2 = float (input ("please enter the sacund number : "))

if operator == "+":
    print(num1+num2)
elif operator == "*":
    print(num1*num2)
elif operator == "/":
    print(num1/num2)
elif operator == "-":
    print(num1-num2)
else:
    print("wrong operator please try again")

#print("المعجم")
print("____________________________________")
key_words=input( "enter the key words : " )
convert_month = {
    "jan" : "junary" ,
    "feb" : "febraury",
    "mar" : "march"
}
print(convert_month[key_words])
g = "I Love Python"
h = "i lOVE pYTHON"
i = "I Love Python"
#startwith
#هل بيبداالحرف الاول ب كذا
print(i.startswith("I"))
print(i.startswith("S"))
print(i.startswith("P", 7, 12))