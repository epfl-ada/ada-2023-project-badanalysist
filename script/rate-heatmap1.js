fetch('viz_data/ratings_rb_corr.json').then(res => res.json()).then(ratingsRbCorrData => {
  let detailedFeatures = Object.keys(ratingsRbCorrData[0]);
  let ratingsRbCorr = ratingsRbCorrData.map(row => detailedFeatures.map(feature => row[feature]));

  let trace1 = {
    z: ratingsRbCorr,
    x: detailedFeatures,
    y: detailedFeatures,
    type: 'heatmap',
    colorscale: 'Cividis',
    showscale: true
  };

  let layout = {
    title: 'RB Rating Features Correlation Heatmap',
    paper_bgcolor: 'transparent',
    plot_bgcolor: 'transparent',
    xaxis: {
      ticks: '',
      side: 'bottom'
    },
    yaxis: {
      ticks: ''
    }
  };

  Plotly.newPlot('heatmap1', [trace1], layout);
}).catch(error => {
  console.error('Error:', error);
});
