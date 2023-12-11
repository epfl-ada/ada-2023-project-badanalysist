var data = [{
    values: [12.149430, 6.770377, 5.887379, 4.993427, 3.422436, 3.054338, 2.979842, 2.602980, 2.258983, 2.055215, 1.976337, 1.877739, 49.971516213847494],
    labels: ['American IPA', 'American Pale Ale (APA)', 'Saison / Farmhouse Ale', 'American Double / Imperial IPA', 'American Wild Ale', 'American Amber / Red Ale', 'American Porter', 'American Stout', 'American Blonde Ale', 'Fruit / Vegetable Beer', 'American Double / Imperial Stout', 'Belgian Pale Ale', 'Others'],
    // domain: {column: 0},
    name: 'Beer Style Popularity',
    hoverinfo: 'label+percent+name',
    opacity: 0.7,
    hole: .4,
    type: 'pie',
    marker: {
        colors: ['#FFD700', '#5596E6', '#D1C87F', '#85A6E0', '#FFEEAA', '#6AB2E7', '#F0E0A1', '#76B6DD', '#FFE08A', '#68A0D8', '#5596E6', '#85A6E0', '#FFEEAA'] 
        }
  }];
  
  var layout = {
    title: 'Popularity of Beer Styles',
    paper_bgcolor: 'transparent',
    plot_bgcolor: 'transparent',
    annotations: [
      {
        font: {
          size: 16
        },
        showarrow: false,
        text: 'Beer Styles',
        x: 0.5,
        y: 0.5
      }
    ],
    showlegend: true,
  };
  
  Plotly.newPlot('style-pgt', data, layout);
  