Todos API with Ajax
===================

Now that we've got the AJAX basics down, let's consume the API we wrote yesterday with a single page application.

If you did not finish the API, now is the time.

#### The Basics

While we are handling it slightly differently, at the end of the day this is still a CRUD app. All we are doing is Creating, Reading, Updating and Deleting Todos. You have faced this simple problem before, let's focus on implementation.

This is a single page application. That means that the page will never reload and never redirect. We're going to use jQuery and Ajax to get from the server, post to the server, and update the HTML on the page when appropriate.

#### Structure

We're going to load all the HTML once, the first time the user hits the page. So add an index route to your API project that renders an HTML file. The HTML file should have our site's general structure - all the HTML elements that create the template for your page, such as divs, a tags, p tags etc.

Inside that HTML file, we're going to need some JavaScript libraries.
```html
<script src="http://ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js"></script>
<script src="http://cdnjs.cloudflare.com/ajax/libs/jquery-cookie/1.4.1/jquery.cookie.min.js"></script>
<script src="http://cdnjs.cloudflare.com/ajax/libs/mustache.js/0.8.1/mustache.min.js"></script>
```

That's jQuery, jQuery Cookie, and Mustache.

jQuery Cookie lets us load and store cookies from the front-end, like so:
```js
$.cookie('key') // get
$.cookie('key', 'value') // set
```
[Mustache](https://github.com/janl/mustache.js) is a front-end templating engine, much like Django's engine. This way we don't have to write lots of HTML.

You're also going to need to link your own JS file and CSS file from static files.

#### Flow

When the user hits the site, jQuery Cookie should look for a user cookie containing the API key. If it's not there, show them the sign up / sign in form in a modal. When they sign up, set the cookie with the API key.

I think this is a good place for a modal because we still want all of our DOM structure present - we just want to give the user a pop up to login from that we can show and hide with jQuery. If you have another idea that's fine.

If the cookie is there, it should load their todo list using AJAX.

At the bare minimum, there should be elements on the page that trigger AJAX calls to your API to load their todos, add a todo, update a todo, and delete a todo. How you want to design this is up to you.

Of course, the page's HTML should update appropriately. That's where Mustache comes in.

#### Mustache

Also in our index.html, we're going to want to define some Mustache templates. Again, these are very similar to Django templates.

Try this basic one for your `get_all_todos` endpoint. This goes in the `<head>` of the html document. This assumes that the endpoint returns a json object with a key called `todos` with an array for a value.
```html
{%verbatim%} ##For Django not to try to parse the variables
  <script id="todo-template" type="text/template">
    {{#todos}} <!-- Tells Mustache it's an array and to iterate, the same as "for todo in todos" -->
      <div class = "todo">
        <p>{{todo_text}}</p> <!-- key names in your enumerated todo objects -->
        <p>Completed: {{completed}}</p>
      </div>
    {{/todos}} <!-- end Mustache Loop -->
  </script>
{%endverbatim%}
```
For your JS file, here's the corresponding AJAX request and jQuery to put it on the page:
```js
$.getJSON('/mysite/alltodos', function(data){
  var template = $('#todo-template').html();
  var info = Mustache.to_html(template, data);
  $('.todos').html(info);
})
```
#### Tips

Don't forget about event delegation. You'll probably need it.

Use Mustache liberally, and definitely for your forms!

Plan your DOM carefully, and do at least _some_ CSS styling.

If you don't have good error handling in your API, you'll need it now. Think about user experience.
