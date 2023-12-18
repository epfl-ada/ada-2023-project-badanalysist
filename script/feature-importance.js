// // Load the JSON data
// fetch('viz_data/feature_importance.json')
//   .then(response => response.json())
//   .then(data => {
//     // Process the data and create the chart
//     createFeatureImportanceChart(data);
//   })
//   .catch(error => console.error('Error loading the feature importance data:', error));

// // Function to create the Plotly chart
// function createFeatureImportanceChart(data) {
//   var traces = [];
  
//   // Create a trace for each cluster
//   data.forEach((cluster, index) => {
//     var trace = {
//       x: cluster.features,
//       y: cluster.importances,
//       type: 'bar',
//       name: `Cluster ${cluster.cluster}`
//     };
//     traces.push(trace);
//   });

//   var layout = {
//     // Define the layout
//     title: 'Feature Importances by Cluster',
//     barmode: 'group'
//   };

//   // Create the Plotly chart
//   Plotly.newPlot('feature_importance', traces, layout);
// }

fetch('viz_data/feature_importance.json')
  .then(res => res.json())
  .then(radarChartData => {
    Plotly.newPlot('featureImp', radarChartData.data, radarChartData.layout);
  })
  .catch(error => {
    console.error('Error:', error);
  });
