var app = angular.module('myApp', []);

app.controller('formCtrl', function($scope){
    if ($scope.password1 === $scope.password2){
        $scope.ok = false;
    }else{
        $scope.ok = true;
    }
});