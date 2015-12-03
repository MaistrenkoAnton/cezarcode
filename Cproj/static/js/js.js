var app = angular.module('myApp', []).config(function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
});

app.controller('myCtrl', function($scope, $http)
{
    $scope.ajax = function(command)
    {
        var req = {
            method: 'GET',
            url: '/',
            params: {text: $scope.text,
                    command: command,
                    code: $scope.code
            }
        }
        var response = $http(req);
            response.success(function(data){$scope.text_deshifr = data.text;});
            response.error(function(){alert('error');});
    }

})