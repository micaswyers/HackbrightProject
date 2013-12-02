function render_graph(plotData){
    var graph1 = new Rickshaw.Graph( {
        element: document.querySelector("#chart1"),
        width: 235,
        height: 85,
        renderer: 'bar',
        series: [ {
            data: plotData,
            color: 'steelblue'
        } ]
    } );
    graph1.render();
}


// var graph2 = new Rickshaw.Graph( {
//     element: document.querySelector("#chart2"),
//     width: 235,
//     height: 85,
//     renderer: 'bar',
//     series: [ {
//         data: [{'y': 0, 'x': 1}, {'y': 300, 'x': 2}, {'y': 240, 'x': 3}, {'y': 300, 'x': 4}, {'y': 60, 'x': 5}, {'y': 0, 'x': 6}, {'y': 180, 'x': 7}, {'y': 240, 'x': 8}, {'y': 240, 'x': 9}, {'y': 300, 'x': 10}, {'y': 300, 'x': 11}, {'y': 361, 'x': 12}, {'y': 180, 'x': 13}, {'y': 180, 'x': 14}, {'y': 0, 'x': 15}, {'y': 240, 'x': 16}, {'y': 60, 'x': 17}, {'y': 120, 'x': 18}, {'y': 60, 'x': 19}, {'y': 120, 'x': 20}, {'y': 180, 'x': 21}, {'y': 300, 'x': 22}, {'y': 481, 'x': 23}, {'y': 240, 'x': 24}, {'y': 421, 'x': 25}, {'y': 180, 'x': 26}, {'y': 60, 'x': 27}, {'y': 240, 'x': 28}, {'y': 60, 'x': 29}, {'y': 361, 'x': 30}, {'y': 300, 'x': 31}, {'y': 601, 'x': 32}, {'y': 180, 'x': 33}, {'y': 120, 'x': 34}, {'y': 240, 'x': 35}, {'y': 300, 'x': 36}, {'y': 60, 'x': 37}, {'y': 361, 'x': 38}, {'y': 240, 'x': 39}, {'y': 120, 'x': 40}, {'y': 300, 'x': 41}, {'y': 60, 'x': 42}, {'y': 120, 'x': 43}, {'y': 120, 'x': 44}, {'y': 180, 'x': 45}, {'y': 240, 'x': 46}, {'y': 120, 'x': 47}, {'y': 0, 'x': 48}, {'y': 60, 'x': 49}, {'y': 60, 'x': 50}],
//         color: 'steelblue'
//     } ]
// } );
// graph2.render()