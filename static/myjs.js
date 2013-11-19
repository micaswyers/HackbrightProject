 
 $(document).ready(function() {
    console.log('ready!');
    $("#search_results").hide();
    });

 $("#submit").click(function (e) { //what does the e do again?
    console.log("User clicked submit button.");
    e.preventDefault(); //Overrides submit button defaults or return False prevents event bubbling
    $("#search_results").show();
    var input=$("#text_area_sample").val();

//.get == .ajax 
    // $.get("/butts", {'words': input}, function (response) {
    //     var returned_dictionary = $.parseJSON(response);
    //     $("#search_results").html("\"" + returned_dictionary[0].title + ": \n" +returned_dictionary[0].post + "\"");
    // });


//before send to show loading behavior; add loading here 
    $.ajax({
        url:"/butts",
        data: input,
        // beforeSend: (function() {$("#search_results").show();})
    }).done(function(response) {
        console.log("The response came back");
        var returned_dictionary = $.parseJSON(response);
        $("#search_results").html( returned_dictionary[0].title + ": \n" + "\"" +returned_dictionary[0].post + "\"");
    });
});
