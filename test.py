import math

def chec_sochinhphuong(n):#1. Viết chương trình kiểm tra số nguyên n nhập vào là số chính phương hay không
    #for i in range(1,n):
    #    if(i*i == n):
    #        print("n là số chính phương")
    #        break
    #else:
    #    print('không phải là số chính phương')
    #a = math.sqrt(n)
    #if a - int(a) == 0:return True 
    #return False
    if int(math.sqrt(n))**2 == n: return True
    return False
    
#2. Viết chương trình tìm số lớn nhất trong 3 số nguyên a, b, c nhập vào
def max3(a,b,c):
    max = a
    if max > b: max = b
    if max > c: max = c
    return mx

#3. Viết chương trình giải phương trình bậc 1: ax+b=0
def solveFisrtEquation(a,b):
    if a ==0:
        if b == 0:print(" pt vô số nghiệm")
        else: print("phương trình vô nghiệm")
    else:
        print(" phương trình có nghiệm là ",-b/a)

#4. Viết chương trình giải phương trình bậc 2: ax2+bx+c=0 (hệ số a#0)
def solveSecondEquation(a,b,c):
    if a == 0:
        solveFisrtEquation(b,c)
    else:
        delta = b*b - 4*a*c
        if delta < 0 :
            print("phương trình vô nghiệm")
        elif delta ==0:
            print("phương trình có nghiệm kép là ",-b/2*a)
        else:
            print("phương trình có hai nghiệm là  x1: %.2f và x2: %.2f" %((-b+math.sqrt(delta))/(2*a),(-b-math.sqrt(delta))/(2*a)))
#5. Viết chương trình in ra màn hình các số nguyên lẻ nằm trong khoảng từ 1 đến n (nnhập vào)
def printOddsNumber(n):
    for i in range(1,n+1,2):
        print(i,end =" ")
#6. Viết chương trình tính tổng các số nguyên lẻ từ 1 đến n (n nhập vào)
def sumOddsNumber(n):
    s = 0
    for i in range(1,n+1,2):
        s += i
    return s
#7. Viết chương trình tính tổng các số nguyên chia hết cho 3 nằm trong khoảng từ 1đến n (n nhập vào)
#8. Viết chương trình tính n! (n nhập vào)
def factorial(n):
    fac = 0
    for i in range(1,n+1):
        fac *= i
    return fac
#9. Viết chương trình in ra bảng cửu chương n (1&lt;=n&lt;=10)
def multiplication(m,n):
    for j in range(1,11):
        for i in range(m,n):
            print('%2i*%2i=%2i'%(i,j,i*j),end=" ")
        print()
#10. Viết chương trình in ra màn hình các số nguyên tố nằm trong khoảng từ 1 đến n (n nhập vào) 
# 11. Viết chương trình in ra màn hình các số nguyên tố nằm trong khoảng từ 1 đến n (n nhập vào) 
# 12. Viết chương trình in ra màn hình các số nguyên tố nằm trong khoảng từ 1 đến n (n nhập vào) 
# 13. Viết chương trình in ra màn hình các số nguyên tố nằm trong khoảng từ 1 đến n (n nhập vào) 
# 14. Viết chương trình in ra màn hình các số nguyên tố nằm trong khoảng từ 1 đến n (nnhập vào)
#15. Viết chương trình In ra dãy số Fobonaxia. 2  3  5  8  13  …  N (N nhập vào)
def fibonacci(n):
    fibo = [1, 1]
    for i in range(2,n+1):
        fibo.append(fibo[i-1]+fibo[i-2])
    return fibo
#16. Viết chương trình đổi năm dương lịch sang năm âm lịch


def isPerfectNum(num):# kiểm tra số  hoàn hảo
    total = 1
    for i in range(2,num):
        if (num % i == 0):
            total +=i
    if total == num:
        return True
    return False
def isPrime(num): #kiểm  tra số nguyên tố
    for i in range(2,n):
        if (num % i == 0):
            return False
    return True