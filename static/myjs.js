 
 $(document).ready(function() {
                console.log('ready!');
            });

 $("#submit").click(function (e) {
    console.log("User clicked submit button.");
    e.preventDefault(); //Overrides submit button defaults
    var input = $("#text_area_sample").val();
    $.get("/butts", {'words': input}, function (response) {
        $("#description").html("Based on your input you should read: ");
        $("#text_area_sample").hide(" ");
        $("#submit").hide(" ");
        var obj = $.parseJSON(response);
        $("#sample_input").append("\"" + obj[0].post + "\"");
    });
});