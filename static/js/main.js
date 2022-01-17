function selectWeatherLocation() {
    const API_URL = '/weather';
    var selectBox = document.getElementById("selectBox");
    //call post from here when selection is made

    console.log(selectBox);
    var selectedValue = selectBox.options[selectBox.selectedIndex].value;
    alert(selectedValue);
}

console.log("loaded file");