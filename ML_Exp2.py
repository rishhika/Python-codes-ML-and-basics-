import pandas as pd

d1 = pd.DataFrame([[10, 20], [21, 28], [8, 12],
                   [10, 15], [7, 15], [9, 2]],
                  columns=['Speed', 'Distance'],
                  index=['Data1', 'Data2','Data3', 'Data4','Data5', 'Data6'])
d2=pd.DataFrame({'Speed':[65,33,90,99,70,34,58,76,23,100],'Distance':[94,89,89,83,78,74,84,57,86,99]})


print("\n----------- Calculating Mean -----------\n")
print(d1.mean())

print("\n----------- Calculating Median -----------\n")
print(d1.median())

print("\n----------- Calculating Mode -----------\n")
print(d1.mode())

print("\n----------- Calculating Standard Deviation -----------\n")
print(d2.std())