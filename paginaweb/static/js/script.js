var rut = document.getElementById('rut');
var nombre = document.getElementById('nombre');
var apellido = document.getElementById('apellido');
var genero = document.getElementById('genero');
var email = document.getElementById('email');
var modelo = document.getElementById('modelo');
var fecha = document.getElementById('fecha');
var reparo = document.getElementById('reparo');
var error = document.getElementById('error');

function Validar() {
  console.log('Enviando Formulario');

  var errores = [];

  if(rut.value === null || rut.value === ''){
    errores.push('Ingrese su rut');
  }
  if(nombre.value === null || nombre.value === ''){
    errores.push('Ingrese su nombre ');
  }
  if(apellido.value === null || apellido.value === ''){
    errores.push('Ingrese su apellido');
  }
  if(genero.value === null || genero.value === ''){
    errores.push('Seleccione su genero');
  }
  if(email.value === null || email.value === ''){
    errores.push('Ingrese su Email');
  }
  if(modelo.value === null || modelo.value === ''){
    errores.push('Ingrese el modelo de su auto');
  }
  if(fecha.value === null || fecha.value === ''){
    errores.push('Ingrese la fecha a acordar');
  }
  if(reparo.value === null || reparo.value === ''){
    errores.push('Ingrese el tipo de reparo');
  }

  error.innerHTML = errores.join(', ');

  return false;
}

function myFunction() {
    var x = document.getElementById("myTopnav");
    if (x.className === "topnav") {
      x.className += " responsive";
    } else {
      x.className = "topnav";
    }
}

