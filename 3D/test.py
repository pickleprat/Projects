import pandas as pd 
from clusterplot import ClusterPlot3D

if __name__ == '__main__':
    df = pd.read_csv('ed_sheeran_spotify.csv', index_col='id').drop(['Unnamed: 0'], axis=1)
    df['pc'] = pd.cut(df.popularity, bins=3)
    plot = ClusterPlot3D(x = 'energy', y = 'loudness', z = 'danceability', data = df, target='pc' )
    plot.displayplot()
    
