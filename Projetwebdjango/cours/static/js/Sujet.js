const onglets = document.querySelectorAll('.onglets');
const contenu1 = document.querySelectorAll('.contenu1')  
let index1 = 0 ;

const onglet = document.querySelectorAll('.onglet');
const contenu2 = document.querySelectorAll('.contenu2')  
let index2 = 0 ;


onglets.forEach(onglet1 => {

    onglet1.addEventListener("click", () => {

        if (onglet1.classList.contains('active1')) {
            return;
        } else {
            onglet1.classList.add('active1');
        }

        index1 = onglet1.getAttribute('data-anim');
        console.log(index1);

        for(i = 0; i < onglets.length; i++) {

            if(onglets[i].getAttribute('data-anim') != index1) {
              onglets[i].classList.remove('active1');  
            }
        }

        for(j=0; j < contenu1.length; j++) {

            if(contenu1[j].getAttribute('data-anim') == index1) {
                contenu1[j].classList.add('activeContenu1');  
            } else{
                contenu1[j].classList.remove('activeContenu1')
            }


            
            if(contenu1[j].getAttribute('data-anim') == 3) {
                onglet.style.display ='none'
            }
        }


    })
})



onglet.forEach(onglet2 => {

    onglet2.addEventListener("click", () => {

        if (onglet2.classList.contains('active')) {
            return;
        } else {
            onglet2.classList.add('active');
        }

        index2 = onglet2.getAttribute('data-id');
        console.log(index2);

        for(i = 0; i < onglet.length; i++) {

            if(onglet[i].getAttribute('data-id') != index2) {
              onglet[i].classList.remove('active');  
            }
        }

        for(j=0; j < contenu2.length; j++) {

            if(contenu2[j].getAttribute('data-id') == index2) {
                contenu2[j].classList.add('activeContenu2');  
            } else{
                contenu2[j].classList.remove('activeContenu2')
            }
        }


    })
})
