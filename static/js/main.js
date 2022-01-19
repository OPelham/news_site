function selectWeatherLocation() {
    const API_URL = '/weather/';
    let xhr = new XMLHttpRequest();
    xhr.open("POST", API_URL);

    xhr.setRequestHeader("Accept", "application/json");
    xhr.setRequestHeader("Content-Type", "application/json");

    let selectBox = document.getElementById("selectBox");
    //call post from here when selection is made

    let selectedValue = selectBox.options[selectBox.selectedIndex].value;
    console.log(selectedValue);


    let data = `{ "Selection": ${selectedValue} }`;

    console.log(data)

    console.log(xhr)
    xhr.send(data);
    console.log(xhr.responseText);
}





