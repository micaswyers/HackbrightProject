$(document).ready(function() {
    console.log('ready!');
    $(".loading").hide();
    $("#chart1").hide();
    $("#chart2").hide();
    });

$("#submit").click(function (e) {
    console.log("User clicked submit button.");
    e.preventDefault();
    $(".loading").show();
    $("#chart1").empty();
    $("#chart2").empty();
    $(".search_results").html(" ");
    var input=$("#text_area_sample").val();

    $.ajax({
    url:"/butts",
    data: {'input_text': input},
    }).done(function(response) {
    console.log("The response came back!");
    var returned_dictionary = $.parseJSON(response);
    var sample_plot_data = returned_dictionary["sample_plot_data"];
    var post_plot_data = returned_dictionary["post_plot_data"];
    render_graph(sample_plot_data, "#chart1");
    render_graph(post_plot_data, "#chart2");
    $(".loading").hide();
    
    $("#chart1").show().append('<h2>Blog Sample Word Frequency</h2>');
    $("#chart2").show().append('<h2>Suggested Post Word Frequency</h2>');
    $(".search_results").append('<p class="big-text">' + "Based on that sample of text, you should read: " +  '</p>');
    $(".search_results").append('<p class="fv">' + "Post ID#: " + returned_dictionary.id + '</p>');
    $(".search_results").append('<p class="fv">' + "Cluster ID#: " + returned_dictionary.cluster + '</p>');
    $(".search_results").append('<p class="text">' + returned_dictionary.title + '</p>');
    $(".search_results").append('<p class="text">' + returned_dictionary.url + '</p>');
    $(".search_results").append('<p class="text">' + returned_dictionary.text + '</p>');
    });
});
