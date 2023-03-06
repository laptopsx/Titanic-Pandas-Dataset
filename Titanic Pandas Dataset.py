#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv("C://Users//savan//OneDrive - Temple University//Documents//ICAtitanic.csv")
subset = df[['PassengerId']]
#print(subset.tail(1))
passenger = df['PassengerId']
print("The number of people that were on the Titanic were")
print(passenger.loc[passenger.shape[0]-1])


# In[3]:


print("The number of people who survived are...")
survived = df[df['Survived'] == 1]
print(len(survived))
print("The number of people who died are...")
died = df[df['Survived'] == 0]
print(len(died))
print("The amount of people in the first class were...")
print(len(df[df['Pclass'] == 1]))
print("The amount of people in the second class were...")
print(len(df[df['Pclass'] == 2]))
print("The amount of people in the third class were...")
print(len(df[df['Pclass'] == 3]))
print("The amount of people who died in the first class were...")
print(len(died[died['Pclass'] == 1]))
print("The amount of people who died in the second class were...")
print(len(died[died['Pclass'] == 2]))
print("The amount of people who died in the third class were...")
print(len(died[died['Pclass'] == 3]))


# In[4]:


print("The amount of men '(who were the age of 18 or older)' that died...")
print(len(died))


# In[7]:


#making a death by class histogram 
import matplotlib.pyplot as plt
titanicDeaths = df[df["Survived"] == 0]
titanicSurvived = df[df["Survived"] == 1]
n, bins, patches = plt.hist(titanicDeaths['Pclass'], bins =3)
plt.title('Titanic Deaths by Class')
plt.xlabel('Class')
plt.ylabel('Number of deaths')
plt.show()


# In[20]:


titanicDeathsMale = titanicDeaths[titanicDeaths["Sex"] == "male"]
titanicDeathsMen = titanicDeathsMale[titanicDeathsMale["Age"] >= 18]
print(len(titanicDeathsMale))
print(len(titanicDeathsMen))
titanicDeathsFemale = titanicDeaths[titanicDeaths["Sex"] == "female"]
titanicDeathsWomen = titanicDeathsFemale[titanicDeathsFemale["Age"] >= 18]
titanicDeathsChildren = titanicDeaths[titanicDeaths["Age"] < 18]
n, bins, patches = plt.hist(titanicDeathsMen['Pclass'], bins=3)
plt.title('Titanic Deaths Men by Class')
plt.xlabel('Class')
plt.ylabel('Number of Deaths')
plt.show()
#deaths from the women off the titanic
n, bins, patches = plt.hist(titanicDeathsWomen['Pclass'], bins=3)
plt.title('Titanic Deaths Women by Class')
plt.xlabel('Class')
plt.ylabel('Number of Deaths')
plt.show()
#deaths from children off the titanic
n, bins, patches = plt.hist(titanicDeathsChildren['Pclass'], bins=3)
plt.title('Titanic Deaths Children by Class')
plt.xlabel('Class')
plt.ylabel('Number of Deaths')
plt.show()
#the combined of women and children deaths off the titanic
titanicDeathsWomenAndChildren = pd.concat([titanicDeathsWomen, titanicDeathsChildren])
#combined plot of deaths of men & women and children off the titanic
n, bins, patches = plt.hist(titanicDeathsMen['Pclass'], bins=3, label="Men")
n, bins, patches = plt.hist(titanicDeathsWomenAndChildren['Pclass'], bins=3, label="Women and Children")
plt.title('Titanic Deaths by Class')
plt.xlabel('Class')
plt.ylabel('Number of Deaths')
plt.legend()
plt.show()


# In[1]:


#in class activity create new dataframes for men who survived 
import pandas as pd
import matplotlib.pyplot as plt
titanicdf = pd.read_csv("C://Users//savan//OneDrive - Temple University//Documents//ICATitanic.csv")
titanicSurvivors = titanicdf[titanicdf["Survived"] == 1]

titanicSurvivorsMen = titanicSurvivors[(titanicSurvivors["Sex"] == "male") & (titanicSurvivors["Age"] >= 18)]
titanicSurvivorsWomenAndChildren = titanicSurvivors[(titanicSurvivors["Sex"] == "female") | (titanicSurvivors["Age"] < 18)]
n, bins, patches = plt.hist(titanicSurvivorsWomenAndChildren['Pclass'], bins=3, label='Survivors Women and Children')
n, bins, patches = plt.hist(titanicSurvivorsMen['Pclass'], bins=3, label='Survivors Men')
plt.title("Titanic Deaths By Class")
plt.xlabel("Class")
plt.ylabel("Number of Deaths")
plt.legend()
plt.show()


# In[ ]:




