const onglets = document.querySelectorAll('.onglets');
const contenue = document.querySelectorAll('.contenue')  
let index = 0 ;


onglets.forEach(onglet => {

    onglet.addEventListener("click", () => {

        if (onglet.classList.contains('active')) {
            return;
        } else {
            onglet.classList.add('active');
        }

        index = onglet.getAttribute('data-id');
        console.log(index);

        for(i = 0; i < onglets.length; i++) {

            if(onglets[i].getAttribute('data-id') != index) {
              onglets[i].classList.remove('active');  
            }
        }

        for(j=0; j < contenue.length; j++) {

            if(contenue[j].getAttribute('data-id') == index) {
              contenue[j].classList.add('activeContenue');  
            } else{
                contenue[j].classList.remove('activeContenue')
            }
        }


    })
})
