# This file holds all the code from the Highcharts JavaScript library to drive basic graph creation

# Code pulled from the "Charts and series types" section here: https://www.highcharts.com/docs/index

spline_chart_code = """
{
    chart: {
        type: 'spline',
        inverted: false
    },
    title: {
        text: 'Average Course Rating By Day (All Courses)'
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