angular.module('PMAPP').controller('GroupsController', ['$http', '$log', '$scope', '$rootScope', '$location',
    function($http, $log, $scope, $rootScope, $location)  {
        var thisCtrl = this;

        this.groupList = [];
        this.counter  = 2;
        this.newText = "";
        $rootScope.prueba = "";


           this.loadGroups = function(){
            // Get the list of parts from the servers via REST API

            // First set up the url for the route
            var url = "http://localhost:5000/PhotoMessagingApp/home/mygroups/"+window.person;

            // Now set up the $http object
            // It has two function call backs, one for success and one for error
            $http.get(url).then(// success call back
                function (response){
                // The is the sucess function!
                // Copy the list of parts in the data variable
                // into the list of parts in the controller.

                    console.log("response: " + JSON.stringify(response));

                    thisCtrl.groupList = response.data.Groups;
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

            $log.error("Messages Loaded: ", JSON.stringify(thisCtrl.chatList));
        };


        this.postMsg = function(){
            var msg = thisCtrl.newText;
            // Need to figure out who I am
            var author = "Me";
            var nextId = thisCtrl.counter++;
            thisCtrl.messageList.unshift({"id": nextId, "text" : msg, "author" : author, "like" : 0, "nolike" : 0});
            thisCtrl.newText = "";
        };

        this.delete = function(gid,uid){
            // Get the target part id from the parameter in the url
            // using the $routerParams object


            if(uid!= window.person){
                alert("YOU DO NOT OWN THIS GROUP")
            }else{
            // Now create the url with the route to talk with the rest API
            var reqURL = "http://localhost:5000/PhotoMessagingApp/deleteGroup/"+gid;
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
                    console.log("Grupo Borrado: " + $rootScope.prueba);
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
        }};

        this.viewChats = function(){
            $location.url('/chat');
        };
        this.viewMembers = function(gid){
            $location.url('/groupMembers/'+ gid);
        };

        this.addMember = function(gid){
            $location.url('/addMember/'+ gid);
        };
        this.viewMBG = function(gid){
            $location.url('/messagesByGroup/'+ gid);
        };
        this.createGroup =function(){
            $location.url('/newGroup');
        };


        this.loadGroups();
}]);
