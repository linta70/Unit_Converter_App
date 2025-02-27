import streamlit as st
import pandas as pd

# Set page configuration
st.set_page_config(
    page_title="Universal Unit Converter",
    page_icon="🔄",
    layout="wide"
)

# Custom CSS to make the app more attractive
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stSelectbox {
        margin-bottom: 1rem;
    }
    .converter-container {
        background-color: #f8f9fa;
        padding: 2rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    h1 {
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("🔄 Universal Unit Converter")
st.markdown("---")

# Conversion functions
def length_conversion(value, from_unit, to_unit):
    # Base unit: meters
    length_units = {
        'Kilometers': 1000,
        'Meters': 1,
        'Centimeters': 0.01,
        'Millimeters': 0.001,
        'Miles': 1609.34,
        'Yards': 0.9144,
        'Feet': 0.3048,
        'Inches': 0.0254
    }
    return value * length_units[from_unit] / length_units[to_unit]

def weight_conversion(value, from_unit, to_unit):
    # Base unit: kilograms
    weight_units = {
        'Tonnes': 1000,
        'Kilograms': 1,
        'Grams': 0.001,
        'Milligrams': 0.000001,
        'Pounds': 0.453592,
        'Ounces': 0.0283495
    }
    return value * weight_units[from_unit] / weight_units[to_unit]

def temperature_conversion(value, from_unit, to_unit):
    if from_unit == 'Celsius':
        if to_unit == 'Fahrenheit':
            return (value * 9/5) + 32
        elif to_unit == 'Kelvin':
            return value + 273.15
    elif from_unit == 'Fahrenheit':
        if to_unit == 'Celsius':
            return (value - 32) * 5/9
        elif to_unit == 'Kelvin':
            return (value - 32) * 5/9 + 273.15
    elif from_unit == 'Kelvin':
        if to_unit == 'Celsius':
            return value - 273.15
        elif to_unit == 'Fahrenheit':
            return (value - 273.15) * 9/5 + 32
    return value

def area_conversion(value, from_unit, to_unit):
    # Base unit: square meters
    area_units = {
        'Square Kilometers': 1000000,
        'Square Meters': 1,
        'Square Miles': 2589988.11,
        'Square Yards': 0.836127,
        'Square Feet': 0.092903,
        'Acres': 4046.86,
        'Hectares': 10000
    }
    return value * area_units[from_unit] / area_units[to_unit]

# Available conversions
conversion_types = {
    'Length': ['Kilometers', 'Meters', 'Centimeters', 'Millimeters', 'Miles', 'Yards', 'Feet', 'Inches'],
    'Weight': ['Tonnes', 'Kilograms', 'Grams', 'Milligrams', 'Pounds', 'Ounces'],
    'Temperature': ['Celsius', 'Fahrenheit', 'Kelvin'],
    'Area': ['Square Kilometers', 'Square Meters', 'Square Miles', 'Square Yards', 'Square Feet', 'Acres', 'Hectares']
}

# Main conversion interface
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="converter-container">', unsafe_allow_html=True)
    conversion_type = st.selectbox('Select Conversion Type', list(conversion_types.keys()))
    
    from_unit = st.selectbox('From Unit', conversion_types[conversion_type])
    value = st.number_input('Enter Value', value=0.0)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="converter-container">', unsafe_allow_html=True)
    to_unit = st.selectbox('To Unit', conversion_types[conversion_type])
    
    # Perform conversion
    if conversion_type == 'Length':
        result = length_conversion(value, from_unit, to_unit)
    elif conversion_type == 'Weight':
        result = weight_conversion(value, from_unit, to_unit)
    elif conversion_type == 'Temperature':
        result = temperature_conversion(value, from_unit, to_unit)
    elif conversion_type == 'Area':
        result = area_conversion(value, from_unit, to_unit)
    
    st.markdown(f'### Result')
    st.markdown(f'<h2 style="color: #1f77b4;">{result:.6g} {to_unit}</h2>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Add information about the converter
st.markdown("---")
st.markdown("""
### About this Unit Converter
This universal unit converter supports various conversion types including:
- Length (km, m, cm, mm, miles, yards, feet, inches)
- Weight (tonnes, kg, g, mg, pounds, ounces)
- Temperature (Celsius, Fahrenheit, Kelvin)
- Area (km², m², miles², yards², feet², acres, hectares)

Simply select the type of conversion you want to perform, choose your input and output units, 
and enter the value you want to convert. The result will be displayed instantly!
""")
