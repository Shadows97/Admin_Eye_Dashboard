var endPoint =" api/info/1"
var data = {
        labels: label,
        datasets: [{
            label: '# of Votes',
            data: defaultData,
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: [
                'rgba(255,99,132,1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1,

        }]
    }
    var option = {
  maintainAspectRatio: false,
  scales: {
      scaleLabel:{
          display:true,
          labelString: 'TEST',
      },
    yAxes: [{
        label:"test",
      stacked: true,
      gridLines: {
        display: false,
        color: "rgba(255,99,132,0.2)"
      }
    }],
    xAxes: [{

      gridLines: {
        display: false
      }
    }]
  }
}
        var defaultData = []
        var cpu_data = []
        var cpu_lable = []
        var label = []
        var ram_data = []
        var byte_dat1 = []
        var byte_dat2 = []
        var byte_label1 = []
        var byte_label2 = []
        var myChart1 = null
        var myChart2 = null
        var myChart3 = null
        var myChart4 = null

         function first() {
            $.ajax({
            method :'GET',
            url :endPoint,
            success:function (data) {
                label = data.label
                defaultData = data.default
                cpu_lable =data.cpuLabel
                cpu_data = data.cpuInfo
                ram_data = data.ramInfo
                byte_dat1 = data.byteInfo1
                byte_dat2 = data.byteInfo2
                console.log(data)
                window.onload =function () {
                    setChart();
                    setCpuChart();
                    setRamChart();
                    setByteChart();


                }
              // interval= setTimeout(first,5000)

            },
            error:function (error_data) {


            }
        });
        }
        first();








  function setChart() {
      var ctx = document.getElementById("Chart").getContext('2d');
      ctx.canvas.width = 100;
        ctx.canvas.height = 100;
     myChart1 = new Chart(ctx, {
    type: 'pie',
    data:  {
        labels: label,
        datasets: [{
            label: 'Mémoir du disque dur',
            data: defaultData,
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: [
                'rgba(255,99,132,1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1,

        }]
    },
    options:option
});
  }


  function setCpuChart() {
      var ctx = document.getElementById("cpuChart").getContext('2d');
      ctx.canvas.width = 100;
        ctx.canvas.height = 100;
     myChart2 = new Chart(ctx, {
    type: 'line',
    data:  {
        labels: cpu_lable,
        datasets: [{
            label: 'Fréquence du CPU ',
            data: cpu_data,
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: [
                'rgba(255,99,132,1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1,

        }]
    },
    options:option
});
  }

   function setRamChart() {
      var ctx = document.getElementById("ramChart").getContext('2d');
      ctx.canvas.width = 100;
        ctx.canvas.height = 100;
     myChart3 = new Chart(ctx, {
    type: 'line',
    data: {
        labels: label,
        datasets: [{
            label: 'Mémoir Ram',
            data: ram_data,
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: [
                'rgba(255,99,132,1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1,

        }]
    },
    options:option
});
  }

   function setByteChart() {
      var ctx = document.getElementById("bandeChart").getContext('2d');
      ctx.canvas.width = 100;
        ctx.canvas.height = 100;
     myChart4 = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['Envoyé ','Reçu '],
        datasets: [{
            label: ' ',
            data: byte_dat1,
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: [
                'rgba(255,99,132,1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1,

        },
        ]
    },
    options:option
});
  }

  function addData() {
    myChart3.data.datasets[0].data.push(50);
    myChart3.update();
}