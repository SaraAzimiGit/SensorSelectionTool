# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import streamlit as st
import pandas as pd
from itertools import combinations


@st.cache
def r_subset(arr, r):
    return list(combinations(arr,r))

def convert(string):
    li = list(string.split(",", ))
    return li

def main():
    siteHeader = st.beta_container()
    appSelection = st.beta_container()
    with siteHeader:
        st.title('Occupancy detection technology screening tool')
        st.text("""With this tool you can screen for the best occupancy detection options 
that suits your facility management application needs""")

    with appSelection:
        info_app = {'Occupancy Resolution': [4, 4, 2, 3, 3, 3, 2, 1, 2, 1, 1, 2, 2, 2],
                    'Spatial Resolution': [3, 3, 2, 3, 3, 2, 3, 2, 2, 3, 4, 2, 2, 2],
                    'Accuracy': [3, 3, 2, 3, 3, 3, 2, 1, 1, 3, 2, 1, 1, 1]}
        info_app_1 = {
            'Occupancy_Resolution': ['Tracking', 'Tracking', 'Count', 'Identity', 'Identity', 'Identity', 'Count',
                                     'Presence', 'Count', 'Presence', 'Presence', 'Count', 'Count', 'Count'],
            'Spatial_Resolution': ['Room', 'Room', 'Floor', 'Room', 'Room', 'Floor', 'Room', 'Floor', 'Floor', 'Room',
                                   'Workstation', 'Floor', 'Floor', 'Floor'],
            'Accuracy': ['High', 'High', 'Medium', 'High', 'High', 'High', 'Medium', 'Low', 'Low', 'High', 'Medium',
                         'Low', 'Low', 'Low']}
        columns = ['Occupancy Resolution', 'Spatial Resolution', 'Accuracy']
        df = pd.DataFrame(data=info_app, columns=columns,
                          index=['Emergency evacuation and rescue', 'Disease control', 'Space utilization rate',
                                 'Access control', 'Intrusion detection',
                                 'Surveillance', 'Smart cleaning', 'Heating/cooling control',
                                 'Ventilation control', 'Lighting control', 'Plug load control',
                                 'Heating/cooling energy usage', 'Lighting energy usage', 'Plug load energy usage'])
        df_1 = pd.DataFrame(data=info_app_1, columns=columns,
                            index=['Emergency evacuation and rescue', 'Disease control', 'Space utilization rate',
                                   'Access control', 'Intrusion detection', 'Surveillance', 'Smart cleaning',
                                   'Heating/cooling control',
                                   'Ventilation control', 'Lighting control', 'Plug load control',
                                   'Heating/cooling energy usage', 'Lighting energy usage', 'Plug load energy usage'])
        info_sensor_0 = {
            'Sensor': ['PIR/Break beam/Ultrasonic/Microwave', 'TOF/Binocular/SL/Infrared camera',
                       'Optical camera', 'Wi-Fi', 'RFID tag/UWB/Bluetooth', 'Acoustic/Smart meters', 'Door', 'CO2',
                       'Piezoelectric'],
            'Occupancy Resolution': [1, 2, 3, 4, 4, 2, 1, 2, 1],
            'Spatial Resolution': [4, 4, 4, 4, 3, 3, 3, 3, 3],
            'Accuracy': [1, 3, 3, 3, 3, 2, 1, 1, 1],
            'Privacy': [3, 3, 1, 1, 1, 3, 3, 3, 3],
            'Cost': [1, 3, 3, 1, 2, 1, 1, 1, 1]}
        info_sensor_1 = {
            'Occupancy Resolution': ['Presence', 'Count', 'Identity', 'Tracking', 'Tracking', 'Count', 'Presence',
                                     'Count', 'Presence'],
            'Spatial Resolution': ['Workstation', 'Workstation', 'Workstation', 'Workstation', 'Room', 'Room', 'Room',
                                   'Room', 'Room'],
            'Accuracy': ['Low', 'High', 'High', 'High', 'High', 'Medium', 'Low', 'Low', 'Low'],
            'Privacy': ['High', 'High', 'Low', 'Low', 'Low', 'High', 'High', 'High', 'High'],
            'Cost': ['Low', 'High', 'High', 'Low', 'Medium', 'Low', 'Low', 'Low', 'Low']}
        columns_sensor_0 = ['Sensor','Occupancy Resolution', 'Spatial Resolution', 'Accuracy', 'Privacy', 'Cost']
        columns_sensor_1 = ['Occupancy Resolution', 'Spatial Resolution', 'Accuracy', 'Privacy', 'Cost']

        df_0 = pd.DataFrame(data=info_sensor_0, columns=columns_sensor_0,
                            index=['PIR/Break beam/Ultrasonic/Microwave', 'TOF/Binocular/SL/Infrared camera',
                                   'Optical camera', 'Wi-Fi', 'RFID tag/UWB/Bluetooth', 'Acoustic/Smart meters', 'Door',
                                   'CO2', 'Piezoelectric'])
        df1_1 = pd.DataFrame(data=info_sensor_1, columns=columns_sensor_1,
                             index=['PIR/Break beam/Ultrasonic/Microwave', 'TOF/Binocular/SL/Infrared camera',
                                    'Optical camera', 'Wi-Fi', 'RFID tag/UWB/Bluetooth', 'Acoustic/Smart meters',
                                    'Door', 'CO2', 'Piezoelectric'])
        menu_items = ["View all sensors available", "Select single type of sensor based on application criteria",
                      "Select combination of sensors based on application criteria"]
        occ_res_cat=['N/A','Presence','Count','Identity','Tracking']
        occ_res_num=[0,1,2,3,4]
        df2_occ=pd.DataFrame(data=occ_res_num,index=occ_res_cat)
        st.write(df2_occ)
       # df3_occ=pd.DataFrame(data=occ_res_num)
        with st.form(key="Selecting columns"):
            q1 = st.multiselect('Select facility management application(s)', df_1.index)
            menu_choices = st.selectbox('Select your sensor options', menu_items)
            privacy_q=st.multiselect('What level of occupancy resolution is not allowed for data collection',df1_1['Occupancy Resolution'].unique())
            submit_button = st.form_submit_button(label='Update')

        if submit_button:
            #res=df2_occ.loc[privacy_q]
            st.write(privacy_q)

            result_1 = df_1.loc[q1]
            app_selected = pd.DataFrame(data=result_1, columns=columns)
            app_selected.update(df)

            max_occ_res = app_selected['Occupancy Resolution'].max()
            max_spatial_res = app_selected['Spatial Resolution'].max()
            max_acc = app_selected['Accuracy'].max()

            min_occ_res = app_selected['Occupancy Resolution'].min()
            min_spatial_res = app_selected['Spatial Resolution'].min()
            min_acc = app_selected['Accuracy'].min()

            if menu_choices == "View all sensors available":
                st.write("Below are all the sensors Available")
                st.dataframe(df1_1)
            if menu_choices == "Select single type of sensor based on application criteria":
                df_0 = df_0.drop(columns='Sensor')
                filter_table1 = df_0.loc[
                    (df_0['Occupancy Resolution'] >= max_occ_res) & (df_0['Accuracy'] >= max_acc) & (
                            df_0['Spatial Resolution'] >= max_spatial_res)]
                filter_table1.update(df1_1)
                if filter_table1[filter_table1["Occupancy Resolution"].isin(privacy_q)]:
                    st.dataframe(filter_table1)
            if menu_choices == "Select combination of sensors based on application criteria":
                min_table = df_0.loc[(min_occ_res <= df_0['Occupancy Resolution']) & (min_acc <= df_0['Accuracy']) & (
                            min_spatial_res <= df_0['Spatial Resolution'])]
                sensor = min_table.index
                min_table = df_0.loc[(min_occ_res <= df_0['Occupancy Resolution']) & (min_acc <= df_0['Accuracy']) & (
                            min_spatial_res <= df_0['Spatial Resolution'])]

                for f in range(len(sensor) + 1):  # iterate number of items in combination
                    if f >= 2:
                        for i in r_subset(sensor, f):  # iterate over every combination
                            is_ok=False
                            for key in i:  # iterate over any item in a combination
                                multi_row = min_table[min_table['Sensor'].isin(convert(key))]
                                value_occ_res = multi_row['Occupancy Resolution'].item()
                                value_spatial_res = multi_row['Spatial Resolution'].item()
                                value_acc = multi_row['Accuracy'].item()
                                if value_occ_res >= max_occ_res or value_spatial_res >= max_spatial_res or value_acc >= max_acc:  # pick any item in a  combination that meets the criteria
                                    is_ok=True
                            if is_ok==True:
                                info = df_0.loc[i,:]
                                info = info.drop(columns='Sensor')
                                info.update(df1_1)
                                st.dataframe(info)
                                st.write(info['Occupancy Resolution'])


if __name__ == "__main__":
    main()
