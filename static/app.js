var app = angular.module("app", ["ui.bootstrap"], function(){});

app.controller("MainCtl", function($scope, $http){
	$http({
		method: "GET",
		url: "/get"
	}).success(function(data){
		$scope.equations = data;
	}).error(function(error){
		alert("FAILED TO LOAD");
		console.log(error);
	});

	$scope.asc = {
		value: "",
		op: "add",
		side: "l"
	};

	$scope.chop = function(v){
		$scope.op = v;
	};

	$scope.chside = function(v){
		$scope.side = v;
	};

	$scope.execute = function() {
		var q = $http({
			method: "POST",
			url: "/step",
			data: {
				op: $scope.asc.op,
				side: $scope.asc.side,
				value: $scope.asc.value
			}
		});
		q.success(function(data){
			$scope.equations = data;
		});
		q.error(function(error){
			alert("check console for error");
			console.log(error);
		});
	}
});
