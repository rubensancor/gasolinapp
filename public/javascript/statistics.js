var sumaTot95 = 0.00;
var tot95 = 0;
var sumaTot98 = 0.00;
var tot98 = 0;
var sumaTotD = 0.00;
var totD = 0;
$.ajax({
    type: 'GET',
    url: 'https://gasolinapp.herokuapp.com/a',
    success: function(data) {
        console.log(data);
        for (var i = 0; i < data.length; i++) {
            var cords = data[i].Coordenadas;
            var LatLng = cords.replace("[", "").replace("]", "").split(", ");

            if (data[i].Gasolina95 != "") {
                var str = data[i].Gasolina95;
                var res = str.replace(",", ".");
                sumaTot95 = sumaTot95 + parseFloat(res);
                tot95++;
            }
            if (data[i].Gasolina98 != "") {
                var str = data[i].Gasolina98;
                var res = str.replace(",", ".");
                sumaTot98 = sumaTot98 + parseFloat(res);
                tot98++;
            }
            if (data[i].Gasoleo != "") {
                var str = data[i].Gasoleo;
                var res = str.replace(",", ".");
                sumaTotD = sumaTotD + parseFloat(res);
                totD++;
            }

            var Lat = parseFloat(LatLng[0]);
            var Lng = parseFloat(LatLng[1]);
            var tag95 = 'Gasolina95';
            var tag98 = 'Gasolina98';
            var tagD = 'Diesel';

            if (data[i].Gasolina95 != 0) {
                if (data[i].Gasolina98 != 0) {
                    if (data[i].Gasoleo != 0) {
                        var marker = L.marker([Lat, Lng], {
                            tags: [tag95, tag98, tagD]
                        }).addTo(map);
                        var string = data[i].Compania + "<br> <b>Gasolina95:</b> " + data[i].Gasolina95 + "<br> <b>Gasolina98:</b> " + data[i].Gasolina98 + "<br> <b>Diesel:</b> " + data[i].Gasoleo;
                        marker.bindPopup(string);
                    } else {
                        var marker = L.marker([Lat, Lng], {
                            tags: [tag95, tag98]
                        }).addTo(map);
                        var string = data[i].Compania + "<br> <b>Gasolina95:</b> " + data[i].Gasolina95 + "<br> <b>Gasolina98:</b> " + data[i].Gasolina98 + "<br> <b>Diesel:</b> " + data[i].Gasoleo;
                        marker.bindPopup(string);
                    }
                } else if (data[i].Gasoleo != 0) {
                    var marker = L.marker([Lat, Lng], {
                        tags: [tag95, tagD]
                    }).addTo(map);
                    var string = data[i].Compania + "<br> <b>Gasolina95:</b> " + data[i].Gasolina95 + "<br> <b>Gasolina98:</b> " + data[i].Gasolina98 + "<br> <b>Diesel:</b> " + data[i].Gasoleo;
                    marker.bindPopup(string);
                } else {
                    var marker = L.marker([Lat, Lng], {
                        tags: [tag95]
                    }).addTo(map);
                    var string = data[i].Compania + "<br> <b>Gasolina95:</b> " + data[i].Gasolina95 + "<br> <b>Gasolina98:</b> " + data[i].Gasolina98 + "<br> <b>Diesel:</b> " + data[i].Gasoleo;
                    marker.bindPopup(string);
                }
            } else if (data[i].Gasolina98 != 0) {
                if (data[i].Diesel != 0) {
                    var marker = L.marker([Lat, Lng], {
                        tags: [tag98, tagD]
                    }).addTo(map);
                    var string = data[i].Compania + "<br> <b>Gasolina95:</b> " + data[i].Gasolina95 + "<br> <b>Gasolina98:</b> " + data[i].Gasolina98 + "<br> <b>Diesel:</b> " + data[i].Gasoleo;
                    marker.bindPopup(string);
                } else {
                    var marker = L.marker([Lat, Lng], {
                        tags: [tag98]
                    }).addTo(map);
                    var string = data[i].Compania + "<br> <b>Gasolina95:</b> " + data[i].Gasolina95 + "<br> <b>Gasolina98:</b> " + data[i].Gasolina98 + "<br> <b>Diesel:</b> " + data[i].Gasoleo;
                    marker.bindPopup(string);
                }
            } else {
                var marker = L.marker([Lat, Lng], {
                    tags: [tagD]
                }).addTo(map);
                var string = data[i].Compania + "<br> <b>Gasolina95:</b> " + data[i].Gasolina95 + "<br> <b>Gasolina98:</b> " + data[i].Gasolina98 + "<br> <b>Diesel:</b> " + data[i].Gasoleo;
                marker.bindPopup(string);
            }

        }

        document.getElementById("Gas95").innerHTML = (sumaTot95/tot95).toFixed(3);
        document.getElementById("Gas98").innerHTML = (sumaTot98/tot98).toFixed(3);
        document.getElementById("D").innerHTML = (sumaTotD/totD).toFixed(3);
    }
});
