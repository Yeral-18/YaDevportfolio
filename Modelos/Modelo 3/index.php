<!doctype html>
<html lang="es">
    <?php 
	 $seccion="Bienvenidos"; 
	?>
<?php include("design/head.php"); ?>
<body>
    <?php 
    include("design/navbar.php");
    include("top/slider.php"); 
    include("text/txtindex.php");
    include("text/service_index.php");
    include("text/txtcifras.php");
    include("text/txtclientes_index.php");
    include("form/txtcontact_ind.php"); 
    include("design/footer.php");  
    ?>
    <!-- jQuery (necessary for Bootstrap's JavaScript plugins) --> 
    <script src="js/jquery-3.3.1.min.js"></script>
    <script src="js/jquery.waypoints.min.js"></script>
    <script src="js/jquery.counterup.min.js"></script>
    <script>
        jQuery(document).ready(function() {
        $('.counter').counterUp({
            delay: 10,
            time: 1000
        });
        });
    </script>
    <!-- Include all compiled plugins (below), or include individual files as needed --> 
    <script src="js/popper.min.js"></script>
    <script src="js/bootstrap-4.3.1.js"></script>    
</body>
</html>