import pandas as pd
data = {
    "Roll Number": [1,2,3,4,5,6,7,8,9,10],
    "Name": ["Asha","Ravi","Meera","Kiran","Sita","Arjun","Lata","Vikram","Nina","Raj"],
    "Gender": ["F","M","F","M","F","M","F","M","F","M"],
    "Marks1": [55, 72, 38, 90, 67, 45, 88, 76, 59, 81],
    "Marks2": [60, 35, 78, 92, 40, 25, 85, 66, 55, 89],
    "Marks3": [70, 80, 65, 88, 55, 60, 95, 72, 68, 77]
}
df = pd.DataFrame(data)
print(df)

print(df.head(2)) #first 2 rows
print(df.tail(3)) #last 3 rows

#loc and iloc
print(df.iloc[1:3]) #prints all columns for the selected rows
print(df.iloc[1:3,:2]) #rows,columns

print(df.loc[1:2,["Name","Gender"]]) #loc for specific columns since it's label based

print(df["Name"]) #print only specific column
print(df[["Name","Gender"]])

#drop
print(df.drop("Gender",axis=1))  #drops the whole column since axis is 1
#DRAWBACK-when you print dataframe, won't reflect in it
print(df)
df.drop("Marks2",axis=1,inplace=True) #performs operation in original dataframe
print(df)

print(df.shape) #index not counted as part of column
#rows->samples-->sample size here=10
#columns->features

print(df.info())

print(df.describe()) #statistical info on dataset

#BROADCASTING
#broadcasts the scalar to match the shape and size of particular column and then performs operation
df["Marks1"]=df["Marks1"]+10
print(df["Marks1"])

#RENAMING COLUMN
df.rename(columns={"Marks1":"Marks"},inplace=True)
print(df)

print(df["Marks"].unique())

print(df["Gender"].value_counts())

#creating new column
df["Marks4"]=df["Marks3"]*10
print(df)
