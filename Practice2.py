#Q1
korea = 80
english = 75
math = 55
avg = (korea + english + math)/3
print(avg)
#Q2
num = 13 
if num % 2 == 0 :
    print("짝수")
else :
    print("홀수")
#Q3
hong = "881120-1068234"
hong = "99" + hong
print(hong[:8])
#Q4
pin = "881120-1068234"
print(pin[7])
#Q5
a = "a:b:c:d"
a = a.replace(":","#")
print(a)
#Q6
list = [1,3,5,4,2]
list.sort()
list.reverse()
print(list)
#Q7
list = ['Life','is','too','short']
print(" ".join(list))
#Q8
tuple1 = (1,2,3)
tuple2 = (4,)
print(tuple1 + tuple2)
#Q9
#리스트는 그 값이 변경할수 있기 때문에 3번은 오류가 발생한다.
#Q10
a = {'A':90, 'B':80, 'C':70}
print(a.pop('B'))
#Q11 ##################################################
#a = [1,1,1,2,2,3,3,3,4,4,5]
#aset = set(a)
#b = list(aset)
#print(b)
#Q12
a = b = [1,2,3]
a[1] = 4
print(b)
