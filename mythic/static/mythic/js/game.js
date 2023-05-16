const sendMessageURL = document.getElementById('send-message-url')

const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

const textField = document.getElementById('message');
const messageBox = document.getElementById('message-box');




textField.addEventListener('keydown', function (event) {
    if (event.key === 'Enter') {
        let text = textField.value;
        resetTextField(event);
        let message = document.createElement('p');
        message.textContent = text;
        messageBox.appendChild(message)
        messageBox.scrollTop = messageBox.scrollHeight - messageBox.clientHeight;
    }
});


function resetTextField(event) {
    event.preventDefault();
    textField.value = "";
    textField.selectionStart = 0;
    textField.selectionEnd = 0;
}

function sendMessage() {
    const xhr = new XMLHttpRequest();
    xhr.open('POST', sendMessageURL);

    xhr.responseType = 'json';

    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.setRequestHeader('X-CSRFToken', csrfToken);
}