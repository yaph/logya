(function( $ ){

  $.fn.headerIndex = function(options) {
    var headings = {};

    var settings = $.extend({
      'exclude': [],
      'topLink': false,
      'topLinkText': 'Top'
    }, options);

    $(':header').each(function(index, element){
      // make sure tag is not excluded
      if (-1 !== settings.exclude.indexOf(element.nodeName.toLowerCase()))
        return true;
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

    // make sure there are headings in the index
    if (Object.keys(headings).length)
      this.headerIndexCreate(headings, settings);
  };

  $.fn.headerIndexCreate = function(headings, settings) {
    this.prepend('<div id="headerIndex"></div>');
    var HTML = '<ul>';
    if (settings.topLink) {
      HTML += '<li class="headerIndexTop"><a href="#">' + settings.topLinkText + '</a></li>';
    }
    for (h in headings) {
      var tag = headings[h].tag;
      var content = headings[h].content;
      HTML += '<li class="headerIndex' + tag + '"><a href="#' + h + '">' + content + '</li>';
    }
    HTML += '</ul>';
    $('#headerIndex').html(HTML);
  };
})( jQuery );