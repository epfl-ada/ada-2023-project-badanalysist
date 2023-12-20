fetch('viz_data/feature_importance.json')
  .then(res => res.json())
  .then(impData => {
    Plotly.newPlot('featureImp', impData.data, impData.layout);
  })
  .catch(error => {
    console.error('Error:', error);
  });
