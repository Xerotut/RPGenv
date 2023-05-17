const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
const getListOfGamesURL = document.getElementById('get-list_of_games-url').value;
const listOfGames = document.getElementById('list-of-games');
const goToGameURL = document.getElementById('go-to-game-url').value.substring(0, document.getElementById('go-to-game-url').value.length - 2);
const deleteGameURL = document.getElementById('delete-game-url').value.substring(0, document.getElementById('delete-game-url').value.length - 2);

const createNewGameForm = document.getElementById('create-new-game-form');
const createNewGameButton = document.getElementById('create-new-game-button');



const getListOfGames = (method, url, data, contentTypeHeader = 'application/x-www-form-urlencoded') => {
    const promise = new Promise((resolve, reject) => {
        const xhr = new XMLHttpRequest();
        xhr.open(method, url);

        xhr.responseType = 'json';

        xhr.setRequestHeader('Content-Type', contentTypeHeader);
        xhr.setRequestHeader('X-CSRFToken', csrfToken);

        xhr.onload = () => {
            resolve(xhr.response);
        }

        xhr.send(data);
    });
    return promise;
}

function createNewListElement(data) {
    let gameListElement = document.createElement('li');
    let gameRefElement = document.createElement('a');
    let gameDelButton = document.createElement('button');
    let gameDateCreatedElement = document.createElement('p');
    gameDelButton.innerText = "Delete";
    gameDelButton.setAttribute('data-pk', data.pk);
    gameRefElement.innerText = data.fields.name;
    gameRefElement.setAttribute('href', goToGameURL + data.pk);
    gameDateCreatedElement.innerText = data.fields.time_created;
    // gameRefElement.appendChild(gameDateCreatedElement);
    gameListElement.appendChild(gameRefElement);
    gameListElement.appendChild(gameDelButton);
    listOfGames.appendChild(gameListElement);
}

getListOfGames('GET', getListOfGamesURL).then(responceData => {
    const data = JSON.parse(responceData);
    for (let i = 0; i < data.length; i++) {
        createNewListElement(data[i])
    }
});

listOfGames.addEventListener('click', function (event) {
    if (event.target.tagName === "BUTTON") {

        const pk = event.target.dataset.pk;
        deleteGame(pk);
    }
});

function deleteGame(pk) {
    console.log(pk);
    getListOfGames('GET', deleteGameURL + pk);
}

function showCreateNewGameForm() {
    createNewGameForm.removeAttribute('hidden');
    createNewGameButton.setAttribute('hidden', '');
}

function cancelCreateNewGame() {
    createNewGameForm.setAttribute('hidden', '');
    createNewGameButton.removeAttribute('hidden');
}

createNewGameForm.addEventListener('submit', function (event) {
    event.preventDefault();
    const data = new FormData(createNewGameForm);
    const encodedData = new URLSearchParams(data).toString();
    getListOfGames('POST', getListOfGamesURL, encodedData).then(responceData => {
        const data = JSON.parse(responceData);

        createNewListElement(data[0]);
        cancelCreateNewGame();
        createNewGameForm.reset();
    });
});

