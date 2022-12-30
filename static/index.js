var database_data = [];
var hologram_data = [];

function submit_my_form(){
	
	$.ajax({
		type : "POST",
		data:{
			csrfmiddlewaretoken:$('input[name="csrfmiddlewaretoken"]')[0].value,
			type:document.getElementById("type").value,
			quantity:document.getElementById("quantity").value,
			price:document.getElementById("price").value,
			emotion:document.getElementById("emotion").value
		},
		success:function(data){
			location.reload();
		}
	});
}

google.charts.load('current', {'packages':['corechart']});
function load_charts(){
	var area_data = google.visualization.arrayToDataTable(database_data);
	var area_options = {
        title: 'Your PnL',
        hAxis: {title: 'Date',  titleTextStyle: {color: '#333'}},
        vAxis: {minValue: 0}
	};
	var area_chart = new google.visualization.AreaChart(document.getElementById('graph'));
	area_chart.draw(area_data, area_options);
}

function load_pie_chart(prof,loss){
	
	var ctx = document.getElementById('holograph');
	
	var data = google.visualization.arrayToDataTable([
         ['PnL', 'Rs', { role: 'style' }],
         ['Profit', prof, ''],            // RGB value
         ['Loss', loss, '#FFA500']
	]);
	var options = {
        title: "Profit and loss",
        width: 600,
        height: 400,
        bar: {groupWidth: "95%"},
        legend: { position: "none" },
      };
      var chart = new google.visualization.BarChart(ctx);
      chart.draw(data, options);
}


function load_whole_data(data,holo_data,x,y){
	database_data = data;
	hologram_data = holo_data;
	load_charts();
	load_pie_chart(x,y);
}

function add_PnL(){
	
	$.ajax({
		type : "POST",
		data:{
			csrfmiddlewaretoken:$('input[name="csrfmiddlewaretoken"]')[0].value,
			Profit:document.getElementById("Profit").value
		},
		success:function(data){
			location.reload();
		}
	});
}

function end_trade(){
	$.ajax({
		type : "GET",
		data:{
			TYP : 'end_trade'
		},
		success:function(data){
			location.reload();
		}
	});
}




/*
   

*/


