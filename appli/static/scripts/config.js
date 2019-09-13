var mod_start = document.getElementById('i_mod_st')
var h_start = document.getElementById('p_start')
var actif = 'badge badge-secondary mr-2'
var inactif = 'badge badge-light mr-2'
var lundi = document.getElementById('lundi')
var mardi = document.getElementById('mardi')
var mercredi = document.getElementById('mercredi')
var jeudi = document.getElementById('jeudi')
var vendredi = document.getElementById('vendredi')
var samedi = document.getElementById('samedi')
var dimanche = document.getElementById('dimanche')
var week = [lundi, mardi, mercredi, jeudi, vendredi, samedi, dimanche]

week.forEach(function(jour){
    jour.onclick = function(){
        event.preventDefault()
        if(jour.className == actif){
            jour.className = inactif
        }
        else if(jour.className == inactif){
            jour.className = actif
        } 
    }
})


/*
<input type="time" id="p_start" class="btn btn-secondary btn-sm mr-2"></input>
*/