<!DOCTYPE html>
<html>
    <head>
        <title>Hello</title>
        <link rel="stylesheet" href="/static/css/app.css">
    </head>
    
    <body>
        <div class="hexcont">
            <div class="hexagon"><span></span></div>
        </div>
        <div class="hexcont">
            <div class="hexagon"><span></span></div>
        </div>
        <div class="hexcont">
            <div class="hexagon"><span></span></div>
        </div>
        <div class="hexcont">
            <div class="hexagon"><span></span></div>
        </div>

        <img class="imglogo" src="/static/img/logo.svg">
	{{ error }}
	<form method="post">
	  {% csrf_token %}
	  Fecha:<input name="fecha" > <br>
	  Matrícula de vehículo:<input name="matricula"> <br>
	  <input type="submit" value="Submit">
	</form>
    </body>
</html>
