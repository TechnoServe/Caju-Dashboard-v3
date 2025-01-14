from branca.element import Template, MacroElement

template_fr = """
{% macro html(this, kwargs) %}

<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="//code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css">

  <script src="https://code.jquery.com/jquery-1.12.4.js"></script>
  <script src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script>

  <script>
  $( function() {
    $( "#maplegend" ).draggable({
                    start: function (event, ui) {
                        $(this).css({
                            right: "auto",
                            top: "auto",
                            bottom: "auto"
                        });
                    }
                });
});

  </script>
</head>
<body>


<div id='maplegend' class='maplegend' 
    style='position: absolute; z-index:9999; border:2px solid grey; background-color:rgba(255, 255, 255, 0.8);
     border-radius:6px; padding: 10px; font-size:14px; right: 20px; bottom: 20px;'>

<div class='legend-title'>Legende</div>
<div class='legend-scale'>
  <ul class='legend-labels'>
    <li><img src="https://cdn.mapmarker.io/api/v1/font-awesome/v5/pin?icon=fa-warehouse&size=25&hoffset=0&voffset=-1
    &background=1167b1">&nbsp;&nbsp;Entrepot de cajoux</li>
    <li><img src="https://cdn.mapmarker.io/api/v1/font-awesome/v5/pin?icon=fa-globe-africa&size=25&hoffset=0&voffset
    =-1&background=008000">&nbsp;&nbsp;Plantation</li>
    <li><img src="https://cdn.mapmarker.io/api/v1/font-awesome/v5/pin?icon=fa-leaf&size=25&hoffset=0&voffset=-1
    &background=c63e2b">&nbsp;&nbsp;Pépinière</li>
    <li><img src="https://cdn.mapmarker.io/api/v1/font-awesome/v5/pin?icon=fa-warehouse&size=25&hoffset=0&voffset=-1
    &background=DBA800">&nbsp;&nbsp;Lieu d'Apprentissage</li>
    <li>&nbsp;<img src="https://i.ibb.co/J3L37CV/Picture3.png" width="17" height="24">&nbsp;&nbsp;&nbsp;Prédictions 
    satellitaire</li>
  </ul>
</div>
</div>
</body>
</html>

<style type='text/css'>
  .maplegend .legend-title {
    text-align: left;
    margin-bottom: 5px;
    font-weight: bold;
    font-size: 90%;
    }
  .maplegend .legend-scale ul {
    margin: 0 0 5px;
    padding: 0;
    float: left;
    list-style: none;
    }
  .maplegend .legend-scale ul li {
    font-size: 80%;
    list-style: none;
    margin-left: 0;
    line-height: 18px;
    margin-bottom: 2px;
    }
  .maplegend ul.legend-labels li span {
    display: block;
    float: left;
    height: 16px;
    width: 30px;
    margin-right: 5px;
    margin-left: 0;
    border: 1px solid #999;
    }
  .maplegend .legend-source {
    font-size: 80%;
    color: #777;
    clear: both;
    }
  .maplegend a {
    color: #777;
    }
</style>
{% endmacro %}"""

template_en = """
{% macro html(this, kwargs) %}

<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="//code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css">

  <script src="https://code.jquery.com/jquery-1.12.4.js"></script>
  <script src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script>

  <script>
  $( function() {
    $( "#maplegend" ).draggable({
                    start: function (event, ui) {
                        $(this).css({
                            right: "auto",
                            top: "auto",
                            bottom: "auto"
                        });
                    }
                });
});

  </script>
</head>
<body>


<div id='maplegend' class='maplegend' 
    style='position: absolute; z-index:9999; border:2px solid grey; background-color:rgba(255, 255, 255, 0.8);
     border-radius:6px; padding: 10px; font-size:14px; right: 20px; bottom: 20px;'>

<div class='legend-title'>Legend</div>
<div class='legend-scale'>
  <ul class='legend-labels'>
    <li><img src="https://cdn.mapmarker.io/api/v1/font-awesome/v5/pin?icon=fa-warehouse&size=25&hoffset=0&voffset=-1
    &background=1167b1">&nbsp;&nbsp;Cashew Warehouse</li>
    <li><img src="https://cdn.mapmarker.io/api/v1/font-awesome/v5/pin?icon=fa-globe-africa&size=25&hoffset=0&voffset
    =-1&background=008000">&nbsp;&nbsp;Plantation Location</li>
    <li><img src="https://cdn.mapmarker.io/api/v1/font-awesome/v5/pin?icon=fa-leaf&size=25&hoffset=0&voffset=-1
    &background=c63e2b">&nbsp;&nbsp;Nursery</li>
    <li><img src="https://cdn.mapmarker.io/api/v1/font-awesome/v5/pin?icon=fa-warehouse&size=25&hoffset=0&voffset=-1
    &background=DBA800">&nbsp;&nbsp;Training Location</li>
    <li>&nbsp;<img src="https://i.ibb.co/J3L37CV/Picture3.png" width="17" height="24">&nbsp;&nbsp;&nbsp;Satellite 
    predictions</li>

  </ul>
</div>
</div>

</body>
</html>

<style type='text/css'>
  .maplegend .legend-title {
    text-align: left;
    margin-bottom: 5px;
    font-weight: bold;
    font-size: 90%;
    }
  .maplegend .legend-scale ul {
    margin: 0 0 5px;
    padding: 0;
    float: left;
    list-style: none;
    }
  .maplegend .legend-scale ul li {
    font-size: 80%;
    list-style: none;
    margin-left: 0;
    line-height: 18px;
    margin-bottom: 2px;
    }
  .maplegend ul.legend-labels li span {
    display: block;
    float: left;
    height: 16px;
    width: 30px;
    margin-right: 5px;
    margin-left: 0;
    border: 1px solid #999;
    }
  .maplegend .legend-source {
    font-size: 80%;
    color: #777;
    clear: both;
    }
  .maplegend a {
    color: #777;
    }
</style>
{% endmacro %}"""

macro_fr = MacroElement()
macro_fr._template = Template(template_fr)

macro_en = MacroElement()
macro_en._template = Template(template_en)
