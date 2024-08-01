import pandas as pd

df= pd.read_csv('netflix2.csv')

print(df.head())

print(df.info())

print(df.isnull().sum())

'''for handling missing values
remove missing value
fill missing value(use mean,mode,median)
compute missing values(using algorithm[regression,k-nearest neighbours]'''
df_cleaned = df.dropna()
print(df_cleaned)

df.fillna({'type': 'unknown'}, inplace=True)
print(df)

df['duration'] = df['duration'].str.replace('min',' ').astype(float)
print(df)

df['duration'] = df['duration'].fillna(df['duration'].median())
print(df)
#check for duplicate rows
print("The duplicated rows are",df.duplicated().sum())
#remove duplicate rows
df_cleaned1 = df.drop_duplicates()
print(df)

#converting text to lowercase
df['type'] = df['type'].str.lower()
print(df)
#standardize date format
df['date_added'] = pd.to_datetime(df['date_added'])
print(df['date_added'])

#standardize categorical data
df['rating'] = df['rating'].str.upper()
print(df['rating'])

#fix typos in categorical data
df['country'] = df['country'].replace({'Usa': 'USA','United States':'USA'})
print(df['country'])



df['country'] = df['country'].replace({'USA':'Pakistan'})
print(df['country'])

df.fillna({'director': 'unknown'}, inplace=True)
print(df['director'])

df.to_excel('my.xlsx',sheet_name= 'one' , index=False)
print("data is written to my.xlsx")
