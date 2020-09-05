'''
orders = [2.50, 4.50, 2.00, 2.75, 2.50, 5.00, 8.00, 2.25]

average = sum(orders) / len(orders)

print("The average coffee order price today is $" + str(round(average, 2)))
'''
'''
no_list = [22,68,90,78,90,88]

def average(x):
    #complete the function's body to return the average
    average = sum(no_list) / len(no_list)
    return
print(round(average, 2))
'''
def averageOfList(num):
    sumOfNumbers = 0
    for t in num:
        sumOfNumbers = sumOfNumbers + t

    avg = sumOfNumbers / len(num)
    return avg


print("The average of List is", averageOfList([19, 21, 46, 11, 18]))