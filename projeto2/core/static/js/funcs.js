function soNumero(evt) {
    var ASCIICode = (evt.which) ? evt.which : evt.keyCode
    if (ASCIICode > 31 && (ASCIICode < 48 || ASCIICode > 57))
    return false;
return true;
}

$(document).keypress(
    function(event){
      if (event.which == '13') {
        event.preventDefault();
      }
  });

  $('body').on('keydown', 'input, select', function(e) {
    if (e.key === "Enter") {
        var self = $(this), form = self.parents('form:eq(0)'), focusable, next;
        focusable = form.find('input,a,select,button,textarea').filter(':visible');
        next = focusable.eq(focusable.index(this)+1);
        if (next.length) {
            next.focus();
        } else {
            form.submit();
        }
        return false;
    }
});

var m = document.getElementsByClassName("alert");  // Return an array

setTimeout(function(){
   if (m && m.length) {
       m[0].classList.add('hide');
   }
}, 3000);