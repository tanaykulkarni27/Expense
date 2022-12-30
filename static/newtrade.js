function submit_my_form(){
	$.ajax({
		type : "POST",
		//~ url : "",
		data:{
			csrfmiddlewaretoken:$('input[name="csrfmiddlewaretoken"]')[0].value,
			type:document.getElementById("type").value,
			name:document.getElementById("name").value,
			quantity:document.getElementById("quantity").value,
			price:document.getElementById("price").value,
			emotion:document.getElementById("emotion").value
		},
		success:function(data){
			location.href="/";
		}
	});
}
