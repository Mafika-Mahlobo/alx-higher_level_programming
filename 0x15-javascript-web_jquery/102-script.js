$(document).ready(function(){

	$("#btn_translate").click(function(){
		var code = $("#language_code").val();
		var apiurl = "https://hellosalut.stefanbohacek.dev/"+"?lang="+code;
		$.ajax({
			url: apiurl,
			type: "GET",
			success: function(data){
				$("#hello").text(data.hello);
			},
		});
	});

});