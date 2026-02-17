<?php 
 include_once("config.php");
// Body del msj
$asunto="".$purpose."";
$titlemjs="Gracias por preferirnos!";
$img_mail="https://". $nombreweb ."/images/logo_transtecolsas.png";
$bodymjs ="
<p style=\"text-align: justify;\">Hoy<strong> ". $names ." </strong>nos has contactado a través de nuestro sitio web (<strong> www.". $nombreweb ."</strong>) con el fin de: <b>".$purpose."</b>.<br> Nos proporcionastes la siguiente información:<br><br> 
<b>Su Nombre:</b>  ". $names ."<br> 
<b>Su email:</b>  ". $email ."<br>
<b>Su Teléfono de Contacto:</b> ". $phone. "<br>
<p><b>Su mensaje fue:</b><br>". $message. "</p>
Agradecemos su paciencia, verificaremos lo antes posible sus datos y solicitud.<br>
<b style=\"text-align: center;\">Recuerde: No respondas a este correo electrónico. No se responderán a los correos electrónicos enviados a esta dirección.</b><br>
</p>";
$notemjs="<p style=\"font-size:0.7rem;line-height: 0.85rem;text-align:center;\">No comparta este email con ninguna otra persona, el personal de <strong>". $namecompany ."</strong> jamas le solicitara la clave o la compartirá con otra persona que no sea el titular de su c&oacute;digo, proteja siempre sus datos. Para cualquier informaci&oacute;n extra necesaria puede utilizar los canales regulares de comunicaci&oacute;n.</p>";


// Propiedades del Correo
//Header 
$colorTxTHeader="#fffff";
$colorBGHeader="#b20404";

$colorTxTBody="#000000";
$colorBGBody="#ffffff";

$colorTxTFooter="#000000";
$colorBGFooter="#c4c4c4";

$colorTxTnote="#ffffff";
$colorBGnote="#565656";

//*Formato de envio de correo
$rmail =''.$donotreply.'<'.$donotreplymail.'>';

$header = 'From: ' . $rmail . " \r\n";
$header .= "X-Mailer: PHP/" . phpversion() . " \r\n";
$header .= "Mime-Version: 1.0 \r\n";
$header .= "Content-Type: text/html";

$mensaje ="
<table cellpadding=\"50px 0px 25px 0px\" cellspacing=\"0\" border=\"0\" height=\"100%\" width=\"100%\" bgcolor=\"".$colorBGHeader."\" style=\"border-collapse:collapse;\">
  <tr>
    <td><center style=\"width: 100%;\">
        <div style=\"max-width: 600px;\"> 
          <!--[if (gte mso 9)|(IE)]>
            <table cellspacing=\"0\" cellpadding=\"0\" border=\"0\" width=\"600\" align=\"center\">
            <tr>
            <td>
            <![endif]--> 
         
          <!-- Email Body : BEGIN -->
          <table cellspacing=\"0\" cellpadding=\"0\" border=\"0\" align=\"center\" bgcolor=\"". $colorBGBody ."\" width=\"100%\" style=\"max-width: 600px;\">
            
            <!-- Hero Image, Flush : BEGIN -->
            <tr>
              <td class=\"full-width-image\" align=\"center\" >
			  <img src=\"".$img_mail."\" width=\"100%\" height=\"auto\" border=\"0\" style=\"display:block;\"></td>
            </tr>
            <!-- Hero Image, Flush : END --> 
            
            <!-- 1 Column Text : BEGIN -->
            <tr>
              <td><table cellspacing=\"0\" cellpadding=\"0\" border=\"0\" width=\"100%\">
                  <tr>
                    <td style=\"padding: 40px; font-family: sans-serif; font-size: 15px; mso-height-rule: exactly; line-height: 20px; color:".$colorTxTBody.";\">
					<h1 style=\"text-align: center;\">".$titlemjs."</h1>					
					<p>".$bodymjs."</p>
					</td>
                  </tr>
                </table></td>
            </tr>
            <!-- 1 Column Text : BEGIN --> 
          </table>
          <!-- Email Body : END --> 
          
          <!-- Email Footer : BEGIN -->
          <table cellspacing=\"0\" cellpadding=\"0\" border=\"0\" align=\"center\"  bgcolor=\"".$colorBGFooter."\"  width=\"100%\" style=\"max-width: 680px;\">
            <tr>
              <td style=\"padding: 20px 10px;width: 100%;font-size: 12px; font-family: sans-serif; mso-height-rule: exactly; line-height:18px; text-align: center; color:".$colorTxTFooter."\">
	             <b style=\"font-size: 14px;\"> &copy; Copyright ".$copyright.", ".$namecompany."</b><br>
                 ".$sede_address."<hr>
				<strong>Llamanos:</strong> ".$sede_telf1txt."&nbsp; / &nbsp; ".$sede_telf2txt."<hr>
                <strong>Nuestro Horario de Atención:</strong> ".$horariopen."</td>
            </tr>
          </table>
          <!-- Email Footer : END --> 
          <!-- note Footer : BEGIN -->
          <table cellspacing=\"0\" cellpadding=\"0\" border=\"0\" align=\"center\"  bgcolor=\"".$colorBGnote."\"  width=\"100%\" style=\"max-width: 680px;\">
            <tr>
              <td style=\"padding: 1px 10px;width: 100%; color: ".$colorTxTnote.";\">
				  ".$notemjs."
			  </td>
            </tr>
          </table>
          <!-- Email Footer : END -->
          <!--[if (gte mso 9)|(IE)]>
            </td>
            </tr>
            </table>
            <![endif]--> 
        </div>
      </center></td>
  </tr>
</table>
<!-- note Footer : BEGIN -->
          <table cellspacing=\"0\" cellpadding=\"0\" border=\"0\" align=\"center\" width=\"100%\">
            <tr>
              <td style=\"padding: 1px 10px;width: 100%;font-size: 12px; font-family: sans-serif; mso-height-rule: exactly; line-height:13px; text-align: center; color: #000000;\">
				  <p>Diseñado por: <a href=\"http://".$autorwebsite."\">".$autorweb."</a></p>
			  </td>
            </tr>
          </table>
          <!-- Email Footer : END --> 
";

$para = ''.$names.' <' . $email . '>, Admin <'. $em_info .'>';
mail($para, $asunto, utf8_decode($mensaje), $header);
?>
