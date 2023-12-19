Plotly.newPlot('recommendation_similarity', [], {
    sliders: [{
      pad: {t: 40},
      currentvalue: {
        xanchor: 'right',
        font: {
          size: 20
        }
      },
      steps: [{
        label: 'American IPA',
        method: 'relayout',
        args: [{'images[0].source': 'img/similarity_ipa.jpg'}]
      }, {
        label: 'Fruit / Vegetable Beer',
        method: 'relayout',
        args: [{'images[0].source': 'img/similarity_fruit.jpg'}]
      }, {
        label: 'Stout',
        method: 'relayout',
        args: [{'images[0].source': 'img/similarity_stout.jpg'}]
      }]
    }],
    images: [{
      source: 'img/similarity_ipa.jpg', // Initial image displayed
      xref: 'paper',
      yref: 'paper',
      x: 0,
      y: 1,
      sizex: 1,
      sizey: 1.5,
      sizing: 'stretch',
      layer: 'below'
    }],
    layout: {
        paper_bgcolor: 'transparent',
        plot_bgcolor: 'transparent',

        xaxis: {
          visible: false, // Hides the x-axis
          showgrid: false,
          zeroline: false,
          showticklabels: false
        },
        yaxis: {
          visible: false, // Hides the y-axis
          showgrid: false,
          zeroline: false,
          showticklabels: false
        }
    }
  });

Plotly.relayout('recommendation_similarity', {
    paper_bgcolor: 'transparent',
    plot_bgcolor: 'transparent',
    // ... other layout configurations
    xaxis: {
        visible: false, // Hides the x-axis
        showgrid: false,
        zeroline: false,
        showticklabels: false
      },
      yaxis: {
        visible: false, // Hides the y-axis
        showgrid: false,
        zeroline: false,
        showticklabels: false
        }
});

  