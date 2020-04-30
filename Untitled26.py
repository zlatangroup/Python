#!/usr/bin/env python
# coding: utf-8

# In[87]:


import pandas as pd


# In[88]:


cars=pd.Series(['BMW','Toyota','Honda'])


# In[89]:


cars


# In[90]:


colours=pd.Series(['Red','Green','Yellow'])


# In[91]:


colours


# In[92]:


car_data=pd.DataFrame(
    {"Car Make":cars,"Car Colours":colours})


# In[93]:


car_data


# In[94]:


car_data.info()


# In[95]:


car_data.columns


# In[96]:


car_sales=pd.read_csv("7.1 car-sales.csv")


# In[97]:


car_sales


# In[98]:


car_sales["Price"]=car_sales["Price"].str.replace('[\$\,\.]','')
car_sales


# In[99]:


car_sales["Price"]=car_sales["Price"].str[:-2]


# In[100]:


car_sales["Sales Date"]=pd.date_range('1/1/2020',periods=len(car_sales))
car_sales


# In[101]:



car_sales["Price"]=car_sales["Price"].astype(int)
car_sales["Total Sales"]=car_sales["Price"].astype(int).cumsum()
car_sales


# In[102]:


car_sales.plot(x='Sales Date',y='Total Sales');


# In[103]:


car_sales.plot(x='Odometer (KM)',y='Price', kind="scatter");


# In[ ]:




