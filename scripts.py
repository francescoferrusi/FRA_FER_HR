    #Say "Hello, World!" With Python
if __name__ == '__main__':
    print("Hello, World!")
    
    
    #Python If-Else
    #!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
if n%2 == 1:
    print('Weird')
elif n>20:
    print('Not Weird')
elif 1<n<6:
    print('Not Weird')
else :
    print('Weird')
    
   # Arithmetic Operators
  if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a+b)
    print(a-b)
    print(a*b)
    
    
    #Python: Division
    if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a//b)
    print(a/b)
    
    #Loops
    if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i*i)
        
    #Write a function
    def is_leap(year):
    leap = False
    if (year%400 == 0) or (year%4 == 0 and year%100 != 0):
        leap = True
    return leap
        
    #Print Function
    if __name__ == '__main__':
    n = int(input())
    r=0
    if n<10:
        for i in range(n+1):
            r = 10*r+ i
        print(r)
    elif n< 100:
        for i in range(10):
            r = 10*r+ i
        for i in range(10,n+1):
            r = 100*r + i
        print(r)    
    else:
        for i in range(10):
            r = 10*r+ i
        for i in range(10,100):
            r = 100*r + i
        for i in range(100,n+1):
            r = 1000*r + i
        print(r)
        
        
       #List Comprehensions
      if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    listx= [i for i in range(x+1)]
    listy =[i for i in range(y+1)]
    listz = [i for i in range(z+1)]
    list=[]
    for c1 in listx:
        for c2 in listy:
            for c3 in listz:
                list.append([c1,c2,c3])
    list=[k for k in list if ((k[0]+k[1]+k[2])!=n )]
    print(list)
    
    
    #Find the Runner-Up Score!
    if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr=list(arr)
    s=-101
    f=arr[0]
    parimerito=True
    for i in range(1,len(arr)):
        if arr[i]!=arr[i-1]:
            parimerito=False
    if parimerito:
        print(f)
    else:
        for i in range(1,len(arr)):
            if f < arr[i]:
                f = arr[i]
        for i in range(len(arr)):
            if (s <arr[i]<f):
                s= arr[i]
        print(s)
        
   #Lists
  if __name__ == '__main__':
    N = int(input())
    l=[]
    for i in range(N):
        cmd=input().split()
        if len(cmd)==3:
            l.insert(int(cmd[1]),int(cmd[2]))
        elif cmd[0]=='print':
            print(l)
        elif cmd[0]=='remove':
            l.remove(int(cmd[1]))
        elif cmd[0]=='append': 
            l.append(int(cmd[1]))   
        elif cmd[0]=='sort':   
            l.sort() 
        elif cmd[0]=='pop':
            l.pop()    
        elif cmd[0]=='reverse': 
            l.reverse()
            
            
      #Birthday Cake Candles
      #!/bin/python3

import math
import os
import random
import re
import sys

def birthdayCakeCandles(candles):
    # Write your code here
    t=candles[0]
    i=1
    for c in range(1,len(candles)):
        if t==candles[c]:
            i=1+i
        elif candles[c]>t:
            t=candles[c]
            i=1 
    return i                
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()
    
    
    #Number Line Jumps
    #!/bin/python3

import math
import os
import random
import re
import sys

def kangaroo(x1, v1, x2, v2):
    # Write your code here
    dx= x1-x2
    dv= v1-v2
    if dv==0:
        return'NO'
    t=-dx/dv
    if t%1==0 and t>=0 :
       return 'YES'
    else:
       return 'NO'
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
    
    
    #Viral Advertising
    #!/bin/python3

import math
import os
import random
import re
import sys

def viralAdvertising(n):
    r=2
    c=2
    for i in range(n-1):
        r=(r*3)/2 -((r*3))/2%1 
        c=c+r
    return int(c)    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
    
    
    #Recursive Digit Sum
    #!/bin/python3

import math
import os
import random
import re
import sys

def superDigit(n, k):
    # Write your code here
     cifre=list(str(sum([int(i) for i in list(n)])*k))
     c=10
     while c>9:
        c=sum([int(i) for i in cifre])
        cifre=list(str(c))
     return c            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
    
    
    #Nested Lists
    if __name__ == '__main__':
    lisn=[]
    liss=[]
    lsort=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        lisn.append(name)
        liss.append(score)
    l=liss[0]
    parimerito=True
    for i in range(1,len(liss)):
        if liss[i]!=liss[i-1]:
            parimerito=False
    if  parimerito:
        for n in sorted(lisn) :
            print(n)
    else:
     s=liss[len(liss)-1]
     c=1
     while s==l:
         s=liss[c]
         c+=1            
     for i in range(1,len(liss)):
            if liss[i]<l:
                l=liss[i]           
     for i in range(len(liss)):
            if l<liss[i]<s:
                s=liss[i]           
     for n in range(len(lisn)):
            if liss[n]==s:
                lsort.append(lisn[n])
     for n in sorted(lsort):
         print(n)
        
        
        #Finding the percentage
    if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    m=(sum(student_marks[query_name]))/3 
    print("{:.2f}".format(m))
    
    
    #Insertion Sort - Part 1
    #!/bin/python3

