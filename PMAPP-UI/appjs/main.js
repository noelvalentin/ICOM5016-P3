
(function() {

    var app = angular.module('PMAPP',['ngRoute']);

    app.config(['$routeProvider', '$locationProvider', function ($routeProvider, $locationProvider, $location) {
        $routeProvider.when('/login', {
            templateUrl: 'pages/login.html',
            controller: 'LoginController',
            controllerAs : 'loginCtrl'
        }).when('/signup', {
            templateUrl: 'pages/sign-up.html',
           controller: 'SignUpController',
           controllerAs : 'signUpCtrl'
        }).when('/chat', {
            templateUrl: 'pages/chat.html',
            controller: 'ChatController',
            controllerAs : 'chatCtrl'
        }).when('/home', {

           controller: 'HomeController',
           controllerAs : 'homeCtrl' ,
            templateUrl: 'pages/home.html'
        }).when('/users', {
            templateUrl: 'pages/users.html',
           controller: 'UsersController',
           controllerAs : 'usersCtrl'
        }).when('/groups', {
            templateUrl: 'pages/groups.html',
           controller: 'GroupsController',
           controllerAs : 'groupsCtrl'
        }).when('/groupMembers/:gid', {
            templateUrl: 'pages/groupMembers.html',
           controller: 'GroupMembersController',
           controllerAs : 'gMembersCtrl'
        }).when('/contacts/:uid', {
            templateUrl: 'pages/contacts.html',
           controller: 'ContactsController',
           controllerAs : 'contactsCtrl'
        }).when('/messagesByGroup/:gid', {
            templateUrl: 'pages/messagesByGroup.html',
           controller: 'MessagesByGroupController',
           controllerAs : 'mbgCtrl'
        }).when('/likes/:mid', {
            templateUrl: 'pages/likes.html',
           controller: 'LikesController',
           controllerAs : 'likesCtrl'
        }).when('/dislikes/:mid', {
            templateUrl: 'pages/dislikes.html',
           controller: 'DislikesController',
           controllerAs : 'dislikesCtrl'
        }).when('/userInfo/:uid', {
            templateUrl: 'pages/userInfo.html',
            controller: 'UserInfoController',
            controllerAs : 'userInfoCtrl'
        }).when('/newGroup', {
            templateUrl: 'pages/newGroup.html',
            controller: 'NewGroupController',
            controllerAs : 'newGroupCtrl'
        }).when('/addContact', {
            templateUrl: 'pages/addContact.html',
            controller: 'AddContactController',
            controllerAs : 'addContactCtrl'
        }).when('/welcome', {
            templateUrl: 'pages/welcome.html',
            controller: 'WelcomeController',
            controllerAs : 'welcomeCtrl'
        }).otherwise({
            redirectTo: '/login'
        });
    }]);

})();

