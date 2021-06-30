import streamlit as st
import pandas as pd
import plotly.express as px

st.title('Austin Animal Center Data Exploration')

df = pd.read_csv('data/Intakes_2021_withlocationdetails.csv')

st.header("Found Animal Types")

types = df['Animal Type'].value_counts()
types = types.reset_index().rename(columns={'index':'Type', 'Animal Type':'Count'})

for an_type in types.index:
    st.write(f"{types['Type'][an_type]}: {types['Count'][an_type]}")

fig1 = px.pie(
    types,
    names='Type',
    values='Count',
)
st.plotly_chart(fig1)

st.header("Found Animal Locations")

loc_df = df[~df['found_lat'].isna()]
loc_df['Date'] = pd.to_datetime(loc_df['DateTime']).dt.date

min_date = loc_df['Date'].min()
max_date = loc_df['Date'].max()

range_min, range_max = st.sidebar.date_input(label="What time frame?", 
    value = [min_date, max_date],
    min_value=min_date, max_value=max_date)

sub_loc = loc_df.loc[(loc_df['Date'] >= range_min) &
                     (loc_df['Date'] <= range_max)]

sub_loc = sub_loc.groupby(['Found Location', 'found_lat', 'found_lon'])['Animal ID'].count().reset_index()
sub_loc = sub_loc.rename(columns={'Animal ID':'count'})

fig2 = px.scatter_mapbox(sub_loc, lat="found_lat", lon="found_lon", 
                        hover_name="Found Location", size='count', color='count', zoom=9)

fig2.update_layout(
    mapbox_style="open-street-map",
    margin={"r":0,"t":0,"l":0,"b":0},
    mapbox=dict(
        center={'lat': 30.2672, 'lon': -97.7431},
    )
)

st.plotly_chart(fig2)


