function updateClock(){
    let now = new Date();
    let hours = now.getHours().toString().padStart(2 , '0');
    let minutes = now.getMinutes().toString().padStart(2, '0');
    let seconds = now.getSeconds().toString().padStart(2, '0');

    let timeString = hours + ":" + minutes + ":" + seconds;
    document.getElementById("clock").textContent = timeString
}

setInterval(updateClock, 1000)


function goToPage(page){
    const container = document.getElementById("container");
    container.style.transform= `translateX(${-(page - 1) * 100}%)`;
}


// const toggleLine = document.getElementById("toggleLine");
// const hiddenbutton = document.getElementById("hidden-button");

// toggleLine.addEventListener("click", function(){
//     hiddenbutton.classList.toggle("show");
// });

const garis = document.getElementById("toggleLine")
const beberapabutton = document.getElementById("beberapa-button")

garis.addEventListener('click', function(){
    if (beberapabutton.style.display === 'none' || beberapabutton.style.display === ''){
        beberapabutton.style.display = 'flex';
    }else{
        beberapabutton.style.display = 'none';
    }
    beberapabutton.classList.toggle('show');
})


