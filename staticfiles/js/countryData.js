var countryname  = document.getElementById("countryname").innerHTML

var endpoint = '/api/data/'+countryname
var globalData = null
console.log(endpoint)
if(countryname){
$.ajax({
    method : "GET", 
    url :endpoint ,
    success : function(data){
        globalData = data 
        console.log("I got the data yaya")
        console.log(data)
        console.log(endpoint)
        displayChart(globalData['alldata'] , globalData['labels']);
    },
    error : function(error_data){
        console.log("Error Occured")
        console.log(error_data)
    }  
    
})}

function displayChart(data , labels){
    const ctx = document.getElementById('myChart');
    const myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: labels,
            datasets: [{
                label: 'Total Confirmed Cases  ',
                data: data,
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
  
                ],
                borderColor: [
                    'rgba(255, 99, 132, 0.2)',
 
                ],
                borderWidth: 1
            }]
        },
        options: {
            scales: {
              xAxes: [{
                type: 'time',
              }]
              ,yAxes: [
                {
                    ticks: {
                        callback: function(label, index, labels) {
                            return label/1000000+'m';
                        }
                    },
                    scaleLabel: {
                        display: true,
                        labelString: '1m = 1000k'
                    }
                }
            ]
            }
        }
    });

}