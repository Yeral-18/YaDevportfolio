<?php

	$purpose =$_POST['contact_reason'];

	$names =$_POST['contact_names'];
	$email =$_POST['contact_email'];
	$phone =$_POST['contact_phone'];
	$address = $_POST['contact_address'];
	$message =$_POST['contact_message'];

  include ("mail/msjcontact.php");
  header("location: success.php");
?>
