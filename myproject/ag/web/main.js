var all_data= {};
function lode_data() {
eel.lode_data();
}
function save_data() {
eel.save_data();


}
function getres() {
eel.getres();
}

eel.expose(setres);
function setres(data) {
var res=document.getElementById("res")
res.innerHTML =data
}
function getStatut() {
eel.getStatut();
}

eel.expose(setStatut);
function setStatut(data) {
var res=document.getElementById("Statut")
res.innerHTML =data
}
eel.expose(setdata);
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
    if(data){input=document.getElementById(id).checked = true}
    else{input=document.getElementById(id).checked = false}
    }
}
eel.expose(getdata);
function getdata(id,typ) {
var id2='id_'+id
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

eel.expose(write_f);
function write_f() {
if (all_data["nb"] !== "") {

console.log(all_data["nb"])
var aa= JSON.stringify(all_data)
eel.write_f(aa);
}
}