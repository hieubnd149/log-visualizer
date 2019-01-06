( function ( $ ) {
    "use strict";

    // const brandPrimary = '#20a8d8'
    const brandSuccess = '#4dbd74'
    const brandInfo = '#63c2de'
    const brandDanger = '#f86c6b'

    initHourTrafficChart();
    initTrafficByUrlChart();

    function getRandomColor() {
        var letters = '0123456789ABCDEF';
        var color = '#';
        for (var i = 0; i < 6; i++) {
          color += letters[Math.floor(Math.random() * 16)];
        }
        return color;
    }

    function convertHex (hex, opacity) {
        hex = hex.replace('#', '')
        const r = parseInt(hex.substring(0, 2), 16)
        const g = parseInt(hex.substring(2, 4), 16)
        const b = parseInt(hex.substring(4, 6), 16)

        return 'rgba(' + r + ',' + g + ',' + b + ',' + opacity / 100 + ')'
    }

    function random (min, max) {
        return Math.floor(Math.random() * (max - min + 1) + min)
    }

    function initHourTrafficChart() {
        if (!djangoHourTrafficAnalyzedData) {
            return;
        }

        let timeSeriesLabels = [];
        let timeSeriesData = [];
        for (let key in djangoHourTrafficAnalyzedData) {
            timeSeriesLabels.push(key);
            timeSeriesData.push(djangoHourTrafficAnalyzedData[key]);
        }

        let ctx = document.getElementById( "hourTrafficChart" ).getContext('2d');
        let myChart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: timeSeriesLabels,
                datasets: [{
                    label: 'Request(count)',
                    backgroundColor: convertHex(brandInfo, 10),
                    borderColor: brandInfo,
                    pointHoverBackgroundColor: '#fff',
                    borderWidth: 2,
                    data: timeSeriesData
                }]
            },
            options: {
                maintainAspectRatio: true,
                legend: {
                    display: false
                },
                responsive: true,
                scales: {
                    xAxes: [{
                        scaleLabel: {
                            display: true
                        },
                        gridLines: {
                            display: true
                        },
                        ticks: {
                            autoSkip: false
                        }
                    }],
                    yAxes: [ {
                        ticks: {
                            // beginAtZero: true,
                            maxTicksLimit: timeSeriesLabels.length,
                            max: Math.max(...timeSeriesData) + (100 - Math.max(...timeSeriesData) % 100)
                        },
                        gridLines: {
                            display: true
                        }
                    } ]
                },
                elements: {
                    point: {
                        radius: 0,
                        hitRadius: 10,
                        hoverRadius: 4,
                        hoverBorderWidth: 3
                    }
                }
            }
        } );
    }

    function initTrafficByUrlChart() {
        if (!djangoUrlTrafficAnalyzedData) {
            return;
        }

        let chartData = djangoUrlTrafficAnalyzedData.data;
        let maxValue = 0;
        
        // achieve all labels first
        let setLabels = new Set();
        for (let index in chartData) {
            setLabels.add(chartData[index].date_time);
        }

        let timeSeriesLabels = [...setLabels];
        let defaultData = {};
        for (let i in timeSeriesLabels) {
            defaultData[timeSeriesLabels[i]] = 0;
        }

        let dict = {};
        for (let index in chartData) {
            if (!dict[chartData[index].url]) {
                dict[chartData[index].url] = Object.assign({}, defaultData);
            } 
            dict[chartData[index].url][chartData[index].date_time] = chartData[index].count;

            if (maxValue < chartData[index].count) {
                maxValue = chartData[index].count;
            }
        }

        let datasets = [];
        for (let key in dict) {
            let dts = Object.keys(dict[key]).map(i => dict[key][i]);
            let randColor = getRandomColor()
            datasets.push({
                label: key,
                borderColor: randColor,
                backgroundColor: randColor,
                pointHoverBackgroundColor: '#fff',
                pointStyle: 'rectRot',
                pointRadius: 5,
                pointBorderColor: 'rgb(0, 0, 0)',
                fill: false,
                borderWidth: 2,
                data: dts
            });
        }

        let ctx = document.getElementById( "urlTrafficChart" );
        let myChart = new Chart( ctx, {
            type: 'line',
            data: {
                labels: [...timeSeriesLabels],
                datasets: datasets
            },
            options: {
                maintainAspectRatio: true,
                responsive: true,
                legend: {
                    labels: {
                        usePointStyle: true
                    }
                },
                scales: {
                    xAxes: [{
                        gridLines: {
                            display: true
                        },
                        ticks: {
                            autoSkip: false
                        }
                    }],
                    yAxes: [ {
                        ticks: {
                            maxTicksLimit: timeSeriesLabels.length,
                            max: maxValue
                        },
                        gridLines: {
                            display: true
                        }
                    } ]
                },
                elements: {
                    point: {
                        radius: 0,
                        hitRadius: 10,
                        hoverRadius: 4,
                        hoverBorderWidth: 3
                    }
                }
            }
        } );
    }
} )( jQuery );