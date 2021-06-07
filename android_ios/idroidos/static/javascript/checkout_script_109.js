{% if first_time_accessed %}
<script type="text/javascript">
  ;(function(p,l,o,w,i,n,g){if(!p[i]){p.GlobalSnowplowNamespace=p.GlobalSnowplowNamespace||[];
  p.GlobalSnowplowNamespace.push(i);p[i]=function(){(p[i].q=p[i].q||[]).push(arguments)
  };p[i].q=p[i].q||[];n=l.createElement(o);g=l.getElementsByTagName(o)[0];n.async=1;
  n.src=w;g.parentNode.insertBefore(n,g)}}
    (window,document,"script","https://d2ft3xf0i1jq1c.cloudfront.net/sp.js","l5plow"));
window.l5plow('newTracker', 'ssc', 'www.pittara.com', { // Initialise a tracker
    appId: '109',
    post: false,
    sessionCookieTimeout: 0,
    cookieDomain: '.pittara.com',
    });
window.l5plow('setUserId', '{{customer.id}}');
  window.l5plow('trackPageView');
window.l5plow('enableLinkClickTracking');
window.l5plow('addTrans',
    '{{order.order_number}}',
    '1',
    '{{order.subtotal_price}}',
    '{{order.tax_price}}',
    '{{order.shipping_price}}',
    '{{order.shipping_address.city}}',
    '{{order.shipping_address.province}}',
    '{{order.shipping_address.country}}',
    '{{shop.currency}}',
);
window.l5plow('trackTrans'); 
</script>
{% endif %}