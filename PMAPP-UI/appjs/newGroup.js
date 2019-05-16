angular.module('PMAPP').controller('NewGroupController', ['$http', '$log', '$scope', '$rootScope', '$location','$routeParams',
    function($http, $log, $scope, $rootScope, $location,$routeParams)  {
        var thisCtrl = this;


        this.gname = "";
        this.ownerID= window.person;

       this.createGroup = function(){
            // Build the data object
            var data = {};

            data.gname  = this.gname;
            data.ownerID= this.ownerID;

            // Now create the url with the route to talk with the rest API
            var reqURL = "http://localhost:5000/PhotoMessagingApp/group/create";
            console.log("reqURL: " + reqURL);

            // configuration headers for HTTP request
            var config = {
                headers : {
                    'Content-Type': 'application/json;charset=utf-8;'
                    //'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8;'

                }
            }
            // Now issue the http request to the rest API

            $http.post(reqURL, data, config).then(
                // Success function
                function (response) {
                    console.log("data: " + JSON.stringify(response.data));
                    // tira un mensaje en un alert
                   alert("New Group Created: " + response.data.Groups);
                    $location.url('/groups');
                }, //Error function
                function (response) {
                    // This is the error function
                    // If we get here, some error occurred.
                    // Verify which was the cause and show an alert.
                    var status = response.status;
                    //console.log("Error: " + reqURL);
                    //alert("Cristo");
                    if (status == 0) {
                        alert("No hay conexion a Internet");
                    }
                    else if (status == 401) {
                        alert("Su sesion expiro. Conectese de nuevo.");
                    }
                    else if (status == 403) {
                        alert("No esta autorizado a usar el sistema.");
                    }
                    else if (status == 404) {
                        alert("No se encontro la informacion solicitada.");
                    }
                    else {
                        alert("Error interno del sistema.");
                    }
                }
            );
        };
        this.viewChats = function(){
            $location.url('/chat');
        };

        this.back= function(){
            $location.url('/groups');
        };

        this.showLikes =function(mid){
            $location.url('/likes/'+ mid);
        };
        this.showDislikes =function(mid){
            $location.url('/dislikes/'+mid);
        };



        //this.getLikes();

}]);
