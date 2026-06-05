const API_URL = "http://127.0.0.1:5000";

// ======================
// Register User
// ======================

async function registerUser(){

    const username =
    document.getElementById("username").value;

    const email =
    document.getElementById("email").value;

    const password =
    document.getElementById("password").value;

    const response =
    await fetch(`${API_URL}/register`,{

        method:"POST",

        headers:{
            "Content-Type":"application/json"
        },

        body:JSON.stringify({
            username,
            email,
            password
        })

    });

    const data = await response.json();

    alert(data.message);

    window.location.href="login.html";
}

// ======================
// Login User
// ======================

async function loginUser(){

    const email =
    document.getElementById("email").value;

    const password =
    document.getElementById("password").value;

    const response =
    await fetch(`${API_URL}/login`,{

        method:"POST",

        headers:{
            "Content-Type":"application/json"
        },

        body:JSON.stringify({
            email,
            password
        })

    });

    const data =
    await response.json();

    alert(data.message);

    if(data.message === "Login Successful")
    {
        window.location.href =
        "dashboard.html";
    }
}