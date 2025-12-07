/*
NO HE CONSEGUIDO HACER QUE FUNCIONE EL TIPO DE ANIMACION

import TypeIt from "typeit";

new TypeIt("#header2Bienvenida", {
    strings: "Bienvenido al foro de proyectos",
    speed: 50,
    waitUntilVisible: true,
}).go();

document.addEventListener('DOMContentLoaded', () => {
    const input = document.getElementById('userInput')
    const ul = document.getElementById('listaU')
    const li = document.getElementById('Iusuario')

    input.addEventListener('keyup', function() {
        const filter = input.value.toUpperCase();
        for (let i = 0; i < li.length; i++){
            const a = li[i].getElementsByTagName('a')[0];
            const txtValue = a.textContent || a.innerText;
        }
    })
})

/**/
//const output = document.querySelector('.output');
//const search = document.querySelector('.filter-input');

//search.addEventListener('input', filter);

//function filter(e){
//    console.log(e.target.value.toLowerCase());
//}

// Segunda opcion/intento de tipo de animacion: (sin usar la liberira externa typeit)

/*
var i = 0;
var txt = 'Bienvenido al foro de proyectos';
var speed = 50;
function typeWrite() {
    if (i < txt.length) {
        document.getElementById("header2Bienvenida").innerHTML += txt.charAt(i);
        i++;
        setTimeout(typeWrite, speed);
    }
}
typeWrite();
*/

// Segunda opción de busqueda:

const buscarUsuario = () => {
    const searchbox = document.getElementById("inputUsuario").value.toUpperCase();
    const storeItems = document.getElementById("listaU");
    const user = document.querySelectorAll("#Iusuario");
    const pname = storeItems.getElementsByTagName("a");

    for (let i = 0; i < pname.length; i++) {
        let match = user[i].getElementsByTagName('a')[0];

        if (match) {
            let textvalue = match.textContent || match.innerHTML;

            if (textvalue.toUpperCase().indexOf(searchbox) > -1) {
                user[i].style.display = "";
            } else {
                user[i].style.display = "none";
            }
        }
    }
}
const buscarPregunta = () => {
    const searchbox = document.getElementById("inputPregunta").value.toUpperCase();
    const storeItems = document.getElementById("listaP");
    const pregunta = document.querySelectorAll("#Ipregunta");
    const pname = storeItems.getElementsByTagName("a");

    for (let i = 0; i < pname.length; i++) {
        let match = pregunta[i].getElementsByTagName('a')[0];
        if (match) {
            let textvalue = match.textContent || match.innerHTML;

            if (textvalue.toUpperCase().indexOf(searchbox) > -1) {
                pregunta[i].style.display = "";
            } else {
                pregunta[i].style.display = "none";
            }
        }
    }
}
const buscarRespuesta = () => {
    const searchbox = document.getElementById("inputRespuesta").value.toUpperCase();
    const storeItems = document.getElementById("listaR");
    const respuesta = document.querySelectorAll("#Irespuesta");
    const pname = storeItems.getElementsByTagName("a");

    for (let i = 0; i < pname.length; i++) {
        let match = respuesta[i].getElementsByTagName('a')[0];
        if (match) {
            let textvalue = match.textContent || match.innerHTML;

            if (textvalue.toUpperCase().indexOf(searchbox) > -1) {
                respuesta[i].style.display = "";
            } else {
                respuesta[i].style.display = "none";
            }
        }
    }
}

/* ANIMACION DE TEXTO (Fuente -> https://www.youtube.com/watch?v=h_Uv_9OxA2k)*/
/*
var messageArray = ["Bienvenido al foro de proyectos"];
var textPosition = 0;
var speed = 100;

typewriter = () => {
    document.querySelector("#header2Bienvenida").innerHTML =
    messageArray[0].substring(0, textPosition) + "<span>\u25AE</span>";
    if (textPosition++ != messageArray[0].length){
        setTimeout(typewriter, speed);
    }
    
}
*/