var chartDom = document.getElementById('reco-kg');
var myChart = echarts.init(chartDom);
var option;

myChart.showLoading();
$.get('viz_data/reco-kg-data.json', function (webkitDep) {
  myChart.hideLoading();
  option = {
    legend: {
      data: ['Cluster 1', 'Cluster 2', 'Cluster 3', 'Cluster 4', 'Cluster 5']
    },
    series: [
      {
        type: 'graph',
        layout: 'force',
        animation: false,
        label: {
          position: 'right',
          formatter: '{b}'
        },
        draggable: true,
        data: webkitDep.nodes.map(function (node, idx) {
          node.id = idx;
          return node;
        }),
        categories: webkitDep.categories,
        force: {
          edgeLength: 5,
          repulsion: 20,
          gravity: 0.2
        },
        edges: webkitDep.links
      }
    ]
  };
  myChart.setOption(option);
});

option && myChart.setOption(option);
