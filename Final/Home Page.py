'''
Name:       Olivia Siracusa
CS230:      Section 004
Data:       Motor Vehicle Crashes in MA in 2017
URL:

Description: This website displays data about motor crash vehicles in 2017.
                It include 4 pages about the total amount of crashes, analysis on crash
                conditions, maps, and anaylsis on the speed limit.
'''

#Import packages
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Home Page", page_icon="🏠")

#Import Data
path = "C:/Users/sirac/OneDrive - Bentley University/CS 230/"
df_crash = pd.read_csv(path + "2017_Crashes.csv", index_col='OBJECTID', nrows=10000)

#Title
st.title("Welcome!")

st.write("This website explores the first 10000 entries in dataset Motor Vehicle Crashes in 2017.")

#Sidebar
st.sidebar.success("Click on the other pages of the website")

#[DA2]
st.title("Motor Vehicle Data")
st.write("This data is ascending in date and descending in town name. ")
df_multi_sorted = df_crash.sort_values(by=['CRASH_DATE_TEXT', 'CITY_TOWN_NAME'], ascending=[True, False])
st.write(df_multi_sorted)

#[PY4]
def extract_column_values(data, column_name):
    '''
        Extract values from a specified column of a DataFrame using a list comprehension.

        Parameters:
            - data: The dataframe containing the crash data
            - column_name: The name of the column from which the values are to be extracted.

        Returns:
            - A list containing the values of the specified column.
    '''
    return [value for value in data[column_name]]

st.title("Data in each Column")
selected_columns = st.selectbox("Select column", ['(None Selected)'] + list(df_crash.columns)) #[ST3]

if selected_columns and selected_columns != '(None Selected)': #[DA5]
    values = extract_column_values(df_crash, selected_columns)
    st.write(f"Values for column '{selected_columns}': {values}")



