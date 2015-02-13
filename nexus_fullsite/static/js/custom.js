
jQuery(document).ready(function($) 
    {
	$(".vote_form").submit(function(e) 
		{
		    e.preventDefault(); 
		    var btn = $("button", this);
		    var l_id = $(".hidden_id", this).val();
		    btn.attr('disabled', true);
		    $.post("/vote/", $(this).serializeArray(),
			  function(data) {
			      if(data["voteobj"]) {
				  btn.text("-");
			      }
			      else {
				  btn.text("+");
			      }
			});
		btn.attr('disabled', false);
	});

});
	function setCookie(cname, cvalue, exdays){
		var d = new Date();
		d.setTime(d.getTime() + (exdays*24*60*60*1000));
		var expires = "expires=" + d.toUTCString();
		document.cookie = cname + "=" + cvalue +";" + expires;
	}

	function getCookie(cname){
		var name = cname + "=";
		var ca = document.cookie.split(';');
		for(var i = 0; i < ca.length; i++){
			var c = ca[i];
			while(c.charAt(0)== ' ') c = c.substring(1);
			if(c.indexOf(name) == 0) return c.substring(name.length, c.length);
		}
		return "";
	}

	function checkCookie(){
		var user = getCookie("username");
		var apiKey = getCookie("api_key")
		if(user != "" && apiKey != ""){
			alert("Welcome again " + user + ", Your API Key: " + apiKey);
		}
	}

	function delete_cookie(name, apiKey) {
	  document.cookie = name + '=; expires=Thu, 01 Jan 1970 00:00:01 GMT;';
	  document.cookie = apiKey + '=; expires=Thu, 01 Jan 1970 00:00:01 GMT;';
	  alert("Cookie Destroyed");
	}