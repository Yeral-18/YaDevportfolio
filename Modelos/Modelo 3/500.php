<!doctype html>
<html lang="es">
<?php
    $seccion="ERROR 500"; 
    include("design/head.php"); 
?>
<body>
<?php
    include("design/navbar.php"); 
?>
      <div class="jumbotron">
        <div class="container">
          <div class="row">
            <div class="text-center col-md-6 offset-md-3">
              <h1><i class="animated fadeInDown fas fa-exclamation-triangle fa-5x"></i></h1>
              <h2 class="animated fadeInDown delay-1">ERROR 500</h2>
              <p class="text-center text-danger">Consulte con el Proveedor de Hosting</p>
            </div>
          </div>
        </div>
      </div>
<?php 
    include("design/footer.php"); 
?>
    <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
    <script src="js/jquery-3.3.1.min.js"></script>
    <!-- Include all compiled plugins (below), or include individual files as needed -->
    <script src="js/popper.min.js"></script>
    <script src="js/bootstrap-4.3.1.js"></script>
</body>
</html>