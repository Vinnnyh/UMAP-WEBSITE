var btnAbrirPopup = document.getElementById('btn-abrir-popup'),
	overlay = document.getElementById('overlay'),
	popup = document.getElementById('popup'),
	btnCerrarPopup = document.getElementById('btn-cerrar-popup');

btnAbrirPopup.addEventListener('click', function(){
	overlay.classList.add('active');
	popup.classList.add('active');
});

btnCerrarPopup.addEventListener('click', function(e){
	e.preventDefault();
	overlay.classList.remove('active');
	popup.classList.remove('active');
});

const form=document.querySelector(".contact_form");
        function enviar(e){
            e.preventDefault();
            const nombre=document.querySelector(".nombre"),
                correo=document.querySelector(".correo");
            Email.send({
                SecureToken : "30f7b662-f2a0-4eef-bb89-bfe531d0b27a",
                To : correo.value,
                From : "umapbot@gmail.com",
                Subject : "Subscripción",
                Body : "Gracias por suscribirte a UMAP , " + nombre.value + "."
            }).then(
                    alert('¡Gracias por suscribirte!')
                );
        }
        form.addEventListener("submit", enviar)
