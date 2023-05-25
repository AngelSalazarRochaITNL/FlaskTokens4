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
        if(data.auth_token != undefined) {
            alert('Inicio exitoso!');

            console.log(data.auth_token);
            localStorage.setItem('token',data.auth_token);

            console.log(data.admin);
            localStorage.setItem('admin',data.admin);

            if(data.admin) {
                window.location.href='/main/admin';
            }
            else {
                window.location.href='/main/user';
            }
        }
        else {}
    })
})
