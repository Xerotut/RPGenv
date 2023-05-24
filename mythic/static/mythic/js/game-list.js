import { sendXMLHttpRequest } from "./xmlhttpresponcewraper.js";

const listOfGames = document.getElementById('list-of-games');


const createNewGameForm = document.getElementById('create-new-game-form');
const createNewGameButton = document.getElementById('create-new-game-button');
const cancelCreateNewGameButton = document.getElementById('cancel-create-new-game')
const deleteButtons = document.querySelectorAll('.delete-button');


createNewGameButton.addEventListener('click', function () {
    createNewGameForm.removeAttribute('hidden');
    createNewGameButton.setAttribute('hidden', '');
});
cancelCreateNewGameButton.addEventListener('click', cancelCreateNewGame)

function cancelCreateNewGame() {
    createNewGameForm.setAttribute('hidden', '');
    createNewGameButton.removeAttribute('hidden');
}

deleteButtons.forEach((button) => addDeleteListener(button));
function addDeleteListener(button) {
    button.addEventListener('click', (event) => deleteGame(event.currentTarget.value))
}

function deleteGame(game_delete_url) {
    sendXMLHttpRequest('DELETE', game_delete_url).catch(err => { console.log(err); });
}

createNewGameForm.addEventListener('submit', function (event) {
    event.preventDefault();
    const data = new FormData(createNewGameForm);
    const encodedData = new URLSearchParams(data).toString();
    sendXMLHttpRequest('POST', undefined, encodedData).then(responceData => {
        listOfGames.insertAdjacentHTML('beforeend', responceData.html);
        const button = document.getElementById('delete-button-' + responceData.game_id);
        addDeleteListener(button);
        cancelCreateNewGame();
        createNewGameForm.reset();
    });
});

