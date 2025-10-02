import streamlit as st
import pandas as pd
import pickle

# Load the trained pipeline (Random Forest with preprocessing inside)
with open('LaptopProject.pkl', 'rb') as f:
    model = pickle.load(f)

# Streamlit App Title
st.title("💻 Laptop Price Prediction App")

st.write(
    """s
    This app predicts the **estimated price** of a used Laptop.
    
    Fill out the details below:
    """
)

# Input fields for user
Brand = st.text_input("Enter Brand Name")
Processor = st.text_input("Enter Processor")
Ram=st.selectbox("Select Ram Type",[4,8,12,16,32,64])
Storage=st.number_input("Enter storage ")
Storage_Type=st.selectbox("Select Storage Type",["HDD","SSD","HDD + SSD"])
GPU=st.text_input("Enter GPU")
Screen_size=st.number_input("Enter screen_size")
OS=st.selectbox("Select OS",["Linux","macos","Windows 10","Windows 11"])
Weight=st.number_input("Enter a Weight")

# Prediction Button
if st.button("Predict Price"):
    # Create input DataFrame with correct column order
    # input_data = pd.DataFrame(
    #     [[Brand,Processor,Ram,Storage,Storage_Type,GPU,Screen_size,OS,Weight]],
    #     columns=["Brand", "Processor", "RAM(GB)", "Storage Type","GPU","Screen Size(inches)","OS","Weight(kg)"]
    # )

    input_data = pd.DataFrame(
    [[Brand, Processor, Ram, Storage, Storage_Type, GPU, Screen_size, OS, Weight]],
    columns=["Brand", "Processor", "RAM (GB)", "Storage (GB)", "Storage Type", "GPU", "Screen Size (inches)", "OS", "Weight (kg)"]
)

    # # Predict using the loaded model
    predicted_price = model.predict(input_data)[0]

    # Show result
    st.success(f"Estimated Car Price: ₹ {int(predicted_price):,}")