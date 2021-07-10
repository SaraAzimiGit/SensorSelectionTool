# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pandas as pd
import streamlit as st
import numpy as np
import time
st.title('Occupancy detection selection tool')

q1=st.text_input("Are there energy code compliance requirements? (Yes/No)")

if q1 in ["No","NO","no"]:
    q2 = st.text_input("Would you like occupancy based controls? (Yes/No)")
    if q2 in ["No","NO","no"]:
        st.write("Other control strategies are more appropriate")
    if q2 in ["Yes","YES","yes"]:
        q3 = st.text_input("Does space contain partitions, large equipment or furniture?")
if q1 in ["Yes", "YES", "yes"]:
        q3 = st.text_input("Does space contain partitions, large equipment or furniture?")
        if q3 in ["No", "NO", "no"]:
            st.write("Cameras/vision sensors, PIR, break beam sensors")
        if q3 in ["Yes", "YES", "yes"]:
            q4 = st.text_input("Is space small or well defined?")
            if q4 in ["Yes", "YES", "yes"]:
                q5 = st.text_input("Is there a clear line of sight to all areas?")
                if q5 in ["No","NO","no"]:
                    st.write("Radio frequency-based technology, ultrasonic and smart meters ")
                if q5 in ["Yes", "YES", "yes"]:
                    q6 = st.text_input("Would installation of additional sensors justify payback?")
                    if q6 in ["Yes", "YES", "yes"]:
                        st.write("Cameras/vision sensors, PIR, break beam sensors, electro-mechanical sensors")
                    if q6 in ["No","NO","no"]:
                        st.write("Wi-Fi, Building data")
            if q4 in ["No","NO","no"]:
                q7 = st.text_input("Are there definite space boundaries?")
                if q7 in ["No", "NO", "no"]:
                    st.write("Ultrasonic, microwave, radio frequency-based technology")
                if q7 in ["Yes", "YES", "yes"]:
                    q8 = st.text_input("Is there a high volume of air flow and non-human heat sources?")
                    if q8 in ["Yes", "YES", "yes"]:
                        q9 = st.text_input("Can owners choose an appropriate mounting location away from air flow?")
                        if q9 in ["Yes", "YES", "yes"]:
                            st.write("Ultrasonic, microwave, PIR, infrared camera, acoustic and CO2 sensor")
                        if q9 in ["No", "NO", "no"]:
                            st.write("""Radio frequency-based technology, TOF, Binocular SL depth and optical cameras, 
                            smart meters, electro-mechanical sensors""")
                    if q8 in ["No","NO","no"]:
                        q10 = st.text_input("Is there moving mechanical equipment in the space?")
                        if q10 in ["No", "NO", "no"]:
                            st.write("""Radio frequency-based technology, TOF, Binocular SL depth and optical cameras, 
                            smart meters, electro-mechanical sensors""")
                        if q10 in ["Yes", "YES", "yes"]:
                            st.write("Radio frequency-based technology, smart meters")






