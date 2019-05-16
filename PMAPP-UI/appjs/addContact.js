angular.module('PMAPP').controller('AddContactController', ['$http', '$log', '$scope', '$rootScope', '$location','$routeParams',
    function($http, $log, $scope, $rootScope, $location,$routeParams)  {
        var thisCtrl = this;


        this.first_name = "";
        this.last_name="";
        this.target ="";
        this.uid = window.person;


       this.addContact = function(){
            // Build the data object
           var sel = document.getElementById('s');
            var data = {};
            data.uid = this.uid;
            data.first_name  = this.first_name;
            data.last_name= this.last_name;


             function getSelectedOption(sel) {
        var opt;
        for ( var i = 0, len = sel.options.length; i < len; i++ ) {
            opt = sel.options[i];
            if ( opt.selected === true ) {
                break;
            }
        }
        return opt.value;}

        var x = getSelectedOption(sel);
             console.log(x);

            if(x == "email"){
            // Now create the url with the route to talk with the rest API
                //If email is the option use this route.
                data.email = this.target;

                 var reqURL = "http://localhost:5000/PhotoMessagingApp/addByEmail";}

            else {

                data.phone = this.target;

                var reqURL = "http://localhost:5000/PhotoMessagingApp/addByPhone";

            }
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
                   alert("User Added To Contact List " );
                   $location.url('/contacts/' + window.person);

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
