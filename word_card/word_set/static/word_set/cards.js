// 翻轉效果
let card = document.getElementsByClassName('card-wrapper');
console.log(card);
for(let i = 0 ; i < card.length; i++){
    card[i].addEventListener("click", function(){
        console.log(this.firstElementChild);
        let carBack = this.firstElementChild.classList;
        let carFront = this.lastElementChild.classList;
        console.log(carBack);
        if (carBack.contains('card-back_flip')){
            carBack.remove('card-back_flip');
        } else{
            carBack.add('card-back_flip');
        }
        if (carFront.contains('card-front_flip')){
            carFront.remove('card-front_flip');
        } else{
            carFront.add('card-front_flip');
        }
    })
}
// 卡片切換效果
$(document).ready(function(){

var $cards = $('.Offercards .cards'),
    zIn = $cards.length,
    newzIn = 0,
    mt = -2,
    ml = -11,
    scale = 1,
    cnt = 0,
    newScale = 0.8;

function forIndex(){
    $($cards).each(function(){
        zIn--;
        $(this).css({'z-index': zIn});
    });
}
forIndex();

function forEach(){
    $($cards).each(function(){
        mt+=2;
        ml+=11;
        scale-=0.05;
        $(this).css({'margin': ''+ mt +'px 0 0 '+ ml +'px', 'transform': 'scale('+ scale +')'});
    });
}
forEach();

$('.cardBtn').click(function(){
    var btnCard = $(this).closest('.cards');
    $(btnCard).css({'transform': 'translate3d(200px,0,0) rotate(15deg)'}).removeClass('active').next().css({'transform': 'scale(0.94)', 'margin': 0}).addClass('active');
    cnt++;
    newScale+=0.04;
    newzIn-=1;;
    setTimeout(()=>{
        $(btnCard).fadeOut(200, function(){
            setTimeout(()=>{
                $(btnCard).css({'transform': 'scale('+ newScale +')', 'z-index': newzIn});
                setTimeout(()=>{
                    $(btnCard).show();
                }, 400)
            }, 150);
            if(cnt >= $cards.length){
                cnt = 0;
                $($cards).first().css({'transform':'scale(0.94)'}).addClass('active');
                zIn = $cards.length;
                mt = -2;
                ml = -11;
                newScale = 0.8;
                newzIn = 0;
                scale = 1;
                forIndex();
                forEach();
            }
        });
    }, 100);
});
});

// 改變completed

    var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    // 設定token
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
    // 送出request的方法
    function toggle_completed(id){
        let btn = $('#' + id)
        $.ajax({
            type: 'POST',   
            url: '/word/' + id + '/update/',
            data: JSON.stringify({'status': status}),
        }).done(function(value) {
            if (value.msg === 'True'){
                btn.html('<img src="https://img.icons8.com/metro/24/000000/checked.png"/>')
            }
            else{
                btn.html('<img src="https://img.icons8.com/material-two-tone/24/000000/circled.png"/> ')
            }

                
        })
    }
    