fetch('viz_data/regional_analysis.json')
    .then(response => response.json())
    .then(data => {
        prepareHoverTextAndPlot(data);
    })
    .catch(error => {
        console.error('Error fetching data: ', error);
    });

function prepareHoverTextAndPlot(regions) {
    regions.forEach(region => {
        region.hover_text = `Region: ${region.region}<br>` +
                            `Rank: ${region.rank}<br>` +
                            `Popular Beer: ${region.popular_beers} (Count: ${region.counts_pop_beers.toFixed(2)}, Rating: ${region.rating_pop_beers.toFixed(2)})<br>` +
                            `Popular Style: ${region.popular_styles} (Count: ${region.counts_pop_styles.toFixed(2)}, Rating: ${region.rating_pop_styles.toFixed(2)})`;
    });

    // Now create the Plotly map
    createMap(regions);
}

const regionCoordinates = {
    'Europe': { lat: 54.5260, lon: 15.2551 },
    'US': { lat: 37.0902, lon: -95.7129 },
    'North America': { lat: 45.0000, lon: -100.0000 },
    'Asia': { lat: 34.0479, lon: 100.6197 },
    'Australia': { lat: -25.2744, lon: 133.7751 },
    'South America': { lat: -8.7832, lon: -55.4915 },
    'Africa': { lat: -8.7832, lon: 34.5085 }
};

function createMap(regions) {
    var data = [{
        type: 'scattergeo',
        mode: 'markers',
        lat: regions.map(region => regionCoordinates[region.region].lat),
        lon: regions.map(region => regionCoordinates[region.region].lon),
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
            },
            bgcolor: 'transparent'
        },
        paper_bgcolor: 'transparent', 
        plot_bgcolor: 'transparent', 
    };

    Plotly.newPlot('regional_analysis', data, layout);
}
