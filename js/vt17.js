(function(){ // scoping

    var hash = window.location.hash.slice(1)

    var collapsable = []

    $('main h1.collapse-trigger').each(function() {
	var handle = $(this);
	collapsable.push(handle);
	var group = handle.nextUntil('h1').wrapAll('<section></section>').end().next();
	var id = handle.attr('id');
	if( (id != undefined && id == hash) ){ handle.addClass('open'); }
	handle.on('click',function(){ handle.toggleClass('open'); return false; });
    });


    if(collapsable.length > 1){
	console.log(collapsable);
	$('<span class="collapse-menu">[Expand all]</span>').prependTo('main').on('click',function(){
	    for (var i = 0; i < collapsable.length; i++) { collapsable[i].addClass('open'); }
	});
	$('<span class="collapse-menu">[Collapse all]</span>').prependTo('main').on('click',function(){
	    for (var i = 0; i < collapsable.length; i++) { collapsable[i].removeClass('open'); }
	});
	
    }


})()
