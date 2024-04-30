import pickle
import pandas as pd
import streamlit as st
import streamlit


import requests

def fetch_poster(movie_id):
     url = "https://api.themoviedb.org/3/movie/{}?api_key=c7ec19ffdd3279641fb606d19ceb9bb1&language=en-US".format(movie_id)
     data=requests.get(url)
     data=data.json()
     poster_path = data['poster_path']
     full_path = "https://image.tmdb.org/t/p/w500/"+poster_path
     return full_path


movie=pickle.load(open('merger_movie_cluster.pkl', 'rb'))
movie=pd.DataFrame(movie)
#cluster_list = movie["Cluster"].values

 #sidebar for navigation

    
    
# Loan Default Prediction Page

    # page title
st.title('Movie Clustering')
st.text('Praise Ganyiwa')
st.text('Shamiso Makainganwa')
st.text('Gamuchirai Nyasulu')
    
    
    
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
