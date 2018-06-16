
            result = JSON.parse(req.responseText);
            var i;
            var div = document.getElementById("asientos");
            var tabla = document.createElement('table');
            var tbody = document.createElement('tbody');
            var fila = 1;
            var tr = document.createElement('tr');
            for (i in result){
             
               if(result[i].fields.fila != fila){
                  tbody.appendChild(tr);
                  fila = i.fila;
                  tr = document.createElement('tr');
               }
               
               var td = document.createElement('td');
               td.appendChild(document.createTextNode(result[i].fields.libre));
               tr.appendChild(td);


            }
            tabla.appendChild(tbody);
            div.appendChild(tabla);