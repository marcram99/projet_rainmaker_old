var bout_on = document.getElementById('v1_on')
var bout_off = document.getElementById('v1_off')
var bout_prog = document.getElementById('v1_prog')
var active = "btn btn-secondary m-2"
var inactive = "btn btn-outline-secondary m-2"
var p1_nom = document.getElementById("p_nom")
var p1_start = document.getElementById("p_start")
var p1_stop = document.getElementById("p_stop")
var p1_period = document.getElementById("p_jour")

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
            console.log(res)  
        } 
    )
}
function dig_2(numb){
    return numb.toLocaleString(undefined, {minimumIntegerDigits:2})
}
function jour_bg(val){
    if(val == true){
        return "badge badge-secondary mr-2"
    }
    else{
        return "badge badge-light text-secondary mr-2"
    }
}
function affiche_prog(prog){
    console.log(prog['start'])
    console.log(prog['stop'])
    console.log(prog['period'])
    p1_nom.innerHTML = prog['nom'] + ':'
    p1_start.innerHTML = dig_2(prog['start'][0]) + ':' + dig_2(prog['start'][1])
    p1_stop.innerHTML = dig_2(prog['stop'][0]) + ':' + dig_2(prog['stop'][1])
    for(var key in prog['period']){
        var val = prog['period'][key]
        console.log(key + ':' + val)
        var prov = document.getElementById(key)
        prov.className = jour_bg(prog['period'][key])
    }
}

window.addEventListener("DOMContentLoaded", (event) => {
    console.log("DOM entièrement chargé et analysé")
    $.post("/",
        {'command':'update'},
        function(results){
            var res = JSON.parse(results)
            affiche_prog(res.prog01) 
        } 
    )       
})

