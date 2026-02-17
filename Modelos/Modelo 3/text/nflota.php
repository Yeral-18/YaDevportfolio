<div class="animated fadeInDown section-title section_red img_nflota h1 text-center">
    Nuestra Flota <img src="images/aliados.png" class="img-fluid" alt=""/>
</div>
<section>
  <div class="container">
    <div class="row justify-content-center">
      <div class="col-10"><p class="text-justify">Contamos con una amplia y moderna flota de vehículos propios y de contratistas aliados, con la cual cumplimos los requerimientos de transporte de nuestros clientes de forma oportuna y dejando nuestra huella de calidad. </p></div>
    </div>
  </div>
</section>
<section id="imgflotas" class="bg-light">
  <div class="container">
    <div class="row justify-content-center">
        <ul class="list-inline nav justify-content-center">
        <?php	
          $sentencia =1;
          while ($sentencia <= 17) {
          echo "
          <li class=\"photo-item text-center\">
              <div class=\"img-gal\"><img src=\"images/nflota/nflota$sentencia.jpg\" class=\"img-fluid\" alt=\"\"/></div>
        </li>";
          $sentencia++;
          }
        ?></ul>
    </div>
  </div>
</section>