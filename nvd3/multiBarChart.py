#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Python-nvd3 is a Python wrapper for NVD3 graph library.
NVD3 is an attempt to build re-usable charts and chart components
for d3.js without taking away the power that d3.js gives you.

Project location : https://github.com/areski/python-nvd3
"""

from NVD3Chart import NVD3Chart


#TODO: Add extensive documentation on multiBarChart
#settings supported
#examples
class multiBarChart(NVD3Chart):
    """
    usage ::

        from nvd3 import multiBarChart
        chart = multiBarChart(name='multiBarChart', height=400, width=400)
        xdata = [0, 1, 3, 4]
        ydata = [6, 12, 9, 16]
        chart.add_serie(y=ydata, x=xdata)
        chart.buildhtml()

    js-code ::

        data_MultiBarChart = [{ "key" : "Serie 1",
           "values" : [
                { "x" : 0
                  "y" : 6
                },
                { "x" : 1,
                  "y" : 12
                },
                { "x" : 3,
                  "y" : 9
                },
              ],
            "yAxis" : "1"
        }]

        nv.addGraph(function() {
            var chart = nv.models.multiBarChart();
            chart.xAxis
                .tickFormat(d3.format(',.2f'))
            chart.yAxis
                .tickFormat(d3.format(',.2f'))
            d3.select('#MultiBarChart svg')
                .datum(data_MultiBarChart)
                .transition()
                .duration(500)
                .call(chart);
            return chart;
        });
    """
    def __init__(self, height=450, width=None, date=False, **kwargs):
        NVD3Chart.__init__(self, **kwargs)
        if date:
            self.create_x_axis('xAxis', format='%d %b %y', date=True)
        else:
            self.create_x_axis('xAxis', format=".2f")
        self.create_y_axis('yAxis', format=".2f")
        # must have a specified height, otherwise it superimposes both chars
        if height:
            self.set_graph_height(height)
        if width:
            self.set_graph_width(width)