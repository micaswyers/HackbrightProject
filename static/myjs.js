 
 $(document).ready(function() {
    console.log('ready!');
    $("#search_results").hide();
    });

 $("#submit").click(function (e) { //what does the e do again?
    console.log("User clicked submit button.");
    e.preventDefault(); //Overrides submit button defaults
    $("#search_results").show();
    var input=$("#text_area_sample").val();

    // $.get("/butts", {'words': input}, function (response) {
    //     var returned_dictionary = $.parseJSON(response);
    //     $("#search_results").html("\"" + returned_dictionary[0].title + ": \n" +returned_dictionary[0].post + "\"");
    // });

    $.ajax({
        url:"/butts",
        data: input
    }).done(function(response) {
        console.log("The response came back");
        var returned_dictionary = $.parseJSON(response);
        $("#search_results").html( returned_dictionary[0].title + ": \n" + "\"" +returned_dictionary[0].post + "\"");
    });
});
