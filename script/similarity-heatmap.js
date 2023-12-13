var xValues = ['English Brown Ale', 'American Brown Ale', 'Smoked Beer', 'American Pale Lager', 'American IPA'];

var yValues = ['English Brown Ale', 'American Brown Ale', 'Smoked Beer', 'American Pale Lager', 'American IPA'];

var zValues = [
  [1.00, 0.99, 0.55, 0.89, 0.97],
  [0.99, 1.00,  0.56, 0.89, 0.98],
  [0.55,  0.56, 1.00, 0.42, 0.52],
  [0.89, 0.89, 0.42, 1.00, 0.87],
  [0.97, 0.98, 0.52, 0.87, 1.00]
];

var data = [{
  x: xValues,
  y: yValues,
  z: zValues,
  type: 'heatmap',
  colorscale: 'Cividis',
  showscale: false
}];

var layout = {
  title: 'An Example Heatmap about Beer Sytle Similarities',
  paper_bgcolor: 'transparent',
  plot_bgcolor: 'transparent',
  annotations: [],
  xaxis: {
    ticks: '',
    side: 'top'
  },
  yaxis: {
    ticks: '',
    tickangle: -45, 
    autosize: false
  },
  margin: {
    l: 100, 
    r: 50,
    t: 50,
    b: 50
  }
};

for ( var i = 0; i < yValues.length; i++ ) {
  for ( var j = 0; j < xValues.length; j++ ) {
    var currentValue = zValues[i][j];
    if (currentValue < 0.8) {
      var textColor = 'white';
    }else{
      var textColor = 'black';
    }
    var result = {
      xref: 'x1',
      yref: 'y1',
      x: xValues[j],
      y: yValues[i],
      text: zValues[i][j],
      font: {
        family: 'Arial',
        size: 12,
        color: 'rgb(50, 171, 96)'
      },
      showarrow: false,
      font: {
        color: textColor
      }
    };
    layout.annotations.push(result);
  }
}

Plotly.newPlot('similarity-heatmap', data, layout);
