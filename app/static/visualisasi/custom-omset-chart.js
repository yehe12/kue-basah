console.log("custom omset chart");

function customOmsetChart(dataCustomOmset) {
    var ctxCustomOmset = document.getElementById("customOmsetChart");

    if (dataCustomOmset.length === 0) {
        console.log("data omset custom kosong");
    } else {
        var selectedDataCustomOmset = dataCustomOmset;

        selectedDataCustomOmset.forEach(function(item) {
            var formattedDate = new Date(item[0]).toLocaleDateString('en-GB', {
                year: 'numeric',
                month: '2-digit',
                day: '2-digit'
            });
            data.push(item[1]);
            labels.push(formattedDate);
        });

        customOmsetChartInstance = new Chart(ctxCustomOmset, {
            type: "line",
            data: {
                labels: labels,
                datasets: [
                    {
                        label: "Grafik Omset",
                        data: data,
                        borderWidth: 2,
                        borderColor: 'rgb(153, 102, 255)',
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