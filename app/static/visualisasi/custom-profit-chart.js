console.log("custom profit chart");

function customProfitChart(dataCustomProfit) {
    var ctxCustomProfit = document.getElementById("customProfitChart");

    if (dataCustomProfit.length === 0) {
        console.log("data profit custom kosong");
    } else {
        var selectedDataCustomProfit = dataCustomProfit;

        selectedDataCustomProfit.forEach(function(item) {
            var formattedDate = new Date(item[0]).toLocaleDateString('en-GB', {
                year: 'numeric',
                month: '2-digit',
                day: '2-digit'
            });
            data.push(item[1]);
            labels.push(formattedDate);
        });

        customProfitChartInstance = new Chart(ctxCustomProfit, {
            type: "line",
            data: {
                labels: labels,
                datasets: [
                    {
                        label: "Grafik Profit",
                        data: data,
                        borderWidth: 2,
                        borderColor: 'rgb(99, 255, 128)',
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