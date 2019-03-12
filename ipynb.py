
# coding: utf-8

# In[1]:


import pandas as pd
import gmaps
import requests
import json

from api_keys import gkey
gmaps.configure(api_key = gkey )


# In[2]:


top_10 = "top_10_change.csv"
bottom_10 = "bottom_10_change.csv"


# In[3]:


top10_change = pd.read_csv(top_10)
bottom10_change = pd.read_csv(bottom_10)

bottom10_change.head()


# In[4]:


cities = top10_change['City']
Top_location = []

for city in cities:
    target_url = (f'https://maps.googleapis.com/maps/api/geocode/json?address={city}&key={gkey}')
    
    try:
        city_data = requests.get(target_url).json()
        
        lat = city_data["results"][0]["geometry"]["location"]["lat"]
        lng = city_data["results"][0]["geometry"]["location"]["lng"]
        Top_location.append({"City":city,
                          "Lat": lat,
                          "Lng": lng
                      })
        
    except:
        pass


# In[5]:


Top_location = pd.DataFrame(Top_location)

Top_location = Top_location[["City","Lat","Lng"]]
Top_location


# In[6]:


locations = Top_location[['Lat', 'Lng']]

AVG = top10_change['2009 VS 2015']


# In[7]:


fig = gmaps.figure()

heat_layer = gmaps.heatmap_layer(locations, 
                                 weights = AVG, 
                                 dissipating = False, 
                                 max_intensity = 10, 
                                 point_radius = 1.5 )

type(heat_layer)


# In[8]:


fig.add_layer(heat_layer)
fig


# In[9]:


cities = bottom10_change['City']
Bottom_location = []

for city in cities:
    target_url = (f'https://maps.googleapis.com/maps/api/geocode/json?address={city}&key={gkey}')
    
    try:
        city_data = requests.get(target_url).json()
        
        lat = city_data["results"][0]["geometry"]["location"]["lat"]
        lng = city_data["results"][0]["geometry"]["location"]["lng"]
        Bottom_location.append({"City":city,
                          "Lat": lat,
                          "Lng": lng
                      })
        
    except:
        pass


# In[10]:


Bottom_location = pd.DataFrame(Bottom_location)

Bottom_location = Bottom_location[["City","Lat","Lng"]]
Bottom_location


# In[12]:


locations = Bottom_location[['Lat', 'Lng']]

AVG = bottom10_change['2009 VS 2015']


# In[15]:


fig = gmaps.figure()

heat_layer = gmaps.heatmap_layer(locations, 
                                 weights = AVG, 
                                 dissipating = False, 
                                 max_intensity = 10, 
                                 point_radius = 1.5 )

type(heat_layer)


# In[16]:


fig.add_layer(heat_layer)
fig

