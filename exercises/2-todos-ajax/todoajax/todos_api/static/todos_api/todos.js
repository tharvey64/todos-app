$(document).ready(function(){
    if (!$.cookie('key')){
        $('.start').css('display', 'inline-block');
    }else{
        $('.access').css('display', 'inline-block');
        var template = $('#add_key').html();
        var info = Mustache.render(template, {'key':$.cookie('key')});
        $('.access').append(info);
        // $('.delete').css('display', 'inline-block');
    }

    $('#new_user').on('submit',function(event){
       event.preventDefault()
       $.post("/todos/new_user/", $('#new_user').serialize(), function(data){
            
            $.cookie('key', data.user_key);
            var template = $('#add_key').html();
            var info = Mustache.render(template, {'key':$.cookie('key')});
            $('.access').append(info);

            $('.start').css('display', 'none');
            $('.access').css('display', 'inline-block');
        });
    });

    $('#sign_in').on('submit',function(event){
       event.preventDefault()
       $.post("/todos/sign_in/", $('#sign_in').serialize(), function(data){
            
            $.cookie('key', data.user_key);
            var template = $('#add_key').html();
            var info = Mustache.render(template, {'key':$.cookie('key')});
            $('.access').append(info);

            $('.start').css('display', 'none');
            $('.access').css('display', 'inline-block');
        });
    });

    $('#log_out').on('click',function(event){
        event.preventDefault()
        $.removeCookie('key');
        $('.start').css('display', 'inline-block');
        $('.access').css('display', 'none');
    });
    
    $('.access').on('submit', '#add_form',function(event){
        event.preventDefault()
        $.post("/todos/add_todo/"+$.cookie('key')+"/", $('#add_form').serialize(), function(data){
            // change this to call list function
            var template = $('#todo-template').html();
            var info = Mustache.render(template, data);
            $('footer').append(info);

        });     
    });
    $('.access').on('click', '#list-all',function(event){
        event.preventDefault()
        $.getJSON('/todos/get_todos/'+ $.cookie('key') +'/', function(data){
            var template = $('#todo-template').html();
            var info = Mustache.render(template, {'todos':data.todos});
            $('footer').append(info);
            console.log(info)
        });
    });
});