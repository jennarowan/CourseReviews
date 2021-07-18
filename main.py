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

    # Creates Day, Week, and Month columns using just the date portion of the Timestamp (all time of day data is dropped for these columns)
    review_data["Day"] = review_data["Timestamp"].dt.date
    review_data["Week"] = review_data["Timestamp"].dt.strftime("%Y-%U")
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

def create_month_average_by_course():

    # This function creates a new data frame showing the monthly average rating for each course separately
    month_average_by_course = review_data.groupby(["Month", "Course Name"])["Rating"].mean().unstack()

    return month_average_by_course

async def tooltip_formatter(self, msg):

    # This function customizes graph hover-over tooltips to be more useful
    tooltip_html = f"""
    <div style="color: {msg.color};">{msg.series_name}</div>
    <div>{msg.category}</div>
    <div>{msg.y}</div>
    """
    return await self.tooltip_update(tooltip_html, msg.websocket)

def build_spline_chart(webpage, time_frame, time_framely, pd_data):

    # This function is used to build the various spline charts

    chart = HighCharts(a = webpage, options = ChartCreationCode.        spline_chart_code, classes = "q-pt-lg q-px-md")  
    chart.on('tooltip', tooltip_formatter)
    chart.options.title.text = "Average Course Rating By " + time_frame + " (All Courses)"  
    chart.options.xAxis.categories = list(pd_data.index)
    chart.options.series[0].name = "Average " + time_framely + " Rating"
    chart.options.series[0].data = list(pd_data["Rating"])

    return chart

def build_area_spline_chart(webpage, time_frame, time_framely, pd_data):

    chart = HighCharts(a = webpage, options = ChartCreationCode.area_spline_chart_code, classes = "q-pt-lg q-px-md")
    chart.options.title.text = "Average Course Rating By " + time_frame + " For Each Course"  
    chart.options.xAxis.categories = list(pd_data.index)

    chart_data = [{"name": col_name, "data": [col_data for col_data in month_average_by_course[col_name]]} for col_name in month_average_by_course.columns]

    chart.options.series = chart_data

    return chart

def build_stream_graph_chart(webpage, time_frame, time_framely, pd_data):

    chart = HighCharts(a = webpage, options = ChartCreationCode.stream_graph_code, classes = "q-pt-lg q-px-md")
    chart.options.title.text = "Average Course Rating By " + time_frame + " For Each Course"  
    chart.options.xAxis.categories = list(pd_data.index)

    chart_data = [{"name": col_name, "data": [col_data for col_data in month_average_by_course[col_name]]} for col_name in month_average_by_course.columns]

    chart.options.series = chart_data

    return chart

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
    h2 = jp.QDiv(a = webpage, text = "Average Ratings By Time Frame For All Courses Together", classes = "text-h4 text-center q-pt-md text-bold")

    # Creates spline chart to show average rating per day for all courses
    spline_chart_day = build_spline_chart(webpage, "Day", "Daily", day_average)

    # Creates spline chart to show average rating per week for all courses
    spline_chart_week = build_spline_chart(webpage, "Week", "Weekly", week_average)

    # Creates spline chart to show average rating per month for all courses
    spline_chart_month = build_spline_chart(webpage, "Month", "Monthly", month_average)

    # Header for graph covering timed ratings broken down by course
    h2 = jp.QDiv(a = webpage, text = "Average Ratings For Each Course Separately", classes = "text-h4 text-center q-pt-md text-bold")

    # Creates area spline chart to show monthly average rating for each course
    area_spline_chart = build_area_spline_chart(webpage, "Month", "Monthly", month_average_by_course)

    # Creates stream graph chart to show monthly average rating for each course
    stream_graph_chart = build_stream_graph_chart(webpage, "Month", "Monthly", month_average_by_course)

    return webpage

# Calls functions to load and manipulate course review data
review_data = load_review_data()
day_average = create_day_average()
week_average = create_week_average()
month_average = create_month_average()
month_average_by_course = create_month_average_by_course()

# Calls website creator
jp.justpy(create_webpage)