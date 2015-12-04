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
                    code: $scope.code,
                    label: $scope.label
            }
        }
        var response = $http(req);
            response.success(function(data){
                $scope.text_deshifr = data.text;
            });
            response.error(function(){alert('Неверный формат введенных данных');});
    }
})
function func() {


    data = document.getElementById('id_shifr').value;
    labels = [];
    values = []
    for(var i=0; i < data.length; i++)
    {
        if(data.substring(i+1, data.length).indexOf(data[i])==-1) {
            labels.push(data[i]);
            values.push(data.split(data[i]).length - 1);
        }

    }
        var options = {
            chart: {
                renderTo: 'container',
                type: 'column',
                margin: 75,
                options3d: {
                    enabled: true,
                    alpha: 15,
                    beta: 15,
                    depth: 50,
                    viewDistance: 25
                }
            },
            title: {
                text: 'Количество введенных символов'
            },
            subtitle: {
                text: 'Для поворота используйте слайдеры снизу графика'
            },
            plotOptions: {
                column: {
                    depth: 100
                }
            },
            xAxis: {
            categories: labels
            },
            series: [{
                data: values
            }]
        };
        chart = new Highcharts.Chart(options);
        function showValues() {
            $('#R0-value').html(chart.options.chart.options3d.alpha);
            $('#R1-value').html(chart.options.chart.options3d.beta);
        }

        // Activate the sliders
        $('#R0').on('change', function () {
            chart.options.chart.options3d.alpha = this.value;
            showValues();
            chart.redraw(false);
        });
        $('#R1').on('change', function () {
            chart.options.chart.options3d.beta = this.value;
            showValues();
            chart.redraw(false);
        });

        showValues(data);

        if(!is_text(labels, values))
        {
            document.getElementById('message').innerHTML = 'Сложно сказать на текст не похоже';
            document.getElementById('message').style.backgroundColor = 'red';
        }
        else {
            document.getElementById('message').innerHTML = 'Похоже на текст';
            document.getElementById('message').style.backgroundColor = 'green';
        }



}
function is_text(labels, values)
{
    for(var j = 0; j < labels.length; j++)
    {

        if(labels[j]==' ')
        {
            var count = values[j]/data.length*100;
            if(count < 5 || count > 35 )
            {
                return false;
            }
        }
        else if(labels[j]=='e')
        {
            var count = values[j]/data.length*100;
            if(count < 7 || count > 12 )
            {
                return false
            }
        }
        else if(labels[j]=='a')
        {
            var count = values[j]/data.length*100;
            if(count < 3 || count > 9 )
            {
                return false
            }
        }
        else if(labels[j]=='t')
        {
            var count = values[j]/data.length*100;
            if(count < 5 || count > 10 )
            {
                return false
            }
        }
        else if(labels[j]=='n')
        {
            var count = values[j]/data.length*100;
            if(count < 3 || count > 10 )
            {
                return false
            }
        }
        else if(labels[j]=='i')
        {
            var count = values[j]/data.length*100;
            if(count < 3 || count > 8 )
            {
                return false
            }
        }
        else if(labels[j]=='i')
        {
            var count = values[j]/data.length*100;
            if(count < 2 || count > 6 )
            {
                return false
            }
        }
        else if(labels[j]=='i')
        {
            var count = values[j]/data.length*100;
            if(count < 2 || count > 6 )
            {
                return false
            }
        }
    }
    return true;
}