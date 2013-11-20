 
 $(document).ready(function() {
    console.log('ready!');
    $("#search_results").hide();
    });

 $("#submit").click(function (e) {
    console.log("User clicked submit button.");
    e.preventDefault(); //Overrides submit button defaults or return False prevents event bubbling
    $("#search_results").show();
    var input=$("#text_area_sample").val();

    $.ajax({
        url:"/butts",
        data: {'input_text': input},
    }).done(function(response) {
        console.log("The response came back");
        var returned_dictionary = $.parseJSON(response);
        console.log(returned_dictionary);
        $("#search_results").html("average sentence length: " + returned_dictionary[0].average_sentence_length + "1PS p-nouns: " + returned_dictionary[0].I_count);
    });
});
