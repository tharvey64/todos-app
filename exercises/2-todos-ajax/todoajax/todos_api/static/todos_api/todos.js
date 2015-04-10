$(document).ready(function(){
    if (!$.cookie('key')){
        $('.start').css('display', 'inline-block');
    }else{
        $('.access').css('display', 'inline-block');
        // $('.delete').css('display', 'inline-block');
    }
    
    $('#new_user').on('submit', function(event){
       event.preventDefault()
       $.post("/todos/new_user/", $('#new_user').serialize(), function(data){
            $.cookie('key',data.user_key);
            var template = $('#userkey').html();
            var info = Mustache.to_html(template, {'key':$.cookie('key')});
            $('.new').css('display', 'inline-block');
            $('.log_in').css('display', 'inline-block');
            $('#addddd').html(info);
        });
    });

    $('#sign_in').on('submit',function(event){
       event.preventDefault()
       $.post("/todos/sign_in/", $('#sign_in').serialize(), function(data){
            $.cookie('key', data.user_key);
            var template = $('#user-key').html();
            var info = Mustache.to_html(template, {'user_key':$.cookie('key')});
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

    $('#add_form').on('submit',function(event){
        event.preventDefault()
        $.post("/todos/add_todo/", $('#add_form').serialize(), function(data){
            
            // $.getJSON('/mysite/alltodos', function(data){
            //     var template = $('#todo-template').html();
            //     var info = Mustache.to_html(template, data);
            //     $('.todos').html(info);
            // });

        });
    });

    $('#update_form').on('submit',function(event){
        event.preventDefault()
        console.log()
    });
    // not forms yet
    // $('.list').on('submit',function(event){});
    // $('.delete').on('submit',function(event){});
});