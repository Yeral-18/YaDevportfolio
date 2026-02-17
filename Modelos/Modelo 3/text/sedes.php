<div class="animated fadeInDown section-title section_red img_agencias h1 text-center">
    Nuestras Agencias<img src="images/aliados.png" class="img-fluid" alt=""/>
</div>
<section>
  <div class="container">
    <div class="row">
         <div class="col-md-6 animated fadeInDown d-none d-sm-block">
            <img src="images/map_sede.png" alt="Nuestras Agencias" width="640" border="0" usemap="#mapa_sedes">
              <map name="mapa_sedes">
                  <?php
                       $coords_sede = "SELECT `id_sede`, `nam_sede`, `coords_imgmap` FROM `sedes` WHERE 1";;
                      if ($sql_sede = $configdb->prepare($coords_sede)) {
                          /* ejecutar la sentencia */
                          $sql_sede->execute();
                          /* vincular las variables de resultados */
                          $sql_sede->bind_result($idXY_sede, $cnamXY_sede, $coords_imgmap);
                          /* obtener los valores */
                          while ($sql_sede->fetch()) {
                          echo "
                          <area alt=\"$cnamXY_sede\" shape=\"circle\" coords=\"$coords_imgmap,10\" data-toggle=\"collapse\" href=\"#sede_$idXY_sede\" aria-controls=\"sede_$idXY_sede\">
                          ";     }
                          /* cerrar la sentencia */
                          $sql_sede->close();
                      }
                      /* cerrar la conexión */
                  ?>   
            </map>
        </div>
         <div class="col-md-6">
           <div id="sedes_plegable" role="tablist">
        <?php
         $consulta_tab1 = "SELECT `id_sede`, `nam_sede`, `sede_address`, `sede_telf1`, `sede_telf1txt`, `sede_telf2`, `sede_telf2txt`, `sede_cel`, `sede_celtxt`, `sede_email`, `gmapsp` FROM `sedes` WHERE 1  ORDER BY `nam_sede` ASC";
		if ($sentencia = $configdb->prepare($consulta_tab1)) {
			/* ejecutar la sentencia */
			$sentencia->execute();
			/* vincular las variables de resultados */
			$sentencia->bind_result($id_sede, $cnam_sede, $csede_address, $csede_telf1, $csede_telf1txt, $csede_telf2, $csede_telf2txt, $csede_cel, $csede_celtxt, $csede_email, $gmapsp);
			/* obtener los valores */
			while ($sentencia->fetch()) {
			echo "
            <div class=\"card animated fadeInDown delay-2\"> 
               <div class=\"card-header\" role=\"tab\" id=\"$id_sede\">
                 <h5 class=\"mb-0\">
                 <a class=\"collapsed\" href=\"#sede_$id_sede\" role=\"button\"";
				if ($id_sede!=="1") { echo "data-toggle=\"collapse\" aria-expanded=\"true\"";}
                else{ echo "data-toggle=\"collapsed\" aria-expanded=\"false\" 
                ";}
                echo "aria-controls=\"sede_$id_sede\">$cnam_sede</a>    
                  </h5>
               </div>
               <div id=\"sede_$id_sede\" class=\"collapse
               ";
				if ($id_sede<"2") { echo "show";}
                echo "  
                \" role=\"tabpanel\" aria-labelledby=\"$id_sede\" data-parent=\"#sedes_plegable\">
                 <div class=\"card-body text-justify\">";
				if ($gmapsp!="") {
					echo "
                    <div class=\"embed-responsive embed-responsive-16by9\">
                    <iframe class=\"embed-responsive-item\" src=\"https://www.google.com/maps/embed?pb=!$gmapsp\" frameborder=\"0\" style=\"border:0;\" allowfullscreen=\"\"></iframe>
                 </div>
                    ";
                }
                echo "
                 <p>
                 <address>
                  <i class=\"fas fa-map-marker-alt\"></i>&nbsp;$csede_address<br>";
				if ($csede_telf1!="") {
					echo "<abbr title=\"Telefonos\"><i class=\"fas fa-phone-alt\"></i></abbr>&nbsp;<a href=\"tel:$csede_telf1\" target=\"_blank\">&nbsp;$csede_telf1txt</a>&nbsp;/";
                }
                if ($csede_telf2!="") {
					echo "&nbsp;<a href=\"tel:$csede_telf2\" target=\"_blank\">&nbsp;$csede_telf2txt</a><br>";
                }
                if ($csede_cel!="") {
					echo "<i class=\"fas fa-mobile-alt\"></i>&nbsp;<a href=\"tel:$csede_cel\" target=\"_blank\">&nbsp;$csede_celtxt</a><br>";
                }
                echo"</abbr>";
                if ($csede_email!="") {
					echo "<strong><i class=\"fas fa-envelope-open-text\"></i></strong>&nbsp;<a href=\"mailto:$csede_email\">$csede_email</a>";
                }
                echo"
                   </address></p>
                 </div>
               </div>
             </div>
            ";     }
			/* cerrar la sentencia */
			$sentencia->close();
		}
		/* cerrar la conexión */
	?>      
           </div>
         </div>
    </div>
  </div>
</section>