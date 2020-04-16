	function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?1
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
 }
 var csrftoken = getCookie('csrftoken');
// Setup ajax connections safetly

 function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
 }
 $.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
 });

 
  function lode_data(type_data) {
    // alert("Hello! I am an alert box!!");
      for(var key in type_data) {
  var value = type_data[key];

  setdata(key,value,d_data[key]);


	}
  }




  
  function setres(data) {
    var res=document.getElementById("res")
    res.innerHTML =data
  }
  
  function setStatut(data) {
    var res=document.getElementById("Statut")
    res.innerHTML =data
  }
  
  function setdata(id,typ,data) {
          //	document.getElementById("nb").value = nb
          if (typ =='list') {
          	createTable_l(id,data);
          }
          else if (typ =='matrix') {
            createTable_a(id,data);
          }
          else if (typ =='int') {
            input=document.getElementById(id);
            input.value=data
          }
          else if (typ =='double') {
            input=document.getElementById(id);
            input.value=data
          }
          else if (typ =='bool') {
          	input=document.getElementById(id);
          	// console.log(id);
          	// console.log(input);
            if(data=="True"){input=document.getElementById(id).checked = true}
              else{input=document.getElementById(id).checked = false}
            }
          }

  function getdata(id,typ) {
  var id2=id
  var val=''
  if (['list', 'matrix'].includes(typ)) {
    var table = document.getElementById(id2);

    val = [];
    tblLength = table.rows.length;
    for(i=0;i<tblLength;i++){
      var arrayOfThisRow = [];
      let raw_i=table.rows[i]
      for(j=0;j<raw_i.cells.length;j++){
        let d=raw_i.cells[j].children[0].value
        let nn=Number(d)
        if(isNaN(nn)){
          arrayOfThisRow.push(d)
        }
        else{arrayOfThisRow.push(nn)}

      }
    val.push(arrayOfThisRow);
  }
  if(typ=='list'){
    val=val[0]

  }

  }
    
    else if (['int', 'double'].includes(typ)) {
      input=document.getElementById(id2);
      val=Number(input.value)
    }
    
    else if (typ =='bool') {

      input=document.getElementById(id2);
      val=input.checked;
    }
    all_data[id]=val;
    }

 function opendata(evt, dataName) {
  var i, tabcontent, tablinks;
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }
  tablinks = document.getElementsByClassName("tablinks");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }
  document.getElementById(dataName).style.display = "block";
  evt.currentTarget.className += " active";
  }
 function createTable_l(id,tableData,) {
    //  var table = document.createElement('table');
    // console.log(d_data); 
    var tableData= eval(tableData) ;
     // console.log(tableData); 
    var table = document.getElementById(id);
    table.innerHTML = "";
    var tableBody = document.createElement('tbody');
    var row = document.createElement('tr');
    tableData.forEach(function(cellData) {
    
    
      var cell = document.createElement('td');
    
      var input = document.createElement('input');
      input.setAttribute('value',cellData)
      input.setAttribute('style','width:85%;height:85%')
    
      cell.appendChild(input);
    
      row.appendChild(cell);
    });
    
    tableBody.appendChild(row);
    
    table.appendChild(tableBody);
    //  document.getElementById("t_nb")=table
    //  document.body.appendChild(table);
    }
 function createTable_a(id,tableData,) {
  //  var table = document.createElement('table');
  var table = document.getElementById(id);
  table.innerHTML = "";
  var tableBody = document.createElement('tbody');
    var tableData= eval(tableData) ;

  
  tableData.forEach(function(rowData) {
    var row = document.createElement('tr');
  
    rowData.forEach(function(cellData) {
      var cell = document.createElement('td');
  
      var input = document.createElement('input');
      input.setAttribute('value',cellData)
      input.setAttribute('style','width:85%;height:85%')
  
  //      input.
  //      cell.appendChild(document.createTextNode(cellData));
  cell.appendChild(input);
  
  row.appendChild(cell);
  });
  
    tableBody.appendChild(row);
  });
  
  table.appendChild(tableBody);
  
  }

 // Expand groups using blue chevrons
 function expand(el) {
  let expandDiv_node = document.getElementById(el.dataset.expand);
  if (el.style.transform !== "rotate(0deg)") {
    el.style.transform = 'rotate(0deg)';
    if (el.dataset.display !== undefined) {
      expandDiv_node.style.display = el.dataset.display;
    } else {
      expandDiv_node.style.display = 'block';
    }
  } else {
    el.style.transform = 'rotate(180deg)';
    expandDiv_node.style.display = 'none';
  }
  }


  function save_data() {

	for(var key in type_data) {
  	var value = type_data[key];
  	getdata(key,value); }
  	// alert(save_datas);
 	// 
   
  	}
    
    var inicio=0;
    var timeout=0;
   
    function empezarDetener(elemento,a)
    {
      if(a==0)
      {
        // empezar el cronometro
   
        elemento.value="Detener";
   
        // Obtenemos el valor actual
        inicio=vuelta=new Date().getTime();
   
        // iniciamos el proceso
        funcionando();
      }else{
        // detemer el cronometro
   
        elemento.value="Empezar";
        clearTimeout(timeout);
        timeout=0;
      }
    }
   
    function funcionando()
    {
      // obteneos la fecha actual
      var actual = new Date().getTime();
   
      // obtenemos la diferencia entre la fecha actual y la de inicio
      var diff=new Date(actual-inicio);
   
      // mostramos la diferencia entre la fecha actual y la inicial
      var result=LeadingZero(diff.getUTCHours())+":"+LeadingZero(diff.getUTCMinutes())+":"+LeadingZero(diff.getUTCSeconds());
      document.getElementById('crono').innerHTML = result;
   
      // Indicamos que se ejecute esta función nuevamente dentro de 1 segundo
      timeout=setTimeout("funcionando()",1000);
    }
   
    /* Funcion que pone un 0 delante de un valor si es necesario */
    function LeadingZero(Time) {
      return (Time < 10) ? "0" + Time : + Time;
    }
