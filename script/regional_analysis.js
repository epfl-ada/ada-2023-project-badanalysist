fetch('viz_data/regional_analysis.json')
    .then(response => response.json())
    .then(data => {
        // Process the data
        prepareHoverText(data);
    })
    .catch(error => {
        console.error('Error fetching data: ', error);
    });

function prepareHoverText(data) {
    data.forEach(region => {
        region.hover_text = `Region: ${region.region}<br>` +
                            `Rank: ${region.rank}<br>` +
                            `Popular Beer: ${region.popular_beers} (Count: ${region.counts_pop_beers.toFixed(2)}, Rating: ${region.rating_pop_beers.toFixed(2)})<br>` +
                            `Popular Style: ${region.popular_styles} (Count: ${region.counts_pop_styles.toFixed(2)}, Rating: ${region.rating_pop_styles.toFixed(2)})`;
    });
}

// Plotly map
var data = [{
    type: 'scattergeo',
    mode: 'markers',
    locations: regions.map(region => region.region), 
    text: regions.map(region => region.hover_text),
    hoverinfo: 'text',
    marker: {
        size: 10
    }
}];

var layout = {
    title: 'Beer Preferences by Region',
    geo: {
        projection: {
            type: 'natural earth'
        }
    }
};

Plotly.newPlot('regional_analysis', data, layout);