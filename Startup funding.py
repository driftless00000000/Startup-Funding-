#!/usr/bin/env python
# coding: utf-8
This dataset has funding information of the Indian startups from January 2015 to August 2017.

Feature Details :
SNo - Serial number.
Date - Date of funding in format DD/MM/YYYY.
StartupName - Name of the startup which got funded.
IndustryVertical - Industry to which the startup belongs.
SubVertical - Sub-category of the industry type.
CityLocation - City which the startup is based out of.
InvestorsName - Name of the investors involved in the funding round.
InvestmentType - Either Private Equity or Seed Funding.
AmountInUSD - Funding Amount in USD.
Remarks - Other information, if any.

Insights -
Find out what type of startups are getting funded in the last few years?
Who are the important investors?
What are the hot fields that get a lot of funding these days?


# Given File 'startup_funding.csv'

# Number of Fundings
# 
# Check the trend of investments over the years. To check the trend, find -
# Total number of fundings done in each year.
# Plot a line graph between year and number of fundings. Take year on x-axis and number of fundings on y-axis.
# Print year-wise total number of fundings also. Print years in ascending order.
# 
# Note :
# There is some error in the 'Date' feature. Make sure to handle that.

# In[5]:


import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/khush/Downloadsstartup_funding.csv")
df.Date = df.Date.str[-4:]
df = df.groupby(by='Date').size()
year_No_dict = df.to_dict()
year = []
no_of_funding=[]

for k,v in year_No_dict.items():
    no_of_funding.append(v)
    year.append(k)
    print(k,v)

#Plotting the Graph
plt.plot(year,no_of_funding)
plt.title('trend of investments over the years')
plt.xlabel('Year')
plt.ylabel('No. of Fundings')
plt.show()

Top Indian Cities


Problem Statement :
Find out which cities are generally chosen for starting a startup.
Find top 10 Indian cities which have most number of startups ?
Plot a pie chart and visualise it.
Print the city name and number of startups in that city also.

Note :
Take city name "Delhi" as "New Delhi".
Check the case-sensitiveness of cities also. 
That means - at some place, instead of "Bangalore", "bangalore" is given. 
Take city name as "Bangalore".
For few startups multiple locations are given, one Indian and one Foreign. 
Count those startups in Indian startup also. Indian city name is first.
Print the city in descending order with respect to the number of startups.
# In[6]:


import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/khush/Downloads/startup_funding.csv")
df = df.dropna(subset=['CityLocation'])
def separateCity(city): 
    return city.split('/')[0].strip() 
df['CityLocation']=df['CityLocation'].apply(separateCity)
df[df['CityLocation']=='bangalore'] = 'Bangalore'
df[df['CityLocation']=='Delhi'] = 'New Delhi'

df = df.groupby(by='CityLocation').size()
df = df.nlargest(10)
df = df.to_dict()
City=[]
no_of_statup=[]
for i , j in df.items():
    City.append(i)
    no_of_statup.append(j)
    print(i,j)

plt.pie(no_of_statup,labels=City,autopct='%.2f')
plt.show()


# Funding amount
# 
# Problem Statement :
# Find out if cities play any role in receiving funding.
# Find top 10 Indian cities with most amount of fundings received. 
# Find out percentage of funding each city has got (among top 10 Indian cities only).
# Print the city and percentage with 2 decimal place after rounding off.
# 
# Note:
# Take city name "Delhi" as "New Delhi".
# Check the case-sensitiveness of cities also. 
# That means - at some place, instead of "Bangalore", "bangalore" is given. 
# Take city name as "Bangalore".
# For few startups multiple locations are given, one Indian and one Foreign. 
# Count those startups in Indian startup also. Indian city name is first.
# Print the city in descending order with respect to the percentage of funding.

# In[13]:


import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/khush/Downloads/startup_funding.csv",encoding = 'utf-8')
df.dropna(subset=["CityLocation"],inplace=True)
def separateCity(city):
    return city.split('/')[0].strip()
df['CityLocation'] = df['CityLocation'].apply(separateCity)
df['CityLocation'].replace("Delhi","New Delhi",inplace = True)
df['CityLocation'].replace("bangalore","Bangalore",inplace = True)

df['AmountInUSD'] = df['AmountInUSD'].apply(lambda x: float(str(x).replace(",","")))
df = df.groupby('CityLocation')['AmountInUSD'].sum()
df = df.sort_values(ascending = False)[0:10]
city = df.index
amount = df.values
explode = [0.2,0.2,0.2,0.2,0.1,0.1,0.2,0.2,0.2,0.2]
plt.pie(amount,labels = city,autopct='%0.2f',counterclock=False,startangle=90,explode = explode, radius=1.5)
plt.show()

percent = np.true_divide(amount,amount.sum())*100
for i in range(len(city)):
    print(city[i],format(percent[i],'0.2f'))


# Investment Type
# 
# Problem Statement :
# There are 4 different type of investments. Find out percentage of amount funded for each investment type.
# Plot a pie chart to visualise.
# Print the investment type and percentage of amount funded with 2 decimal places after rounding off.
# 
# Note :
# Correct spelling of investment types are - "Private Equity", "Seed Funding", "Debt Funding", and "Crowd Funding". 
# Keep an eye for any spelling mistake. 
# You can find this by printing unique values from this column.
# Print the investment type in descending order with respect to the percentage of the amount funded.

# In[24]:


