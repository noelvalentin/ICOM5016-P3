angular.module('PMAPP').controller('MessagesByGroupController', ['$http', '$log', '$scope', '$rootScope', '$location','$routeParams',
    function($http, $log, $scope, $rootScope, $location,$routeParams) {
        var thisCtrl = this;

        this.mbgList = [];
        this.counter  = 2;
        this.newText = "";


           this.loadMessages = function(){
            // Get the list of parts from the servers via REST API
            var  gid = $routeParams.gid;
            // First set up the url for the route
            var url = "http://localhost:5000/PhotoMessagingApp/home/groups/"+gid+"/messages";

            // Now set up the $http object
            // It has two function call backs, one for success and one for error
            $http.get(url).then(// success call back
                function (response){
                // The is the sucess function!
                // Copy the list of parts in the data variable
                // into the list of parts in the controller.

                    console.log("response: " + JSON.stringify(response));

                    thisCtrl.mbgList = response.data.Messages;
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
        this.viewChats = function(){
            $location.url('/chat');
        };
        this.showdetails =function(){
            $location.url('/postDetails');
        };

        this.showLikes= function(){
              $location.url('/likes');
        };

        this.showDislikes= function(){
              $location.url('/dislikes');
        };

        this.loadMessages();
}]);
