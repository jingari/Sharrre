jQuery Sharrre Plugin
===

Make your sharing widget!
Sharrre is a jQuery plugin that allows you to create nice widgets sharing for Facebook, Twitter, Google Plus (with PHP script) and more.
More information on [Sharrre] (http://sharrre.com/#demos)

About this fork
===

- Pinterest is now handled without the server-side script.
- The server-side script (previously "sharrre.php") is now made in Python (see sharrre.py).
- The server-side script no longer handles some HTTP response and answer, it just contains an util function `get_count`, it's up to you to integrate it with your favorite Python framework. The URL to your view must be specified in the `urlCurl` option.
- The client-side plugin makes JSONP requests, so the server-side view must handle a `callback` parameter and wrap `get_count` result into a JSONP response.

Usage
===

	$('#sharrre').sharrre({
    share: {
      googlePlus: true,
      facebook: true,
      twitter: true
    },
    url: 'http://sharrre.com'
  });

Example
===
    
  <div id="demo1" data-title="sharrre" data-url="http://sharrre.com" ></div>
  $(document).ready(function(){
    $('#demo1').sharrre({
      share: {
        googlePlus: true,
        facebook: true,
        twitter: true,
        delicious: true
      },
      buttons: {
        googlePlus: {size: 'tall'},
        facebook: {layout: 'box_count'},
        twitter: {count: 'vertical'},
        delicious: {size: 'tall'}
      },
      hover: function(api, options){
        $(api.element).find('.buttons').show();      
      },
      hide: function(api, options){
        $(api.element).find('.buttons').hide();
      }
    });
  });

  See example on [official website] (http://sharrre.com/#demos)
	

Dependencies
===

jQuery 1.7

Author
===

- [Julien Hany](http://hany.fr)
- [Twitter (@_JulienH)](http://twitter.com/_JulienH)
- [Google+](http://plus.google.com/111637545317893682325)
