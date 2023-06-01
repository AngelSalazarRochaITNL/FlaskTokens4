<?php
    ob_start();
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mis Donaciones</title>

    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <link rel="stylesheet" href="{{url_for('static', filename='css/home_styles.css')}}">
    
    <script src="{{ url_for('static', filename='js/usuarios/donaciones.js') }}"></script>
    <script src="https://kit.fontawesome.com/41bcea2ae3.js"></script>
    
</head>
<body id="body">
    <div class="container col-md-10 justify-content-center">

        <div class="container-form row form-group mt-3">
            <h3 class="col-3">Mis donaciones</h3>
        </div>
        
        <div class="container-form col-10 mt-3">
            <table class="table table-striped table-bordered">
                <thead>
                    <tr class="table-success">
                        <th>Monto</th>
                        <th>Donador</th>
                    </tr>
                </thead>
                <tbody id="donacion_list">
                    
                </tbody>
            </table>
        </div>
    </div>

    <script src="{{ url_for('static', filename='js/auth.js') }}"></script>

</body>
<?php
    $html = ob_get_clean();

    echo $html;

    require_once '../../static/lib/dompdf/autoload.inc.php';
    
    use Dompdf\Dompdf;
    $dompdf = new Dompdf();

    $options = $dompdf->getOptions();

    $options->set(array('isRemoteEnabled' => true));

    $dompdf->setOptions($options);

    $dompdf->loadHtml($html);

    $dompdf->setPaper('letter');

    $dompdf->render();

    $dompdf->stream("Donaciones", array("Attachment" => false));
?>