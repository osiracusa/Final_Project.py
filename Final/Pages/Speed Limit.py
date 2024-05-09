#Import packages
import streamlit as st
import pydeck as pdk
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
st.set_page_config(page_title="Speed Limit")
st.sidebar.header("Speed Limit ")
#Import Data
path = "C:/Users/sirac/OneDrive - Bentley University/CS 230/"
df_crash = pd.read_csv(path + "2017_Crashes.csv", index_col='OBJECTID', nrows=10000)



def calc_avg_speed_limit(data):
    """
        Find the average speed limit for roads where crashes were recorded

        Parameters:
            - data: The dataframe containing the crash data

        Returns:
            - The average speed limit of the roads where crashes occurred
    """
    average_speed_limit = data['SPEED_LIMIT'].mean()
    return average_speed_limit

st.title("Average Speed Limit Analysis")
st.write("Serves as a valuable tool for analyzing and understanding the speed limit dynamics "
         "surrounding motor vehicle crashes, offering insights into road safety and traffic management.")

avg_speed_limit = calc_avg_speed_limit(df_crash)
st.write(f"The average speed limit of roads where crashes occurred is: {avg_speed_limit:.2f}")

st.title("Speed limit compared to the average speed of crashes")
slider_speed = st.slider("Select a speed", min_value=0, max_value=100, value= 40, step=1) #[ST2]

if avg_speed_limit < slider_speed: #[DA4]
    st.write(f"The speed limit of {slider_speed} on roads where crashes occurred is relatively high compared to the average speed of {avg_speed_limit:.2f}.")
else:
    st.write(f"The speed limit of {slider_speed} on roads where crashes occurred is relatively low compared to the average speed of {avg_speed_limit:.2f}.")

s_speed = df_crash['SPEED_LIMIT'].value_counts()
st.set_option('deprecation.showPyplotGlobalUse', False)
plt.figure(figsize=(10,10))
explode = (0,0.1,0,0,0,0,0,0,0,0,0,0,0,) #explode second slice
s_speed.plot(kind='pie', startangle=180,explode=explode,autopct=lambda p:'{:.0f}'.format(p*sum(s_speed/100))) #[DA1]
plt.title('Distribution of Speed Limits')
plt.legend(title="Speed Limits", loc='lower right')
st.pyplot()


#[DA3] Highest speed and lowest speed
st.write("Below displays the highest and the lowest speed limits at all the crash sites. ")
highest_speed = df_crash['SPEED_LIMIT'].nlargest(1)
lowest_speed = df_crash['SPEED_LIMIT'].nsmallest(1)
st.write(f"The highest speed limit recorded at a crash site is {highest_speed.values[0]:.0f} mph.")
st.write(f"The lowest speed limit recorded at a crash site is {lowest_speed.values[0]:.0f} mph.")

