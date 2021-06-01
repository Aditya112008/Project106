import plotly.express as px
import csv
import numpy as np

def plotFigure(data_path):
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df,x="CoffeeInMl", y="sleepInHours")
        fig.show()

def getDataSource(data_path):
    coffee_in_ml = []
    sleep_in_hours = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            coffee_in_ml.append(float(row["CoffeeInMl"]))
            sleep_in_hours.append(float(row["sleepInHours"]))

    return {"x" : coffee_in_ml , "y": sleep_in_hours }

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between Coffee In Ml and Sleep In Hours:-  \n--->",correlation[0,1])

def setup():
    data_path  = "./cupsOfCoffeeVsHoursOfSleep.csv"

    datasource = getDataSource(data_path)
    findCorrelation(datasource)
    plotFigure(data_path)

setup()
