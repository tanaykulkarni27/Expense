function add_schedule(){
    var tmp_date = document.getElementById('date').value.split('-');
    tmp_date.reverse();
    var datess= '';
    for(var i of tmp_date){
        datess += i; 
        if(i.length != 4)
            datess += '-';
    }
    var work = document.getElementById('work').value;
    $.ajax({
		type : "POST",
		data:{
			csrfmiddlewaretoken:$('input[name="csrfmiddlewaretoken"]')[0].value,
			work:work,
			date:datess
		},
		success:function(data){
			location.reload();
		}
	});
}
function delete_record(id,token){
    //$('input[name="csrfmiddlewaretoken"]')[0].value
    $.ajax({
		type : "GET",
		data:{
            type:'delete',
			id:id
		},
		success:function(data){
			location.reload();
		}
	});
}