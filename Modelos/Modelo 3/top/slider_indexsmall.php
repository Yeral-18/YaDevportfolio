<!--#Our Partners assets/images start -->
  <div id="slideras" class="carousel slide" data-ride="carousel">
    <div class="carousel-inner" role="listbox">
    <?php	
      echo "<div class=\"carousel-item active\"><img src=\"images/ssocial/imgss1.jpg\" class=\"d-block mx-auto\" alt=\"\"/></div>";
      $nimgss =2;
      while ($nimgss <= 8) {
      echo "
      <div class=\"carousel-item\"><img src=\"images/ssocial/imgss$nimgss.jpg\" class=\"d-block mx-auto\" alt=\"\"/></div>";
      $nimgss++;
      }
    ?>
    </div>
    <a class="carousel-control-prev" href="#slideras" role="button" data-slide="prev"> <span class="carousel-control-prev-icon" aria-hidden="true"></span> <span class="sr-only">Anterior</span> </a> <a class="carousel-control-next" href="#slideras" role="button" data-slide="next"> <span class="carousel-control-next-icon" aria-hidden="true"></span> <span class="sr-only">Siguiente</span> </a> </div> 
<!--#End Our Partners assets/images -->