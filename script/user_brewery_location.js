var trace1 = {
    x: ["Users", "Breweries"],
    y: [658, 4323],
    name: 'in Non-US countries',
    type: 'bar',
    opacity: 0.8,
    marker: { color: '#03257E' }
  };
  
  var trace2 = {
    x: ["Users", "Breweries"],
    y: [2683, 3958],
    name: 'in US',
    type: 'bar',
    opacity: 0.8,
    marker: { color: '#FEDD00' },
  };
  
  var data = [trace1, trace2];
  
  var layout = {barmode: 'group',paper_bgcolor: 'transparent',plot_bgcolor: 'transparent',
              title: 'Number of Users and Breweries in U.S. and non-U.S countries',
              yaxis: {title: 'Counts'}};
  
  Plotly.newPlot('user-brewery-location', data, layout);
  