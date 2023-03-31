import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import os
BASE_PATH = '../'

data_path = os.path.join(BASE_PATH, 'AE', 'Karnataka_AE.csv')
shape_path = os.path.join(BASE_PATH, 'maps', 'AC_Boundary_SHP_Karnataka', 'AC_Boundary.shp')

df_AE = pd.read_csv(data_path, low_memory=False)
current_assembly = 10
filter_assembly = (df_AE['Assembly_No']==current_assembly)
filter_poll_zero = (df_AE["Poll_No"] == 0)
filter_winners = (df_AE['Position']==1)
filter_data = filter_assembly & filter_poll_zero & filter_winners
temp_df = df_AE.loc[filter_data]

df_vote_share_pct = temp_df[['Constituency_No', 'Constituency_Name', 'Vote_Share_Percentage']]
# df_margin_pct = temp_df[['Constituency_No', 'Constituency_Name', 'Margin_Percentage']]

shape = gpd.read_file(shape_path)

shape['Constituency_No'] = shape['AC_CODE'].astype('int64')

df_merged = pd.merge(
    left=shape,
    right = df_vote_share_pct,
    left_on='Constituency_No',
    right_on='Constituency_No',
    how='left'
)

df_merged = df_merged.dropna()

ax = df_merged.boundary.plot(edgecolor='black', linewidth=0.2, figsize=(10,5))

df_merged.plot(
    ax=ax, 
    column= 'Vote_Share_Percentage', 
    legend=True, 
    cmap='RdBu', 
    legend_kwds = {
    'shrink': 0.3,
    'orientation': 'horizontal',
    'format': '%.1f%%'
    }
)

ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

edges = ['left', 'right', 'top', 'bottom']

for edge in edges:
    ax.spines[edge].set_visible(False)

ax.set_title('Vote Share Percentage of Assembly Election in Karnatka 2018')
plt.show()
