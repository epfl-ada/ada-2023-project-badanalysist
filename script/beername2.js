var trace1 = {
  x: ['All sample', 'US', 'Canada', 'Europe'],
  y: [0.009337767718972156, 0.008460685955406038, 0.016488308291557327, 0.007765784621942523],
  name: 'RateBeer',
  error_y: {
    type: 'data',
    array: [0.0066655464992233385, 0.00789796127317343, 0.016124490424050994, 0.04252970592524668],
    visible: true
  },
  type: 'bar', 
  marker: {color :'#FFD700'}
};
var trace2 = {
  x: ['All sample', 'US', 'Canada', 'Europe'],
  y: [0.014435159904625464, 0.017166796821000987, 0.019316368808710304, -0.025148273116590087],
  name: 'BeerAdvocate',
  error_y: {
    type: 'data',
    array: [0.005832114578295564, 0.00698984721820662, 0.013652767532893243, 0.039899482430543184],
    visible: true
  },
  type: 'bar',
  marker: {color : '#5161d6'}
};
var data = [trace1, trace2];
var layout = {barmode: 'group',   paper_bgcolor: 'transparent',
  plot_bgcolor: 'transparent',  title:'The impact of the sentiment conveyed by beer names on ratings (95% CI)'};
Plotly.newPlot('beername2', data, layout);
