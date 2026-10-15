import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

IN_FILE = 'iowa_merged_data.csv'
PLOT1 = 'Connectedness_vs_Mortality.png'
PLOT2 = 'Age_vs_Mortality.png'

df = pd.read_csv(IN_FILE)

fig1, ax = plt.subplots(figsize=(8,5))

#configure plot 1
ax.scatter(
    df['ec_county'],
    df['Crude Rate'],
    color='steelblue',
    alpha=.7
)

x = df['ec_county']
y = df['Crude Rate']

slope, intercept = np.polyfit(x, y, deg=1)

# add trendline
trendline = np.linspace(x.min(), x.max(), 2)
ax.plot(
    trendline,
    slope * trendline + intercept,
    color='red'
)

ax.legend()

#set labels
ax.set_xlabel('Social Connectedness')
ax.set_ylabel('Deaths per 100,000')
ax.set_title('Social Connectedness vs Mortality')

fig1.tight_layout()
plt.savefig(PLOT1, dpi=300, bbox_inches="tight")



fig2, ax2 = plt.subplots(figsize=(8,5))
#configure plot 2
ax2.scatter(
    df['Percent_65+'],
    df['Crude Rate'],
    color='steelblue',
    alpha=.7
)

x = df['Percent_65+']
y = df['Crude Rate']

slope, intercept = np.polyfit(x, y, deg=1)

# add trendline
trendline = np.linspace(x.min(), x.max(), 2)
ax2.plot(
    trendline,
    slope * trendline + intercept,
    color='red'
)

ax2.legend()

#set labels
ax2.set_xlabel('Percent of Population Age 65 and Older')
ax2.set_ylabel('Deaths per 100,000')
ax2.set_title('Age vs Mortality')

fig2.tight_layout()
plt.savefig(PLOT2, dpi=300, bbox_inches="tight")