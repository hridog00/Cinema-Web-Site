function pintarSala(id){
  
   var req =  new XMLHttpRequest();
   req.open("GET", "asientosSesion/"+id, true);
   req.onreadystatechange = function(){
   	   if(req.readyState == 4 && req.status == 200){
               result = Json.parse(req.responseText);
   	   	  alert(result.length);
   	   }
   }
   req.send();
}



