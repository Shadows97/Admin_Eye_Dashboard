 let cpuChart = document.getElementById("bandeTotal");
let diskMemoryChart = document.getElementById("diskMemoryChart");
let ramChart = document.getElementById("ramChart");
let bandeChart = document.getElementById("bandeChart");
var endPoint =" bandeTotal";


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

function ajaxDataGetter(){
	$.ajax({
		method :'GET',
		url: endPoint,
		success: function(data){
		    console.log(data.cpuInfo);
			getData(data.bande);
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
		        label: chartParametersValues.data.label,
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
		label:"Bande Passante"
	},
	chartOptionValues:{
		isLegendDisplay: true,
		isTitleDisplay: true,
		title: "Historique d'utilisation totale de la Bande Passante "
	}
}

//Initialize Chart
let contextChartLine1 = createLineChart(cpuChart, lineChartParametersValues); //CPU Initialization


var getData = function(ajaxData) {

  //CPU Chart Section Start
  let onlyLineOfChartLine1 = contextChartLine1.data.datasets[0];
  let dataOfOnlyLineOfChartLine1 = onlyLineOfChartLine1.data;

  if (dataOfOnlyLineOfChartLine1.length >= 50) {
    dataOfOnlyLineOfChartLine1.pop();
    onlyLineOfChartLine1.pointBackgroundColor.pop();
  }
  let theData = ajaxData;
  dataOfOnlyLineOfChartLine1.unshift(theData);
  console.log(theData);

  onlyLineOfChartLine1.pointBackgroundColor.unshift("#"+Math.floor(Math.random()*16777215).toString(16));
  //CPU Chart Section End

    console.error(ajaxData)
  contextChartLine1.update();

}

setInterval(ajaxDataGetter, 1000);