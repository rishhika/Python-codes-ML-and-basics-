def mean(L):
    sum=0
    for x in L:
        sum+=x
        mean=sum/len(L)

    return mean
def median(L):
    L.sort()
    if len(L)%2!=0:
        median=L(int(len(L)/2))
    else:
        median = [L(int(len(L) / 2))-1]+L(int(len(L)/2))
        median=median/2
    return median
def mode(L):
    count=0
    num=L(0)

    for i in L:
        cf=L.count(i)
        if(cf>count):
            count=cf
            num=i
        if len(set(L))==len(L):
            print("There is no mode.")

numbers=[]
while(True):
    ask=input("Enter a number and type STOP to end.")

    if ask=='Stop':
        break
    numbers.append(int(ask))
    
mean=mean(numbers)
meadian=median(numbers)
mode=mode(numbers)

print('Mean= '+ mean+'/n'+'Median= '+ median+'/n'+'Mode= '+ mode+'/n')




