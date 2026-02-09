import pandas as pd
s=pd.Series([10,20,30,40])
print(s)
s1=pd.Series([10,20,30,"abc"])
print(s1)
print(s.values)
print(s.index)

#Indexing
print(s[0])
print(s[0:2])

index=["apple","banana","orange","kiwi"]
s.index=index #needs to be of same size
print(s)
print("_________________")

#iloc->location based indexing--->for numerical indices
print(s.iloc[0])
print(s.iloc[[1,2]]) #double brackets for multiple

#loc->label based indexing--START AS WELL AS STOP VALUE INCLUDED IN OUTPUT
print(s.loc['kiwi'])
print(s.loc["apple":"orange"])

fruit_protein={
"avocado":2.0,
"banana":2.6,
"orange":3.2,
"kiwi":2.0,
"grapes":2.4,
"pomogrenate":3.5,
"mango":4.2,
"cherries":4.0}
s2=pd.Series(fruit_protein,name="protein")
print(s2)

#conditional selection
print(s2>3) #prints boolean-masked
print(s2[s2>3]) #pass masked series inside original series to print

#logical operators: and,or,not
print("______________")
print(s2[(s2>2.5)&(s2<3)])

#modifying series
s2["kiwi"]=2.8  #have to pass index
print(s2)


