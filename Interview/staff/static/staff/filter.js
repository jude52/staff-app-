<script>


function filterSearch() {
  var input, filter, table, tr, td, i, txtValue;
  input = document.getElementById("last_names");
  filter = input.value.toUpperCase();
  table = document.getElementById("staff_results");
  tr = table.getElementsByTagName("tr");
  for (i = 0; i < tr.length; i++) {
    td = tr[i].getElementsByTagName("td");
    var flag = false;
    for (var j =0; j <td.length; j++){
      var tds = td[j];
      if (tds.innerHTML.toUpperCase().indexOf(filter) > -1) {
        flag = true;
      } 
    }
    if(flag){
        tr[i].style.display = "";
    }
    else {
        tr[i].style.display = "none";
    }
  }
}

</script>