(function( $ ){

  $.fn.headerIndex = function() {
    // TODO add sticky option to move with the page when scrolled
    var headings = {};
    $(":header").each(function(index, element){
      var id = '';
      if ('undefined' !== typeof $(element).attr('id')) {
        id = $(element).attr('id');
      } else {
        id = 'headerIndex' + index;
        $(element).attr('id', id);
      }
      if ('undefined' === typeof $(element).attr('name')) {
        $(element).attr('name', id);
      }
      headings[id] = {
          'content': $(element).html(),
          'tag': element.nodeName
      };
    });
console.log(headings);
  };
})( jQuery );