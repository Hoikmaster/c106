import csv
import numpy as np
import plotly.express as px

def plotFigure(data_path):
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df,x="Coffee in ml", y="sleep in hours")
        fig.show()

def getDataSource(data_path):
    icecreamSale = []
    cooldrinkSale = []

    with open(data_path) as f:
        df = csv.DictReader(f)

        for row in df:
            icecreamSale.append(float(row["Coffee in ml"]))
            cooldrinkSale.append(float(row["sleep in hours"]))

    return {"x":icecreamSale, "y":cooldrinkSale}

def getCorrelation(data_source):
    correlation = np.corrcoef(data_source["x"],data_source["y"])
    print("Correlation between Coffee drunk and sleep in hours", correlation[0,1])

def setup():
    data_path = "cups of coffee vs hours of sleep.csv"
    data_source = getDataSource(data_path)
    getCorrelation(data_source)
    plotFigure(data_path)

setup()
