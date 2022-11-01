
    $(document).ready(function(){
    $("#load_button").click(function(){
    jQuery.support.cors = true;

    $.ajax(
    {
        type: "GET",
        url: 'https://summit.dhakachamber.com/summit/document/get/'+$("#meeting_id").html(),
        data: "{}",
        dataType: "json",
        cache: false,
        success: function (data) {
        $("#location tbody").html('');

        $.each(data,function(i,item){
            $("#location tbody").append(
                "<tr>"
                    +"<td>"+item.name+"</td>"
                    +"<td><a href='"+item.file+"' target='_blank'>Download</a></td>"
                +"</tr>" )
        });

        },

        error: function (msg) {

            alert(msg.responseText);
        }
        });
    });
})
//$(document).ready(function() {
//  setTimeout(function() {
//    $("#load_button").click();
//  }, 5000);
//});