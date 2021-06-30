import streamlit as st
import pandas as pd
import pickle

st.title("What's Your House Worth in Ames, Iowa")

st.header("What are your home's details?")

lot_area = st.slider(label= "What's the total lot area, in square feet?", 
                     min_value=1300, max_value=40000)

sqft_1st = st.slider(label= "What's the area of the first floor, in square feet?", 
                     min_value=350, max_value=2250)

gr_area = st.slider(label= "What's the ground-level living area, in square feet?", 
                    min_value=350, max_value=3000)

if st.button("Click here to get started!"):
    st.write("### Calculating the estimated price for the following home details:")
    st.write(f"Lot Area: {lot_area} sqft")
    st.write(f"First Floor Area: {sqft_1st} sqft")
    st.write(f"Ground-Level Living Area: {gr_area} sqft")

    loaded_model = pickle.load(open('models/model.sav', 'rb'))
    test_data = pd.DataFrame(columns = ['LotArea', '1stFlrSF', 'GrLivArea'])
    test_data = test_data.append({'LotArea': lot_area, '1stFlrSF' : sqft_1st, 'GrLivArea': gr_area}, 
                                 ignore_index=True)

    result = loaded_model.predict(test_data)[0]
    st.write(f"Predicted Sale Price in Ames, Iowa: ${result:.0f}")
