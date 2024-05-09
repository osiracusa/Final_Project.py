#Import packages
import streamlit as st
import pydeck as pdk
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
st.set_page_config(page_title="Maps", page_icon="🗺️")
st.sidebar.header("🗺️ Maps")
#Import Data
path = "C:/Users/sirac/OneDrive - Bentley University/CS 230/"
df_crash = pd.read_csv(path + "2017_Crashes.csv", index_col='OBJECTID', nrows=10000)

st.title("Maps")
st.write("This page has multiple different maps visualization of the crash data. ")

df_crash.dropna(subset=['LAT', 'LON'],inplace=True)

# Maps
df_crash.rename(columns={"LAT":"lat", "LON": "lon"}, inplace= True)

select_map = st.radio('Please select the type of map', ['Simple', 'Heatmap', '3d'])

if select_map == 'Simple':
    st.title('Simple Map')
    st.map(df_crash)

elif select_map == '3d':

    st.title('3d Map of Crashes in Massachusetts in 2017')

    st.pydeck_chart(pdk.Deck(
        map_style=None,
        initial_view_state=pdk.ViewState(
            latitude=42.4072,
            longitude=-71.3824,
            zoom=7,
            pitch=50
        ),
        layers=[
            pdk.Layer('HexagonLayer',
                      data=df_crash,
                      get_position='[lon,lat]',
                      radius=200,
                      elevation_scale=4,
                      elevation_range=[0,1000],
                      pickable=True,
                      extruded=True,),
            pdk.Layer(
                'ScatterplotLayer',
                data=df_crash,
                get_position='[lon,lat]',
                get_color='[200, 30, 0, 160]',
                get_radius=200,),
        ],
    ))
    select_city = st.selectbox('Select a City to look further into:', ('Choose a City','Springfield', 'Chelsea', 'Fitchburg', 'Holyoke', 'Hudson', 'New Bedford'))
    if select_city == 'Springfield':
        df_crash_springfield = df_crash[df_crash['CITY_TOWN_NAME'] == 'SPRINGFIELD']
        st.title('3d Map of Crashes in Springfield in 2017')

        st.pydeck_chart(pdk.Deck(
            map_style=None,
            initial_view_state=pdk.ViewState(
                latitude=42.1015,
                longitude=-72.5898,
                zoom=11,
                pitch=50
            ),
            layers=[
                pdk.Layer('HexagonLayer',
                          data=df_crash_springfield,
                          get_position='[lon,lat]',
                          radius=200,
                          elevation_scale=4,
                          elevation_range=[0, 1000],
                          pickable=True,
                          extruded=True, ),
                pdk.Layer(
                    'ScatterplotLayer',
                    data=df_crash_springfield,
                    get_position='[lon,lat]',
                    get_color='[200, 30, 0, 160]',
                    get_radius=200, ),
            ],
        ))
    elif select_city == 'Chelsea':
        df_crash_chelsea = df_crash[df_crash['CITY_TOWN_NAME'] == 'CHELSEA']
        st.title('3d Map of Crashes in Chelsea in 2017')

        st.pydeck_chart(pdk.Deck(
            map_style=None,
            initial_view_state=pdk.ViewState(
                latitude=42.3918,
                longitude=-71.0328,
                zoom=11,
                pitch=50
            ),
            layers=[
                pdk.Layer('HexagonLayer',
                          data=df_crash_chelsea,
                          get_position='[lon,lat]',
                          radius=200,
                          elevation_scale=4,
                          elevation_range=[0, 1000],
                          pickable=True,
                          extruded=True, ),
                pdk.Layer(
                    'ScatterplotLayer',
                    data=df_crash_chelsea,
                    get_position='[lon,lat]',
                    get_color='[255, 0, 0, 128]',
                    get_radius=200, ),
            ],
        ))
    elif select_city == 'Fitchburg':
        df_crash_fitchburg = df_crash[df_crash['CITY_TOWN_NAME'] == 'FITCHBURG']
        st.title('3d Map of Crashes in Fitchburg in 2017')

        st.pydeck_chart(pdk.Deck(
            map_style=None,
            initial_view_state=pdk.ViewState(
                latitude=42.5834,
                longitude=-71.8023,
                zoom=11,
                pitch=50
            ),
            layers=[
                pdk.Layer('HexagonLayer',
                          data=df_crash_fitchburg,
                          get_position='[lon,lat]',
                          radius=200,
                          elevation_scale=4,
                          elevation_range=[0, 1000],
                          pickable=True,
                          extruded=True, ),
                pdk.Layer(
                    'ScatterplotLayer',
                    data=df_crash_fitchburg,
                    get_position='[lon,lat]',
                    get_color='[255, 0, 0, 128]',
                    get_radius=200, ),
            ],
        ))
    elif select_city == 'Holyoke':
        df_crash_holyoke = df_crash[df_crash['CITY_TOWN_NAME'] == 'HOLYOKE']
        st.title('3d Map of Crashes in Holyoke in 2017')

        st.pydeck_chart(pdk.Deck(
            map_style=None,
            initial_view_state=pdk.ViewState(
                latitude=42.2043,
                longitude=-72.6162,
                zoom=11,
                pitch=50
            ),
            layers=[
                pdk.Layer('HexagonLayer',
                          data=df_crash_holyoke,
                          get_position='[lon,lat]',
                          radius=200,
                          elevation_scale=4,
                          elevation_range=[0, 1000],
                          pickable=True,
                          extruded=True, ),
                pdk.Layer(
                    'ScatterplotLayer',
                    data=df_crash_holyoke,
                    get_position='[lon,lat]',
                    get_color='[255, 0, 0, 128]',
                    get_radius=200, ),
            ],
        ))
    elif select_city == 'Hudson':
        df_crash_hudson = df_crash[df_crash['CITY_TOWN_NAME'] == 'HUDSON']
        st.title('3d Map of Crashes in Hudson in 2017')

        st.pydeck_chart(pdk.Deck(
            map_style=None,
            initial_view_state=pdk.ViewState(
                latitude=42.3917,
                longitude=-71.5661,
                zoom=11,
                pitch=50
            ),
            layers=[
                pdk.Layer('HexagonLayer',
                          data=df_crash_hudson,
                          get_position='[lon,lat]',
                          radius=200,
                          elevation_scale=4,
                          elevation_range=[0, 1000],
                          pickable=True,
                          extruded=True, ),
                pdk.Layer(
                    'ScatterplotLayer',
                    data=df_crash_hudson,
                    get_position='[lon,lat]',
                    get_color='[255, 0, 0, 128]',
                    get_radius=200, ),
            ],
        ))
    elif select_city == 'New Bedford':
        df_crash_newbedford = df_crash[df_crash['CITY_TOWN_NAME'] == 'NEW BEDFORD']
        st.title('3d Map of Crashes in New Bedford in 2017')

        st.pydeck_chart(pdk.Deck(
            map_style=None,
            initial_view_state=pdk.ViewState(
                latitude=41.6362,
                longitude=-70.9342,
                zoom=11,
                pitch=50
            ),
            layers=[
                pdk.Layer('HexagonLayer',
                          data=df_crash_newbedford,
                          get_position='[lon,lat]',
                          radius=200,
                          elevation_scale=4,
                          elevation_range=[0, 1000],
                          pickable=True,
                          extruded=True, ),
                pdk.Layer(
                    'ScatterplotLayer',
                    data=df_crash_newbedford,
                    get_position='[lon,lat]',
                    get_color='[255, 0, 0, 128]',
                    get_radius=200, ),
            ],
        ))
if select_map == 'Heatmap':
    st.title('Heatmap')
    st.pydeck_chart(pdk.Deck(
        map_provider="mapbox",
        map_style= pdk.map_styles.SATELLITE,
        tooltip={"text": "Town Name: {CITY_TOWN_NAME}"},
        initial_view_state=pdk.ViewState(
            latitude=42.4072,
            longitude=-71.3824,
            zoom=7,
            pitch=50
        ),
        layers=[
            pdk.Layer(
                "HeatmapLayer",
                data=df_crash,
                opacity=0.9,
                get_position=['lon','lat'],
                get_color=[255, 0, 0, 128],
                pickable=True,
            ),
            pdk.Layer(
                "ScatterplotLayer",
                data=df_crash,
                get_position=['lon', 'lat'],
                get_color=[255, 0, 0, 128],
                get_radius = 200,
                pickable=True,
            )
        ]
    ))
