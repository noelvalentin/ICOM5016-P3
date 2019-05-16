angular.module('PMAPP').controller('MessagesByGroupController', ['$http', '$log', '$scope', '$rootScope', '$location','$routeParams',
    function($http, $log, $scope, $rootScope, $location,$routeParams) {
        var thisCtrl = this;

        this.mbgList = [];
        this.counter  = 2;
        this.newText = "";
        this.image="";
        this.text="";
        this.gid=$routeParams.gid;
        this.oid=null;
        this.likes=[];
        this.dislikes=[];


           this.loadMessages = function(){
            // Get the list of parts from the servers via REST API
            var  gid = $routeParams.gid;
            // First set up the url for the route
            var url = "http://localhost:5000/PhotoMessagingApp/home/groups/"+this.gid+"/messages";

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
             for(let i=0; i<100;i++){
        this.likes[i] = this.getLikes(i);
        this.dislikes[i]=this.getDislikes(i);
        }

            $log.error("Messages Loaded: ", JSON.stringify(thisCtrl.chatList));
        };

        this.postMsg = function(){
            var msg = thisCtrl.newText;
            var tags={};

           function getHashTags(inputText) {
            var regex = /(?:^|\s)(?:#)([a-zA-Z\d]+)/gm;
            var matches = [];
            var match;

            while ((match = regex.exec(inputText))) {
                matches.push(match[1]);
                }

                    return matches
}
            // Need to figure out who I am
            tags=getHashTags(this.text);
           console.log(tags)
            var author = "Me";
            thisCtrl.mbgList.unshift({"id": window.person, "text" : msg, "author" : author, "like" : 0, "nolike" : 0});


            // First set up the url for the route
           var data = {};
            data.image = this.image;
            data.text = this.text;
            data.uid  = window.person;
            data.gid=this.gid;
            data.oid = this.oid;

            // Now create the url with the route to talk with the rest API
            var reqURL = "http://localhost:5000/PhotoMessagingApp/postToGroup";
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
                    console.log("Hash created" );

                    for( i in tags) {
                        console.log(tags[i]);
                       thisCtrl.hashtag(tags[i])
                    }


                    thisCtrl.mbgList.unshift({"date":"","first_name":"Me","image":"","mid": data.text,"text": data.text,"uid":window.person});
                //$location.url('/messagesByGroup/'+ $routeParams.gid);
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

            $log.error("Messages Loaded: ", JSON.stringify(thisCtrl.chatList))





            thisCtrl.newText = "";
        };
        this.getLikes =function(value){
            var mid = value;



            var url2 = "http://localhost:5000/PhotoMessagingApp/home/messages/"+mid+"/likes";


            // Now set up the $http object
            // It has two function call backs, one for success and one for error
            $http.get(url2).then(// success call back
                function (response){
                // The is the sucess function!
                // Copy the list of parts in the data variable
                // into the list of parts in the controller.

                    console.log("response: " + JSON.stringify(response));

                    thisCtrl.likes[mid] = response.data.Likes;
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
        this.getDislikes =function(value){
            var mid = value;



            var url2 = "http://localhost:5000/PhotoMessagingApp/home/messages/"+mid+"/dislikes";


            // Now set up the $http object
            // It has two function call backs, one for success and one for error
            $http.get(url2).then(// success call back
                function (response){
                // The is the sucess function!
                // Copy the list of parts in the data variable
                // into the list of parts in the controller.

                    console.log("response: " + JSON.stringify(response));

                    thisCtrl.dislikes[mid] = response.data.Dislikes;
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

        this.like = function(mid){
            // Need to figure out who I am

            // First set up the url for the route
           var data = {};

            data.uid=window.person;
            data.mid = mid;

            // Now create the url with the route to talk with the rest API
            var reqURL = "http://localhost:5000/PhotoMessagingApp/likeMessage";
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
                    alert("Message Liked" );
                //$location.url('/messagesByGroup/'+ $routeParams.gid);
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

            $log.error("Messages Liked: ");




        };
        this.dislike = function(mid){
            // Need to figure out who I am

            // First set up the url for the route
           var data = {};

            data.uid=window.person;
            data.mid = mid;

            // Now create the url with the route to talk with the rest API
            var reqURL = "http://localhost:5000/PhotoMessagingApp/dislikeMessage";
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
                    alert("Message Disliked" );
                //$location.url('/messagesByGroup/'+ $routeParams.gid);
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

            $log.error("Messages Liked: ");




        };
        this.hashtag = function(tag){
            // Build the data object
            var data = {};
            data.tag = tag;


            // Now create the url with the route to talk with the rest API
            var reqURL = "http://localhost:5000/PhotoMessagingApp/createHashtag";
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
                    console.log("success")

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

        this.viewReplies = function(oid){
            $location.url('/chat/'+oid);
        };
        this.showdetails =function(){
            $location.url('/postDetails');
        };

        this.showLikes= function(mid){
              $location.url('/likes/'+mid);
        };

        this.showDislikes= function(mid){
              $location.url('/dislikes/'+mid);
        };



        this.loadMessages();
}]);
