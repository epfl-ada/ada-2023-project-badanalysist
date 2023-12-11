Promise.all([
  fetch('viz_data/ratings_rb.json').then(res => res.json()),
  fetch('viz_data/ratings_ba.json').then(res => res.json())
]).then(([ratingsRbData, ratingsBaData]) => {
  let traces = [];
  let layout = {
    title: 'Histograms of 5 Rating Dimensions and Rating After Scaling',
    barmode: 'overlay',
    paper_bgcolor: 'transparent',
    plot_bgcolor: 'transparent',
    grid: { rows: 2, columns: 3, pattern: 'independent', roworder: 'bottom to top'},
    margin: { t: 100, r: 30, b: 0, l: 50 },
    xaxis: { title: 'ABV',tickmode: 'array', tickvals: [0, 0.25, 0.5, 0.75, 1], ticktext: ["0", "0.25", "0.5", "0.75", "1"], automargin: true},
    xaxis2: { title: 'Appearance',tickmode: 'array', tickvals: [0, 0.25, 0.5, 0.75, 1], ticktext: ["0", "0.25", "0.5", "0.75", "1"], automargin: true },
    xaxis3: { title: 'Aroma',tickmode: 'array', tickvals: [0, 0.25, 0.5, 0.75, 1], ticktext: ["0", "0.25", "0.5", "0.75", "1"], automargin: true },
    xaxis4: {title: 'Palate',tickmode: 'array', tickvals: [0, 0.25, 0.5, 0.75, 1], ticktext: ["0", "0.25", "0.5", "0.75", "1"], automargin: true },
    xaxis5: {title: 'Rating',tickmode: 'array', tickvals: [0, 0.25, 0.5, 0.75, 1], ticktext: ["0", "0.25", "0.5", "0.75", "1"], automargin: true },
    xaxis6: {title: 'Taste',tickmode: 'array', tickvals: [0, 0.25, 0.5, 0.75, 1], ticktext: ["0", "0.25", "0.5", "0.75", "1"], automargin: true },
    yaxis: { title: 'Counts' },
    yaxis2: { title: 'Counts' },
    yaxis3: { title: 'Counts' },
    yaxis4: {title: 'Counts' },
    yaxis5: {title: 'Counts' },
    yaxis6: {title: 'Counts' },
    legend: {
      orientation: 'h', // 水平显示图例
      x: 0.5, // 图例中心在 x 方向上的位置
      xanchor: 'center', // 图例以 x 的中心点对齐
      y: -0.5, // 图例在 y 方向上的位置
      yanchor: 'bottom' // 图例以 y 的顶部对齐
    },
  };
  let convert_features = ['abv', 'appearance', 'aroma', 'palate', 'rating', 'taste'];

  convert_features.forEach((feature, i) => {
    let showLegend = i === 0; 

    traces.push({
      x: ratingsRbData.map(row => row[feature]),
      type: 'histogram',
      opacity: 0.5,
      name: 'RateBeer',
      marker: { color: '#FFD700' },
      xbins: {
        size: (Math.max(...ratingsRbData.map(row => row[feature])) - Math.min(...ratingsRbData.map(row => row[feature]))) / 30
      },
      xaxis: `x${i + 1}`,
      yaxis: `y${i + 1}`,
      showlegend: showLegend
    });

    traces.push({
      x: ratingsBaData.map(row => row[feature]),
      type: 'histogram',
      opacity: 0.5,
      name: 'BeerAdvocate',
      marker: { color: '#4169E1' }, 
            xbins: {
        size: (Math.max(...ratingsBaData.map(row => row[feature])) - Math.min(...ratingsBaData.map(row => row[feature]))) / 30
      },
      xaxis: `x${i + 1}`,
      yaxis: `y${i + 1}`,
      showlegend: showLegend
    });
  });

  Plotly.newPlot('rate-dist', traces, layout);
}).catch(error => {
  console.error('Error loading or processing data:', error);
});
