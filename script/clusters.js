fetch('viz_data/vis_clusters.json')
  .then(res => res.json())
  .then(clusterData => {
    Plotly.newPlot('clusterVis', clusterData.data, clusterData.layout);
  })
  .catch(error => {
    console.error('Error:', error);
  });
