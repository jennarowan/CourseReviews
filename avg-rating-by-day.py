import justpy as jp
import pandas as pd
from pytz import utc
from datetime import datetime
from justpy.chartcomponents import HighCharts

chart_definition = """
{
    chart: {
        type: 'spline',
        inverted: false
    },
    title: {
        text: 'Average Course Rating By Day'
    },
    subtitle: {
        text: ''
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'Date'
        },
        labels: {
            format: '{value}'
        },
        maxPadding: 0.05,
        showLastLabel: true
    },
    yAxis: {
        title: {
            text: 'Average Rating'
        },
        labels: {
            format: '{value}'
        },
        lineWidth: 2
    },
    legend: {
        enabled: false
    },
    tooltip: {
        headerFormat: '<b>{series.name}</b><br/>',
        pointFormat: '{point.x}: {point.y}'
    },
    plotOptions: {
        spline: {
            marker: {
                enable: false
            }
        }
    },
    series: [{
        name: 'Average Daily Rating',
        data: []
    }]
}
"""

def load_review_data():

    review_data = pd.read_csv("reviews.csv", parse_dates = ["Timestamp"])

    review_data["Day"] = review_data["Timestamp"].dt.date
    global day_average
    day_average = review_data.groupby(["Day"]).mean()

def app():

    webpage = jp.QuasarPage(dark = True)
    
    h1 = jp.QDiv(a = webpage, text = "Analysis of Course Reviews", classes = "text-h2 text-center q-pt-md text-bold")

    p1 = jp.QDiv(a = webpage, text = "These graphs represent course review analysis", classes = "text-body-1 text-center q-pt-lg")

    chart = HighCharts(a = webpage, options = chart_definition, classes = "q-pt-lg")
    
    chart.options.xAxis.categories = list(day_average.index)
    chart.options.series[0].data = list(day_average["Rating"])
    return webpage

load_review_data()
jp.justpy(app)