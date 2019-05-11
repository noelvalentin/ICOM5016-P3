
angular.module('PMAPP').controller('WelcomeController', ['$http', '$log', '$scope', '$rootScope', '$location',
    function($http, $log, $scope, $rootScope, $location) {

        // got to screen to add new parts
        this.continue = function(){

            $location.url('/home');
        };



}]);
