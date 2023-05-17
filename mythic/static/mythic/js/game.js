import { sendXMLHttpRequest } from "./xmlhttpresponcewraper.js";
window.messagesURL = window.messagesURL.substring(0, window.messagesURL.length - 2);

const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

const textField = document.getElementById('message');
const messageBox = document.getElementById('message-box');
const messageForm = document.getElementById('message-form');

const noteTab = document.getElementById('notes-tab')

let tabs = document.querySelectorAll('.tab');

let activeTab = window.activeTab;

if (activeTab === null) {
    activeTab = noteTab;
} else {
    activeTab = document.getElementById(activeTab)
}
activeTab.classList.add('active');


tabs.forEach(function (tab) {
    tab.addEventListener('click', function (event) {
        const id = event.currentTarget.id;
        if (id != activeTab.id) {
            makeTabActive(id);
        }
    });
});
/* messageForm.addEventListener('keydown', function (event) {
    if (event.key == 'Enter') {
        messageForm.submit();
    }
})
 */
messageForm.addEventListener('submit', function (event) {
    event.preventDefault();
    const data = new FormData(messageForm);
    const encodedData = new URLSearchParams(data).toString();
    postMessage();
    let adress = activeTab.id;
    if (adress == 'notes-tab') {
        adress = '0';
    }
    sendXMLHttpRequest('POST', messagesURL + adress + '/', csrfToken, encodedData).then(responceData => {
        console.log(responceData);
    })
});

function makeTabActive(scene) {
    messageBox.innerHTML = "";
    activeTab.classList.remove('active');
    activeTab = document.getElementById(scene);
    activeTab.classList.add('active');
    if (scene == 'notes-tab') {
        scene = 0;
    }
    sendXMLHttpRequest('GET', window.messagesURL + scene + "/", csrfToken).then(responceData => {
        const data = JSON.parse(responceData)
        data.forEach(function (messageInfo) {
            const messageText = messageInfo.fields.text;
            const message = document.createElement('p');
            message.innerText = messageText;
            messageBox.appendChild(message);
        })
    })
}


function postMessage() {
    let text = textField.value;
    textField.value = "";
    textField.selectionStart = 0;
    textField.selectionEnd = 0;
    let message = document.createElement('p');
    message.textContent = text;
    messageBox.appendChild(message)
    messageBox.scrollTop = messageBox.scrollHeight - messageBox.clientHeight;
}

