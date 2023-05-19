const marcas1 = document.getElementById("marcas1");
const marcas2 = document.getElementById("marcas2");


marcas1.addEventListener("click", () => {
         console.log("marcas1");
         document.getElementById('wrapper_ford').style.display = 'none';
         document.getElementById('wrapper_chevrolet').style.display = 'flex';
})

marcas2.addEventListener("click", () => {
        console.log("marcas2 clicked");
        document.getElementById('wrapper_ford').style.display = 'flex';
        document.getElementById('wrapper_chevrolet').style.display = 'none';
})