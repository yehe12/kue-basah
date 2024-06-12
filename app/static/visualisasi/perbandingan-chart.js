console.log("perbandingan chart");

function perbandinganChart(dataPerbandingan) {

    var ctxPerbandingan = document.getElementById("perbandinganChart");

    if (dataPerbandingan.length === 0) {
        console.log("data Perbandingan kosong");
    } else {
        var selectedDataPerbandingan = dataPerbandingan;

        selectedDataPerbandingan.forEach(function(item) {
            data.push(item[1]);
            labels.push(item[0]);
        });

        perbandinganChartInstance = new Chart(ctxPerbandingan, {
            type: "pie",
            data: {
                labels: labels,
                datasets: [
                    {
                        label: "Grafik Perbandingan",
                        data: data,
                        borderWidth: 2,
                        borderWidth: 2,
                        backgroundColor: [
                            'rgba(99, 255, 128, 0.2)',
                            'rgba(255, 99, 132, 0.2)',
                        ],
                        borderColor: [
                            'rgb(99, 255, 128)',
                            'rgb(255, 99, 132)',
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