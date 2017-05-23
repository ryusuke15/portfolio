$( document ).ready(function() {

    $(".button-collapse").sideNav();
 
    $(".coverTitle").typed({
        strings: ["<h4>Hello! ^500 <br> My name is <br> Ryusuke Lavalla. ^500 <br> Welcome.</h4>" ],
        typeSpeed: 60
    });


    $(window).scroll(function(){
        var position = $(window).scrollTop();
        if (position > $(document).height()*0.14){
            $('.navigation, .btnUp').fadeIn("fast");  
        }
        else{
            $('.navigation, .btnUp').hide("slow")
        }
    });

    $(".naviBtn").each(function(){
        $(this).on("click", function(){ 
            var data = $( this ).find("p").text();
            var location = data.toLowerCase();

            if (location === "explore"){
                location = "about"
            }
            else if (!location){
                location = "top" 
            }
            else {
                location = location
            }

            $('html,body').animate({
                scrollTop: $("."+location).offset().top},
            'slow');

         });


    });

});

