// document.addEventListener("DOMContentLoaded", function () {
//     fetch('/')
//         .then(response => response.json())
//         .then(data => {
//             // Extracting data for Plotly
//             // var city = [...new Set(data.map(d => d[1]))]; // Get unique cities

//             // var pm10_last_values = city.map(c => {
//             //     // Get the last value of pm10 for a city
//             //     var cityData = data.filter(d => d[1] === c && d[5] === 'pm10');
//             //     return cityData.length ? cityData[0][8] : null;
//             // });

//             // var pm25_last_values = city.map(c => {
//             //     // Get the last value of pm25 for a city
//             //     var cityData = data.filter(d => d[1] === c && d[5] === 'pm25');
//             //     return cityData.length ? cityData[0][8] : null;
//             // });

//             // Creating Plotly chart
//             var trace1 = {
//                 type: 'bar',
//                 x: city,
//                 y: pm10_last_values,
//                 name: 'PM10'
//             };
//             var trace2 = {
//                 type: 'bar',
//                 x: city,
//                 y: pm25_last_values,
//                 name: 'PM2.5'
//             };
//             var layout = {
//                 title: 'Air Quality',
//                 barmode: 'group'
//             };
//             Plotly.newPlot('plotly-graph', [trace1, trace2], layout);
//         })
//         .catch(error => console.error('Error:', error));
// });

