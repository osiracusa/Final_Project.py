#Import packages
import streamlit as st
import pandas as pd
st.set_page_config(page_title="Analysis on Crash Conditions", page_icon="☁️")
st.sidebar.header("☁️ Analysis on Crash Conditions ")
#Import Data
path = "C:/Users/sirac/OneDrive - Bentley University/CS 230/"
df_crash = pd.read_csv(path + "2017_Crashes.csv", index_col='OBJECTID', nrows=10000)

st.title("Analysis on Crash Conditions")
st.write("This page offers a valuable tool for analyzing and visualizing motor vehicle crash data, enabling users to extract"
         " key information about specific crashes and gain insights into the prevailing conditions at the time of the incidents.")

# [PY2]
def get_crash_conditions(data, crash_number):
    '''
        Get the light description, weather condition, and road surface condition based on the crash number

        Parameters:
            - data: The dataframe containing the crash data
            - crash_number: The number of the crash for which the conditions are retrieved
        Returns:
            - Light Description, weather condition, and road surface condition for the specified crash.
    '''
    if crash_number in data['CRASH_NUMB'].astype(str).values:
        crash_index = data[data['CRASH_NUMB'].astype(str) == crash_number].index[0]
        light_descript = data.at[crash_index, 'AMBNT_LIGHT_DESCR']
        weather_condition = data.at[crash_index, 'WEATH_COND_DESCR']
        road_surface = data.at[crash_index, 'ROAD_SURF_COND_DESCR']
        return light_descript, weather_condition, road_surface
    else:
        return None, None, None

st.title("Crash Condition Viewer")

crash_num = st.text_input("Enter the crash number: ", "4304436")
if st.button("Get Crash Conditions"):
    light, weather, road_surface = get_crash_conditions(df_crash, crash_num)
    if light is not None:
        st.write(f"The light description for crash number {crash_num} is:", light)
        st.write(f"The weather condition for crash number {crash_num} is:", weather)
        st.write(f"The road surface condition for crash number {crash_num} is:", road_surface)
    else:
        st.write(f"No crash found with number {crash_num}")

st.title('Bar Chart for various conditions')
selected_columns = ['AMBNT_LIGHT_DESCR', 'WEATH_COND_DESCR', 'ROAD_SURF_COND_DESCR']
df_selected = df_crash[selected_columns]
melt_df = df_selected.melt(var_name='Condition', value_name='Description')
selected_condition = st.selectbox("Select a condition", selected_columns)
pivot_df = melt_df[melt_df['Condition'] == selected_condition].groupby('Description').size().reset_index(name='count')
st.bar_chart(pivot_df.set_index('Description'), color="#C70039")

