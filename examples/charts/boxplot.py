import pandas as pd
import numpy as np
from collections import OrderedDict

# we throw the data into a pandas df
from bokeh.sampledata.olympics2014 import data
df = pd.io.json.json_normalize(data['data'])

# we filter by countries with at least one medal and sort
df = df[df['medals.total'] > 0]
df = df.sort("medals.total", ascending=False)

# then, we get the countries and we group the data by medal type
countries = df.abbr.values.tolist()
gold = df['medals.gold'].astype(float).values
silver = df['medals.silver'].astype(float).values
bronze = df['medals.bronze'].astype(float).values

# later, we build a dict containing the grouped data
medals = OrderedDict(bronze=bronze, silver=silver, gold=gold)
#medals = pd.DataFrame(medals)
#medals = medals.values()
medals = tuples(medals.values())
#medals = np.array(medals.values())

# non ordered df
#df.pop('name')
#df.pop('abbr')
#df.pop('medals.total')
#df.index = countries
#
#medals = df

# and finally we drop the dict into our BoxPlot chart
from bokeh.charts import BoxPlot, NewBoxPlot
boxplot = NewBoxPlot(medals, marker='circle', outliers=True, title="boxplot test", xlabel="medal type", ylabel="medal count",
             width=600, height=400, filename="boxplot.html")
boxplot.show()