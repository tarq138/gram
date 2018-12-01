$(function(){    
    $("#search").keyup(function(){
        var current_query = $("#search").val();
        $("#results div").hide();
        if (current_query.length > 0) {
            $("#results div").each(function(){
                var current_keyword = $(this).attr("data-keywords");
                if (current_keyword.indexOf(current_query) >=0){
                    $(this).show();
                }
            });
        }
    });
})
