# This file creates a webpage where review data for several programming courses is plotted onto different types of graphs

import justpy as jp
import pandas as pd
import ChartCreationCode
from pytz import utc
from datetime import datetime
from justpy.chartcomponents import HighCharts

def load_review_data():

    # This function loads in the reviews.csv as a Pandas dataframe and creates additional columns that will be used in the creation of different graphs

    # Loads all review data, makes Timestamp column useable as dates
    review_data = pd.read_csv("reviews.csv", parse_dates = ["Timestamp"])

    # Creates Day column with just the date portion of the Timestamp (all time of day data is dropped for this column)
    review_data["Day"] = review_data["Timestamp"].dt.date    

    return review_data

def create_day_average():

    # This function creates a new data frame of just each day and the average review for that day (all courses)
    day_average = review_data.groupby(["Day"]).mean()

    return day_average

def create_webpage():

    # This function actually creates and returns the webpage

    webpage = jp.QuasarPage(dark = True) # Dark mode for life
    
    # Page header
    h1 = jp.QDiv(a = webpage, text = "Analysis of Course Reviews", classes = "text-h2 text-center q-pt-md text-bold")

    # Body text, lists courses the data covers
    p1 = jp.QDiv(a = webpage, text = "These graphs represent course review data for the following programming courses:", classes = "text-body-1 text-left q-py-lg q-px-md")

    x = 1

    for course in review_data["Course Name"].unique():

        p1 = jp.QDiv(a = webpage, text = str(x) + ". " + course, classes = "text-body-1 text-left q-px-md")

        x += 1

    # Creates spline chart to show average rating per day for all courses
    spline_chart = HighCharts(a = webpage, options = ChartCreationCode.spline_chart_code, classes = "q-pt-lg q-px-md")    
    spline_chart.options.xAxis.categories = list(day_average.index)
    spline_chart.options.series[0].data = list(day_average["Rating"])

    return webpage

# Calls functions to load and manipulate review data
review_data = load_review_data()
day_average = create_day_average()

# Calls website creator
jp.justpy(create_webpage)