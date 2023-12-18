fetch('viz_data/feature_importance.json')
  .then(res => res.json())
  .then(radarChartData => {
    Plotly.newPlot('featureImp', radarChartData.data, radarChartData.layout);
  })
  .catch(error => {
    console.error('Error:', error);
  });
