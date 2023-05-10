listOfGames = document.getElementById('list-of-games');
getGamesUrl = document.getElementById('get-games-url').value
let gamesDisplayed = 0;
const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

function loadOneMoreGame() {

    const xhr = new XMLHttpRequest();
    xhr.open('POST', getGamesUrl);

    xhr.responseType = 'json';

    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.setRequestHeader('X-CSRFToken', csrfToken);

    xhr.onload = () => {
        const data = JSON.parse(xhr.response);

        console.log(data);

        let newElement = document.createElement('li');
        newElement.innerText = data[0].fields.name;
        listOfGames.appendChild(newElement);
        gamesDisplayed += 1;
    }


    xhr.send(JSON.stringify({ games_displayed: gamesDisplayed }));

}

/* let new_element = document.createElement('p');
new_element.innerText = document.getElementById('get-games-url').value();
document.body.appendChild(new_element); */
