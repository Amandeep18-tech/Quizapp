const end_time=document.getElementById('end-time')
const countdown_1=document.getElementById('countdown_1')
const time=Date.parse(end_time.textContent)
const start_time=document.getElementById('start-time')
console.log(time)
function timer(url){
setInterval(() => {
    const now=new Date().getTime()
    const difference=time-now
    const minutes=Math.floor((time/(1000*60)-(now/(1000*60)))%60)
    let seconds=Math.floor((time/(1000)-(now/(1000)))%60)
    seconds = seconds < 10 ? '0' + seconds : seconds
    if (difference>0){
        countdown_1.innerHTML=minutes+":" +seconds
    }
    else{
        var cells = document.getElementsByClassName("rb")
        for (var i = 0; i < cells.length; i++) {
            cells[i].disabled = true;
        countdown_1.innerHTML='Timer Over'
        url=url
        location.href=url
        }
    }
    
    
}, 1000);
}
