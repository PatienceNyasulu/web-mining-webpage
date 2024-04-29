def main():
    # Load the data
    #df = load_data('NETFLIX MOVIES AND TV SHOWS CLUSTERING.csv')

    # Perform K-means clustering
    cluster_labels = run_kmeans_clustering(df)

    # Display the clustering results
    st.title('K-means Clustering Results')
    st.write('Cluster Labels:', cluster_labels)

if __name__ == '__main__':
    main()
