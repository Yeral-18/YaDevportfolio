<?php 
//Datos de la Pagina
$namecompany ="TRANSTECOL S.A.S.";
$slogan ="Construimos País, Transportamos Desarrollo!";
$copyright="2014-2020";

$nombreproductweb ="transtecol.com.co";
$autorweb="@FJPMGDesigner";
$autorwebsite="www.fjpycia.com";
$nombreweb = "transtecol.com.co";
$nhttp="www.";
$horariopen = "Lunes a Sábado: 8:00 a.m. a 6:00 p.m.";
$ogdescription_link="Somos una empresa Santandereana que brinda soluciones en el área de Transporte de Carga sólida y liquida; Obra Civil, Ambiental y Administración de Personal, con más de 12años de experiencia";
// Google Cuenta
$codVerifGoogle="";
$googleAnalytics ="";

// Sede Pincipal
$nam_sede="Floridablanca";
$mapsg_sede="1gM9B8oJeDZhPqL0mqIltd4iPmWk";
$sede_address="Km 2+176 Anillo vial Floridablanca-Girón, Ecoparque Natura, Torre 1, Oficina 415.";
$sede_telf1="+5776784700";
$sede_telf1txt="(+57)(7)678 4700"; 
$sede_telf2="+5776782176";
$sede_telf2txt="(+57)(7)678 2176";
$sede_email="hse@".$nombreweb."";

// Datos Correos

$bgcoloremail_bar="#AA0002";
$donotreply = $namecompany;
$donotreplymail = "donotreply@".$nombreweb."";
$email_protect="juridica@".$nombreweb."";

//email
$em_info="hse@".$nombreweb."";
$em_cotiz="";
$em_report="";
$em_recla="";
$em_jobs="";

// Datos Base de Datos
$host="localhost";
/*$user="root";
$pw="";
$bd="transtecol";*/

$user="transtec";
$pw="Carros2019%&";
$bd="transtec_sedes";

$configdb = new mysqli($host,$user,$pw,$bd);

/* comprobar la conexión */
if (!$configdb) {
    echo "Error: No se pudo conectar a MySQL." . PHP_EOL;
    echo "errno de depuración: " . mysqli_connect_errno() . PHP_EOL;
    echo "error de depuración: " . mysqli_connect_error() . PHP_EOL;
    exit;
}
?>