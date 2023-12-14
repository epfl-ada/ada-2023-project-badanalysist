fetch('viz_data/regional_analysis.json')
    .then(response => response.json())
    .then(data => {
        const aggregatedData = aggregateDataByRegion(data);
        prepareHoverTextAndPlot(aggregatedData);
    })
    .catch(error => {
        console.error('Error fetching data: ', error);
    });

function aggregateDataByRegion(data) {
    const aggregated = {};

    data.forEach(item => {
        if (!aggregated[item.region]) {
            aggregated[item.region] = {
                region: item.region,
                details: []
            };
        }
        aggregated[item.region].details.push({
            rank: item.rank,
            popular_beers: item.popular_beers,
            counts_pop_beers: item.counts_pop_beers,
            rating_pop_beers: item.rating_pop_beers,
            popular_styles: item.popular_styles,
            counts_pop_styles: item.counts_pop_styles,
            rating_pop_styles: item.rating_pop_styles
        });
    });

    return Object.values(aggregated);
}

function prepareHoverTextAndPlot(regions) {
    regions.forEach(region => {
        region.hover_text = region.details.map(detail => 
            `Rank: ${detail.rank}<br>` +
            `Popular Beer: ${detail.popular_beers} (Count: ${detail.counts_pop_beers.toFixed(2)}, Rating: ${detail.rating_pop_beers.toFixed(2)})<br>` +
            `Popular Style: ${detail.popular_styles} (Count: ${detail.counts_pop_styles.toFixed(2)}, Rating: ${detail.rating_pop_styles.toFixed(2)})`
        ).join('<br><br>');
    });
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
            size: [82, 8, 15, 28, 10, 6, 6],
            color: [20, 30, 10, 15, 50, 20, 70 ],
            colorscale: 'Blues',
        }
    }];

    var layout = {
        title: 'Beer Preferences by Region',
        geo: {
            projection: {
                type: 'natural earth'
            },
            bgcolor: 'transparent',
            showland: true,
            landcolor: '#FEDD00',
            showocean: true,
            oceancolor: '#CDEDFD'
        },
        paper_bgcolor: 'transparent', 
        plot_bgcolor: 'transparent', 
    };

    Plotly.newPlot('regional_analysis', data, layout);
}
