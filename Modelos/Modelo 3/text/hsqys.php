<div class="animated fadeInDown section-title section_red h1 text-center img_HSEQ">
    HSEQ y Seguridad <img src="images/seguridad.png" class="img-fluid" alt=""/>
</div>
<section>
 <div class="container">
     <ul id="politicas" class="nav nav-tabs nav-fill" role="tablist">
     <li class="nav-item"> <a class="nav-link active"  href="#hseq" id="ptabs1" role="tab" data-toggle="tab" aria-controls="home" aria-expanded="true"><i class="fas fa-hard-hat"></i> HSEQ</a>
      </li>
      <li class="nav-item"><a class="nav-link"  href="#cyspseguridad" role="tab" id="ptabs2" data-toggle="tab" aria-controls="hats"><i class="fas fa-road"></i> Control y Seguimiento Vial</a>
      </li>
      <li class="nav-item"><a class="nav-link"   href="#catd" role="tab" id="ptabs3" data-toggle="tab" aria-controls="hats"><i class="fas fa-beer"></i> Consumo de Alcohol, Tabaco y Sustancias Psicoactivas</a>
      </li>
      <li class="nav-item"><a class="nav-link" href="#ppacosol" role="tab" id="ptabs4" data-toggle="tab" aria-controls="hats"><i class="fas fa-user-shield"></i> Acoso Laboral</a>
      </li>
      <li class="nav-item"><a class="nav-link" href="#ppti" role="tab" id="ptabs5" data-toggle="tab" aria-controls="hats"><i class="fas fa-child"></i> Trabajo Infantil</a>
      </li>
    </ul>
    <!-- Content Panel -->
    <div id="politicascontent" class="tab-content">
      <div role="tabpanel" class="tab-pane fade show active" id="hseq" aria-labelledby="ptabs1">
        <?php
        include("text/p_hseq.php");
        ?>
      </div>
      <div role="tabpanel" class="tab-pane fade" id="cyspseguridad" aria-labelledby="ptabs2">
      <?php
      include("text/p_cyspseguridad.php");
      ?>
      </div>
      <div role="tabpanel" class="tab-pane fade" id="catd" aria-labelledby="ptabs3">
      <?php
      include("text/p_catysp.php");
      ?>
      </div>
      <div role="tabpanel" class="tab-pane fade" id="ppacosol" aria-labelledby="ptabs4">
      <?php
      include("text/p_pacosolaboral.php");
      ?>
      </div>
      <div role="tabpanel" class="tab-pane fade" id="ppti" aria-labelledby="ptabs5">
      <?php
      include("text/p_ptrabinf.php");
      ?>
      </div>
    </div>
  </div>
</section>
