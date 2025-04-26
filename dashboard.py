import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

# Load the dataset
df = pd.read_csv("cowrie_login_events.csv")

# Streamlit title
st.title("Login Attempt Dashboard")
st.markdown("This dashboard visualizes the login attempts by username.")

# Show the first few rows of the dataframe
st.subheader("Data Preview")
st.write(df.head())

# Check if the necessary columns exist
if 'event' not in df.columns or 'username' not in df.columns:
    st.error("Required columns ('event', 'username') not found in the dataset.")
else:
    # Option to filter the data for specific events, like failed logins
    event_filter = st.selectbox("Select event type", options=df['event'].unique())
    df_filtered = df[df['event'] == event_filter]
    
    # Create the countplot using Seaborn and Matplotlib
    st.subheader(f"Login Attempts for {event_filter} Event")
    
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.countplot(data=df_filtered, x='event', hue='username', ax=ax, palette='Set2')
    plt.title(f"Login Attempts by Username for {event_filter} Event")
    plt.xticks(rotation=30, ha='right')  # Rotate labels
    st.pyplot(fig)  # Display the plot in Streamlit
    
    # Optionally, show statistics on the filtered data
    st.subheader("Statistics")
    st.write(df_filtered['username'].value_counts())
    
    # Add a download button for the filtered data (optional)
    csv = df_filtered.to_csv(index=False)
    st.download_button(
        label="Download Filtered Data",
        data=csv,
        file_name=f"filtered_{event_filter}_data.csv",
        mime="text/csv",
    )

