
# coding: utf-8

# In[1]:


import pandas as pd
data=pd.read_csv("thanksgiving.csv",encoding="Latin-1")
#data[:3]


# In[2]:


columns=data.columns
columns


# In[8]:


freq=data["Do you celebrate Thanksgiving?"].value_counts()
yes_data=(data["Do you celebrate Thanksgiving?"]=="Yes")
data1=data[yes_data]
freq
#data1["Do you celebrate Thanksgiving?"]


# In[11]:


freq1=data["What is typically the main dish at your Thanksgiving dinner?"].value_counts()
tofurkey_dinner=data["What is typically the main dish at your Thanksgiving dinner?"]=="Tofurkey"
data[tofurkey_dinner]["Do you typically have gravy?"][0:10] #Do you typically have gravy


# In[15]:


apple_null_bool=pd.isnull(data["Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Apple"])
pumpkin_null_bool=pd.isnull(data["Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Pumpkin"])
pecan_null_bool=pd.isnull(data["Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Pecan"])
null_val=apple_null_bool&pumpkin_null_bool&pecan_null_bool
ate_pies=data[null_val]
ate_pies.head(2)
#set of tuples eating any of each pie


# In[21]:



def age_int(age):
        if pd.isnull(age):
            return None
        age=age.split(" ")[0]
        age=age.replace("+","")
        return int(age)
data["new_age"]=data["Age"].apply(age_int)


# In[25]:


desc=data["new_age"].describe()
print(desc)


# Numerical Description of the Age Categories.
# Various Constraints have been applied on the table to retrieve necessary results for analysis.

# In[28]:


def extr_int(dollar):
    if pd.isnull(dollar):
        return None
    first_dollar=dollar.split(" ")[0]
    if first_dollar=="Prefer":
        return None
    first_dollar=first_dollar.replace(",","")
    first_dollar=first_dollar.replace("$","")
    return int(first_dollar)
data["int_income"]=data["How much total combined money did all members of your HOUSEHOLD earn last year?"].apply(extr_int)
print(data["int_income"][:5])


# Extracting the minimum integer part from the earning part of all the members of the household last year and assigning it to a seperate column.

# In[39]:


import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')
thanksgiving_travel=(data["int_income"]<150000)
thanksgiving_travel=data[thanksgiving_travel]
tgt_freq=thanksgiving_travel["int_income"].value_counts()
print(thanksgiving_travel["int_income"].value_counts())

plt.plot(data["int_income"],data["new_age"])
plt.show()


# For lesser ages the frequency of people earning high income is really less or negligible
# 

# In[55]:


data.pivot_table(index="Have you ever tried to meet up with hometown friends on Thanksgiving night?",
                 columns='Have you ever attended a "Friendsgiving?"',
                 values="new_age")


# In[57]:


data.pivot_table(index="Have you ever tried to meet up with hometown friends on Thanksgiving night?",
                 columns='Have you ever attended a "Friendsgiving?"',
                 values="int_income")

