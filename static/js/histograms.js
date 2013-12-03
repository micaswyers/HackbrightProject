function render_graph(plot1Data, plot2Data, chartId){
    var graph = new Rickshaw.Graph( {
        element: document.querySelector(chartId),
        width: 960,
        height: 150,
        renderer: 'line',
        series: [ {
            data: plot1Data,
            color: '#6A94D4'
        }, {
            data: plot2Data,
            color: '#052F6D'
        }]
    } );
    graph.render();

}

