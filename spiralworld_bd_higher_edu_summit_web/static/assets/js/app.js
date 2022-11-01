

function autoloadChat(){
    var expo = $('#edu_expo_zone_id').val();
    var user_id = $('#user_id').val();
    $.get("/get/chat/"+expo, function(data, status){
        $("#chat_message").html("")
        $.each(data, function(k, v){
            if(v.send_by == user_id){
                $("#chat_message").append("<li class='clearfix'><div class='message-data'><span class='message-data-time'>"+v.create_date+"</span></div><div class='message my-message'>"+v.message+"</div></li>");
            }else{
                $("#chat_message").append("<li class='clearfix'><div class='message-data text-right'><span class='message-data-time'>"+v.create_date+"</span><p>"+v.send_name+"</p></div><div class='message other-message float-right'>"+v.message+"</div></li>");
            }
        });
        $('#scrollChat').animate({scrollTop: $('#scrollChat')[0].scrollHeight}, "slow");

    });
}

autoloadChat();

$(document).ready(function(){
  $(".show_result").css("display", "none");
  $('#handraise').hide();
  $('#handraise_join').hide();
  $("#reload").click(function(){
    autoloadVote();
  });
});

$("#vote_submit").click(function(){
    var agenda_id = $('#agenda_id').val();
    var vote = $('input[name=vote]:checked').val()
  $.post("/agm_vote",
  {
    agenda_id: agenda_id,
    vote: vote
  },
  function(data, status){
    $('#agm_vote_btn'+data.id).hide();
    $('#voteModalCenter').modal('hide');
    autoloadVote();
    alert("Success");
  });
});

$("#handraise").click(function(){
  var agm_id = $('#agm_id').val();
  $.post("/agm_handrasie",
  {
    agm_id: agm_id
  },
  function(data, status){
    $('#handraise').hide();
  });
});

$("#message").click(function(){
    var expo_zone = $('#edu_expo_zone_id').val();
    var comment = $('#comment').val();
  $.post("/chat",
  {
    message: comment,
    edu_expo_zone_id: expo_zone
  },
  function(data, status){
    $('#comment').val("");
    autoloadChat();

  });
});

setInterval(function(){ autoloadChat(); }, 30000);

