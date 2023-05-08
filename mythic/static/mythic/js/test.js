games_info_url = document.getElementById('get-games-url').value

function testFunction() {
    fetch(games_info_url)
        .then(response => response.json()) // converts the response to JSON
        .then(data => {
            parsedData = JSON.parse(data)
            console.log(parsedData);
            for (let i = 0; i < parsedData.length; i++) {
                let new_element = document.createElement('p');
                new_element.innerText = parsedData[i].fields.name;
                document.body.appendChild(new_element);
            }
        });
}

let new_element = document.createElement('p');
new_element.innerText = document.getElementById('get-games-url').value
document.body.appendChild(new_element);
