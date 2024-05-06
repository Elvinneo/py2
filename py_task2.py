#------------------------------TASK1-------------------------------------------------
'''
mylist=[-4,-16,0,1,4,5,9,16,25,36,49,64,81,100]
def ifsquare(list):
    result=[]
    for i in list:
        if i>0 and (i**0.5)%1==0:
            print("{} {} ededinin kvadratıdır.".format(i,int(i**0.5)))
ifsquare(mylist)
'''
#-------------------------------TASK2-------------------------------------------------
'''
mylist=input ('List daxil edin : ')
def ifnotrepeat(list):
    print("Tekrarsiz elementler :\n")
    for i in list:
        if list.count(i)==1:
            print(i)
ifnotrepeat(mylist)
'''

#-------------------------------TASK3------------------------------------------------
'''
vuruqlar=input("Vuruqlari daxil edin : ")
def conj(inp):
    a=1
    for i in inp.split(","):
        a=a*int(i)
    print("Cavab : {} ".format(a))
conj(vuruqlar)
'''
#-------------------------------TASK4------------------------------------------------
'''
eded=int(input("Eded daxil edin : "))
print(list(i for i in range(1,eded) if eded % i==0))
'''
#-------------------------------TASK5------------------------------------------------
'''
months=["Yanvar","Fevral","Mart","Aprel","May","Iyun","Iyul","Avqust","Sentyabr","Oktyabr","Noyabr","Dekabr"]
print(dict((i, len(i)) for i in months))
'''
#-------------------------------TASK6------------------------------------------------
'''
names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith","Elvin Abi]
print(list(i.split()[0].lower() for i in names))
'''
#-------------------------------TASK7------------------------------------------------
'''
list1=[2,5,9,7,6,3]
list2=[8,1,15,13,21,7]
result=[]
def average(nums1,nums2):
    for i,j in zip(nums1,nums2):
        result.append(int((i+j)/2))
    print(result)
average(list1,list2)
'''


























