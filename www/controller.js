$(document).ready(function () {
   
    // display speak 
    eel.expose(DisplayMessage) 
    function DisplayMessage(message) {

        $(".siri-animate li:first").text(message); 
        $('.siri-animate').textillate('start');  
    
    } 


    //display hood 
    eel.expose(ShowHood) 
    function ShowHood() {
        $("#oval").attr("hidden", false) 
        $("#siriId").attr("hidden", true)
    }
});