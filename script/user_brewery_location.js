var trace1 = {
    x: ["Users' location", "Breweries' location"],
    y: [658, 4323],
    name: 'Non-US countries',
    type: 'bar',
    opacity: 0.8,
    marker: { color: '#03257E' }
  };
  
  var trace2 = {
    x: ["Users' location", "Breweries' location"],
    y: [2683, 3958],
    name: 'US',
    type: 'bar',
    opacity: 0.8,
    marker: { color: '#FEDD00' },
  };
  
  var data = [trace1, trace2];
  
  var layout = {barmode: 'group',paper_bgcolor: 'transparent',plot_bgcolor: 'transparent'};
  
  Plotly.newPlot('user-brewery-location', data, layout);
  