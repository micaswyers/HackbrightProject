 
 $(document).ready(function() {
    console.log('ready!');
    $(".loading").hide();
    });

 $("#submit").click(function (e) {
    console.log("User clicked submit button.");
    e.preventDefault(); //Overrides submit button defaults or return False prevents event bubbling
    $(".loading").show(4000);
    var input=$("#text_area_sample").val();

    $.ajax({
        url:"/butts",
        data: {'input_text': input},
    }).done(function(response) {
        console.log("The response came back");
        var returned_dictionary = $.parseJSON(response);
        console.log(returned_dictionary);
        $(".loading").hide();
        $("#search_results").html('<p class="big-text">' + "Based on your input text, you should read: " +  '</p>');
        $("#search_results").append('<p class="text">' + returned_dictionary[0].text + '</p>');
    });
});
