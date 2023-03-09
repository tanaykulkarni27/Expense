var expense_data = [];
google.charts.load('current', {'packages':['corechart']});

function load_chart_Expense(database_data){
    expense_data = database_data;
	var area_data = google.visualization.arrayToDataTable(database_data);
	var area_options = {
        title: 'Your expense',
        hAxis: {title: 'Date',  titleTextStyle: {color: '#333'}},
        vAxis: {title: 'Expense',minValue: 0}
	};
	var area_chart = new google.visualization.AreaChart(document.getElementById('graph'));
	area_chart.draw(area_data, area_options);
	var avg = 0;
	var cnt = Math.min(database_data.length - 1,30);
	var itr = database_data.length - 1;
	for(var i = 0;i < cnt;i++){
		avg += database_data[itr][1];
		itr--;
	}
	var tot  = avg;
	avg /= cnt;
	avg = avg.toFixed(2);
	document.getElementById('avg').innerHTML = "Total : " + tot + "<br>Avg : " + avg;
}

function load_chart_Income(database_data){
    expense_data = database_data;
	var area_data = google.visualization.arrayToDataTable(database_data);
	var area_options = {
        title: 'Your Income',
        hAxis: {title: 'Date',  titleTextStyle: {color: '#333'}},
        vAxis: {title: 'Income',minValue: 0}
	};
	var area_chart = new google.visualization.AreaChart(document.getElementById('igraph'));
	area_chart.draw(area_data, area_options);
}


function add_Expense(){
    $.ajax({
		type : "POST",
		data:{
			csrfmiddlewaretoken:$('input[name="csrfmiddlewaretoken"]')[0].value,
			Eamnt:document.getElementById('Exp_amnt').value,
			type:'expense'
		},
		success:function(data){
			location.reload();
		}
	});
}

function add_Income(){
    $.ajax({
		type : "POST",
		data:{
			csrfmiddlewaretoken:$('input[name="csrfmiddlewaretoken"]')[0].value,
			Iamnt:document.getElementById('Inc_amnt').value,
			type:'income'
		},
		success:function(data){
			location.reload();
		}
	});
}


function load_charts(expense_data,income_data){
	load_chart_Expense(expense_data);
	load_chart_Income(income_data);
} 
