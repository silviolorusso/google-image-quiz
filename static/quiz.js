queryName = $("meta[name=nothingimportanttrustme]");
// superproof cypher
query = queryName.attr("content").split("").reverse().join("");

// create form
for (var i = query.length - 1; i >= 0; i--) {
	$('#form').prepend( '<input type="text" size="1" maxlength="1" class="query ' + i + ' ">' );
};
$('.query').first().focus();

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
	if ($(this).val() !== '') { 
		$(this).next().selectRange(0,1);
	}
});
// select letter on focus
$('.query').on('focus', function() {
	field = $(this);
	if (!field.hasClass('hint')) {
		setTimeout(function(){
			field.selectRange(0,1);
		}, 10);
	}
});
// on del press, if it's empty, go back to prev form 
$('.query').on('focus', function() {
	field = $(this);
	$('html').keydown(function(e){
    if ((e.keyCode == 8) && (field.val() === '')) {
    	if (!field.prev().hasClass('hint')) {
    		field.prev().focus();
    	};
    }
	}) 
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
$('#try').click( function(event){
	event.preventDefault();
	attempts++;
	if (getUsrQuery() == query) {
		if ($('#correct').css('display') == 'none') {
			if (attempts == 1) {
				$('#attempts').append(attempts + ' attempt');
			} else {
				$('#attempts').append(attempts + ' attempts');
			}
			if (hints == 1) {
				$('#hints').append(hints + ' hint');
			} else {
				$('#hints').append(hints + ' hints');
			}
			$('#background, #correct').show(0);
		}
	} else {
		$('#background, #wrong').show(0, function(){
			setTimeout(function(){
				$('#background, #wrong').hide(0);
			}, 1200);
		});
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
	if ($('#unlucky').css('display') == 'none') {
		$('.showQuery').append(query);
		$('#background, #unlucky').show(0);
	}
});
		
// new
$('.newpic').click( function(){
	location.reload();
});