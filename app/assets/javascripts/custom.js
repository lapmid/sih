// debugger;
console.log("hi"); 
$(document).on("page:fetch", function(){
   console.log("load"); 
});
  
$(document).on("page:receive", function(){
    console.log("done");
});
$(document).on('click', function() {
    $("#overlay").show();
});
$(document).on('turbolinks:click', function() {
    $("#overlay").show();
});
  
$(document).on('turbolinks:load', function() {
    $("#overlay").hide();
});