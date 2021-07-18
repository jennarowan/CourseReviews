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

    # Creates Week column so that averages can be shown by what week of the year the ratings cover
    review_data["Week"] = review_data["Timestamp"].dt.strftime("%Y-%U")

    # Creates Month column for average ratings
    review_data["Month"] = review_data["Timestamp"].dt.strftime("%Y-%m")

    return review_data

def create_day_average():

    # This function creates a new data frame of just each day and the average review for that day (all courses)
    day_average = review_data.groupby(["Day"]).mean()

    return day_average

def create_week_average():

    # This function creates a new data frame of just each week and the average review for that week (all courses)
    week_average = review_data.groupby(["Week"]).mean()

    return week_average

def create_month_average():

    # This function creates a new data frame of just each month and the average review for that month (all courses)
    month_average = review_data.groupby(["Month"]).mean()

    return month_average

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

    # Header for graphs covering timed ratings not broken down by course
    h1 = jp.QDiv(a = webpage, text = "Average Ratings By Time Frame For All Courses Together", classes = "text-h4 text-center q-pt-md text-bold")

    # Creates spline chart to show average rating per day for all courses
    spline_chart_day = HighCharts(a = webpage, options = ChartCreationCode.spline_chart_code, classes = "q-pt-lg q-px-md")  
    spline_chart_day.options.title.text = "Average Course Rating By Day (All Courses)"  
    spline_chart_day.options.xAxis.categories = list(day_average.index)
    spline_chart_day.options.series[0].name = "Average Daily Rating"
    spline_chart_day.options.series[0].data = list(day_average["Rating"])

    # Creates spline chart to show average rating per week for all courses
    spline_chart_week = HighCharts(a = webpage, options = ChartCreationCode.spline_chart_code, classes = "q-pt-lg q-px-md") 
    spline_chart_week.options.title.text = "Average Course Rating By Week (All Courses)"   
    spline_chart_week.options.xAxis.title.text = "Week"
    spline_chart_week.options.xAxis.categories = list(week_average.index)
    spline_chart_week.options.series[0].name = "Average Weekly Rating"
    spline_chart_week.options.series[0].data = list(week_average["Rating"])

    # Creates spline chart to show average rating per month for all courses
    spline_chart_month = HighCharts(a = webpage, options = ChartCreationCode.spline_chart_code, classes = "q-pt-lg q-px-md") 
    spline_chart_month.options.title.text = "Average Course Rating By Month (All Courses)"   
    spline_chart_month.options.xAxis.title.text = "Month"
    spline_chart_month.options.xAxis.categories = list(month_average.index)
    spline_chart_month.options.series[0].name = "Average Monthly Rating"
    spline_chart_month.options.series[0].data = list(month_average["Rating"])

    return webpage

# Calls functions to load and manipulate course review data
review_data = load_review_data()
day_average = create_day_average()
week_average = create_week_average()
month_average = create_month_average()

# Calls website creator
jp.justpy(create_webpage)