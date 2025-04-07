import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Data Dashboard",
    layout="wide"
)

st.title("Streamlit Data Dashboard")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)

        st.subheader("Data Preview")
        st.write(df.head())

        st.subheader("Data Summary")
        st.write(df.describe())

        st.subheader("Filter Data")
        column = df.columns.tolist()
        selected_column = st.selectbox("Select column to filter by", column)
        unique_values = df[selected_column].unique()
        selected_value = st.selectbox("Select value", unique_values)

        filtered_df = df[df[selected_column] == selected_value]
        st.write(filtered_df)

        st.subheader("Plot Data")
        x_column = st.selectbox("Select x-axis column", column, key="x_axis")
        y_column = st.selectbox("Select y-axis column", column, key="y_axis")

        if st.button("Generate Plot"):
            if not filtered_df.empty:
                if x_column == y_column:
                    st.error("Please select different columns for x and y axes")
                elif pd.api.types.is_numeric_dtype(filtered_df[y_column]):
                    plot_df = filtered_df[[x_column, y_column]].copy()
                    st.scatter_chart(
                        data=plot_df,
                        x=x_column,
                        y=y_column,
                    )
                else:
                    st.error(f"The selected y-axis column '{y_column}' must contain numeric data")
            else:
                st.warning("No data to plot after filtering")

    except Exception as e:
        st.error(f"Error processing file: {str(e)}")

else:
    st.write("Waiting on file upload...")
