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
    $.post("/",
        {'command':'on'},
        function(results){
            var res = JSON.parse(results)
            console.log(res)  
        } 
    )
}
bout_off.onclick = function(){
    event.preventDefault()
    bout_on.className = inactive
    bout_off.className = active
    bout_prog.className = inactive
    $.post("/",
        {'command':'off'},
        function(results){
            var res = JSON.parse(results)
            console.log(res)  
        } 
    )
}
bout_prog.onclick = function(){
    event.preventDefault()
    bout_on.className = inactive
    bout_off.className = inactive
    bout_prog.className = active
    $.post("/",
        {'command':'prog'},
        function(results){
            var res = JSON.parse(results)
            console.log(res['progs'])  
        } 
    )
}

window.addEventListener("DOMContentLoaded", (event) => {
    console.log("DOM entièrement chargé et analysé")
    $.post("/",
        {'command':'update'},
        function(results){
            var res = JSON.parse(results)
            console.log(res)  
        } 
    )       
})