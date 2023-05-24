const loginButton=document.querySelector('#login-btn')

loginButton.addEventListener('click',(e)=>{
    e.preventDefault();

    const email =document.querySelector('#email').value
    const password =document.querySelector('#password').value

    fetch('/auth/login',{
        method:'POST',
        headers:{
            'Content-Type':'application/json'
        },
        body:JSON.stringify({
            'email':email,
            'password':password
        })

    }).then(response=>response.json())
    .then(data=>{
        alert('Inicio exitoso!');
        console.log(data.auth_token);
        localStorage.setItem('token',data.auth_token);
        window.location.href='/main';
    })
})

// const userForm = document.querySelector('#login-form')

// userForm.addEventListener('submit', async e =>{
//     e.preventDefault()
    
   
//    const password =  userForm['password'].value
//    const email =  userForm['email'].value
//    const response = await fetch('/login/user',{
//     method:'POST',
//     headers:{
//         'Content-Type': 'application/json'
//     },
//     body: JSON.stringify({
//         email,
//         password
//     })
//    })
//    const data = await response.json()
   
//    token = data.auth_token
//    localStorage.setItem('token', token);
//    if(token != undefined){
//     alert('Bienvenido')
//     window.location.href = "/main";
//    }
//    else{}
   
// })
