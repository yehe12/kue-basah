console.log("custom return chart");

function customReturnChart(dataCustomReturn) {
    var ctxCustomReturn = document.getElementById("customReturnChart");

    if (dataCustomReturn.length === 0) {
        console.log("data return custom kosong");
    } else {
        var selectedDataCustomReturn = dataCustomReturn;
        
        selectedDataCustomReturn.forEach(function(item) {
            data.push(item[2]);
            labels.push(item[1]);
        });

        customReturnChartInstance = new Chart(ctxCustomReturn, {
            type: "bar",
            data: {
                labels: labels,
                datasets: [
                    {
                        label: "Grafik Return Makanan",
                        data: data,
                        borderWidth: 2,
                        backgroundColor: [
                            'rgba(255, 99, 132, 0.2)',
                            'rgba(99, 255, 128, 0.2)',
                            'rgba(255, 205, 86, 0.2)',
                            'rgba(54, 162, 235, 0.2)',
                            'rgba(153, 102, 255, 0.2)'
                        ],
                        borderColor: [
                            'rgb(255, 99, 132)',
                            'rgb(99, 255, 128)',
                            'rgb(255, 205, 86)',
                            'rgb(54, 162, 235)',
                            'rgb(153, 102, 255)'
                        ],
                        borderWidth: 1
                    },
                ],
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true,
                        ticks: {
                            stepSize: 1,
                        },
                    },
                },
            },
        });
    }
}