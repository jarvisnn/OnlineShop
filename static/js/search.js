$('#basic-addon1').click(function() {
    window.location = "/products/search/?keyword=" + $("#search-box").val()
});

$("#search-box").keyup(function(event){
    if(event.keyCode == 13){
        $("#basic-addon1").click();
    }
});
