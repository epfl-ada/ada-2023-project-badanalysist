var trace1 = {
  x: ['English', 'German', 'French', 'Dutch', 'Romanian', 'Indonesian', 'Italian', 'Danish', 'Norwegian', 'Spanish'],
  y: [0.008185038532063517, 0.03804686605318555, -0.013428427153255214, -0.0025446473708672923, -0.016674237559662963, 0.011504832148072864, -0.040179010848084326, 0.01393994726359641, -0.06087115791001041, 0.04183980006342983],
  name: 'RateBeer',
  error_y: {
    type: 'data',
    array: [0.02023133292694169, 0.02554899126793139, 0.032472098586244336, 0.03959186998865557, 0.03861301058246559, 0.041495095182665934, 0.04451508595264238, 0.04299742803352185, 0.04755074305549076, 0.053476716628750226],
    visible: true
  },
  type: 'bar',
  marker: {color : '#FFD700'}
};

var trace2 = {
  x: ['English', 'German', 'French', 'Dutch', 'Romanian', 'Indonesian', 'Italian', 'Danish', 'Norwegian', 'Spanish'],
  y: [-0.034222357237830126, -0.01255126976858291, -0.06909250616074117, 0.053412065742694304, -0.13660996225407496, -0.05390083332560511, -0.010126155880029693, 0.017854524581935816, -0.11117633726063286, -0.024698439259874683],
  name: 'BeerAdvocate',
  error_y: {
    type: 'data',
    array: [0.016284318585415278, 0.020333548170736265, 0.023336221636894278, 0.0308424736751262, 0.034979304673233375, 0.0257641151563293, 0.03292010959690194, 0.028006884252783075, 0.04363852179614124, 0.043840820194945465],
    visible: true
  },
  type: 'bar', 
  marker: {color :'#5161d6'}
};
var data = [trace1, trace2];
var layout = {barmode: 'group',   paper_bgcolor: 'transparent',
  plot_bgcolor: 'transparent',  title:'The impact of different languages of beer on ratings (95% confidence interval)'};
Plotly.newPlot('beername1', data, layout);
