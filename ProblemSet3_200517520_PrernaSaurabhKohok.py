#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Import the pandas library [Step#1,2,3]
import pandas as pd

# Read the data from the specified URL into a DataFrame
users = pd.read_csv('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user', sep='|')

# Display the first 10 rows of the DataFrame
users.head(10)


# In[3]:


# STep 4 : Group the 'users' DataFrame by the 'occupation' column
# Calculate the mean age for each occupation group
users.groupby('occupation').age.mean()


# In[5]:


#Step 5 # Group the 'users' DataFrame by the 'occupation' column
# Count the number of occurrences of each gender for each occupation group
# Sort the resulting Series in descending order
users.groupby('occupation').gender.count().sort_values(ascending=False)


# In[6]:


#Step 6 


# In[7]:


# Group the 'users' DataFrame by the 'occupation' column
# Calculate the minimum age for each occupation group
users.groupby('occupation').age.min()




# In[9]:


#Step 6 # Group the 'users' DataFrame by the 'occupation' column 
# Calculate the maximum age for each occupation group
users.groupby('occupation').age.max()


# In[10]:


#Step 7 # Group the 'users' DataFrame by the 'occupation' and 'gender' columns
# Calculate the mean age for each group
users.groupby(['occupation', 'gender']).age.mean()


# In[11]:


#Step 8 # Group the 'users' DataFrame by the 'occupation' and 'gender' columns
# Count the number of non-NA/null values for each column in each group
users.groupby(['occupation', 'gender']).count()



# In[12]:


#Question 2


# In[13]:


#Step 1,2,3
# Import the pandas library
import pandas as pd

# Read the data from the specified URL into a DataFrame
euro12 = pd.read_csv('https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/02_Filtering_%26_Sorting/Euro12/Euro_2012_stats_TEAM.csv', sep=',')

# Display the first 10 rows of the DataFrame
euro12.head(10)


# In[14]:


#Step 4 
# Access the 'Goals' column of the 'euro12' DataFrame
euro12.Goals


# In[15]:


#Step 5
# Count the number of  'Team' of the 'euro12' DataFrame
euro12.Team.count()


# In[16]:


#step 6
#What is the number of columns in the dataset?
euro12.shape[1]


# In[17]:


#Step 7
# Create a new DataFrame 'discipline' by selecting the 'Team', 'Yellow Cards', and 'Red Cards' columns from the 'euro12' DataFrame
discipline = euro12[['Team', 'Yellow Cards', 'Red Cards']]

# Display the resulting DataFrame
discipline


# In[19]:


#Step 8
# Sort the 'discipline' DataFrame by the 'Red Cards' and 'Yellow Cards' columns in descending order
discipline.sort_values(by=['Red Cards', 'Yellow Cards'], ascending=False)


# In[20]:


#Step 9 
#Calculate the mean Yellow Cards given per Team
euro12['Yellow Cards'].mean()


# In[21]:


#Step 10
# Filter teams that scored more than 6 goals
euro12[euro12['Goals']>6]


# In[22]:


#Step 11
# Select the teams that start with G
euro12[euro12.Team.str.startswith('G')]


# In[23]:


#Step 12
#Select the first 7 columns
euro12.iloc[:,0:7]


# In[24]:


#Step 13
#Select all columns except the last 3
euro12.iloc[:,0:-3]


# In[25]:


#Step 13
#Present only the Shooting Accuracy from England, Italy and Russia
euro12.loc[euro12.Team.isin(['England','Italy','Russia']),['Team','Shooting Accuracy']]


# In[26]:


#Question 3


# In[29]:


#Step 1
#Importing necessary libraries
import pandas as pd
import numpy as np
import random


# In[30]:


#step2 :Create 3 differents Series, each of length 100, as follows: 
#The first a random number from 1 to 4 
#The second a random number from 1 to 3 
#The third a random number from 10,000 to 30,000
first = pd.Series(np.random.randint(1,5,100))
second = pd.Series(np.random.randint(1,4,100))
third = pd.Series(np.random.randint(1000,30000,100))


# In[31]:


#Step3: Create a DataFrame by joinning the Series by column
ds = pd.concat([first,second,third],axis=1)
ds


# In[32]:


#Step 4: Change the name of the columns to bedrs, bathrs, price_sqr_meter
ds.columns = ['bedrs','bathrs','price_sqr_meter']
ds.head()


# In[33]:


#Step 5: Create a one column DataFrame with the values of the 3 Series and assign it to 'bigcolumn'
bigcolumn = pd.concat([first,second,third],axis=0)
bigcolumn


# In[34]:


#Step 6. Ops it seems it is going only until index 99. Is it true? False
len(bigcolumn)


# In[35]:


#Step 7: Reindex the DataFrame so it goes from 0 to 299
bigcolumn.reset_index(drop=True, inplace=True)
bigcolumn


# In[36]:


#Question 4


# In[37]:


#Step 1: Import the necessary libraries
import pandas as pd
import numpy as np
import datetime as dt


# In[39]:


#Step 2: Import the dataset from the attached file wind.txt 
#Step 3: Assign it to a variable called data and replace the first 3 columns by a proper datetime index.
data = pd.read_csv('wind.txt')
data.head()


# In[40]:


#Question 5


# In[41]:


#Step 1,2 and 3
import pandas as pd
chipo = pd.read_csv('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv',sep='\t')
chipo


# In[42]:


