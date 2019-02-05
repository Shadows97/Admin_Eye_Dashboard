var userNombre = $("#equipNombre")[0];



function changeEtat(id){
	$.ajax({
		method :'GET',
		url: 'userNombre',
		success: function(data){
		    console.log(data.userNombre);

		        userNombre.innerHTML = data.userNombre;


		    },
		error: function(){
			console.log("Error....")
		}
	});
}
setInterval(changeEtat,500);