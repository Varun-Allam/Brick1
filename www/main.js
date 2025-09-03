$(document).ready(function () {
    $('.text').textillate({
        loop: true,
        sync: true,
        in:{
            effect: "bounceIn",

        },
        out: {
            effect:"bounceOut",
        },
    });

    //siri 
  
  var siriWave = new SiriWave({
    container: document.getElementById("siri-container"),
    width: 940,
    height: 200,
    style: "ios9", 
    amplitude: 1,
    autostart: true,
  }); 
  //siri_animate 

  $('.siri-animate').textillate({
    loop: true,
    sync: true,
    in:{
        effect: "fadeInUp",
        sync: true,
    },
    out: {
        effect:"fadeOutUp", 
        sync: true,
    },
}); 

 //mic_btn_click 

 $("#micBtn").click(function () { 
    eel.playAssistantSound2()

    
    $("#oval").attr("hidden", true);
    $("#siriId").attr("hidden", false);

    eel.allCommand()() 
    
 });


});