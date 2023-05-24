import { sendXMLHttpRequest } from "./xmlhttpresponcewraper.js";

const csrfToken = document.querySelector('meta[name="csrf-token"]').content;
const getListOfGamesURL = document.getElementById('get-list_of_games-url').value;
const listOfGames = document.getElementById('list-of-games');
const goToGameURL = document.getElementById('go-to-game-url').value.substring(0, document.getElementById('go-to-game-url').value.length - 2);
const deleteGameURL = document.getElementById('delete-game-url').value.substring(0, document.getElementById('delete-game-url').value.length - 2);


const createNewGameForm = document.getElementById('create-new-game-form');
const createNewGameButton = document.getElementById('create-new-game-button');
const cancelCreateNewGameButton = document.getElementById('cancel-create-new-game')



createNewGameButton.addEventListener('click', function () {
    createNewGameForm.removeAttribute('hidden');
    createNewGameButton.setAttribute('hidden', '');
});
cancelCreateNewGameButton.addEventListener('click', cancelCreateNewGame)

function createNewListElement(data) {
    let gameListElement = document.createElement('li');
    let gameRefElement = document.createElement('a');
    let gameDelButton = document.createElement('button');
    let gameDateCreatedElement = document.createElement('p');
    gameDelButton.innerText = "Delete";
    gameDelButton.setAttribute('data-pk', data.pk);
    gameDelButton.addEventListener('click', function (event) {
        const pk = event.target.dataset.pk;
        deleteGame(pk);
    });
    gameRefElement.innerText = data.fields.name;
    gameRefElement.setAttribute('href', goToGameURL + data.pk);
    gameDateCreatedElement.innerText = data.fields.time_created;
    // gameRefElement.appendChild(gameDateCreatedElement);
    gameListElement.appendChild(gameRefElement);
    gameListElement.appendChild(gameDelButton);
    listOfGames.appendChild(gameListElement);
}

sendXMLHttpRequest('GET', getListOfGamesURL, csrfToken).then(responceData => {
    const data = JSON.parse(responceData);
    for (let i = 0; i < data.length; i++) {
        createNewListElement(data[i]);
    }
});

function deleteGame(pk) {
    sendXMLHttpRequest('POST', deleteGameURL + pk + "/", csrfToken).catch(err => { console.log(err); });
}



function cancelCreateNewGame() {
    createNewGameForm.setAttribute('hidden', '');
    createNewGameButton.removeAttribute('hidden');
}


createNewGameForm.addEventListener('submit', function (event) {
    event.preventDefault();
    const data = new FormData(createNewGameForm);
    const encodedData = new URLSearchParams(data).toString();
    sendXMLHttpRequest('POST', getListOfGamesURL, csrfToken, encodedData).then(responceData => {
        const data = JSON.parse(responceData);
        createNewListElement(data[0]);
        cancelCreateNewGame();
        createNewGameForm.reset();
    });
});

