list_of_games = document.getElementById('list-of-games');
let nextGameNumber = 0;


function loadOneMoreGame() {
    console.log(nextGameNumber);
    let nextGameURL = "get_game/" + nextGameNumber
    fetch(nextGameURL)
        .then(response => response.json()) // converts the response to JSON
        .then(data => {
            parsedData = JSON.parse(data);
            console.log(parsedData);
            let new_element = document.createElement('li');
            new_element.innerText = parsedData[0].fields.name;
            list_of_games.appendChild(new_element);
            nextGameNumber += 1
            // nextGameNumber = data.next_game_number;

        });
}

/* let new_element = document.createElement('p');
new_element.innerText = document.getElementById('get-games-url').value();
document.body.appendChild(new_element); */