import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/khush/Downloads/startup_funding.csv",encoding = 'utf-8')
df['AmountInUSD'] = df['AmountInUSD'].apply(lambda x: float(str(x).replace(",","")))
df['InvestmentType'] = df['InvestmentType'].replace(['Crowd funding','PrivateEquity','SeedFunding'],['Crowd Funding','Private Equity','Seed Funding'])
df= df.groupby(by='InvestmentType')['AmountInUSD'].sum()
df = df.sort_values(ascending = False)
InvestmentType = df.index
amount = df.values
plt.pie(amount,labels = InvestmentType,autopct='%0.2f',counterclock = True,startangle=90, radius=2)
plt.show()

percent = np.true_divide(amount,amount.sum())*100
for i in range(len(InvestmentType)):
    print(InvestmentType[i],format(percent[i],'0.2f'))


# Top Industries
# 
# Problem Statement :
# Which type of companies got more easily funding. To answer this question, find -
# Top 5 industries and percentage of the total amount funded to that industry. (among top 5 only)
# Print the industry name and percentage of the amount funded with 2 decimal place after rounding off.
# 
# Note :
# Ecommerce is the right word in IndustryVertical, so correct it.
# Print the industry in descending order with respect to the percentage of the amount funded.

# In[25]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/khush/Downloads/startup_funding.csv",encoding = 'utf-8')
df['IndustryVertical'].replace('ECommerce','Ecommerce',inplace = True)
df['IndustryVertical'].replace('eCommerce','Ecommerce',inplace = True)
df['IndustryVertical'].replace('ecommerce','Ecommerce',inplace = True)
df['AmountInUSD'] = df['AmountInUSD'].apply(lambda x: float(str(x).replace(",","")))
df = df.groupby('IndustryVertical')['AmountInUSD'].sum()
df = df.sort_values(ascending = False)[:5]
industry = df.index
amount = df.values

plt.pie(amount,labels = industry,autopct='%0.2f',counterclock=False,startangle=100)
plt.show()
percent = np.true_divide(amount,amount.sum())*100
for i in range(len(industry)):
    print(industry[i],format(percent[i],'0.2f'))


# Top startups
# 
# Problem Statement :
# Find top 5 startups with most amount of total funding.
# Print the startup name in descending order with respect to amount of funding.
# 
# Note:
# Ola, Flipkart, Oyo, Paytm are important startups, so correct their names. 
# There are many errors in startup names, ignore correcting all, just handle important ones.

# In[27]:


import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/khush/Downloads/startup_funding.csv",encoding = 'utf-8')
df['AmountInUSD'] = df['AmountInUSD'].apply(lambda x: float(str(x).replace(",","")))
df['StartupName'] = df['StartupName'].replace(['Flipkart.com','Ola Cabs','Olacabs','Oyo Rooms','Oyorooms','OyoRooms','Paytm Marketplace'],['Flipkart','Ola','Ola','Oyo','Oyo','Oyo','Paytm'])
df= df.groupby(by='StartupName')['AmountInUSD'].sum()
df = df.sort_values(ascending = False)
df=df.nlargest(5)

IndustryVertical = df.index
amount = df.values
plt.pie(amount,labels = IndustryVertical,autopct='%0.2f',counterclock=False,startangle=90,radius=1.5)
plt.show()

for i in range(len(IndustryVertical)):
    print(IndustryVertical[i])


# Funding rounds
# 
# Problem Statement :
# Find the top 5 startups who received the most number of funding rounds. 
# That means, startups which got fundings maximum number of times.
# Print the startup name in descending order with respect to the number of funding round as integer value.
# 
# Note:
# Ola, Flipkart, Oyo, Paytm are important startups, so correct their names. 
# There are many errors in startup names, ignore correcting all, just handle important ones.

# In[29]:


import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/khush/Downloads/startup_funding.csv",encoding = 'utf-8')
df['StartupName'] = df['StartupName'].replace(['Flipkart.com','Ola Cabs','Olacabs','Oyo Rooms','Oyorooms','OyoRooms','Paytm Marketplace','OYO Rooms'],['Flipkart','Ola','Ola','Oyo','Oyo','Oyo','Paytm','Oyo'])
df = df.groupby(by='StartupName').size()
df=df.nlargest(5)

StartupName = df.index
amount = df.values
plt.pie(amount,labels = StartupName,autopct='%0.2f',counterclock=False,startangle=90,radius=1.5)
plt.show()

for i in range(len(StartupName)):
    print(StartupName[i],amount[i])


# In[ ]:


Top Investor

Problem Statement :
Find the Investors who have invested maximum number of times.
Print the investor name and number of times invested as integer value.

Note:
In startup, multiple investors might have invested. So consider each investor for that startup.
Ignore the undisclosed investors.


# In[31]:


import csv
import numpy as np
with open("C:/Users/khush/Downloads/startup_funding.csv",encoding = 'utf-8') as file_obj:
    file_data=csv.DictReader(file_obj, skipinitialspace=True)
    investors=[]
    for row in file_data:
        if not ('Undisclosed' in row['InvestorsName'] or 'undisclosed' in row['InvestorsName']):
            for i in row['InvestorsName'].split(','):
                investors.append(i.strip())
    dic=dict()
    for i in investors:
        if i in dic.keys():
            dic[i]+=1
        else:
            dic[i]=1
    x=[]
    y=[]
    for i in dic.keys():
        x.append(i)
        y.append(dic[i])
    np_x=np.array(x)
    np_y=np.array(y)
    np_x=np_x[np.argsort(np_y)]
    np_y=np.sort(np_y)
    
    np_y=np_y[::-1]
    np_x=np_x[::-1]
    print(np_x[0], np_y[0])


# In[ ]:




