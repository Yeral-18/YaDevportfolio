<?php 

//Establezco parametros	
$nombre= $_POST['nombre'];
$email= $_POST['email'];
$telefono=$_POST['telefono'];
$mensaje=$_POST['mensaje'];
$selectservice=$_POST['selectservice'];
$activar = $_POST['activar'];

date_default_timezone_set("America/Bogota");
$fecha=date("Y/m/d H:i");


//Envio correo electronico
$para  = 'servigihearsas@gmail.com' . ', '; // agregar coma para añadir mas correoa
$para  .= 'losotroscomunicaciones@gmail.com' . ', '; 
$para  .= 'losotrosproyectos@gmail.com' . ', '; 
$para  .= 'losotrosdesarrollos@gmail.com' . ', '; 
$para_cliente= $email;


//Estoy recibiendo el formulario, compongo el cuerpo 
$cuerpo = '<html xmlns="http://www.w3.org/1999/xhtml">
   <head>
      <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
   </head>
   <body>
      <table width="100%" border="0" cellspacing="0" cellpadding="0">
         <tr>
            <td align="center" valign="top" bgcolor="#F7F7F7" style="background-color:#F7F7F7;">
               <br>
               <br>
               <table width="600" border="0" cellspacing="0" cellpadding="0">
                   <tr>
                     <img src="http://www.servigihear.com/images/main/header.png" style="max-width: 100%;">
                   </tr>
                  <tr>
                     <td align="center" valign="top" bgcolor="#ffffff" style="background-color:#ffffff; font-family:Arial, Helvetica, sans-serif; font-size:13px; color:#000000; padding:0px 5px 0px 15px;">
                        <table width="100%" border="0" cellspacing="0" cellpadding="0">
                           <tr>
                              <td align="left" valign="top" style="font-size:13px; font-family:Arial, Helvetica, sans-serif; color:#000000;">
                                 <div style="font-family:Georgia, "Times New Roman", Times, serif; font-size:30px; color:#0F6487; text-align: center;"><i><br> Información de Contacto</i></div>
                                 <div>                                 	
                                    <ul style="font-size: 15px">
                                        <li><strong>Nombre:</strong> '.$nombre.' </li>
										<li><strong>Correo electrónico:</strong> '.$email.' </li>
                                        <li><strong>Teléfono de contacto:</strong> '.$telefono.' </li>   
                                    	<li><strong>Asunto:</strong> '.$selectservice.' </li>
                                    	<li><strong>Mensaje:</strong> '.$mensaje.' </li>
                                    	<li><strong>Fecha:</strong> '.$fecha.' </li>
                                    </ul>
                                    <br>
                                    <img src="http://www.servigihear.com/images/main/footer.png" style="max-width: 100%;">
                                    <p style="text-align: center; font-size: 15spx">
                                    Desarrollado por Los Otros Agencia © 2021. Todos los derechos reservados.</p>
                                 </div>
                              </td>
                           </tr>
                        </table>
                     </td>
                  </tr>
               </table>
               
            </td>
         </tr>
      </table>
   </body>
</html>';

$cuerpo_cliente = '<html xmlns="http://www.w3.org/1999/xhtml">
   <head>
      <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
   </head>
   <body>
      <table width="100%" border="0" cellspacing="0" cellpadding="0">
         <tr>
            <td align="center" valign="top" bgcolor="#F7F7F7" style="background-color:#F7F7F7;">
               <br>
               <br>
               <table width="600" border="0" cellspacing="0" cellpadding="0">
                 
                  <tr>
                     <td align="center" valign="top" bgcolor="#ffffff" style="background-color:#ffffff; font-family:Arial, Helvetica, sans-serif; font-size:13px; color:#000000; padding:0px;">
                        <table width="100%" border="0" cellspacing="0" cellpadding="0">
                           <tr>
                              <td align="left" valign="top" style="font-size:13px; font-family:Arial, Helvetica, sans-serif; color:#000000;">
                                 <div style="font-family:Georgia, "Times New Roman", Times, serif; font-size:30px; color:#0F6487; text-align: center;">
								     <img src="http://www.servigihear.com/images/main/header.png" style="max-width: 100%;">
							     </div>
                                 <div >        
								 	<p style="padding-left:20px; padding-top: 30px;"> ¡Hemos recibido su solicitud! </p>
                                    <p style="padding-left:20px;">'.$nombre.'</p> 
									<p style="padding-left:20px;"> 
										Agradecemos su mensaje, pronto estaremos en contacto con usted.
									</p>									
																	
                                    <p style="padding-left:20px; padding-bottom: 30px;"> Servicios Integrales GIHEAR S.A.S.</p>
									<img src="http://www.servigihear.com/images/main/footer.png" style="max-width: 100%;">
                                    <p style="text-align: center; font-size: 15px">
                                    Desarrollado por Los Otros Agencia © 2021. Todos los derechos reservados.</p>
                                 </div>
                              </td>
                           </tr>
                        </table>
                     </td>
                  </tr>
               </table>              
            </td>
         </tr>
      </table>
   </body>
</html>';
	
//Elaboro las cabeceras 
$cabeceras = "From: servigihearsas@gmail.com"." \r\n";
$cabeceras .= "Reply-To: servigihearsas@gmail.com"."\r\n";
$cabeceras .= "MIME-Version: 1.0\r\n";
$cabeceras .= "Content-Type: text/html; charset=UTF-8\r\n";
    
 
if($_SERVER['REQUEST_METHOD'] == 'POST') {
	//mando el correo... primero el correo. luego el asunto. y por ultimo el cuerpo
	$mail= @mail($para,"Mensaje de Contacto - Servicios Integrales GIHEAR",$cuerpo,$cabeceras); 
	$mail2= @mail($para_cliente,"Registro Exitoso | Servicios Integrales GIHEAR",$cuerpo_cliente,$cabeceras);
	
}
echo $mail;
echo $mail2;
// echo 1;

?>