import math
import os
import random
import re
import sys

def insertionSort1(n, arr):
    num_ins=arr[n-1]
    i=n-2
    while num_ins <arr[i] and i>-1:
            arr[i+1]=arr[i]
            s=str(arr[0])
            for j in range(1,n):
                s+=' '+str(arr[j])
            print(s)
            i+=-1
    arr[i+1]=num_ins
    s=str(arr[0])
    for j in range(1,n):
                s+=' '+str(arr[j])
    print(s)        
 if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
    
    
    #Insertion Sort - Part 2
    #!/bin/python3

import math
import os
import random
import re
import sys

def insertionSort2(n, arr):
    # Write your code here
    j=1
    while j in range(1,n) and j<n:
        num_ins=arr[j]
        i=j-1
        while num_ins<arr[i] and i>-1:
            arr[i+1]=arr[i]
            i+=-1 
        arr[i+1]=num_ins
        s=str(arr[0])
        for l in range(1,n):
            s+=' '+str(arr[l])
        print(s)
        j+=1
        
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
    
    
    #sWAP cASE
   def swap_case(s):
    letters=list(s)
    for i in range(len(letters)):
        if letters[i].isupper():
           letters[i]=letters[i].lower()
        else:
           letters[i]=letters[i].upper()
    result=''       
    for i in letters:
        result+=str(i)      
    return result
  
  
  #String Split and Join
  def split_and_join(line):
    # write your code here
    string_list=line.split()
    result='-'.join(string_list)
    return result
  
  
  #What's Your Name?

def print_full_name(first, last):
    string='Hello '+first+' '+last+'! You just delved into python.'
    print(string)
    
    
    #Mutations
   def mutate_string(string, position, character):
    string_mod=string[:position]+character+string[(position+1):]
    return string_mod
  
  
  #Find a string
  def count_substring(string, sub_string):
    count=0
    i=0
    if (len(string)-len(sub_string))==0:
        j=0
        boolean=True
        while j in range(0,len(sub_string)) and boolean:
            if string[i+j]!=sub_string[j]:
                boolean=False
            j+=1
        if boolean:
            return 1
    while i in range(0,(len(string)-len(sub_string))+1):
        j=0
        boolean=True
        while j in range(0,len(sub_string)) and boolean:
            if string[i+j]!=sub_string[j]:
                boolean=False
            j+=1
        if boolean:
            count+=1
        i+=1            
    return count
  
  
  #String Validators
  if __name__ == '__main__':
    s = input()
    alphanum=False
    alpha=False
    num=False
    lower=False
    upper=False
    i=0
    while i in range(len(s)) and  (not(alpha and num and lower and upper)):
       if s[i].isalpha() and (not alpha):
           alpha=True  
       if s[i].isdigit() and (not num):
           num=True
       if s[i].isupper() and (not upper):
           upper=True
       if s[i].islower() and (not lower):
           lower=True
       i+=1   
    if alpha or num:
        alphanum=True
    print(alphanum)
    print(alpha)  
    print(num)  
    print(lower)  
    print(upper)
    
    
    #Text Alignment
thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))
    
    
  #Text Wrap 
  def wrap(string, max_width):
    times=round(len(string)/max_width)
    result=string[:max_width]
    for i in range(1,times):
        result+='\n'+string[i*(max_width):(i+1)*max_width]
    result+='\n'+string[max_width*(times):]
    return result
  
  
  #Designer Door Mat
 
N, M = map(int, input().split())
core='.|.'
result=core.center(M,'-')
j=3
for i in range(2,int((N-1)/2)+1):
    result +='\n'+(core*j).center(M,'-')
    j+=2
result+='\n'+('WELCOME').center(M,'-')
j=j-2
for i in range(int((N-1)/2),0,-1):
    result+='\n'+(core*j).center(M,'-')
    j+=-2
print(result)


#String Formatting
def print_formatted(number):
    distance=len(str(bin(number))[2:])+1
    for i in range(1,n+1):
        print((str(i)).rjust(distance-1)+(str(oct(i))[2:]+(str(hex(i).upper())[2:]+(str(bin(i))[2:]).rjust(distance)).rjust(distance*2)).rjust(distance*3))
        
  
  
  #Alphabet Rangoli
  import string
