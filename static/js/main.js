$(function () {
	$("form#search").submit(function () {
		$.get("/api/search?q=" + $("form#search input#q").val(), function (data) {
			$("ol").empty();
			$(data.results).each(function (index, value) {
				$("ol").append("<li>" + value + "</li>");

			});

		});
		return false;
	});

});