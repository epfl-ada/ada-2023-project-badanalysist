Plotly.newPlot('recommendation_keyword', [], {
    sliders: [{
      pad: {t: 10},
      y: 0,
      currentvalue: {
        xanchor: 'right',
        font: {
          size: 15
        }
      },
      len: 0.8,
      steps: [{
        label: 'Rich',
        method: 'relayout',
        args: [{'images[0].source': 'img/keyword_rich.jpg'}]
      }, {
        label: 'Best',
        method: 'relayout',
        args: [{'images[0].source': 'img/keyword_best.jpg'}]
      }, {
        label: 'Strong',
        method: 'relayout',
        args: [{'images[0].source': 'img/keyword_strong.jpg'}]
      }]
    }],
    images: [{
      source: 'img/keyword_rich.jpg', // Initial image displayed
      xref: 'paper',
      yref: 'paper',
      x: 0,
      y: 1,
      sizex: 1.3,
      sizey: 1.6,
    //   sizing: 'stretch',
      layer: 'below'
    }],
    layout: {
        paper_bgcolor: 'transparent',
        plot_bgcolor: 'transparent',
        margin: { l: 10, r: 10, b: 20, t: 20, pad: 4 }, // Adjusted margins

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
        },
        sliders:{

        }
    }
  });

Plotly.relayout('recommendation_keyword', {
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