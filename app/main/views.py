from app.main import bp
from flask import render_template, current_app
import pandas as pd

import plotly
import plotly.figure_factory as ff
import os
import json


@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
def index():

    df_online = pd.read_csv(
        os.path.join(current_app.config['UPLOAD_FOLDER'],
                     "online.csv"), nrows=20)

    online_list = df_online.to_dict('records')

    return render_template('index.html', online_dataset=online_list)


@bp.route('/cohort', methods=['GET'])
def cohort():

    retention = pd.read_csv(
        os.path.join(current_app.config['UPLOAD_FOLDER'],
                     "retention.csv"),sep='\t', index_col=0)

    graphJSON = create_plot(retention)

    return render_template('cohort.html', plot=graphJSON)


def create_plot(retention):
    cohort_values = []
    cohort_display_values = []
    cohort_labels = []

    for x in retention.columns.tolist():
        temp = retention[x].round(2)
        cohort_values.append(temp.tolist())
        cohort_display_values.append(temp.fillna(0).tolist())
        cohort_labels.append(temp.fillna('').astype(str).tolist())

    colorscale = [[0.0, 'rgb(255,255,255)'], [.2, 'rgb(255, 255, 153)'],
                  [.4, 'rgb(153, 255, 204)'], [.6, 'rgb(179, 217, 255)'],
                  [.8, 'rgb(240, 179, 255)'], [1.0, 'rgb(255, 77, 148)']]

    fig = ff.create_annotated_heatmap(
        z=cohort_display_values[::-1],
        x=retention.index.values.tolist(),
        y=retention.columns.values.tolist()[::-1],
        annotation_text=cohort_labels[::-1],
        colorscale=colorscale,
        hovertemplate=
        'Cohort: %{y}<br>' +
        'Months after registration: %{x}<br>' +
        'Retention percentage: %{z}%<br>' +
        "<extra></extra>"
    )
    fig.layout.yaxis.type = 'category'
    fig.update_layout(
        xaxis_title="Number of months after registration",
        yaxis_title="Cohorts - Monthly registration"
    )
    # fig.show()

    graphJSON = json.dumps(fig,
                           cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON







