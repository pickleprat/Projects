import pandas as pd  
from matplotlib import pyplot as plt 
import numpy as np 
from sklearn.cluster import KMeans
from matplotlib import colors 
import random 
from sklearn.preprocessing import StandardScaler 

class InvalidTargetException(Exception):

    def __init__(self, message='The target variable must be categorical amd must have less than 50 categories'):
        self.message = message 
        super().__init__(self.message)

class ExcessiveCategoriesException(Exception):
    
    def __init__(self, message='The target has excessive categories'):
        self.message = message 
        super().__init__(self.message)

class ClusterPlot3D():

    def __init__(self, x: str, y: str, z: str, data: pd.DataFrame, n_clusters=1, target='cluster') :
        
        self.X, self.Y, self.Z = data[x].values, data[y].values, data[z].values
        self.categoricals = data.columns
        self.numericals = data.select_dtypes(float).columns
        self.scaler = StandardScaler()
        self.scaled_data = self.scaler.fit_transform(data.loc[:, [x, y, z]])
        self.km = KMeans(n_clusters=n_clusters)
        self.km.fit(self.scaled_data)
        self.labels = self.km.labels_
        self.xlabel, self.ylabel, self.zlabel = x, y, z 

        if target not in self.categoricals and target != 'cluster':
            raise InvalidTargetException()

        if target == 'cluster':
            self.unique_targets = np.arange(n_clusters).tolist()
            self.target_count = n_clusters
        else: 
            self.unique_targets = list(data[target].unique()) 
            self.target_count = len(self.unique_targets)

        if n_clusters >= 50 or self.target_count >= 50: 
            raise ExcessiveCategoriesException()
            
        self.colormap = {}
        self.COLORS = list(colors.CSS4_COLORS.keys())

        for ind, t_name in enumerate(self.unique_targets): 
            random.shuffle(self.COLORS)
            self.colormap[t_name] = self.COLORS[ind]

        if target != 'cluster':
            self.labels = data[target]

        self.colors = [self.colormap[target] for target in self.labels]
        

    def displayplot(self):
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1, projection='3d')
        ax.set_xlabel(self.xlabel)
        ax.set_ylabel(self.ylabel)
        ax.set_zlabel(self.zlabel)
        ax.scatter(self.X, self.Y, self.Z, c=self.colors)
        plt.show()


        


        
        