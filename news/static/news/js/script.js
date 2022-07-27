"use strict"

const isMobile = {
    Android: function () {
        return navigator.userAgent.match(/Android/i);
    },
    iOS: function () {
        return navigator.userAgent.match(/iPhone|iPad/i);
    },
    
    any: function () {
        return (
            isMobile.Android() ||
            isMobile.iOS());
        
    }
};


$(document).ready(function(){
    $('.header__burger').click(function(event){
        $('.header__burger,.header__menu').toggleClass('active');
        $('body').toggleClass('lock');
    });
});
const iconMenu = document.querySelector('.menu__icon');
if(iconMenu) {
    const menuBody = document.querySelector('.menu__body');
    iconMenu.addEventListener("click", function(e) {
        iconMenu.classList.toggle('_active');
        menuBody.classList.toggle('_active');
    });
}