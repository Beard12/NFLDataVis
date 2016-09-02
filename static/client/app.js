var app = angular.module('app', ['ngMaterial', 'ngRoute']);
app.config(function($routeProvider){
$routeProvider
	.when('/', {
			templateUrl: 'static/client/partials/home.html',
			controller: 'homeController'
	})
	.when('/toppassers', {
		templateUrl: 'static/client/partials/passing.html',
		controller: 'homeController'
	})
	.when('/rushvspass', {
		templateUrl: 'static/client/partials/rushvspass.html', 
		controller: 'homeController'
	})
	.when('/players', {
		templateUrl: 'static/client/partials/playersover.html', 
		controller: 'homeController'
	})
});