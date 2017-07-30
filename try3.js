$(document).ready(function(){
  var x,lid,iid;
  
    function loadLists(){
        $('.row').hide();
      $('.row1').hide();
      $('.item').hide();
      $('.but2').hide();
      $('.but1').show();
      $('.putitem').hide();
        $('.listscontainer').html("Loading...");
        $.ajax({type:"get",url: "http://127.0.0.1:8000/todo/r_todolists/",dataType:"json", success: function(data){
            
            var items = [];
            items.push("<tr><th>Id</th><th>Name</th><th>Created on</th><th/><th/><th/></tr>");
        $.each( data, function( key, val ) {
        items.push("<tr >"+ "<td>" + JSON.stringify(val["id"]) + "</td>"+"<td>" + JSON.stringify(val["name"]) + "</td>"+"<td>" + JSON.stringify(val["creation_date"]) + "</td><td>"+"<button class = getlists  id='"+JSON.stringify(val["id"])+"'>Items</button></td><td>"+"<button class = updlists  id='"+JSON.stringify(val["id"])+"'>Update</button></td><td>"+"<button class = dellists  id='"+JSON.stringify(val["id"])+"'>Delete</button></td>"+"</tr>");
        });
      $('.listscontainer').html("");
      $( "<table/>", {
        "class": "striped",
        html: items.join( "" )
        }).appendTo( ".listscontainer" );
      $('.listscontainer').show();          
    }});
    }
    loadLists();
    $('body').on('click','#submit',function(butt){
        descrip=$('.item > form > #desc').val();
        //check=$('.item > form > #cb').is(":checked");
        dued=$('.item > form > #dd').val();
        jsonn='{"description":"'+descrip+'","completed":"false","due_by":"'+dued+'","todolist":"'+lid+'"}';
        s=JSON.parse(jsonn);
        console.log(s);
        $.ajax({
          type: "post",
          url: "http://127.0.0.1:8000/todo/r_todoitems/",
    // The key needs to match your method's input parameter (case-sensitive).
          data:JSON.stringify(s) ,
          contentType: "application/json; charset=utf-8",
          dataType: "json",
          success: function(data){alert(data);},
          failure: function(errMsg) {
            alert(errMsg);
           }

          });
        loadLists();
        alert("itempost done");
    });
    $('body').on('click','#psubmit',function(butt){
        descrip=$('.putitem > form > #desc').val();
        check=$('.putitem > form > p > #cb').is(":checked");
        dued=$('.putitem > form > #dd').val();
        jsonn='{"description":"'+descrip+'","completed":"'+check+'","due_by":"'+dued+'","todolist":"'+lid+'"}';
        s=JSON.parse(jsonn);
        console.log(JSON.stringify(s));
        $.ajax({
          type: "put",
          url: "http://127.0.0.1:8000/todo/r_todoitemdetail/"+iid+"/",
    // The key needs to match your method's input parameter (case-sensitive).
          data:JSON.stringify(s) ,
          contentType: "application/json; charset=utf-8",
          dataType: "json",
          success: function(data){alert(data);},
          failure: function(errMsg) {
            alert(errMsg);
           }

          });
        loadLists();
        alert("itempost done");
    });
    $("#clr").keypress(function(e) {
    if(e.which == 13) {
       
        name=e.target.value;
        jsonn='{"name":"'+name+'"}';
        s=JSON.parse(jsonn);
        $.ajax({
          type: "post",
          url: "http://127.0.0.1:8000/todo/r_todolists/",
    // The key needs to match your method's input parameter (case-sensitive).
          data:JSON.stringify(s) ,
          contentType: "application/json; charset=utf-8",
          dataType: "json",
          success: function(data){alert(data);},
          failure: function(errMsg) {
            alert(errMsg);
           }

          });
        alert('Created');
        $('.but2').hide();
    }
    });
    $(".row1").keypress(function(e) {
    if(e.which == 13) {
       id=e.target.id;
        name=e.target.value;
        jsonn='{"name":"'+name+'"}';
        s=JSON.parse(jsonn);alert(x);
        $.ajax({
          type: "put",
          url: "http://127.0.0.1:8000/todo/r_todolistdetail/"+x+"/",
    // The key needs to match your method's input parameter (case-sensitive).
          data:JSON.stringify(s) ,
          contentType: "application/json; charset=utf-8",
          dataType: "json",
          success: function(data){alert(data);},
          failure: function(errMsg) {
            alert(errMsg);
           }
          
          });
          $('.listscontainer').show();
          $('.row').hide();
          $('.row1').hide();
          $('.item').hide();
          $('.but2').hide();
    }
    });
    	$("#b").click(()=>{loadLists()});
      $("#cl").click(function(e){
          $('.listscontainer').hide();
          $('.row').show();
          $('.row1').hide();
          $('.item').hide();
          $('.but2').hide();
      });
      $("#ci").click(function(e){
          $('.listscontainer').hide();
          $('.row').hide();
          $('.row1').hide();
          $('.item').show();
          $('.but2').hide();
          $('.but1').hide();
      });
      $('.datepicker').pickadate({
        selectMonths: true, // Creates a dropdown to control month
        selectYears: 15, // Creates a dropdown of 15 years to control year
        format:'yyyy-mm-dd'
       });
      $("body").on('click','.updlists',function(e){
          $('.listscontainer').hide();x=e.target.id;
          $('.row1').show();
          $('.row').hide();
          $('.but2').hide();
      });
      $("body").on('click','.upditems',function(e){
          $('.listscontainer').hide();
          $('.row1').hide();
          $('.row').hide();
          $('.but2').hide();
          $('.item').hide();
          $('.putitem').show();
          iid=e.target.id;
      });
      $("body").on('click','.dellists',function(e){
        id=e.target.id;
        $.ajax({type:"delete",url:"http://127.0.0.1:8000/todo/r_todolistdetail/"+id+"/",success:function(){
          
          loadLists();
        }});
        $('.but2').hide();
      });
      $("body").on('click','.delitems',function(e){
        id=e.target.id;
        $.ajax({type:"delete",url:"http://127.0.0.1:8000/todo/r_todoitemdetail/"+id+"/",success:function(){
          alert('Deleted');

        }});
        loadLists();
        $('.but1').hide();
        $('.but2').show();
      });
    	$("body").on('click','.getlists',function(e){
        $('.listscontainer').html("Loading...");
          id = e.target.id;
          lid=id;
        	$.ajax({type:"get",url: "http://127.0.0.1:8000/todo/r_todolistdetail/"+id+"/items",dataType:"json", success: function(data){
            	$('.row').hide();
          $('.but1').hide();
          $('.but2').show();
            	var items = [];
              items.push("<tr><th>Id</th><th>Description</th><th>Completed</th><th>Due by</th><th/><th/></tr>");
  				$.each( data, function( key, val ) {
    			items.push( "<tr>"+ "<td>" + JSON.stringify(val["id"]) + "</td>"+"<td>" + JSON.stringify(val["description"]) + "</td>"+"<td>" + JSON.stringify(val["completed"]) + "</td><td>"+JSON.stringify(val["due_by"]) + "</td>"+"<td>"+"<button class = upditems  id='"+JSON.stringify(val["id"])+"'>Update</button></td><td>"+"<button class = delitems  id='"+JSON.stringify(val["id"])+"'>Delete</button></td>"+"</tr>" );
  				});
          $('.listscontainer').html("");
 				$( "<table/>", {
   	 			"class": "striped",	
    			html: items.join( "" )
  				}).appendTo( ".listscontainer" );
           	}});
          
    	});
	}); 