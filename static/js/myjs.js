$(document).ready(function() {
    console.log('ready!');
    $(".stats").hide();
    });

$("#get-stats").click(function (e) {
    console.log("User wants stats! STAT!");
    e.preventDefault();
    $(".stats").toggle();
});


$("#submit").click(function (e) {
    console.log("User clicked submit button.");
    e.preventDefault();
    $("#suggested-reading").empty();
    $("#histogram").empty();
    $("table").hide();
    $("#sample-stats").empty();
    $("#recommended-stats").empty();
    var input=$("#sample-input-textbox").val();

    $.ajax({
        url:"/butts",
        data: {'input_text': input},
    }).done(function(response) {
        console.log("The response came back!");
        var returned_dictionary = $.parseJSON(response);
        console.log(returned_dictionary);
        if (returned_dictionary["error"]) {
            $("#suggested-reading").append(returned_dictionary["error"]);
        }
        else {
            var samplePlotData = returned_dictionary["sample_plot_data"];
            var postPlotData = returned_dictionary["recommended_plot_data"];
            var sampleTableData = returned_dictionary["sample_table_data"];
            var recommendedTableData = returned_dictionary["recommended_table_data"];
            $("table").show();
            render_graph(samplePlotData, postPlotData, "#histogram");
            fillTable(sampleTableData, recommendedTableData);
            $("#suggested-reading").append('<p><b>Post Title: </b><i>' + returned_dictionary.title + '</i></p>');
            $("#suggested-reading").append('<p><b>Excerpt: </b>' + returned_dictionary.excerpt + '</p>');
            $("#suggested-reading").append('<b>Read more at: </b>' + '<a id="link-color" target="tab" href="' + returned_dictionary.url + '">' +returned_dictionary.url + '</a>' );
        }
    });
});

