 
 $(document).ready(function() {
                console.log('ready!');
            });

 $("#submit").click(function (e) {
    console.log("User clicked submit button.");
    e.preventDefault(); //Overrides submit button defaults
    var input = $("#text_area_sample").val();
    $.get("/butts", {'words': input}, function (response) {
        $("#sample_input").html(" ");
        var obj = $.parseJSON(response);
        console.log(obj);
        $("#sample_input").append(obj[0].post);
    });
});