function ping(){
	$.ajax({
		method :'GET',
		url: 'ping',
		success: function(data){
		    console.log("succes");

		},
		error: function(){
			console.log("Error....")
		}
	});
}

setInterval(ping,1000);