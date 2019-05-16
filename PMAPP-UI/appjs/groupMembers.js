
angular.module('PMAPP').controller('GroupMembersController', ['$http', '$log', '$scope', '$rootScope', '$location','$routeParams',
    function($http, $log, $scope, $rootScope, $location,$routeParams) {
        var thisCtrl = this;

        this.membersList = [];
        this.counter  = 2;
        this.newText = "";
        $rootScope.prueba = "";
        this.viewGroupMembers = function(){
            // Get the list of parts from the servers via REST API
            var gid = $routeParams.gid;
            // First set up the url for the route
            var url = "http://localhost:5000/PhotoMessagingApp/home/groups/"+gid+"/members";

            // Now set up the $http object
            // It has two function call backs, one for success and one for error
            $http.get(url).then(// success call back
                function (response){
                // The is the sucess function!
                // Copy the list of parts in the data variable
                // into the list of parts in the controller.

                    console.log("response: " + JSON.stringify(response));

                    thisCtrl.membersList = response.data.Members;
                    $rootScope.prueba = "Probando";
            }, // error callback
            function (response){
                // This is the error function
                // If we get here, some error occurred.
                // Verify which was the cause and show an alert.
                console.log("Err response: " + JSON.stringify(response));

                var status = response.status;
                if (status == 0){
                    alert("No hay conexion a Internet");
                }
                else if (status == 401){
                    alert("Su sesion expiro. Conectese de nuevo.");
                }
                else if (status == 403){
                    alert("No esta autorizado a usar el sistema.");
                }
                else if (status == 404){
                    alert("No se encontro la informacion solicitada.");
                }
                else {
                    alert("Error interno del sistema.");
                }
            });

            $log.error("Users Loaded: ", JSON.stringify(thisCtrl.membersList));
        };

        this.deleteMember = function(member){
            // Get the target part id from the parameter in the url
            // using the $routerParams object



            // Now create the url with the route to talk with the rest API
            var reqURL = "http://localhost:5000/PhotoMessagingApp/deleteMember/"+$routeParams.gid+"/"+member;
            console.log("reqURL: " + reqURL);

                        var config = {
                        headers : {
                        'Content-Type': 'application/json;charset=utf-8;'
                    //'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8;'

                                    }
                                        }


            // Now issue the http request to the rest API
            $http.delete(reqURL,config).then(
                // Success function
                function (response) {
                    console.log("data: " + JSON.stringify(response.data));
                    // assing the part details to the variable in the controller
                    console.log("Miembro borrado: " + $rootScope.prueba);
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
        this.partDetails = function (pid) {
            $location.url('/partsdetails/' + pid);
        };
        // got to screen to add new parts
        this.viewContacts = function(uid){
            $location.url('/contacts/'+uid);
        };

        this.viewInfo= function (uid) {
            $location.url('/userInfo/' + uid);

        };
        this.viewGroupMembers();

}]);
