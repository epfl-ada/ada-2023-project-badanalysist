fetch('viz_data/ratings_ba_corr.json').then(res => res.json()).then(ratingsBaCorrData => {
  let detailedFeatures = Object.keys(ratingsBaCorrData[0]);
  let ratingsBaCorr = ratingsBaCorrData.map(row => detailedFeatures.map(feature => row[feature]));

  let trace2 = {
    z: ratingsBaCorr,
    x: detailedFeatures,
    y: detailedFeatures,
    type: 'heatmap',
    colorscale: 'Cividis', 
    showscale: true
  };

  let layout = {
    title: 'BeerAdvocate Correlation Heatmap',
    paper_bgcolor: 'transparent',
    plot_bgcolor: 'transparent',
    xaxis: { ticks: '', side: 'bottom' },
    yaxis: { ticks: '' }
  };

  Plotly.newPlot('heatmap2', [trace2], layout);
}).catch(error => {
  console.error('Error:', error);
});
