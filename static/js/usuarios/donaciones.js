var token = localStorage.getItem('token');
var usuario_id = localStorage.getItem('id');

//let donaciones = []
window.addEventListener('DOMContentLoaded',async () => {
    // document.getElementById('usuario').value = usuario_id
    // console.log(usuario_id)

    const response = await fetch('/donaciones',{
        method:'GET',
        headers:{
            'Content-Type': 'application/json',
            'token':token,
            'id':usuario_id
        },

    })
    const data = await response.json()

    donacion = data
    //console.log(donacion)
    renderDonate(donacion)
});



function renderDonate(dons){
    
    const donacionList = document.querySelector('#donacion_list')
    donacionList.innerHTML = ''
    for (var i = 0; i < dons.donaciones.length; i++) {
        //console.log(dons.donaciones[i].usuario_id)
        for (const donaciones of Object.keys(dons)) {
            if (dons.donaciones[i].usuario_id == usuario_id) {
                //const donacion = dons.donaciones[0].usuario_id;
                const donacionItem = document.createElement('tr')
                donacionItem.classList ='bg-dark text-light'
                donacionItem.innerHTML = `
                    <td>${dons.donaciones[i].monto}</td>
                    <td>${dons.donaciones[i].usuario_id}</td>
                `
                
                donacionList.append(donacionItem)
            }
        }
    }
}
