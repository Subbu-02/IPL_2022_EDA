import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your dataset
@st.cache_data  # This decorator caches the data to speed up the app
def load_data():
    data_dir = './ipl-player-performance-dataset/IPL Dataset - 2022/IPL Dataset - 2022'
    data = pd.read_csv(data_dir + '/Most Runs - 2022.csv')
    # Perform any data preprocessing here if necessary
    return data

def runs_analysis(df):
    fig, ax = plt.subplots()
    ax.hist(df['Runs'], bins=20)
    return fig

def strike_rate_analysis(df):
    fig, ax = plt.subplots()
    sns.scatterplot(data=df, x='BF', y='Runs', hue='SR', size='SR', ax=ax)
    ax.set_title('Strike Rate Analysis')
    ax.set_xlabel('Balls Faced')
    ax.set_ylabel('Total Runs')
    return fig

def average_analysis(df):
    fig, ax = plt.subplots()
    ax.hist(df['Avg'], bins=20)
    return fig

def fours_analysis(df):
    fig, ax = plt.subplots()
    ax.hist(df['4s'], bins=20)
    return fig

def sixes_analysis(df):
    fig, ax = plt.subplots()
    ax.hist(df['6s'], bins=20)
    return fig

def highest_impact_players(df):
    df['Impact_Score'] = (df['Runs'] * df['SR']) / 100
    top_5_impact_score = df.sort_values(by='Impact_Score', ascending=False).head(5)
    return top_5_impact_score[['Player', 'Impact_Score']]

df = load_data()

# Title of your web app
st.title('Cricket Data Analysis')

# Show the dataset
if st.checkbox('Show Raw Data'):
    st.subheader('Raw Data')
    st.write(df)

# Interactive selection for analysis
option = st.radio('Which metric would you like to analyze?', 
                  ('Runs', 'Strike Rate', 'Average', 'Fours', 'Sixes', 'Highest Impact Players'))

# Based on selection, display appropriate analysis/visualization
if option == 'Runs':
    st.subheader('Runs Analysis')
    fig = runs_analysis(df)
    st.pyplot(fig)
elif option == 'Strike Rate':
    st.subheader('Strike Rate Analysis')
    fig = strike_rate_analysis(df)
    st.pyplot(fig)
elif option == 'Average':
    st.subheader('Average Analysis')
    fig = average_analysis(df)
    st.pyplot(fig)
elif option == 'Fours':
    st.subheader('Fours Analysis')
    fig = fours_analysis(df)
    st.pyplot(fig)
elif option == 'Sixes':
    st.subheader('Sixes Analysis')
    fig = sixes_analysis(df)
    st.pyplot(fig)
elif option == 'Highest Impact Players':
    st.subheader('Highest Impact Players')
    data = highest_impact_players(df)
    st.write(data)