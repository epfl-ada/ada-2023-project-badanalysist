var trace1 = {
  x: ['NameSentiment', 'en*NameSentiment', 'de*NameSentiment', 'fr*NameSentiment', 'nl*NameSentiment', 'es*NameSentiment', 'it*NameSentiment'],
  y: [0.014096916006356649, -0.004360860308210692, -0.025717915158184577, 0.03366006260732455, 0.012391681062490393, 0.03948096206223083, -0.04135701425936894],
  name: 'RB',
  error_y: {
    type: 'data',
    array: [0.011442228088601333, 0.013385133965021483, 0.01655571057270494, 0.021716392300475826, 0.02700797383702753, 0.05263330740815814, 0.029084392036915315],
    visible: true
  },
  type: 'bar', 
  marker: {color :'#FFD700'}
};
var trace2 = {
  x: ['NameSentiment', 'en*NameSentiment', 'de*NameSentiment', 'fr*NameSentiment', 'nl*NameSentiment', 'es*NameSentiment', 'it*NameSentiment'],
  y: [0.017115891204346045, -0.006871536769094563, -0.013316275639131979, 0.0358279267658258, 0.014795903979699963, 0.04264432780952552, -0.055964454942145477],
  name: 'BA',
  error_y: {
    type: 'data',
    array: [0.009191622748132375, 0.011098980673798189, 0.014224472471586092, 0.017422409143137002, 0.021368871448706066, 0.04129312936012942, 0.02450277727072473],
    visible: true
  },
  type: 'bar',
  marker: {color : '#5596E6'}
};
var data = [trace1, trace2];
var layout = {height: 400,
              weight:1000,
              barmode: 'group',   paper_bgcolor: 'transparent',
  plot_bgcolor: 'transparent',  title:'The impact of the sentiment conveyed by beer names in various languages on ratings (95% CI)'};
Plotly.newPlot('beername3', data, layout);