 
 $(document).ready(function() {
    console.log('ready!');
    $(".loading").hide();
    });

 $("#submit").click(function (e) {
    console.log("User clicked submit button.");
    e.preventDefault(); //Overrides submit button defaults or return False prevents event bubbling
    $(".loading").show();
    $(".search_results").html(" ");
    var input=$("#text_area_sample").val();

    $.ajax({
        url:"/butts",
        data: {'input_text': input},
    }).done(function(response) {
        console.log("The response came back");
        var returned_dictionary = $.parseJSON(response);
        console.log(returned_dictionary);
        $(".loading").hide();
        $(".search_results").append('<p class="big-text">' + "Sample text stats: " +  '</p>');
        $(".search_results").append('<p class="text">' + returned_dictionary[0].sample_feature_vector + '</p>');
        $(".search_results").append('<p class="big-text">' + "Based on that sample of text, you should read: " +  '</p>');
        $(".search_results").append('<p class="text">' + "Post ID#: " + returned_dictionary[0].id + '</p>');
        $(".search_results").append('<p class="text">' + "Cluster ID#: " + returned_dictionary[0].cluster + '</p>');
        $(".search_results").append('<p class="text">' + "Feature Vector: " + returned_dictionary[0].post_feature_vector + '</p>');
        $(".search_results").append('<p class="text">' + returned_dictionary[0].text + '</p>');
    });
});
