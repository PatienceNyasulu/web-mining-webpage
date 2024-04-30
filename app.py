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

# Let the user choose a cluster number
st.header('Enter a Cluster')
#num_clusters = kmeans_model.n_clusters
#cluster_number = st.number_input(f'Choose a cluster number (0 to {num_clusters - 1}):', min_value=0, max_value=num_clusters - 1, step=1)
    # getting the input data from the user
col1 = st.columns(1)
    

cluster_number = st.text_input('Enter Cluster 1-12')
        

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
















import requests

def fetch_poster(movie_id):
     url = "https://api.themoviedb.org/3/movie/{}?api_key=c7ec19ffdd3279641fb606d19ceb9bb1&language=en-US".format(movie_id)
     data=requests.get(url)
     data=data.json()
     poster_path = data['poster_path']
     full_path = "https://image.tmdb.org/t/p/w500/"+poster_path
     return full_path


movie=pickle.load(open('kmeans_model.pkl', 'rb'))
movie=pd.DataFrame(movie)
#cluster_list = movie["Cluster"].values
    
    
    # getting the input data from the user
col1 = st.columns(1)
    

cluster = st.text_input('Enter Cluster 1-12')
        

        
    # code for dispay
res = ''


#st.selectbox("select cluster",cluster_list)
# Display movies by cluster



if st.button("show results"):
    
    movie_array = []
    res=movie_array
    cluster_id = cluster
    cluster_movies = movie[movie['cluster_label'] == cluster_id]['title']

    if not cluster_movies.empty:
        print(f"Movies in Cluster {cluster_id}:")
        for movie in cluster_movies:
           movie_array.append(movie)
           
    else:
        res=print(f"No movies found in Cluster {cluster_id}")

st.success(res)
