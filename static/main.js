function getAnswers() {
    document.getElementById("UserAnswers").innerHTML = "";
    var e = document.getElementsByTagName('Input');
    for (i = 0; i < e.length; i++) {
        if (e[i].type == "radio") {
            if (e[i].checked) {
                if (`{{answer}}` == e[i].value) {
                    print("hi")
                }



            }
        }

    }
}
const starting_time = 1;
let time = starting_time * 60;
const countdownel = document.getElementById('countdown_1');
function updatecountdown() {
    const minutes = Math.floor(time / 60);
    let seconds = time % 60;
    if (minutes < 0) {
        var cells = document.getElementsByClassName("rb");
        for (var i = 0; i < cells.length; i++) {
            cells[i].disabled = true;
        }
        countdownel.innerHTML = 'Timer over';
        return;
    }
    seconds = seconds < 10 ? '0' + seconds : seconds;
    countdownel.innerHTML = `${minutes}: ${seconds}`;
    time--;

}
setInterval(updatecountdown, 1000);