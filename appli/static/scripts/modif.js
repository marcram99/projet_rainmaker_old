var actif = 'badge badge-secondary mr-2'
var inactif = 'badge badge-light mr-2'
var start = document.getElementById('start')
var stop = document.getElementById('stop')
var lundi = document.getElementById('lundi')
var mardi = document.getElementById('mardi')
var mercredi = document.getElementById('mercredi')
var jeudi = document.getElementById('jeudi')
var vendredi = document.getElementById('vendredi')
var samedi = document.getElementById('samedi')
var dimanche = document.getElementById('dimanche')
var week = [lundi, mardi, mercredi, jeudi, vendredi, samedi, dimanche]
var period = {'lundi':true, 
              'mardi':true,
              'mercredi':true,
              'jeudi':true,
              'vendredi':true,
              'samedi':true,
              'dimanche':true}

/* recupère valeur periode au chargement de la page */
window.addEventListener("DOMContentLoaded", (event) => {
    console.log("DOM entièrement chargé et analysé")
    week.forEach(function(jour){
        if (jour.className == actif){
            period[jour.id] = true
        }
        if (jour.className == inactif){
            period[jour.id] = false
        }
    })
})
/* modifie period et badge lors du click sur jour */
week.forEach(function(jour){
    jour.onclick = function(){
        event.preventDefault()
        if(jour.className == actif){
            jour.className = inactif
            period[jour.id] = false
            
        }
        else if(jour.className == inactif){
            jour.className = actif
            period[jour.id] = true
        }
    }
})
function valide(){
    var ok = true
    var message = ''
    if (start.value >= stop.value){
        ok = false
        message = 'start time >= stop time'
    }
    var count = 0
    for (var jour in period){
        if (period[jour]){
            count += 1
        }
    }
    if (count == 0){
        ok = false
        message += 'pas de jours sélectionné'
    }
    if(ok){
        message = 'programme valide'
    }
    return [ok, message]
}
valid.onclick = function(){
    event.preventDefault()
    var res = valide()
    console.log(res[0], res[1])
    if (res[0] == false){
        console.log('modal...')
        $("#erreur").modal('show')

    }
}
suprim.onclick = function(){
    event.preventDefault()
    console.log('suprim cliqué')
}
