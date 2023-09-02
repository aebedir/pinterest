const FuncitonList = function () {
   
    const navSlide = function () {
       const navs = document.querySelectorAll(".slider-button");
       const contents = document.querySelectorAll(".slider-content");
       navs.forEach(nav => {
        nav.addEventListener("click", function (e) {   
            var activeContent = document.getElementsByClassName("active");
            var activeStep = document.getElementsByClassName("activeStep");

            activeStep[0].style.backgroundColor =  "rgb(225, 225, 225)";
            activeContent[0].classList.remove("active");
            activeStep[0].classList.remove("activeStep");
            e.target.classList.add("activeStep");

            var navClass = Array.from(e.target.classList);
            var slideIndex = navClass.find(o => o.match(/step.*/));
            slideIndex = slideIndex.replace("step", "");

            contents.forEach(c => {
                var contentClasses = Array.from(c.classList);
                if(contentClasses.includes("content"+slideIndex)){
                    c.classList.add("active");
                    e.target.style.backgroundColor  = window.getComputedStyle(c).getPropertyValue("color");
                }
            });
           
         });
       });
    }

    const navSlideAuto = function () {
       let sliderUl = document.getElementsByClassName("slider-ul");
       var activeStep = document.getElementsByClassName("activeStep");
       var navClass = Array.from(activeStep[0].classList);
       var slideIndex = navClass.find(o => o.match(/step.*/));
       slideIndex = slideIndex.replace("step", "");
       if(slideIndex == 4){
        activeStep[0].style.backgroundColor =  "rgb(225, 225, 225)";
        sliderUl[0].firstElementChild.classList.add('activeStep');
        sliderUl[0].firstElementChild.click();
       }else{
         activeStep[0].nextElementSibling.click();
       }
      
    };

    var initSlide = function () {
       navSlide();
    };
    var initSlideAuto = function () {
        navSlideAuto();
     };
    return {
       "initSlide": initSlide,
       "initSlideAuto" : initSlideAuto
    };
 }();

 $(document).ready(function () {
    FuncitonList.initSlide();
    setInterval(FuncitonList.initSlideAuto,3000);
 });