#!/usr/bin/env python
# coding: utf-8

# In[18]:


import pandas as pd


# In[19]:


#Read CSV File
electionDataDF = pd.read_csv("Resources/election_data.csv")
electionDataDF.head()


# In[20]:


#Confirm there are no incomplete rows
electionDataDF.count()


# In[4]:


#The total number of votes cast
totalVotes = len(electionDataDF.index)


# In[5]:


#A complete list of candidates who received votes
candidateListDF = pd.DataFrame(electionDataDF["Candidate"].value_counts())
candidateListDF.head()


# In[6]:


#The total number of votes each candidate won
khanVotes = candidateListDF.loc["Khan"][0]
correyVotes = candidateListDF.loc["Correy"][0]
liVotes = candidateListDF.loc["Li"][0]
otooleyVotes = candidateListDF.loc["O'Tooley"][0]


# In[7]:


#The percentage of votes each candidate won
khanPercent = (khanVotes/totalVotes) * 100
correyPercent = (correyVotes/totalVotes) * 100
liPercent = (liVotes/totalVotes) * 100
otooleyPercent = (otooleyVotes/totalVotes) * 100


# In[8]:


#The winner of the election based on popular vote
maxVotes = candidateListDF["Candidate"].max()


# In[9]:


#The index (Candidate) of the above maximum value
winner = candidateListDF["Candidate"].idxmax()


# In[10]:


#Concatenate results and print
header = "Election Results" + '\n'
seperator = "-------------------------" + '\n'
totalVotes = "Total Votes: " + str(totalVotes) + '\n'
#-------------------------
khanOutput = "Khan: " + str(round(khanPercent,3)) + "% (" + str(khanVotes) + ")"+ '\n'
correyOutput =  "Correy: " + str(round(correyPercent,3)) + "% (" + str(correyVotes) + ")"+ '\n'
liOutput = "Li: " + str(round(liPercent,3)) + "% (" + str(liVotes) + ")"'\n'
otooleyOutput = "O'Tooley: " + str(round(otooleyPercent,3)) + "% (" + str(otooleyVotes) + ")"+ '\n'
#-------------------------
winnerOutput = "Winner: " + str(winner) + '\n'
#-------------------------

output = (header + 
          seperator + 
          totalVotes + 
          seperator + 
          khanOutput + 
          correyOutput + 
          liOutput + 
          otooleyOutput + 
          seperator + 
          winnerOutput)

print(output)


# In[13]:


#Create text file
f = open('Resources/election_data.txt','w')


# In[14]:


#Write 'output' concatination to text file
print(output, file=f)


# In[ ]:





# In[ ]:




