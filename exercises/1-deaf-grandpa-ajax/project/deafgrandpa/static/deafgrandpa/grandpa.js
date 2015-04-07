$(document).ready(function(){
    $('#say_grandpa').submit(function(event){
        event.preventDefault(); 
        $('.grandpa').remove('p')
        $.post( "/", $( "#say_grandpa" ).serialize(), function(data){
            var response
            if (data.said.toUpperCase() != data.said){
                response = "Speak up I cannot hear you."
            }else{
                response = "I could care less."
            }
            $('.grandpa').append("<p>" + response + "</p>")
        });
    });
})
