# Symple stock prices comparison

This script get two dataframes with stock prices from a Python wrapper (<a href="https://github.com/RomelTorres/alpha_vantage">Github repo</a>) for <a href="https://www.alphavantage.co/">Alpha Vantage</a>. The documentation can be found <a href="https://alpha-vantage.readthedocs.io/en/latest/">here</a>.

<b>Prerequisites</b>

To properly run it needs some Python libraries also listed in the prerequisitie file.

<a href="https://www.alphavantage.co/support/#api-key">API Keys</a>
<a href="https://github.com/RomelTorres/alpha_vantage">Alpha Vantage</a>
matplotlib.pyplot
pandas
numpy
datetime
requests

<b>Output</b>

The script will just output a simple line graph with the trend between the selected start date and today. Both series have been scaled so both will start at 100.

<img src="https://raw.githubusercontent.com/FilippoGalanti/covid19/master/Covid19_Continents.png" alt="Output Example">

<b>Issues and Future Developments</b>

This was a quick excercise to explore the API. I'm working on some front end developments using <a href="https://dash.plotly.com/">Dash</a>.

