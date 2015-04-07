$(document).ready(function(){
    $('#say_grandpa').submit(function(event){
        event.preventDefault(); 
        $.post( "/", $( "#say_grandpa" ).serialize(), function(data){
            $('.grandpa p').remove();

            var response
            if (data.said.toUpperCase() != data.said){
                response = "Speak up I cannot hear you."
            }else{
                response = "Go Away."
            }
            $('.grandpa').append("<p>" + response + "</p>")
        });
    });
})
