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
/*------------------------------------*/
week.forEach(function(jour){/* modifie la présentation des jours */
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
        console.log(jour.id, period[jour.id]) 
    }
})
valid.onclick = function(){
    event.preventDefault()
    console.log('start: ' + start.value)
    console.log('stop: ' + stop.value)
    console.log(period)
}
suprim.onclick = function(){
    event.preventDefault()
    console.log('suprim cliqué')
}