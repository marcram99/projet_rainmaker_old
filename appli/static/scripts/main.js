var bout_on = document.getElementById('v1_on')
var bout_off = document.getElementById('v1_off')
var bout_prog = document.getElementById('v1_prog')
var active = "col-3 btn btn-primary ml-2 "
var inactive = "col-3 btn btn-outline-primary ml-2 "

bout_on.onclick = function(){
    event.preventDefault()
    bout_on.className = active
    bout_off.className = inactive
    bout_prog.className = inactive
}
bout_off.onclick = function(){
    event.preventDefault()
    bout_on.className = inactive
    bout_off.className = active
    bout_prog.className = inactive
}
bout_prog.onclick = function(){
    event.preventDefault()
    bout_on.className = inactive
    bout_off.className = inactive
    bout_prog.className = active
}

window.addEventListener("DOMContentLoaded", (event) => {
    console.log("DOM entièrement chargé et analysé")
    $.post("/",
        {'requete':'intéro'},
        function(results){
            var res = JSON.parse(results)
            console.log(res)  
        } 
    )       
})