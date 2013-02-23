$(function(){

_.templateSettings = {
  interpolate : /\{\{\=(.+?)\}\}/g,
  evaluate: /\{\{(.+?)\}\}/g
};

var update_posts_lock = false;
$(window).scroll(function(){
	// Check if we at end of post stream page
	if ($(window).scrollTop() == ($(document).height() - $(window).height())){
	if (update_posts_lock) return;
	update_posts_lock = true;
	var post_id = $('.poststream .media:last-child').attr('data-id');
	$('.upload-progress').show();
	jsonrpc('/api/?csrf_token=' + X_CSRF_TOKEN, 'get_posts_after', [post_id], function(resp){
		resp = resp.result;
		console.log(resp);
		var compile = _.template($('.post_template').html())
		for (var i=0; i<resp.length; i++){
		        console.log(resp[i]);
			$('.poststream').append($(compile(resp[i])));
		}
		$('.upload-progress').hide();
		update_posts_lock = false;
	})
}
})
}
)


function jsonrpc(url, method, params, callback, id){
	if (typeof(id) == 'undefined'){
		var id = 0;
	}

	jsonrpc_package = {
			jsonrpc: "2.0",
			method: method,
			params: params || [],
			id: id
		}

	// console.log(jsonrpc_package);
	$.ajax({
		url: url,
		type: 'POST',
		dataType: 'json',
		processData: false,
		contentType: 'application/json',
		data: JSON.stringify(jsonrpc_package),
		success: function(response){
				if (typeof(callback) == 'function'){ callback(response); }
			},
		headers: {'X-Csrf-Token': X_CSRF_TOKEN}
	})
}
