
# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from plotly import express as px
from prophet import Prophet
from prophet.plot import plot_plotly, plot_components_plotly
from math import sqrt

df = pd.read_csv("texasWeatherData.csv")

df["date"] = pd.to_datetime(df["Date"], format = '%Y%m')
df['year'] = df['date'].dt.year
df["month"] = df["date"].dt.month

df['Percent Change YOY'] = (df.groupby(['month']))['Value'].pct_change() * 100
year_on_year_change = df.groupby(['month'])['Percent Change YOY'].mean()

plt.figure(figsize=(10, 6))
plt.bar(year_on_year_change.index, year_on_year_change, capsize=6, color='skyblue')
plt.title(f"Percentage Change in Temperature by Month in Texas Since {df['year'].iloc[0]}")
plt.xlabel('Month')
plt.ylabel('Percentage Change')
plt.grid(True)
plt.tight_layout()
plt.grid(False)
plt.show()


n_years = 15
old_data = (df.groupby(['month'])).head(n_years).groupby('month')['Value'].mean().reset_index()
new_data = (df.groupby(['month'])).tail(n_years).groupby('month')['Value'].mean().reset_index()


old_data['dataset'] = f"{df['year'].iloc[0]} - {df['year'].iloc[0]+n_years}"
new_data['dataset'] = f"{df['year'].iloc[-1]-n_years} - {df['year'].iloc[-1]}"
combined_data = pd.concat([old_data, new_data])


plt.figure(figsize=(10, 6))
sns.barplot(data=combined_data, x='month', y='Value', hue='dataset', palette=['blue', 'green'])
plt.title('Average Temperature Comparison in Texas')
plt.xlabel('Month')
plt.ylabel('Temp (Fahrenheit)')
plt.legend(title='Dataset')
plt.grid(True)
plt.tight_layout()
plt.grid(False)
plt.show()



















# %%
df = pd.read_csv("london_weather_2.csv")
df['mean_temp'] =  df['mean_temp'] * 9 / 5 + 32

df["date"] = pd.to_datetime(df["date"], format = '%Y%m%d')
df['year'] = df['date'].dt.year
df["month"] = df["date"].dt.month

df['Percent Change YOY'] = (df.groupby(['month']))['mean_temp'].pct_change() * 100
year_on_year_change = df.groupby(['month'])['Percent Change YOY'].mean()

# Plotting with error bars
plt.figure(figsize=(10, 6))
plt.bar(year_on_year_change.index, year_on_year_change, capsize=6, color='skyblue')
plt.title(f"Percentage Change in Temperature by Month in London Since {df['year'].iloc[0]}")
plt.xlabel('Month')
plt.ylabel('Percentage Change')
plt.grid(True)
plt.tight_layout()
plt.grid(False)
plt.show()


n_years = 15
old_data = (df.groupby(['month'])).head(n_years).groupby('month')['mean_temp'].mean().reset_index()
new_data = (df.groupby(['month'])).tail(n_years).groupby('month')['mean_temp'].mean().reset_index()


# Restructuring data for Seaborn
old_data['dataset'] = f"{df['year'].iloc[0]} - {df['year'].iloc[0]+n_years}"
new_data['dataset'] = f"{df['year'].iloc[-1]-n_years} - {df['year'].iloc[-1]}"
combined_data = pd.concat([old_data, new_data])

# Plotting with Seaborn
plt.figure(figsize=(10, 6))
sns.barplot(data=combined_data, x='month', y='mean_temp', hue='dataset', palette=['blue', 'green'])
plt.title('Average Temperature Comparison in London')
plt.xlabel('Month')
plt.ylabel('Temp (Fahrenheit)')
plt.legend(title='Dataset')
plt.grid(True)
plt.tight_layout()
plt.grid(False)
plt.show()


