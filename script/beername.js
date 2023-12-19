var trace1 = {
  x: ['All_sample', 'US', 'Canada', 'Europe'],
  y: [0.003806773111007229, 0.003827097508194309, 0.008205793547153159, -0.0026610306797792624],
  name: 'RB',
  error_y: {
    type: 'data',
    array: [0.002941265358114441, 0.0033437573353254806, 0.0065980696744756505, 0.022381436500877303],
    visible: true
  },
  type: 'bar', 
  marker: {color :'#FFD700'}
};
var trace2 = {
  x: ['All_sample', 'US', 'Canada', 'Europe'],
  y: [0.0045060924298390825, 0.004685014189658316, -0.004104193673061779, 0.026515942015150853],
  name: 'BA',
  error_y: {
    type: 'data',
    array: [0.004182478771333603, 0.004550157723863449, 0.015526306161878934, 0.02290743885570791],
    visible: true
  },
  type: 'bar',
  marker: {color : '#5596E6'}
};
var data = [trace1, trace2];
var layout = {barmode: 'group',   paper_bgcolor: 'transparent',
  plot_bgcolor: 'transparent',  };
Plotly.newPlot('beername', data, layout);