#Step 4: See the first 10 entries
chipo.head(10)


# In[43]:


#Step 5: What is the number of observations in the dataset?
chipo.order_id.count()


# In[44]:


#Step 6: What is the number of columns in the dataset?
chipo.shape[1]


# In[45]:


#Step 7: Print the name of all the columns.
chipo.columns


# In[46]:


#Step 8: How is the dataset indexed?
chipo.index


# In[47]:


#Step 9: Which was the most-ordered item?
chipo.item_name.value_counts().head(1)


# In[48]:


#Step 10: For the most-ordered item, how many items were ordered?
chipo.item_name.unique().shape[0]


# In[49]:


#Step 11: What was the most ordered item in the choice_description column?
chipo.choice_description.value_counts().head()


# In[50]:


#Step 12: How many items were orderd in total?
chipo.quantity.sum()


# In[51]:


#Step 13: • Turn the item price into a float 
#• Check the item price type 
#• Create a lambda function and change the type of item price 
#• Check the item price type
def item_float(x):
    return float(x[1:-1])
chipo.item_price = chipo.item_price.apply(item_float)
chipo


# In[52]:


chipo.item_price.dtype


# In[53]:


#Step 14: Step 14. How much was the revenue for the period in the dataset?
chipo.item_price.sum()


# In[54]:


#Step 15: How many orders were made in the period?
chipo.order_id.value_counts().count()


# In[55]:


#Step 16: What is the average revenue amount per order?
chipo.item_price.mean()


# In[56]:


#Step 17: Step 17. How many different items are sold?
chipo.item_name.value_counts().count()


# In[57]:


#Question 8


# In[58]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[60]:


US_Mar_Div = pd.read_csv('us-marriages-divorces-1867-2014.csv')
US_Mar_Div.head()


# In[61]:


years = US_Mar_Div['Year']
marriages = US_Mar_Div['Marriages_per_1000']
divorces = US_Mar_Div['Divorces_per_1000']
US_Mar_Div = plt.figure(figsize=(16,8))
US_Mar_Div = plt.plot(years, marriages, label='Marriages')
US_Mar_Div = plt.plot(years, divorces, label='Divorces')
US_Mar_Div = plt.title("Number of marriages and divorces per capita in the U.S. between 1867 and 2014")
US_Mar_Div = plt.xlabel("Years",fontsize=14)
US_Mar_Div = plt.legend(fontsize = 12, loc = "upper left")
US_Mar_Div = plt.ylabel("Marriages",fontsize=14)
US_Mar_Div = plt.grid(True)
US_Mar_Div


# In[62]:


#Question 7


# In[63]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[64]:


Bar_chart_data = pd.read_csv('us-marriages-divorces-1867-2014.csv')
Bar_chart_data.head()


# In[65]:


bar_chart=Bar_chart_data.loc[Bar_chart_data.Year.isin([1900,1950,2000]),['Year','Marriages_per_1000','Divorces_per_1000']]
bar_chart


# In[66]:


bar_chart = bar_chart[bar_chart['Year'].apply(lambda x: x in [1900, 1950, 2000])]
years = bar_chart['Year']
marriages = bar_chart['Marriages_per_1000']
divorces = bar_chart['Divorces_per_1000']
bar_chart = plt.figure(figsize= (16,8))
bar_chart = plt.bar(years, marriages, label ='Marriages')
bar_chart = plt.bar(years, divorces, label = 'Divorces')
bar_chart = plt.title("Number of marriages and divorces per capita in the U.S. between 1990,1950 and 2000", fontsize=16)
bar_chart = plt.xlabel("Years", fontsize=14)
bar_chart = plt.legend(fontsize = 12, loc = "upper left")
bar_chart


# In[67]:


#Question 8 


# In[68]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[70]:


actor_kills = pd.read_csv('actor_kill_counts.csv')
actor_kills


# In[71]:


actors = actor_kills['Actor']
killCount = actor_kills['Count']
actor_kills = plt.figure(figsize=(12,6))
actor_kills = plt.barh(actors, killCount, label='Count')
actor_kills = plt.title("The deadliest actors in Hollywood", fontsize=18)
actor_kills = plt.xlabel("kill count", fontsize=14)
actor_kills = plt.legend(fontsize = 12, loc = "upper right")
actor_kills


# In[72]:


#Question 9


# In[73]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[75]:


roman_emp = pd.read_csv("roman-emperor-reigns.csv")
roman_emp = roman_emp[roman_emp["Cause_of_Death"]=="Assassinated"]


# In[76]:


patches, texts = plt.pie(roman_emp.Length_of_Reign)
plt.legend(roman_emp.Emperor)
plt.show()


# In[77]:


#Question 10


# In[78]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plot


# In[79]:


Scatterplot = pd.read_csv("arcade-revenue-vs-cs-doctorates.csv")
Scatterplot.rename(columns = {'Total Arcade Revenue (billions)':'Revenue', 'Computer Science Doctorates Awarded (US)':'Awards'}, inplace = True)
Scatterplot


# In[80]:


a = Scatterplot.groupby('Year')
for name, group in a:
    plot.plot(group.Revenue, group.Awards, marker='o', linestyle='', markersize=12, label=name)
plot.legend()
plot.xlabel("Total revenue earned by Arcades")
plot.ylabel("Computer Science Awards")
plot.figure(figsize=(17,10))


# In[ ]:




