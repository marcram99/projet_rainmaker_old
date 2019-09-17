var bout_on = document.getElementById('v1_on')
var bout_off = document.getElementById('v1_off')
var bout_prog = document.getElementById('v1_prog')
var active = "btn btn-secondary col-10 m-2"
var inactive = "btn btn-outline-secondary col-10 m-2"
var p1_period = document.getElementById("p_jour")
var prog2 = document.getElementById("prog2")
var ajout = document.getElementById("ajout")

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
function dig_2(numb){/* affiche 'numb' sur 2 digit*/
    return numb.toLocaleString(undefined, {minimumIntegerDigits:2})
}
function jour_bg(val){/* définis le background des badges jours*/
    if(val == true){
        return "badge badge-secondary mr-2"
    }
    else{
        return "badge badge-light text-secondary mr-2"
    }
}
function affiche_prog(prog, nb){
    var nom = document.getElementById(nb + "_nom")
    var start = document.getElementById(nb + "_start")
    var stop = document.getElementById(nb + "_stop")
    nom.innerHTML = prog['nom'].substring(0, 4).toUpperCase() + " " + prog['nom'].substring(4,prog['nom'].lenght)
    start.innerHTML = dig_2(prog['start'][0]) + ':' + dig_2(prog['start'][1])
    stop.innerHTML = dig_2(prog['stop'][0]) + ':' + dig_2(prog['stop'][1])
    for(var key in prog['period']){
        var val = prog['period'][key]
        var prov = document.getElementById(nb + '_' + key)
        prov.className = jour_bg(prog['period'][key])
    }
}

window.addEventListener("DOMContentLoaded", (event) => {
    console.log("DOM entièrement chargé et analysé")
    $.post("/",
        {'command':'update'},
        function(results){ /* suivant nb prog, affiche les cartes progs + btn ajout prog */
            var res = JSON.parse(results)
            affiche_prog(res.prog01,'p1')
            if(res['nb_prog'] >= 2){
                prog2.className = "card shadow col-10 my-2 mx-3 "
                affiche_prog(res.prog02,'p2')
            }
            if(res['nb_prog'] == 3){
                prog3.className = "card shadow col-10 my-2 mx-3 "
                ajout.className = "list-group-item invisible"
                affiche_prog(res.prog03,'p3')
            }

        } 
    )       
})

