import streamlit as st
import pandas as pd

df = pd.read_csv("sample_products.csv")

st.title("Data Elements Exploration")
selected_products = st.multiselect("Select the product", df['Product'])

if selected_products:
    st.dataframe(
        df[df['Product'].isin(selected_products)], 
        hide_index=True
    )
else:
    st.dataframe(df, hide_index=True)

# st.table(df)

column_configuration = {
    "Product": st.column_config.TextColumn(
        "Product Name",
        help = "This is the product name"
    ),
    "Sales_Last_6_Months": st.column_config.LineChartColumn(
        "Sales over last 6 Months"
    ),
    "Website": st.column_config.LinkColumn("Website"),
    "Image": st.column_config.ImageColumn("Image")
}

st.dataframe(df, column_config=column_configuration)

edited_data = st.data_editor(df)

st.dataframe(edited_data)

st.metric("Temparature", value="91 °F", delta="-3 °F")

##### Chart Elements ####
st.divider()

st.title("World Population Exploration")

population = pd.read_csv("world_population.csv").set_index("year")

selected_countries = st.multiselect("Select Countries", options=population.columns.to_list())

st.dataframe(population[selected_countries] if selected_countries else population)

st.area_chart(population[selected_countries] if selected_countries else population)