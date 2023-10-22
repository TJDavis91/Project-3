document.addEventListener('DOMContentLoaded', function() {
    fetch('/get_data')
        .then(response => response.json())
        .then(data => {
            const countries = data.map(item => item.country);
            const reserves = data.map(item => item.reserves);

            const heatmapData = {
                type: 'choropleth',
                locations: countries,
                locationmode: 'country names',
                z: reserves,
                text: countries,
                colorscale: 'Viridis',
                colorbar: {
                    title: 'Gold Reserves (in tonnes)'
                }
            };

            const layout = {
                title: 'Gold Reserves by Country',
            };

            Plotly.newPlot('heatmap', [heatmapData], layout);
        });
});

