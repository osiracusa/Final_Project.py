#Import packages
import streamlit as st
import pandas as pd
import seaborn as sns
st.set_page_config(page_title="Car Crash Analysis", page_icon="🚗")
st.sidebar.header("🚗 Car Crash Analysis")

#Import Data
path = "C:/Users/sirac/OneDrive - Bentley University/CS 230/"
df_crash = pd.read_csv(path + "2017_Crashes.csv", index_col='OBJECTID', nrows=10000)

#Information about the page
st.title("Car Crash Analysis")
st.write("The information below provides an analysis of motor vehicle crashes based on specific location and date parameters."
         "The data below is valuable for conducting targeted analyses and gaining insights into how frequent crashes occur in certain areas over time.")
st.write("\n Look how many crashes occurred on a certain date by inputting a town name and date:")
#[PY1]
def crash_by_location(data, location, date="1/1/2017"):
    '''
        Analyzing motor vehichle crashes for a specific date and location.

        Parameters:
            - data: the dataframe containing the crash data
            - location: The city where the crash occurred
            - date: The date the crash happened. Default is 1/1/2017

        Returns:
            - The total number of crashes on the provided data, year and location
    '''
    total_crashes = 0
    for index, row in data.iterrows(): #[DA8]
        if row['CITY_TOWN_NAME'].lower().capitalize() == location and row['CRASH_DATE_TEXT'] == date: #[DA5]
            total_crashes += 1
    return total_crashes


town_name = st.text_input("Enter the town name:") #[ST1]
date = st.text_input("Enter a date in MM/DD/YYYY format:", "01/01/2017")
if st.button("Analyze"):
    crash_count = crash_by_location(df_crash, town_name, date)
    st.write(f"The total number of crashes in {town_name} in {date}: {crash_count}")


st.title("Barplot")
st.write("This barplot displays whether the car accident is a hit and run, type of road condition and the average number of cars involved with those two criterias. "
         "This plot is aimed to provide information about patterns and trends in crash occurences, and aiding in informed decision-making for improving road safety measures. ")
sns.set_theme(style="whitegrid") #[VIZ3]
g = sns.catplot(
    data=df_crash, kind="bar",
    x="ROAD_SURF_COND_DESCR", y="NUMB_VEHC", hue="HIT_RUN_DESCR",
    errorbar="sd", palette="dark", alpha=.5, height=15
)
g.despine(left=True)
g.set_axis_labels("", "Average Number of Cars")
st.set_option('deprecation.showPyplotGlobalUse', False)
g.legend.set_title("")
st.pyplot()