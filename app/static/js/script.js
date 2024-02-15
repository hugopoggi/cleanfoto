document.addEventListener('DOMContentLoaded', function () {
    var form = document.querySelector('form');
    var inputFile = document.getElementById('image');
    var loadingMessage = document.createElement('p');
    loadingMessage.textContent = 'Imagem em processamento, aguarde para fazer o download...';
    loadingMessage.classList.add('loading-message');

    form.addEventListener('submit', function (event) {
        if (inputFile.files.length === 0) {
            alert('Por favor, escolha uma foto antes de enviar.');
            event.preventDefault();
        } else {
            form.appendChild(loadingMessage);
        }
    });
});
