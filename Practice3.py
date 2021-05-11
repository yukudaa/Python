#Q1
#shirt
#Q2
i = 1
while i<1000:
    if(i %3 == 0):
        print(i)
    i += 1

#Q3
i = 0
while True:
    i += 1
    if i > 5 : break
    print('*' * i)
#Q4
for i in range(1,101):
    print(i)
#Q5
num = 0
test = [70,60,55,75,95,90,80,80,85,100]
for i in test:
    num += i
avg = num / len(test)
print(avg)
    
