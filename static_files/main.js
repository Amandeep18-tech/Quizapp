function displayRadioValue() { 
    document.getElementById("user_answer").innerHTML = "Hello"; 
    var ele = document.getElementsByTagName('input'); 
      
    for(i = 0; i < ele.length; i++) { 
          
        if(ele[i].type="radio") { 
          
            if(ele[i].checked) 
                document.getElementById("user_answer").innerHTML 
                        += ele[i].value+"<br>"; 
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