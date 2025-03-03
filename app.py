import streamlit as st
st.markdown(
    """"
    <style>
    body
    background-color: #f0f2f6;
    color: #000000;

    }
    .stApp {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        
        h1 {
            text-align: center;
            font-size: 36px;
            color: #000000;
            margin-bottom: 20px;
            font-weight: bold;
            text-transform: uppercase;
            letter-spacing: 2px;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            
        
        }
        .stButton>button{
            background-color: #007bff;
            color: #ffffff;
            font-size: 18px;
            padding: 10px 20px;
            border-radius: 5px;
            border: none;
            cursor: pointer;
            transition: background-color 0.3s ease;
            &:hover{
                background-color: #0056b3;
            }
             .stButton>button:hover
                 transform:scale(1.05);
                 background-color: #0056b3;
                 box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
                 transform: scale(1.05);
                 transition: all 0.3s ease;
                 &:active{
                    transform: scale(0.95);
                    background-color: #004085;
                    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
                 }
                 .result-box {
                 font-size: 24px;
                 font-weight: bold;
                 color: #000000;
                 text-align: center;
                 padding: 20px;
                 border-radius: 10px;
                 margin: 20px 0;
                 
                 }
                 .footer{
                    text-align: center;
                    font-size: 14px;
                    color: #6c757d;
                    margin-top: 50px;
               
                }
                </style>
                """,
                unsafe_allow_html=True  
            )

           #title and description
st.markdown("<h1> Unit Converter using Streamlit and Python</h1>", unsafe_allow_html=True)
st.write("Easily convert between different units of length, weight and temperature.")

 #sidebar menu
conversion_type = st.sidebar.selectbox("Select the conversion type", ["Length", "Weight", "Temperature"])
value=st.number_input("Enter the value to convert", value=0.0, min_value=0.0, step=0.1)
col1, col2 = st.columns(2)

if conversion_type == "Length":
    with col1:
        st.write("Convert from")
        from_unit = st.selectbox("Select the unit to convert from", ["Meters","Kilometers","Yards","Miles","Nautical Miles","Centimeters","Millimeters","Micrometers","Nanometers","Feet", "Inches"])
    with col2:
        st.write("Convert to")
        to_unit = st.selectbox("Select the unit to convert to", ["Meters","Kilometers","Yards","Miles","Nautical Miles","Centimeters","Millimeters","Micrometers","Nanometers","Feet", "Inches"])
elif conversion_type == "Weight":
    with col1:
        st.write("Convert from")
        from_unit = st.selectbox("Select the unit to convert from", ["Kilograms","Grams","Pounds","Ounces","Stones","Tons"])
    with col2:
        st.write("Convert to")
        to_unit = st.selectbox("Select the unit to convert to", ["Kilograms","Grams","Pounds","Ounces","Stones","Tons"])

elif conversion_type == "Temperature":
    with col1:
        st.write("Convert from")
        from_unit = st.selectbox("Select the unit to convert from", ["Celsius","Fahrenheit","Kelvin"])
    with col2:
        st.write("Convert to")
        to_unit = st.selectbox("Select the unit to convert to", ["Celsius","Fahrenheit","Kelvin"])

#conversion function
def convert_length(value, from_unit, to_unit):
    length_units = {
        "Meters": 1.0,
        "Kilometers": 1000.0,
        "Yards": 0.9144,
        "Miles": 1609.34,
        "Nautical Miles": 1852.0,
        "Centimeters": 0.01,
        "Millimeters": 0.001,
        "Micrometers": 0.000001,
        "Nanometers": 0.000000001,
        "Feet": 0.3048,
        "Inches": 0.0254
    }
    return value * length_units[from_unit] / length_units[to_unit]

def convert_weight(value, from_unit, to_unit):
    weight_units = {
        "Kilograms": 1.0,
        "Grams": 0.001,
        "Pounds": 0.453592,
        "Ounces": 0.0283495,
        "Stones": 6.35029,  
        "Tons": 1000.0          
    }
    return value * weight_units[from_unit] / weight_units[to_unit]

def convert_temperature(value, from_unit, to_unit):
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "Celsius" and to_unit == "Kelvin":
        return value + 273.15
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5/9
    elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
        return (value - 32) * 5/9 + 273.15      
    elif from_unit == "Kelvin" and to_unit == "Celsius":
        return value - 273.15
    elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
        return (value - 273.15) * 9/5 + 32
    else:
        return value                                                
        
#button for conversion
if st.button("Convert"):
    if conversion_type == "Length":
        converted_value = convert_length(value, from_unit, to_unit)
    elif conversion_type == "Weight":
        converted_value = convert_weight(value, from_unit, to_unit)
    elif conversion_type == "Temperature":
        converted_value = convert_temperature(value, from_unit, to_unit)
        st.markdown(f"<div class='result-box'>{value} {from_unit} is equal to {converted_value} {to_unit}</div>", unsafe_allow_html=True)

#footer
st.markdown("<div class='footer'>Developed by [Sana Moin]</div>", unsafe_allow_html=True)   

