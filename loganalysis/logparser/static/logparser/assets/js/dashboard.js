( function ( $ ) {
    "use strict";

    // const brandPrimary = '#20a8d8'
    const brandSuccess = '#4dbd74'
    const brandInfo = '#63c2de'
    const brandDanger = '#f86c6b'

    initHourTrafficChart();
    initTrafficByUrlChart();

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
            timeSeriesData.push(djangoHourTrafficAnalyzedData[key].count);
        }

        let ctx = document.getElementById( "hourTrafficChart" );
        let myChart = new Chart( ctx, {
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
                        gridLines: {
                            display: true
                        },
                        ticks: {
                            autoSkip: false
                        }
                    }],
                    yAxes: [ {
                        ticks: {
                            beginAtZero: true,
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
        console.log(djangoUrlTrafficAnalyzedData)
        // if (!djangoUrlTrafficAnalyzedData) {
        //     return;
        // }

        // let timeSeriesLabels = [];
        // let timeSeriesData = [];
        // for (let key in djangoUrlTrafficAnalyzedData) {
        //     timeSeriesLabels.push(key);
        //     timeSeriesData.push(djangoUrlTrafficAnalyzedData[key].count);
        // }

        // let ctx = document.getElementById( "urlTrafficChart" );
        // let myChart = new Chart( ctx, {
        //     type: 'line',
        //     data: {
        //         labels: timeSeriesLabels,
        //         datasets: [{
        //             label: 'Request(count)',
        //             backgroundColor: convertHex(brandInfo, 10),
        //             borderColor: brandInfo,
        //             pointHoverBackgroundColor: '#fff',
        //             borderWidth: 2,
        //             data: timeSeriesData
        //         }]
        //     },
        //     options: {
        //         maintainAspectRatio: true,
        //         legend: {
        //             display: false
        //         },
        //         responsive: true,
        //         scales: {
        //             xAxes: [{
        //                 gridLines: {
        //                     display: true
        //                 },
        //                 ticks: {
        //                     autoSkip: false
        //                 }
        //             }],
        //             yAxes: [ {
        //                 ticks: {
        //                     beginAtZero: true,
        //                     maxTicksLimit: timeSeriesLabels.length,
        //                     max: Math.max(...timeSeriesData) + (100 - Math.max(...timeSeriesData) % 100)
        //                 },
        //                 gridLines: {
        //                     display: true
        //                 }
        //             } ]
        //         },
        //         elements: {
        //             point: {
        //                 radius: 0,
        //                 hitRadius: 10,
        //                 hoverRadius: 4,
        //                 hoverBorderWidth: 3
        //             }
        //         }
        //     }
        // } );
    }
} )( jQuery );