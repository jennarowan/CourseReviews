# This file holds all the code from the Highcharts JavaScript library to drive basic graph creation

# Code pulled from the "Charts and series types" section here: https://www.highcharts.com/docs/index

spline_chart_code = """
{
    chart: {
        type: 'spline',
        inverted: false
    },
    title: {
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
        pointFormat: '{msg.x}: {point.y}'
    },
    plotOptions: {
        spline: {
            marker: {
                enable: false
            }
        }
    },
    series: [{
        name: '',
        data: []
    }]
}
"""

area_spline_chart_code = """
{
    chart: {
        type: 'spline'
    },
    title: {
        text: ''
    },
    legend: {
        layout: 'vertical',
        align: 'left',
        verticalAlign: 'middle',
        x: 150,
        y: 100,
        floating: true,
        borderWidth: 1,
        backgroundColor:
            '#FFFFFF'
    },
    xAxis: {
        title: {
            text: "Month"
        }
    },
    yAxis: {
        title: {
            text: 'Average Rating'
        }
    },
    tooltip: {
        shared: true,
        valueSuffix: ''
    },
    credits: {
        enabled: false
    },
    plotOptions: {
        areaspline: {
            fillOpacity: 0.5
        }
    },
    series: [{
        name: '',
        data: []
    }, {
        name: '',
        data: []
    }, {
        name: '',
        data: []
    }, {
        name: '',
        data: []
    }, {
        name: '',
        data: []
    }, {
        name: '',
        data: []
    }, {
        name: '',
        data: []
    }, {
        name: '',
        data: []
    }]
}
"""