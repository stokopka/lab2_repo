from spyre import server
import urllib3
import numpy as numpy
import pandas as pd
import matplotlib.pyplot as plot
import matplotlib


class Lab2App(server.App):
    title = "Second Lab"

    inputs = [{
        "type": 'dropdown',
        "label": 'Choose the region',
        "options": [{"label": "Vinnitsya", "value": 1},
                    {"label": "Volyn'", "value": 2},
                    {"label": "Dnopropetrovs'k", "value": 3},
                    {"label": "Donets'k", "value": 4},
                    {"label": "Zhytomyr", "value": 5},
                    {"label": "Zacarpattya", "value": 6},
                    {"label": "Zaporyzhzhya", "value": 7},
                    {"label": "Ivano-Frankivs'k", "value": 8},
                    {"label": "Kyiv", "value": 9},
                    {"label": "Kirovohrad", "value": 10},
                    {"label": "Luhans'k", "value": 11},
                    {"label": "L'viv", "value": 12},
                    {"label": "Mikolyaiv", "value": 13},
                    {"label": "Odessa", "value": 14},
                    {"label": "Poltava", "value": 15},
                    {"label": "Rivne", "value": 16},
                    {"label": "Sumy", "value": 17},
                    {"label": "Ternopil'", "value": 18},
                    {"label": "Kharkiv", "value": 19},
                    {"label": "Kherson", "value": 20},
                    {"label": "Khmel'nyts'kyy", "value": 21},
                    {"label": "Cherkasy", "value": 22},
                    {"label": "Chernyvtsy", "value": 23},
                    {"label": "Chernihiv", "value": 24},
                    {"label": "Crimea", "value": 25}],
        "variable_name": 'region',
        "value": 25,
        "action_id": "update_data"
    }, {
        "type": 'dropdown',
        "label": 'Choose index',
        "options": [{"label": "VHI", "value": "VHI"},
                    {"label": "VCI", "value": "VCI"},
                    {"label": "TCI", "value": "TCI"}],
        "key": 'index',
        "action_id": "update_data"
    }
        , {
            "input_type": "text",
            "variable_name": "week1",
            "label": "Enter the first week",
            "value": 25,
            "key": 'week1',
            "action_id": "update_data"
        }, {
            "input_type": "text",
            "variable_name": "week2",
            "label": "Enter the last week",
            "value": 35,
            "key": 'week2',
            "action_id": "update_date"
        }, {
            "input_type": "text",
            "variable_name": "year1",
            "label": "Enter the year:",
            "value": 1982,
            "key": "year1",
            "action_id": "update_data"
        }
    ]

    controls = [
        {
            "type": "hidden",
            "id": "update_data"
        }
    ]

    outputs = [
        {
            "type": "table",
            "id": "table_id",
            "control_id": "update_data",
            "tab": "Table",
            "on_page_load": True
        }, {
            "type": "plot",
            "id": "plot_id",
            "tab": "Plot",
            "control_id": "update_data"
        }
    ]

    tabs = ["Plot", "Table"]

    def getData(self, params):
        index = str(params['index'])
        week1 = int(params['week1'])
        week2 = int(params['week2'])
        region = int(params['region'])
        year1 = int(params['year1'])

        column = ['year', 'week','oblast' ,'SMN', 'SMT', 'VCI', 'TCI', 'VHI']
        df = pd.read_csv('final.csv', names=column)
        return df.loc[(df['week'] >= int(week1)) & (df['year'] == int(year1)) & (df['week'] <= int(week2)) & (df['oblast'] == int(region))]



    def getPlot(self, params):
        datatype = params['index']
        df = self.getData(params)
        
        plt_obj = df.plot(x='week', y=datatype,
                          linestyle = '--',
                          linewidth = 2,
                          color = 'pink'
                          )
        
        plt_obj.set_ylabel(datatype)
        fig = plt_obj.get_figure()
        return fig


app = Lab2App()
app.launch()
