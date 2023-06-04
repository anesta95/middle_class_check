import pandas as pd
import plotly.express as px


def plotly_plot(year, provided_income, area_income, national_income, area_name, area_moe, national_moe):
    """
    This function creates the plotly plot comparing user provided household income 
    to median household income in the user provided area in the user provided year.
    """
    area_x_label = f"{area_name} median household income"

    x_data = ["Your household income", area_x_label, "U.S. median household income"]
    y_data = [provided_income, area_income, national_income]
    fig_title = f"Your household income compared to the median household income in {area_name} as of {str(year)}"
    text_labels = []

    for i in range(len(y_data)):
        currency_format = "${:,}".format(y_data[i])
        text_labels.append(currency_format)

    fig = px.bar(x=x_data, 
                 y=y_data, 
                 title=fig_title,
                 text=text_labels,
                 error_y=[None, area_moe, national_moe],
                 labels={
                    "x": "",
                    "y": ""
                 })

    fig.update_layout(yaxis_tickprefix = '$', 
                      yaxis_tickformat = ',.',
                      paper_bgcolor="rgba(0,0,0,0)", 
                      plot_bgcolor="rgba(0,0,0,0)")
    fig.update_yaxes(visible=False)

    bar_chart = fig.to_html(full_html=False, include_plotlyjs=False)

    return bar_chart

