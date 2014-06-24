queryName = $("meta[name=nothingimportanttrustme]");
// superproof cypher
query = queryName.attr("content").split("").reverse().join("");

// create form
for (var i = query.length - 1; i >= 0; i--) {
	$('#form').prepend( '<input type="text" size="1" maxlength="1" class="query ' + i + ' ">' );
};
// after writing go to next box and select letter
$.fn.selectRange = function(start, end) {
    if(!end) end = start; 
    return this.each(function() {
        if (this.setSelectionRange) {
            this.focus();
            this.setSelectionRange(start, end);
        } else if (this.createTextRange) {
            var range = this.createTextRange();
            range.collapse(true);
            range.moveEnd('character', end);
            range.moveStart('character', start);
            range.select();
        }
    });
};
$('.query').on('input', function() {
	$(this).next().selectRange(0,1);
});

// get user query
function getUsrQuery() {
	usrQuery = "";
	$('.query').each(function( index ) {
		if ($(this).val() != "") {
	  	usrQuery = usrQuery + $(this).val();
		} else {
			usrQuery = usrQuery + " ";
		}
	});
	usrQuery = usrQuery.toLowerCase();
	return usrQuery
}

// try
attempts = 0
$('#try').click( function(){
	if (getUsrQuery() == query) {
		attempts++;
		alert('Correct! You guessed the query in ' + attempts + ' attempts using ' + hints + " hints.");
	} else {
		$('#background, .alert').show(
			setTimeout(function(){
				$(this).fadeOut();
			}, 1000)
		});
		attempts++;
	}
});

// hint
hints = 0;
$('#hint').click( function(){
	k = 0
	j = 0;
	// check correct letters and block them and add hint
	for (var i = 0; i < query.split("").length; i++) {
		val = $('.query.'+i).val().toLowerCase();
		if (query.split("")[i] === val) {
			$('.query.'+i).attr('readonly', 'readonly');
			$('.query.'+i).addClass('hint');
			j++;
		// add hint	
		} else if (k <= 0) {
			$('.query.'+i).val(query.split("")[i]);
			$('.query.'+i).attr('readonly', 'readonly');
			$('.query.'+i).addClass('hint');
			k++;
			j++;
		// clear the others
		} else {
			$('.query.'+i).val("");
		};
	};
	// if not all the letters are shown
	if (j < query.split("").length) {
		hints++;
	}
});

// no luck
$('#noluck').click( function(){
	for (var i = 0; i < query.split("").length; i++) {
		$('.query.'+i).val(query.split("")[i]);
		$('.query.'+i).attr('readonly', 'readonly');
		$('.query.'+i).addClass('hint');
	};
	alert('Aw, snap! The query was: ' + query );
});
		


// new
$('#newpic').click( function(){
	location.reload();
});