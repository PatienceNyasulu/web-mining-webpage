import streamlit as st
import pandas as pd
import pickle  # Import pickle for loading the DataFrame
from sklearn.cluster import KMeans
import joblib

# Load the DataFrame from the pickle file
with open('merged_movie_cluster.pkl', 'rb') as f:
    df = pickle.load(f)

# Load the K-means model and vectorizer
kmeans_model = joblib.load('kmeans_model.pkl')
#vectorizer = joblib.load('vectorizer.joblib')


# Streamlit application
st.title('WebMining Movie Clusters ')
st.text('Praise Ganyiwa')
st.text('Shamiso Makainganwa')
st.text('Gamuchirai Nyasulu')
st.text('Link to github code: https://github.com/PatienceNyasulu/web-mining-webpage ')

# Let the user choose a cluster number
st.header('Enter a Cluster')
#num_clusters = kmeans_model.n_clusters
#cluster_number = st.number_input(f'Choose a cluster number (0 to {num_clusters - 1}):', min_value=0, max_value=num_clusters - 1, step=1)
    # getting the input data from the user
col1 = st.columns(1)
    

cluster_number = st.number_input('Enter Cluster 1-12')
        

# Convert the cluster_number to an integer to match the data type of the 'cluster' column in the DataFrame
cluster_number = int(cluster_number)

# Display movies in the selected cluster
st.header(f'Movies in Cluster {cluster_number}')

# Filter movies based on the chosen cluster
cluster_movies = df[df['cluster_label'] == cluster_number]

# Display each movie in the cluster, but only the first 6 movies
for _, row in cluster_movies.head(6).iterrows():
    st.subheader(row['title'])
    st.text(f"Description: {row['description']}")
    st.text(f"Listed In: {row['listed_in']}")
    st.text('---')  # Separator for better readability
