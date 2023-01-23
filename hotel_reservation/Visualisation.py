import pandas as pd 
import matplotlib.pyplot as plt 
import pickle 

def colors(status):
    if status == 'Canceled':
        return 'blue'
    else: return 'orange'

def maptarget(target: str, data: pd.DataFrame):
    colormap = data[target].apply(colors)
    return colormap

def visualize(x: str, y: str, z: str, colormap: pd.Series, data: pd.DataFrame):
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1, projection='3d')
    ax.scatter(data[x], data[y], data[z], c=colormap)
    ax.set_xlabel(x)
    ax.set_ylabel(y)
    ax.set_zlabel(z)
    plt.show()

def main():
    PATH = 'hotel-reservations-classification-dataset\Hotel Reservations.csv'
    df = pd.read_csv(PATH)

    colormap = maptarget('booking_status', df)
    visualize(x = 'lead_time', y = 'no_of_previous_bookings_not_canceled', z = 'arrival_date', colormap= colormap, data=df)

def seecols():

    with open('MODELS/MLpipeline_cols.pkl', 'rb') as f:
        text = pickle.load(f)

    print(text)

if __name__ == '__main__':
    #main()
    seecols()
    