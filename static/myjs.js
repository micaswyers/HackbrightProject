 
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
        $(".search_results").append('<p class="fv">' + "Text length: " + returned_dictionary[0].sample_feature_vector[0] + '</p>');
        $(".search_results").append('<p class="fv">' + "Words/Sentence: " + returned_dictionary[0].sample_feature_vector[1] + '</p>');
        $(".search_results").append('<p class="fv">' + "Self-references (per 1000 words):  " + returned_dictionary[0].sample_feature_vector[2] + '</p>');
        $(".search_results").append('<p class="fv">' + "Exclamation points (per 1000 words): " + returned_dictionary[0].sample_feature_vector[3] + '</p>');
        $(".search_results").append('<p class="fv">' + "Ellipses (per 1000 words): " + returned_dictionary[0].sample_feature_vector[4] + '</p>');
        $(".search_results").append('<p class="fv">' + "u count (per 1000 words): " + returned_dictionary[0].sample_feature_vector[5] + '</p>');
        $(".search_results").append('<p class="fv">' + "r count (per 1000 words): " + returned_dictionary[0].sample_feature_vector[6] + '</p>');
        $(".search_results").append('<p class="fv">' + "2 count (per 1000 words): " + returned_dictionary[0].sample_feature_vector[7] + '</p>');
        $(".search_results").append('<p class="fv">' + "# of links (per 1000 words): " + returned_dictionary[0].sample_feature_vector[8] + '</p>');
        $(".search_results").append('<p class="big-text">' + "Based on that sample of text, you should read: " +  '</p>');
        $(".search_results").append('<p class="fv">' + "Text length: " + returned_dictionary[0].post_feature_vector[0] + '</p>');
        $(".search_results").append('<p class="fv">' + "Words/Sentence: " + returned_dictionary[0].post_feature_vector[1] + '</p>');
        $(".search_results").append('<p class="fv">' + "Self-references (per 1000 words):  " + returned_dictionary[0].post_feature_vector[2] + '</p>');
        $(".search_results").append('<p class="fv">' + "Exclamation points (per 1000 words): " + returned_dictionary[0].post_feature_vector[3] + '</p>');
        $(".search_results").append('<p class="fv">' + "Ellipses (per 1000 words): " + returned_dictionary[0].post_feature_vector[4] + '</p>');
        $(".search_results").append('<p class="fv">' + "u count (per 1000 words): " + returned_dictionary[0].post_feature_vector[5] + '</p>');
        $(".search_results").append('<p class="fv">' + "r count (per 1000 words): " + returned_dictionary[0].post_feature_vector[6] + '</p>');
        $(".search_results").append('<p class="fv">' + "2 count (per 1000 words): " + returned_dictionary[0].post_feature_vector[7] + '</p>');
        $(".search_results").append('<p class="fv">' + "# of links (per 1000 words): " + returned_dictionary[0].post_feature_vector[8] + '</p>');
        $(".search_results").append('<p class="fv">' + "Post ID#: " + returned_dictionary[0].id + '</p>');
        $(".search_results").append('<p class="fv">' + "Cluster ID#: " + returned_dictionary[0].cluster + '</p>');
        $(".search_results").append('<p class="text">' + returned_dictionary[0].text + '</p>');
    });
});
