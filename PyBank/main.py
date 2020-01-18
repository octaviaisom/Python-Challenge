#!/usr/bin/env python
# coding: utf-8

# In[19]:


import pandas as pd


# In[20]:


#Read CSV file
budgetDataDF = pd.read_csv("Resources/budget_data.csv")
budgetDataDF.head()


# In[21]:


#Confirm there are no incomplete rows
budgetDataDF.count()


# In[22]:


#The total number of months included in the dataset
totalMonths = len(budgetDataDF.index)


# In[23]:


#The net total amount of "Profit/Losses" over the entire period
totalProfit = budgetDataDF["Profit/Losses"].sum()


# In[24]:


#Calculate month-over-month (MoM) change in profit for each month
momChangeDF = budgetDataDF['Profit/Losses']-budgetDataDF['Profit/Losses'].shift()
momChangeDF.head()


# In[25]:


#Add 'MoM Change' column to budget data frame
budgetDataDF["MoM Change"] = momChangeDF
budgetDataDF.head()


# In[26]:


#The average of the changes in "Profit/Losses" over the entire period
avgMoMChange = budgetDataDF["MoM Change"].mean()


# In[27]:


#The greatest increase in profits (amount) over the entire period
maxMoMChange = budgetDataDF["MoM Change"].max()


# In[28]:


#The index of the above maximum value
maxMoMChangeIndex = budgetDataDF["MoM Change"].idxmax()

#The greatest increase in profits (date) over the entire period
maxMoMChangeMth = budgetDataDF.iloc[maxMoMChangeIndex]["Date"]


# In[29]:


#The greatest decrease in losses (amount) over the entire period
minMoMChange = budgetDataDF["MoM Change"].min()


# In[30]:


#The index of the above minimum value
minMoMChangeIndex = budgetDataDF["MoM Change"].idxmin()

#The greatest decrease in losses (date) over the entire period
minMoMChangeMth = budgetDataDF.iloc[minMoMChangeIndex]["Date"]


# In[31]:


#Concatenate results and print
headerOP = "Financial Analysis" + '\n'
seperatorOP = "----------------------------" + '\n'
totalmthsOP = "Total Months: " + str(totalMonths) + '\n'
totalprofitOP = "Total: " + str(totalProfit) + '\n'
avgchangeOP = "Average Change: " + str(round(avgMoMChange,2)) + '\n'
greatincOP = "Greatest Increase in Profits: " + str(maxMoMChangeMth) + " ($" + str(maxMoMChange) +")" + '\n'
greatdecOP = "Greatest Decrease in Profits: " + str(minMoMChangeMth) + " ($" + str(minMoMChange) + ")" + '\n'

output = (headerOP + 
          seperatorOP + 
          totalmthsOP + 
          totalprofitOP + 
          avgchangeOP + 
          greatincOP + 
          greatdecOP)

print(output)


# In[32]:


#Create text file
f = open('Resources/budget_data.txt','w')


# In[33]:


#Write 'output' concatination to text file
print(output, file=f)


# In[ ]:




