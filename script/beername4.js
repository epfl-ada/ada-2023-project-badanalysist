var trace1 = {
  x: ['abv', 'appearance', 'aroma', 'palate', 'taste'],
  y: [0.009313107152162322, 0.00584446591662321, 0.018815905910523713, 0.002907323488403212, 0.020489848787303977],
  name: 'RateBeer',
  error_y: {
    type: 'data',
    array: [0.018555869114326048, 0.00790966589052416, 0.015208068765717501, 0.008552746461300272, 0.0160497708660221],
    visible: true
  },
  type: 'bar', 
  marker: {color :'#FFD700'}
};
var trace2 = {
  x: ['abv', 'appearance', 'aroma', 'palate', 'taste'],
  y: [0.013697513635922483, 0.012685709453806888, 0.0062244606758991095, 0.015193305945303794, 0.014478636883128393],
  name: 'BeerAdvocate',
  error_y: {
    type: 'data',
    array: [0.016655869676083224, 0.006393020450026626, 0.006820141060527169, 0.007063836207193353, 0.007128258107443327],
    visible: true
  },
  type: 'bar',
  marker: {color : '#5161d6'}
};
var data = [trace1, trace2];
var layout = {height: 400,
              weight:1000,
              barmode: 'group',   paper_bgcolor: 'transparent',
  plot_bgcolor: 'transparent',  title:'Effect of Sentiment conveyed by beer name on five categories of characteristics (95\% CI)'};
Plotly.newPlot('beername4', data, layout);
