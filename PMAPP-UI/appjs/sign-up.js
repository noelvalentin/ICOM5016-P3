angular.module('PMAPP').controller('SignUpController', ['$http', '$log', '$scope', '$rootScope', '$location','$routeParams',
    function($http, $log, $scope, $rootScope, $location,$routeParams)  {
        var thisCtrl = this;


        this.counter  = 2;

        this.point=0;
        this.dislikes=[];
        this.email = "";
        this.password = "";
        this.phone = "";
        this.first_name = "";
        this.last_name = "";




       this.createUser = function(){
            // Build the data object
            var data = {};
            data.email = this.email;
            data.password = this.password;
            data.phone = this.phone;
            data.first_name  = this.first_name;
            data.last_name=this.last_name;

            // Now create the url with the route to talk with the rest API
            var reqURL = "http://localhost:5000/PhotoMessagingApp/signup";
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
                    alert("New user added with id: " + response.data.User);
                    $location.url('/users');
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



        this.showLikes =function(mid){
            $location.url('/likes/'+ mid);
        };
        this.showDislikes =function(mid){
            $location.url('/dislikes/'+mid);
        };



        //this.getLikes();

}]);
