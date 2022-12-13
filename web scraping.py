#!/usr/bin/env python
# coding: utf-8

# In[10]:


get_ipython().getoutput('pip install requests')


# In[9]:


get_ipython().getoutput(' pip install bs4')


# In[79]:


import requests
from bs4 import BeautifulSoup
import pandas as pd


# In[15]:


url="https://www.nobroker.in/prophub/new-builder-projects/new-builder-projects-in-bangalore/"


# In[19]:


res=requests.get(url=url)
html_content=res.content


# In[20]:


soup= BeautifulSoup(html_content,'html.parser')
project_name=[]


# In[34]:


Banglor_property_details={'project Name':[],'BHK':[]}


# In[35]:


for inner_ul in soup.find_all('ul'):
    for inner_li in inner_ul:
        for inner_most_li in inner_li:
            if' Project Name & Locality' in inner_most_li:
                Banglor_property_details['project Name'].append(inner_most_li.strip().split(':')[1])
            if'BHK Type & Price(Lacs)' in inner_most_li:
                Banglor_property_details['BHK'].append(inner_most_li.strip().split(':')[1])
                
                
                
print(Banglor_property_details)


# In[90]:


Banglore=pd.DataFrame.from_dict(Banglor_property_details)
Banglore


# In[89]:


url1='https://www.nobroker.in/prophub/new-builder-projects/new-builder-projects-in-mumbai/'


# In[100]:


res4=requests.get(url=url1)
html_content4=res4.content


# In[106]:


soup4= BeautifulSoup(html_content4,'html.parser')
project_name4=[]


# In[107]:


mumbai_property_details={'project Name_Mumbai':[],'BHK_Mumbai':[]}


# In[108]:


for inner_ul4 in soup4.find_all('ul'):
    for inner_li4 in inner_ul4:
        for inner_most_li4 in inner_li4:
            if' Project Name & Locality' in inner_most_li4:
                mumbai_property_details['project Name_Mumbai'].append(inner_most_li4.strip().split(':')[1])
            if'BHK Type & Price(Lacs)' in inner_most_li4:
                mumbai_property_details['BHK_Mumbai'].append(inner_most_li4.strip().split(':')[1])


# In[109]:


Mumbai=pd.DataFrame.from_dict(mumbai_property_details)
Mumbai


# In[67]:


url2="https://www.nobroker.in/prophub/new-builder-projects/new-builder-projects-in-gurgaon/"


# In[69]:


res=requests.get(url=url2)
html_content2=res.content


# In[70]:


soup2= BeautifulSoup(html_content2,'html.parser')
project_name2=[]


# In[71]:


Delhi_property_details={'project Name_delhi':[],'BHK_delhi':[]}


# In[72]:


for inner_ul2 in soup2.find_all('ul'):
    for inner_li2 in inner_ul2:
        for inner_most_li2 in inner_li2:
            if' Project Name & Locality' in inner_most_li2:
                Delhi_property_details['project Name_delhi'].append(inner_most_li2.strip().split(':')[1])
            if'BHK Type & Price(Lacs)' in inner_most_li2:
                Delhi_property_details['BHK_delhi'].append(inner_most_li2.strip().split(':')[1])


# In[94]:


delhi=pd.DataFrame.from_dict(Delhi_property_details)
delhi


# In[74]:


url3="https://www.nobroker.in/prophub/new-builder-projects/new-builder-projects-in-chennai/"


# In[75]:


res3=requests.get(url=url3)
html_content3=res3.content


# In[76]:


soup3= BeautifulSoup(html_content3,'html.parser')
project_name3=[]


# In[77]:


Chennai_property_details={'project Name_Chennai':[],'BHK_Chennai':[]}


# In[78]:


for inner_ul3 in soup3.find_all('ul'):
    for inner_li3 in inner_ul3:
        for inner_most_li3 in inner_li3:
            if' Project Name & Locality' in inner_most_li3:
                Chennai_property_details['project Name_Chennai'].append(inner_most_li3.strip().split(':')[1])
            if'BHK Type & Price(Lacs)' in inner_most_li3:
                Chennai_property_details['BHK_Chennai'].append(inner_most_li3.strip().split(':')[1])


# In[110]:


Chennai=pd.DataFrame.from_dict(Chennai_property_details)
Chennai


# In[ ]:




