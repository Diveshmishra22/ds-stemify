document.querySelectorAll(".tool-card").forEach(card => {

    card.addEventListener("mouseleave", () => {

        card.scrollTo({
            top: 0,
            behavior: "smooth"
        });

    });

});

const stars = document.querySelectorAll(".star");

const submit = document.getElementById("submitRating");

const msg = document.getElementById("ratingMessage");

let selected = 0;

stars.forEach((star) => {

    star.addEventListener("click", () => {

        selected = star.dataset.rating;

        stars.forEach(s => s.style.color="#666");

        for(let i=0;i<selected;i++){

            stars[i].style.color="#FFD700";

        }

    });

});

submit.addEventListener("click",()=>{

    if(selected==0){

        alert("Please select rating");

        return;

    }

    fetch("/rate",{

        method:"POST",

        headers:{

            "Content-Type":"application/json"

        },

        body:JSON.stringify({

            rating:selected

        })

    })

    .then(r=>r.json())

    .then(data=>{

        document.getElementById("average").innerHTML=data.average;

        document.getElementById("ratingCount").innerHTML=data.ratings;

        msg.innerHTML="⭐ Thank You for Rating DM STEMIFY";

        submit.style.display="none";

    });

});