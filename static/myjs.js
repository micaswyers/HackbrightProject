 
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
        $(".search_results").append($('<p>').addClass("big-text").append("Input text stats:"));
        //DECOMPOSE = THE SECRET TO PROGRAMMING 
        $(".search_results").append('<p class="text">' + returned_dictionary[0].sample_feature_vector[0] + "Total words" + '</p>');
        $(".search_results").append('<p class="text">' + returned_dictionary[0].sample_feature_vector[1] + "1st-person singular pronouns" + '</p>');
        $(".search_results").append('<p class="text">' + returned_dictionary[0].sample_feature_vector[2] + "exclamation points" + '</p>');
        $(".search_results").append($('<p>').addClass("text").append(returned_dictionary[0].sample_feature_vector[3]).append("Ellipses"));
        $(".search_results").append('<p class="text">' + returned_dictionary[0].sample_feature_vector[4] + " average words/sentence" + '</p>');
        $(".search_results").append('<p class="text"' + returned_dictionary[0].     post_feature_vector);
        $(".search_results").append('<p class="big-text">' + "You should read: " +  '</p>');
        $(".search_results").append('<p class="text">' + "Post ID#: " + returned_dictionary[0].id + '</p>');
        $(".search_results").append('<p class="text">' + "Cluster ID#: " + returned_dictionary[0].cluster + '</p>');
        $(".search_results").append('<p class="text">' + "Feature Vector: " + returned_dictionary[0].post_feature_vector + '</p>');
        $(".search_results").append('<p class="text">' + returned_dictionary[0].text + '</p>');
    });
});
