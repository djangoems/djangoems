$(document).ready(function(){

	$(document).mouseup(function(e) 
	{

		var container = $("#master-tools");

		$("#avatar-div").click(function(){

			container.toggle();

		});

	    // if the target of the click isn't the container nor a descendant of the container
	    if (container.has(e.target).length === 0) 
	    {
	        container.css({'display':'none'});
	    }
	  
	});

});