(function( $ ){

  $.fn.headerIndex = function() {
    // TODO add exclude option to exclude headings , e.g. h1
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
    this.headerIndexCreate(headings);
  };

  $.fn.headerIndexCreate = function(headings) {
    this.prepend('<div id="headerIndex"></div>');
    var HTML = '<ul>';
    for (h in headings) {
      var tag = headings[h].tag;
      var content = headings[h].content;
      HTML += '<li class="headerIndex' + tag + '"><a href="#' + h + '">' + content + '</li>';
    }
    HTML += '</ul>';
    $('#headerIndex').html(HTML);
  };
})( jQuery );
