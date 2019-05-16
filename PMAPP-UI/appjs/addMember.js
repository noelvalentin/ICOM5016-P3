angular.module('PMAPP').controller('AddMemberController', ['$http', '$log', '$scope', '$rootScope', '$location', '$routeParams',
    function($http, $log, $scope, $rootScope, $location, $routeParams) {
        // This variable lets you access this controller
        // from within the callbacks of the $http object

        var thisCtrl = this;
        this.uid="";
        this.gid=$routeParams;

        var contactsList = {};


        this.loadContacts = function(){
            // Get the target part id from the parameter in the url
            // using the $routerParams object
            var uId = $routeParams.uid;

            // Now create the url with the route to talk with the rest API
            var reqURL = "http://localhost:5000/PhotoMessagingApp/home/users/" + window.person+"/contacts";
            console.log("reqURL: " + reqURL);
            // Now issue the http request to the rest API
            $http.get(reqURL).then(
                // Success function
                function (response) {
                    console.log("data: " + JSON.stringify(response.data));
                    // assing the part details to the variable in the controller
                    thisCtrl.contactsList = response.data.Contacts;
                    console.log("La prueba: " + $rootScope.prueba);
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

        this.addMember = function(uid){
            // Build the data object
            this.uid=uid;
            var data = {};
            data.uid = this.uid;
            data.gid = this.gid;
            data.gid=data.gid.gid;

            console.log(this.gid)
            console.log(data.gid)
            console.log(data.uid)

            // Now create the url with the route to talk with the rest API
            var reqURL = "http://localhost:5000/PhotoMessagingApp/addMember";
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
                    alert("Usuario agregado al grupo ");
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

        this.userDetails = function (uid) {
            $location.url('/userInfo/' + uid);
        };


        this.addContact = function () {
            $location.url('/addContact');
        };

        this.loadContacts();
}]);