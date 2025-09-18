import streamlit as st
import time
st.title("Welcome to streamlit tutorial")
st.caption("This is a caption")
st.header("This is a header")
st.subheader("This is a subheader")
st.text("This is a simple text")

st.markdown("This is a **markdown** text with _italic_ and **bold** styles.")
st.code("""
    print('Hello, Streamlit!')
    pirnt("hey")
    """, language='python', line_numbers=True)

st.badge("New", color="green")

with st.echo():
    a = 10
    b = 20
    st.write("Sum:", a + b)


# status elements

st.success("This is a success message")
st.info("This is an info message")
st.warning("This is a warning message")
st.error("This is an error message")
st.exception("This is an exception message")

progress_text = "Operation in progress. Please wait."
my_bar = st.progress(0, text=progress_text)
# for percent_complete in range(100):
#     time.sleep(0.1)
    # my_bar.progress(percent_complete + 1, text=progress_text)
# with st.spinner("Loading..."):
#     time.sleep(2)

# with st.status("Status: Downloading data..."):
#     st.write("Searching for data...")
#     time.sleep(2)
#     st.write("Found URL.")
#     time.sleep(1)
#     st.write("Downloading data...")
#     time.sleep(1)
if st.button("Celebrate!"):
    st.snow()

st.text_input("username")
st.text_input("password", type="password")
st.number_input("Enter a number", min_value=0, max_value=100, value=50, step=5)
st.text_area("Enter your address", height=100)
d = st.date_input("Select a date")
st.time_input("Select a time")
st.color_picker("Pick a color", value="#00f900")

st.write(d)

st.toggle("enabled")
st.radio("gender", ["male", "female", "other"])
st.checkbox("I agree to the terms and conditions")
st.selectbox("Select a country", ["USA", "Canada", "UK", "Australia"])
st.multiselect("Select your favorite fruits", ["Apple", "Banana", "Cherry", "Date"])
st.slider("Select a range", 0, 100, 0)
st.select_slider("Select a value", options=["Low", "Medium", "High"])

options = ["Option 1", "Option 2", "Option 3"]
st.pills("Choose an option", options)
st.segmented_control("Choose an option", options)
st.feedback(options='faces')