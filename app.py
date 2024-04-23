{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "ff12c633-4a20-432b-b3e9-f6f16cd899e4",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "from sklearn.feature_extraction.text import TfidfVectorizer\n",
    "from sklearn.cluster import KMeans\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "af25830f-2ff3-4910-b1c5-dcc01aa5b3a7",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Sample movie data\n",
    "movie_data = {\n",
    "    'title': ['Movie 1', 'Movie 2', 'Movie 3', 'Movie 4', 'Movie 5'],\n",
    "    'description': [\n",
    "        'A group of friends embark on a journey to save the world.',\n",
    "        'A young boy discovers he has magical powers.',\n",
    "        'An epic tale of love and betrayal set in ancient times.',\n",
    "        'A comedy about a dysfunctional family on vacation.',\n",
    "        'A thriller about a detective solving a murder mystery.'\n",
    "    ]\n",
    "}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "3c1b0180-b6db-466c-b5c5-4225034def8d",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create DataFrame from movie data\n",
    "df = pd.DataFrame(movie_data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "866d1511-79ab-4ff7-83a7-1f0198672632",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Vectorize movie descriptions\n",
    "vectorizer = TfidfVectorizer(stop_words='english')\n",
    "X = vectorizer.fit_transform(df['description'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "8013e242-76b2-438e-9e61-d90322261cc9",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Perform K-means clustering\n",
    "k = 2  # Number of clusters\n",
    "kmeans = KMeans(n_clusters=k)\n",
    "kmeans.fit(X)\n",
    "df['cluster'] = kmeans.labels_"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "95ef0ce8-3147-43af-a4c0-3b818af94149",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "DeltaGenerator()"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Display clustered movies\n",
    "st.title('Movie Clustering')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "6d7a1de7-828e-45c5-8891-dd2d34992425",
   "metadata": {},
   "outputs": [],
   "source": [
    "for cluster_id in range(k):\n",
    "    st.subheader(f'Cluster {cluster_id + 1}')\n",
    "    cluster_movies = df[df['cluster'] == cluster_id]['title'].tolist()\n",
    "    for movie in cluster_movies:\n",
    "        st.write(movie)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8973c731-684a-4358-b7bc-283a8de4eb59",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