def print_rangoli(size):
 alphabet=string.ascii_lowercase #2*(n-1)*2+1
 result_up=alphabet[size-1].center((size-1)*4+1,'-')
 if size==1:
        print(result_up)
 else:       
  for j in range(size-2,-1,-1):
        core=alphabet[j]
        for i in range(j+1,size):
          core= (alphabet[i]+'-'+core+'-'+alphabet[i])
        result_up+='\n'+(core).center((size-1)*4+1,'-')
  result_down=alphabet[size-1].center((size-1)*4+1,'-')
  for j in range(size-2,0,-1):
        core=alphabet[j]
        for i in range(j+1,size):
          core= (alphabet[i]+'-'+core+'-'+alphabet[i])
        result_down=(core).center((size-1)*4+1,'-')+'\n'+result_down
  result= result_up+'\n'+result_down    
  print(result)
  
  
  #Capitalize!
def solve(s):
   letters=[s[0].upper()]
   for i in range(1,len(s)):
      if s[i-1]==' ':
        letters.append(s[i].upper())
      else:
        letters.append(s[i])
        result=''
   for i in range(len(s)):
        result+=letters[i]
   return result 


#The Minion Game
def minion_game(string):
    vowels={'A','E','I','O','U'}
    n=len(string)
    count_consonants=0
    count_vowels=0
    for i in range(len(string)):        
        if string[i] in vowels:
            count_vowels+=n-i#len(string[i:])
        else:
            count_consonants+=n-i#len(string[i:])
    if count_consonants<count_vowels:
        print('Kevin '+str(count_vowels))
    elif count_consonants>count_vowels:
        print('Stuart '+str(count_consonants))
    else:
        print('Draw')
        
        
        #Merge the Tools!
   def merge_the_tools(string, k):
    len_substring=round(len(string)/k)
    for i in range(len_substring):
        substring_t=list(string[i*k:(i+1)*k])
        letters0=set()
        len_dynamic=len(substring_t)
        j=0
        while j <len_dynamic:
            if substring_t[j] in letters0:
                (substring_t).pop(j)
                len_dynamic+=-1
                j+=-1
            letters1=letters0|{substring_t[j]}
            letters0=letters1
            j+=1
        substring_u=''    
        for i in substring_t:
            substring_u=substring_u+ i    
        print(substring_u)
        
        
        #Introduction to Sets
   def average(array):
    distinct_h=list(set(arr))
    average=sum(distinct_h)/len(distinct_h)
    return "{:.3f}".format(average)
  
  
  #Symmetric Difference
size_1=int(input())
set_1=set(map(int,input().split()))
size_2=int(input())
set_2=set(map(int,input().split()))
sym_diff=list((set_1.union(set_2)).difference(set_1.intersection(set_2)))
for i in sorted(sym_diff):
    print(i)
    
    
    #No Idea!
n_m=list(map(int,input().split( )))
array=list(map(int,input().split()))
set_A=set(map(int,input().split()))
set_B=set(map(int,input().split()))
happiness=0
for i in array:
    if i in set_A:
        happiness+=1
    elif i in set_B:
        happiness+=-1
print(happiness)


#Set .add()
n=int(input())
country=set()
for i in range(n):
    country.add(str(input()))
print(len(country)) 


#Set .discard(), .remove() & .pop()
n = int(input())
s = set(map(int, input().split()))
N=int(input())
for i in range(N):
    command=list(map(str,input().split()))
    if command[0]=='pop':
       s.pop()
    elif command[0]=='remove':
        s.remove(int(command[1]))
    elif command[0]=='discard':
        s.discard(int(command[1]))
print(sum(list(s))) 


#Set .union() Operation
english=int(input())
roll_num_en=set(map(int,input().split( )))
french=int(input())
roll_num_fr=set(map(int,input().split( )))
print(len(roll_num_en.union(roll_num_fr)))


#Set .intersection() Operation
N_eng=int(input())
eng_roll=set(map(int,input().split()))
N_fre=int(input())
fre_roll=set(map(int,input().split()))
print(len(eng_roll.intersection(fre_roll)))


#Set .difference() Operation
n_eng=int(input())
eng_roll=set(map(int,input().split()))
n_fre=int(input())
fre_roll=set(map(int,input().split()))
print(len(eng_roll.difference(fre_roll)))


#Set .symmetric_difference() Operation
n_eng=int(input())
eng_roll=set(map(int,input().split()))
n_fre=int(input())
fre_roll=set(map(int,input().split()))
print(len((eng_roll.union(fre_roll)).difference(eng_roll.intersection(fre_roll))))


#Set Mutations
len_A=int(input())
set_A=set(map(int,input().split()))
N=int(input())
for i in range(N):
    command=list(map(str,input().split()))
    set_cmd=set(map(int,input().split()))
    if command[0]=='intersection_update':
        set_A.intersection_update(set_cmd)
    if command[0]=='update':
        set_A.update(set_cmd)
    if command[0]=='symmetric_difference_update':
        set_A.symmetric_difference_update(set_cmd)
    if command[0]=='difference_update':
        set_A.difference_update(set_cmd)    
print(sum(list(set_A)))


  
  
        

    
  
    
    
        
    
    
    
    
    
        
        
    
    
    
    
