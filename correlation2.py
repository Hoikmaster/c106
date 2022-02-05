import csv
import numpy as np
import plotly.express as px

def plotFigure(data_path):
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df,x="Marks In Percentage", y="Days Present")
        fig.show()

def getDataSource(data_path):
    icecreamSale = []
    cooldrinkSale = []

    with open(data_path) as f:
        df = csv.DictReader(f)

        for row in df:
            icecreamSale.append(float(row["Marks In Percentage"]))
            cooldrinkSale.append(float(row["Days Present"]))

    return {"x":icecreamSale, "y":cooldrinkSale}

def getCorrelation(data_source):
    correlation = np.corrcoef(data_source["x"],data_source["y"])
    print("Correlation between Marks In Percentage and Days Present", correlation[0,1])

def setup():
    data_path = "Student Marks vs Days Present.csv"
    data_source = getDataSource(data_path)
    getCorrelation(data_source)
    plotFigure(data_path)

setup()
