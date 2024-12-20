document.getElementById("phone_btn").addEventListener("click",function(){
    document.getElementById("phone").style.display=block;
    document.getElementById("email").style.display=none;
    
})

document.getElementById("gmail_btn").addEventListener("click",function(){
    document.getElementById("phone").style.display=none;
    document.getElementById("email").style.display=block;
    
})