<form  id="form_contact" name="form_contact" action="contact_ok.php" method="POST" enctype="multipart/form-data" data-toggle="validator" data-disable="false" onSubmit="" accept-charset="UTF-8" role="form">
  <div class="col-md-8 offset-md-2">
    <div class="row">
      <div class="col-md-6">
        <div class="form-group">
          <label for="contact_names">Datos de Contacto</label>
          <input id="contact_names" name="contact_names" type="text" class="form-control" placeholder="Nombre(s) y Apellido(s)*" required="" data-validation-required-message="Por favor ingrese su nombre"  maxlength="30">
        </div>
        <div class="form-group">
          <input  id="contact_email" name="contact_email" type="email" class="form-control" placeholder="e-mail@contacto.com" required="" data-validation-required-message="Por favor ingrese una direcci&oacute;n de correo">
        </div>
        <div class="form-group">
          <input id="contact_phone" name="contact_phone" type="text" class="form-control" placeholder="Numero tel&eacute;fonico" required="" data-validation-required-message="Por favor ingrese un número de tel&eacute;fono">
        </div>
      </div>
      <div class="col-md-6">
        <div class="form-group">
          <label for="contact_reason">Seleccione el Motivo del Contacto</label>
          <select id="contact_reason" name="contact_reason" class="form-control" required>
            <option value="Solicitar Informacion">Deseo Informaci&oacute;n</option>
            <option value="Solicito Cotizacion">Deseo Cotizar</option>
            <option value="Dar Reporte">Deseo Reportar</option>
            <option value="Hacer un Reclamo">Deseo Hacer Reclamo</option>
            <option value="Trabajar con ustedes">Deseo Trabajar</option>
          </select>
        </div> 
        <div class="form-group">
          <label for="contact_message">Mensaje</label>
          <textarea id="contact_message" name="contact_message" rows="2" cols="100"  required="" class="form-control" placeholder="D&iacute;ganos, En que le podemos servir?"></textarea>
        </div>
      </div>
      <div class="col-sm-12">
        <p class="text-center">
          <button id="sendForm" type="submit" class="btn btn-primary btn-block" data-loading-text="Enviando...">Enviar Consulta</button><br>
      </div>
    </div>
    </div>
  </div>
</form>