var marcados = 0;
var asientos ="";

function pintarSala(id){
   marcados = 0;
  var result = []
   var req =  new XMLHttpRequest();
   console.log("ENTRO");
   req.open("GET", "asientosSesion/"+id, true);
   req.onreadystatechange = function(){
   	   if(req.readyState == 4 && req.status == 200){ 
            asientos ="";
            marcados = 0;
            result = JSON.parse(req.responseText);
            var i;
            var div = document.getElementById("asientos");
            div.innerHTML = "";
            var tabla = document.createElement('div');
            var fila = 1;
            var index = 0;
            var tr = document.createElement('div');
            for (i in result){
               console.log(result[i].fields.fila );
               if(result[i].fields.fila != fila){
                  tabla.appendChild(tr);
                  fila = result[i].fields.fila ;
                  tr = document.createElement('div');
               }
               
              // var td = document.createElement('td');
              console.log('paso 1');
               var cb = document.createElement('input');
               console.log('paso 2')

               cb.type = 'checkbox';
               cb.id = index;
               cb.setAttribute("onclick","marcar("+index+")");
               index++;
               if(result[i].fields.libre == 1){
                  asientos = asientos + "1";
                  cb.checked = true;
                  cb.disabled = true;
               }else{
                  asientos = asientos + "0";

               }
               
            //   td.appendChild(cb);
               tr.appendChild(cb);


            }
           // tbody.appendChild(tr);

            tabla.appendChild(tr);
            div.appendChild(tabla);

            document.getElementById('guardar').innerHTML = '<button onclick="guardarAsientos('+id+')">Guardar reserva</button><button onclick="cancelar()">Cancelar</button>';
            
           
                  	   }
   }
   req.send();
}

function guardarAsientos(id){
   if(document.getElementById("nEntradasSesion"+id).value!=marcados){
      alert("El numero de entradas seleccionado no es igual al numero de asientos seleccionados");
   }else{
      console.log(asientos);
        var req =  new XMLHttpRequest();
         console.log("ENTRO");
         req.open("GET", "ocuparAsiento/"+id+"/"+asientos, true);
         req.onreadystatechange = function(){
            marcados = 0;
            asientos = "";
            var div = document.getElementById("asientos");
            div.innerHTML = "";
            if(document.getElementById("nEntradasSesion"+id).value!=0){
               document.getElementById('sesiones').value =  document.getElementById('sesiones').value+"$"+id+"_"+document.getElementById("nEntradasSesion"+id).value;
            }
             
            document.getElementById("nEntradasSesion"+id).value = 0;
               document.getElementById('guardar').innerHTML = "";
              

         }
         req.send();

   }
   
   
}
function cancelar(){
   var div = document.getElementById("asientos");
   div.innerHTML = "";
   document.getElementById('guardar').innerHTML = "";
}

function marcar(id){
         console.log(asientos);

   if(document.getElementById(id).checked==true){
       asientos =asientos.substring(0,parseInt(id))+ '1' +asientos.substring(parseInt(id)+1) ;
      marcados++;
   }else{
      asientos =asientos.substring(0,parseInt(id))+ '0' +asientos.substring(parseInt(id)+1) ;

      marcados--;
   }


}




