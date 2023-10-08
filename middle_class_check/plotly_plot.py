import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


def plotly_plot(year, provided_income, area_income, national_income, area_name, area_moe, national_moe):
    """
    This function creates the plotly plot comparing user provided household income 
    to median household income in the user provided area in the user provided year.
    """
    area_x_label = f"{area_name} median"

    x_data = ["Your household", area_x_label, "U.S. median"]
    y_data = [provided_income, area_income, national_income]
    moe_array = [0, area_moe, national_moe]
    fig_title = f"Your household income compared to the median household income in {area_name} as of {str(year)}"
    text_labels = []

    for i in range(len(y_data)):
        currency_format = "${:,}".format(y_data[i])
        text_labels.append(currency_format)

    fig = go.Figure(go.Bar(
        x = x_data,
        y = y_data,
        error_y=dict(
            type='data',
            array=moe_array,
            color="black",
            thickness=4,
            width=10
        ),
        customdata=moe_array,
        hovertemplate =
        '%{x}:'+
        '<br><b>$%{y:,}, margin of error: ±$%{customdata:,}</b><extra></extra>',
        text=text_labels,
        textfont=dict(
            size=28
        ),
        showlegend = False))

    fig.update_layout(xaxis = dict(tickfont = dict(size=24)),
                      yaxis_tickprefix = '$', 
                      yaxis_tickformat = ',.',
                      paper_bgcolor="rgba(0,0,0,0)", 
                      plot_bgcolor="rgba(0,0,0,0)")
    fig.update_yaxes(visible=False)

    bar_chart = fig.to_html(full_html=False, include_plotlyjs=False)

    return bar_chart


