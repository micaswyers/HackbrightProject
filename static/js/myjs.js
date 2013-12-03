$(document).ready(function() {
    console.log('ready!');
    $("#histogram").hide();
    $("#legend").hide();
    });

$("#submit").click(function (e) {
    console.log("User clicked submit button.");
    e.preventDefault();
    $("#suggested-reading").empty();
    $("#histogram").empty();
    $("#legend").hide();
    var input=$("#sample-input-textbox").val();

    $.ajax({
        url:"/butts",
        data: {'input_text': input},
    }).done(function(response) {
        console.log("The response came back!");
        var returned_dictionary = $.parseJSON(response);
        if (returned_dictionary["error"]) {
            $("#suggested-reading").append(returned_dictionary["error"]);
        }
        else {
            var sample_plot_data = returned_dictionary["sample_plot_data"];
            var post_plot_data = returned_dictionary["post_plot_data"];
            $("#legend").empty();
            render_graph(sample_plot_data, post_plot_data, "#histogram");
            $("#histogram").append('<h3>' + 'Word Frequency Profiles for Sample & Recommended Texts' + '</h3>');
            $("#histogram").show();
            $("#legend").attr("style", " ");
            $("#suggested-reading").append('<p><b>' + "Title: " + '</b><i>' + returned_dictionary.title + '</i></p>');
            $("#suggested-reading").append('<p><b>' + "Excerpt: " + '</b>' + '<i>' + returned_dictionary.text + '</i>' + '</p>');
            $("#suggested-reading").append('<b>' + "Read more at: " + '</b>' + '<a href="' + returned_dictionary.url + '">' +returned_dictionary.url + "</a>" );
        }
    });
});

