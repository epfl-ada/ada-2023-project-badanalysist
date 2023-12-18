fetch('viz_data/radar_chart.json').then(res => res.json()).then(radarChartData => {
    Plotly.newPlot('radarChart', radarChartData.data, radarChartData.layout);
  }).catch(error => {
    console.error('Error:', error);
  });
  