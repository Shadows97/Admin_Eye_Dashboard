
let cpuChart = document.getElementById("cpuChart").getContext('2d');
let diskMemoryChart = document.getElementById("diskMemoryChart").getContext('2d');
let ramChart = document.getElementById("ramChart").getContext('2d');
let bandeChart = document.getElementById("bandeChart").getContext('2d');
var endPoint =" api/info/{{ equipement.id }}";

function lineChartConfig(optionParametersValues){
	return {
       legend : { display : optionParametersValues.isLegendDisplay },
       title : {
        display : optionParametersValues.isTitleDisplay,
        text : optionParametersValues.title        	
       },
       scales: {
            yAxes: [{
                id: 'first-y-axis',
                type: 'linear',
                display: false
            }, {
                id: 'second-y-axis',
                type: 'linear',
                position: 'left'
            }],
            xAxes: [{
              display: false
            }]
        }		
	};  
}

function ajaxDataGetter(equipementURL){
	$.ajax({
		method :'GET',
		url: equipementURL,
		success: function(data){
			return data;
		},
		error: function(){
			console.log("Error....")
		}
	});
}

function createLineChart(element, chartParametersValues){
	return new Chart(element, {
		type:'line',
		data: {
    		labels: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
		    datasets: [
		      { 
		        data: [],
		        label: chartParametersValues.data.Label,
		        borderColor: "#3e95cd",
		        fill: false,
		        pointRadius: 2,
		        pointBackgroundColor: [],
		        pointBorderColor: ["#000000", "#800000", "#000075", "#ffe119", "#42d4f4", "#008000", "#0000FF", "#800080", "#FFA500", "#00FA9A"],
		        pointHoverRadius: 10,
		        yAxisID: 'first-y-axis'
		      }
		    ]
		  },
		options: lineChartConfig(chartParametersValues.chartOptionValues)
	});
}


lineChartParametersValues = {
	data:{
		label:"CPU%"
	},
	chartOptionValues:{
		isLegendDisplay: true,
		isTitleDisplay: true,
		title: "Historique d'utilisation du CPU"
	}
}

//Initialize Chart
let contextChartLine1 = createLineChart(cpuChart, lineChartParametersValues); //CPU Initialization


var getData = function() {

  let ajaxData = ajaxDataGetter(endPoint);



  //CPU Chart Section Start
  let onlyLineOfChartLine1 = contextChartLine1.data.datasets[0];
  let dataOfOnlyLineOfChartLine1 = onlyLineOfChartLine1.data;
  
  if (dataOfOnlyLineOfChartLine1.length >= 50) {
    dataOfOnlyLineOfChartLine1.pop();
    onlyLineOfChartLine1.pointBackgroundColor.pop();
  }
  dataOfOnlyLineOfChartLine1.unshift(ajaxData.cpuData);

  onlyLineOfChartLine1.pointBackgroundColor.unshift("#"+Math.floor(Math.random()*16777215).toString(16));
  //CPU Chart Section End 
  

  myChart.update();
 
}