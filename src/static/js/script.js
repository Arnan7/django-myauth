document.addEventListener('DOMContentLoaded', function() {
    console.log('DOM cargado');
    // Añadir un efecto de hover a las tarjetas del dashboard
    const dashboardCards = document.querySelectorAll('.shadow-lg');
    dashboardCards.forEach(card => {
        // elevar la tarjeta al pasar el mouse
        card.addEventListener('mouseenter', () => {
            card.style.transform = 'translateY(-3px)';
            card.style.transition = 'transform 0.2s ease-out';
        });
        // volver a la posición original
        card.addEventListener('mouseleave', () => {
            card.style.transform = 'translateY(0)';
        });
    });

    const editProfileButton = document.querySelector('a[href="#"]'); // Ajusta el selector si es necesario
    if (editProfileButton) {
        // Mostrar una alerta simple al hacer clic en un botón
        editProfileButton.addEventListener('click', function(event) {
            event.preventDefault(); // Previene la acción por defecto del enlace
            alert('Funcionalidad "editar perfil" en desarrollo!');
        });
    }
});