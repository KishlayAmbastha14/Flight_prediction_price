# import streamlit as st
# st.html(
#     # "<p><span style='text-decoration: line-through double red;'>Oops</span>!</p>
# )



import streamlit as st
import pickle
import pandas as pd
import requests


import os
if not os.path.exists("flights.pkl"):
    url = "https://drive.google.com/file/d/1r2hO9zENE6CVSS9JAPmL1NJ64bAh9rrc/view?usp=drive_link"
    r = requests.get(url)
    with open("flights.pkl", "wb") as f:
        f.write(r.content)


with open('flights.pkl', 'rb') as f:
    result = pickle.load(f)



def work():
    st.markdown("# Flight Price Prediction")

    airline = ['SpiceJet', 'AirAsia', 'Vistara', 'GO_FIRST', 'Indigo', 'Air_India']
    cities = ['Delhi', 'Mumbai', 'Bangalore', 'Kolkata', 'Hyderabad', 'Chennai']
    times = ['Select Time', 'Early_Morning', 'Morning', 'Afternoon', 'Evening', 'Night', 'Late_Night']
    classes = ['Select Class', 'Economy', 'Business']
    # stop_options = [0,1,2,3]

    st.markdown("<h5 style='color:#4F46E5;'>Airline</h5>",unsafe_allow_html=True)
    selected_airline = st.selectbox("",airline)

    st.markdown("<h5 style='color: #0EA5E9;'>Source City</h5>", unsafe_allow_html=True)
    selected_source = st.selectbox("",cities)

    destination_options = [city for city in cities if city != selected_source]
    st.markdown("<h5 style='color:#0EA5E9;'>Destination City</h5>",unsafe_allow_html=True)

    # **** DEPARTURE TIME ****
    selected_destination = st.selectbox("",destination_options)
    st.markdown("<h5 style='color:#0D9488;'>Departure Time</h5>",unsafe_allow_html=True)
    departure_time = st.selectbox("",times,index=0)

    # **** ARRIVIAL TIME ****
    arrival_options = [time for time in times if time!= departure_time]
    st.markdown("<h5 style='color:#0D9488;'>Arrivial Time</h5>",unsafe_allow_html=True)
    arrival_time = st.selectbox("",arrival_options,index=0)

    st.markdown("<h5 style='color:#ff3300;'>Class</h5>",unsafe_allow_html=True)
    selected_class = st.selectbox("",classes)
    
    # **** DURATION AND DAYS_LEFT ****
    
    duration = st.slider("Flight Duration (hours)", 1, 49, 1)
    days_left = st.slider("Days Left Before Flight", 1, 49, 1)

    # **** STOPS COLUMN ****
    stops_options = ['Select Stops','0', '1', '2', '3']
    st.markdown("<h5 style='color:#F59E0B;'>Number of Stops</h5>",unsafe_allow_html=True)
    stops = st.selectbox("", stops_options)

    if st.button("Predict Price"):
        if departure_time == 'Select Time' or arrival_time == 'Select Time' or selected_class == 'Select Class':
            st.warning("Please select valid input")


        else:
            try:
                input_data = {
                    'airline': selected_airline,
                    'source_city': selected_source,
                    'destination_city': selected_destination,
                    'departure_time': departure_time,
                    'arrival_time': arrival_time,
                    'class': selected_class,
                    'duration': duration,
                    'days_left': days_left,
                    'stops' : stops
                }
        
                input_df = pd.DataFrame([input_data])
                prediction = result.predict(input_df)

                st.success(f"Predicted Price: ₹{int(prediction[0])}")
                st.balloons()
                # st.badge("Thank you! Have a safe journey", icon=":material/check:", color="green")s
                # st.badge("Thank you! Have a safe journey", icon=":material/flight_takeoff:", color="green")
                # st.markdown
                st.markdown("<h5 style='color:#F59E0B;'>Have a safe Journey❤</h5>",unsafe_allow_html=True)

              

            except Exception as e:
                st.error("Something making wrong while making prediction. Please check your inputs")



work()


