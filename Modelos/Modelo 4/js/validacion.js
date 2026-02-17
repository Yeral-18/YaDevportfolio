$().ready(function() {
	
//Ejecutar el validador
	$("#form_contacto").validate({
		submitHandler: function(form){
			funcion_ajax_agregar();
         },	
				
                doNotHideMessage: true, //this option enables to show the error/success messages on tab switch.
                errorElement: 'span', //default input error message container
                errorClass: 'help-block help-block-error', // default input error message class
                focusInvalid: false, // do not focus the last invalid input
                
				rules: {
                    //datos basicos
                    nombre: {
                        required: true
                    },										
                    email: {
                        required: true,
						email: true
					},
                    telefono: {
                        required: true,
						digits: true
                    },	
					selectservice: {
                        required: true
					},	
					mensaje: {
                        required: true
					},	
					activar: {
                        required: true
					}
					
                },

                messages: {}
			
	});
});

function funcion_ajax_agregar() {
 	$('#send').prop('disabled', true).text("Enviando...");
		var formData = new FormData(document.getElementById("form_contacto"));
		formData.append("dato", "valor");
		$.ajax({
			url: "requestfolder/contact.php",
			type: "post",
			dataType: "html",
			data: formData,
			cache: false,
			contentType: false,
	        processData: false,
		})
			.done(function(resultado){				
				$(".messsage-contact").show().fadeOut(18000);
				$('#form_contacto').trigger("reset");		
				$('#send').removeAttr('disabled').text("Enviar");
			});
}

