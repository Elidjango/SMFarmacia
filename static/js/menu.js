${".submenu"}.click(function(){
	${this}.children("ul").slideToggle(slow/400/fast);
})

${"ul"}.click(function(p){
	p.stopPropagation
})