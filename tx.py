#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from plotly import express as px

df = pd.read_csv("london.csv")
print(df.head())


# In[ ]:


df.describe()


# In[ ]:


df.info()


# In[ ]:

figure = px.line(df, x='Year', 
                 y="Temp", 
                 title='Mean Temperature in London Over the Years')
figure.show()


# In[ ]:


# figure = px.line(df, x="Date", 
#                  y="humidity", 
#                  title='Humidity in Delhi Over the Years')
# figure.show()


# In[ ]:


# figure = px.line(df, x="date", 
#                  y="wind_speed", 
#                  title='Wind Speed in Delhi Over the Years')
# figure.show()


# # In[ ]:


# figure = px.scatter(data_frame = df, x="humidity",
#                     y="meantemp", size="meantemp", 
#                     trendline="ols", 
#                     title = "Relationship Between Temperature and Humidity")
# figure.show()


# In[ ]:


# From df.info() we saw that date is an object
# We need to reclass it to datetime
# We're also going to add a year and month column into the df

# df["Date"] = pd.to_datetime(df["Date"], format = '%Y')
# df['year'] = df['Date'].dt.year
# #df["month"] = df["Date"].dt.month
# print(df.head())
# df.info()


# In[ ]:

# flatui = ["blue", "yellow", "red"]
# sns.set_palette(flatui)

# plt.style.use('fivethirtyeight')
# plt.figure(figsize=(15, 10))
# plt.title("Temperature Change in Texas Over the Years")
# sns.lineplot(data = df, x='month', y='Value', hue='year')
# plt.show()


# # In[ ]:


# forecast_data = df.rename(columns = {"Date": "ds", 
#                                      "Value": "y"})


# # In[ ]:


# from prophet import Prophet
# from prophet.plot import plot_plotly, plot_components
# model = Prophet()
# model.fit(forecast_data)
# forecasts = model.make_future_dataframe(periods=3650)
# #fig2 = model.plot(forecast_data)
# predictions = model.predict(forecasts)
# predictions[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()
# fig3 = model.plot_components(predictions)

# # In[ ]:


# forecasts.info()



