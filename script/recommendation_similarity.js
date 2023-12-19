Plotly.newPlot('recommendation_similarity', [], {
    sliders: [{
      pad: {t: 30},
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
        args: [{'images[0].source': '.similarity_stout'}]
      }]
    }],
    images: [{
      source: 'path_to_your_first_image.jpg', // Initial image displayed
      xref: 'paper',
      yref: 'paper',
      x: 0,
      y: 1,
      sizex: 1,
      sizey: 1,
      sizing: 'stretch',
      layer: 'below'
    }]
  });
  