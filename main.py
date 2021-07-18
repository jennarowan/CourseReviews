# This file creates a webpage where review data for several programming courses is plotted onto different types of graphs

import justpy as jp
import pandas as pd
import ChartCreationCode
from pytz import utc
from datetime import datetime
from justpy.chartcomponents import HighCharts



def load_review_data():

    review_data = pd.read_csv("reviews.csv", parse_dates = ["Timestamp"])

    review_data["Day"] = review_data["Timestamp"].dt.date
    global day_average
    day_average = review_data.groupby(["Day"]).mean()

def create_webpage():

    webpage = jp.QuasarPage(dark = True)
    
    h1 = jp.QDiv(a = webpage, text = "Analysis of Course Reviews", classes = "text-h2 text-center q-pt-md text-bold")

    p1 = jp.QDiv(a = webpage, text = "These graphs represent course review analysis", classes = "text-body-1 text-center q-pt-lg")

    spline_chart = HighCharts(a = webpage, options = ChartCreationCode.spline_chart_code, classes = "q-pt-lg q-px-md")    
    spline_chart.options.xAxis.categories = list(day_average.index)
    spline_chart.options.series[0].data = list(day_average["Rating"])

    return webpage

load_review_data()
jp.justpy(create_webpage)