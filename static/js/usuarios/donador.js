const donacionForm = document.querySelector('#donacion_form')

var token = localStorage.getItem('token');
var usuario_id = localStorage.getItem('id');

let donaciones = []
let edit =false;
let id_donacion=null;
window.addEventListener('DOMContentLoaded',async () => {
    document.getElementById('usuario').value = usuario_id
    console.log(usuario_id)

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


donacionForm.addEventListener('submit', async e =>{
    e.preventDefault()
    
    const usuario_id =  donacionForm['usuario_id'].value;
    const monto =  donacionForm['monto'].value;
    const tarjeta = donacionForm['tarjeta'].value;

    // console.log(cardno)
    if(!edit){   
    const response = await fetch('/auth/registrodonacion',{
        method:'POST',
        headers:{
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            usuario_id,
            monto,
            tarjeta
        })
    })
    const data = await response.json()
    }else{
        console.log('si')
        const response = await fetch(`/auth/actualizardonacion/${donacionid}`,{
            method:'PUT',
            headers:{
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                usuario_id,
                monto,
                tarjeta
            })
        })
        const data = await response.json()
        donacion = data
        console.log(data + " donacion hecha!")
    }
    donacionForm.reset();
})


// async function eliminar(id) {
//     console.log(id)
//     const response = await fetch(`/auth/eliminardonacion/${id}`,{
//         method:'DELETE',
//         headers:{
//             'Content-Type': 'application/json'
//         }
        
//        })
//        const data =  await response.json()
// }

// async function actualizar(id) {
//     const response = await fetch(`/donaciones/${id}`,{
//         method:'GET',
        
//        })
//     const data = await response.json()
//     console.log(data)
  
//     donacionForm["usuario_id"].value = data.donaciones[0].usuario_id
//     donacionForm["monto"].value = data.donaciones[0].monto;
//     donacionForm["precio"].value = data.donaciones[0].precio;
//     donacionForm["talla"].value = data.donaciones[0].talla;
//     edit = true;
//     donacionid = data.donaciones[0].id;
// }
