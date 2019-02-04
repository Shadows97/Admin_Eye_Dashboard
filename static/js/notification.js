//console.log("Hello Ajax");

$("document").ready(function () {

    // A modifier et recupérer directement le nombre dans le controlleur
    var element = $("#notif")[0];
    //console.log(element);

    function appelAjax() {
        $.ajax({
            type: 'get',
            url: 'notification/nombre',
            beforeSend: function(){
                console.log("Début Ajax");
            },
            success: function (data) {
                $nbre = parseInt(data.nombre);

                if($nbre !== 0){
                    element.innerHTML=$nbre;
                    console.log("Cool! Modification effectuée");
                }else{
                    console.log("Oups! Rien pour le moment, je me repose");
                }

            }
        });
    }

  setInterval(appelAjax,5000);
});
