const onglet = document.querySelectorAll('.onglet');
const contenu = document.querySelectorAll('.contenu')  
let index = 0 ;


onglet.forEach(ongle => {

    ongle.addEventListener("click", () => {

        if (ongle.classList.contains('activ')) {
            return;
        } else {
            ongle.classList.add('activ');
        }

        index = ongle.getAttribute('data-anim');
        console.log(index);

        for(i = 0; i < onglet.length; i++) {

            if(onglet[i].getAttribute('data-anim') != index) {
              onglet[i].classList.remove('activ');  
            }
        }

        for(j=0; j < contenu.length; j++) {

            if(contenu[j].getAttribute('data-anim') == index) {
              contenu[j].classList.add('activContenu');  
            } else{
                contenu[j].classList.remove('activContenu')
            }
        }


    })
})