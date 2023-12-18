var data = [{
  values: [3.05499909, 15.98524859, 35.20305955,  2.12620652,  7.70806775,
        3.43744309,  3.3509379 ,  4.0202149 ,  2.22181752, 19.37260973,
        3.51939537],
  labels: ['da', 'de', 'en', 'es', 'fr', 'id', 'it', 'nl', 'no', 'other',
       'ro'],
  domain: {column: 0},
  name: 'RB',
  hoverinfo: 'label+percent+name',
  hole: .4,
  type: 'pie'
},{
  values: [3.56940002, 21.87976443, 28.72858808,  1.8474784 , 10.77097845,
        6.05960958,  2.76523871,  3.29437087,  1.3542196 , 16.77677797,
        2.95357388],
  labels: ['da', 'de', 'en', 'es', 'fr', 'id', 'it', 'nl', 'no', 'other',
       'ro'],
  text: 'BA',
  textposition: 'inside',
  domain: {column: 1},
  name: 'CO2 Emissions',
  hoverinfo: 'label+percent+name',
  hole: .4,
  type: 'pie',
  marker: {
        colors: ['#FFD700', '#5596E6', '#D1C87F', '#85A6E0', '#FFEEAA', '#6AB2E7', '#F0E0A1', '#76B6DD', '#FFE08A', '#68A0D8', '#5596E6', '#85A6E0', '#FFEEAA'] 
        }
  }];

var layout = {
  title: 'Distribution of Languages of Beer\'s Name',
  annotations: [
    {
      font: {
        size: 20
      },
      showarrow: false,
      text: 'RB',
      x: 0.2,
      y: 0.5
    },
    {
      font: {
        size: 20
      },
      showarrow: false,
      text: 'BA',
      x: 0.8,
      y: 0.5
    }
  ],
  height: 400,
  width: 600,
  showlegend: false,
  grid: {rows: 1, columns: 2}
};

Plotly.newPlot('myDiv', data, layout);