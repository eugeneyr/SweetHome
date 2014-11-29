var lifeServiceModule = angular.module('LifeService', []);

lifeServiceModule.provider('Cells', { $get: function () {
    var svc = {};
    svc.getCells = function() {
        return [];
    };
    return svc;
}});

