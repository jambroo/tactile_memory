var word = null
$('.submit').on('click', function(){
  word = $("#password").val()
  $("#enter").addClass("fadeout")
  console.log($("#enter"))
})

/*shakevar $formContainer = $('.form-container');
$formContainer.addClass('invalid');
setTimeout(function(){
  $formContainer.removeClass('invalid');
},500);
*/
