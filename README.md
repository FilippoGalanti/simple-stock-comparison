# Simple stock prices comparison

This script get two dataframes with stock prices from a Python wrapper (<a href="https://github.com/RomelTorres/alpha_vantage">Github repo</a>) for <a href="https://www.alphavantage.co/">Alpha Vantage</a>. The documentation can be found <a href="https://alpha-vantage.readthedocs.io/en/latest/">here</a>.

<b>Prerequisites</b>

To properly run it needs some Python libraries also listed in the prerequisitie file.

 <ul>
  <li><a href="https://www.alphavantage.co/support/#api-key">API Keys</a></li>
  <li><a href="https://github.com/RomelTorres/alpha_vantage">Alpha Vantage</a></li>
  <li>matplotlib</li>
  <li>pandas</li>
  <li>numpy</li>
  <li>datetime</li>
  <li>requests</li>
</ul> 

<b>Output</b>

The script will just output a simple line graph with the trend between the selected start date and today. Both series have been scaled so both will start at 100.
A couple of additional information will be added regarding start and end price since otherwise the only info available is the scaled price.
<PRE> 
Microsoft Corporation start value $46.76 on 2015-01-01. End value $212.48 on 2020-08-07.
Apple Inc. start value $109.33 on 2015-01-01. End value $444.45 on 2020-08-07.
</PRE> 
<img src="https://raw.githubusercontent.com/FilippoGalanti/symple-stock-comparison/master/MSFT%20AAPL.png" alt="Output Example">

<b>Issues and Future Developments</b>

This was a quick excercise to explore the API. I'm working on some front end developments using <a href="https://dash.plotly.com/">Dash</a>.

