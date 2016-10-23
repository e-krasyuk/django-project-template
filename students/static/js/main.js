function initJournal() {
	var indicator = $('#ajax-progress-indicator');

	$('.day-box input[type="checkbox"]').click(function(event){
		var box = $(this);
		$.ajax(box.data('url'), {
			'type': 'POST',
			'async': true,
			'dataType': 'json',
			'data': {
				'pk': box.data('student-id'),
				'date': box.data('date'),
				'present': box.is(':checked') ? '1': '',
				'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()
			},
			'beforeSend': function(xhr, settings){
				indicator.show();
			},
			'error': function(xhr, status, error){
				$('#ajax-error').show();
				$('#ajax-error-text').text("ERROR: " + error);
				indicator.hide();
			},
			'success': function(data, status, xhr){
				indicator.hide();
			}
		});
	});
}


function initGroupSelector() {
	//look up select element with groups and attach our event handler
	//on field "change" event
	$('#group-selector select').change(function(evenr){
		//get value of currently selected group option
		var group = $(this).val();

		if (group) {
			//set cookie with expiration date 1 year since now;
			//cookie creation function takes period in days
			$.cookie('current_group', group, {'path': '/', 'expires': 365});
		} 
		else {
			//otherwise we delete the cookie
			$.removeCookie('current_group', {'path': '/'});
		}

		//and reload a page
		location.reload(true);

		return true;
	});
}


function initDateFields() {
	$('input.dateinput').datetimepicker({
		'format': 'YYYY-MM-DD',
		locale: 'uk'
	}).on('dp.hide', function(event){
		$(this).blur();
	});
}

function initDateTimeFields() {
	$('input.datetimeinput').datetimepicker({
		'format': 'YYYY-MM-DD h:mm',
		locale: 'uk'
	}).on('dp.hide', function(event){
		$(this).blur();
	});
}

function initEditStudentForm(form, modal) {
	//attach datepicker
	initDateFields();

	//close modal window on Cancel button click
	form.find('input[name="cancel_button"]').click(function(event) {
		modal.modal('hide');
		return false;
	});

	//make form work in AJAX mode
	form.ajaxForm({
		'dataType': 'html',
		'beforeSend': function() {
			$('.ajax-loader-modal img').show();
			$('input, select, textarea, a, button').attr('disabled', 'disabled');
		},
		'complete': function() {
			$('.ajax-loader-modal img').hide();
			$('input, select, textarea, a, button').removeAttr('disabled', 'disabled');
		},
		'error': function(){
			alert('Помилка на сервері. Спробуйте пізніше.');
			return false;
		},
		'success': function(data, status, xhr) {
			var html = $(data), newform = html.find('#content-column form');

			//copy alert to modal window
			modal.find('.modal-body').html(html.find('.alert'));

			//copy form to modal if we found it in server response
			if (newform.length > 0) {
				modal.find('.modal-body').append(newform);

				//initialize form fields and buttons
				initEditStudentForm(newform, modal);
			} else {
				//if no form, it means success and we need to reload page
				//to get updated students list;
				//reload after  2 seconds, so that user can read
				//success message
				setTimeout(function() {
					location.reload(true);}, 500);
			}
		}
	});
}

function initEditStudentPage() {
	$('a.student-edit-form-link').click(function(event){
		var link = $(this);
		$.ajax({
			'url': link.attr('href'),
			'dataType': 'html',
			'type': 'get',
			'beforeSend': function() {
				$('.ajax-loader').show();
			},
			'complete': function() {
				$('.ajax-loader').hide();
			},
			'success': function(data, status, xhr) {
				//check if we got successfull response from the server
				if (status != 'success') {
					alert('Помилка на сервері. Спробуйте пізніше.');
					return false;
				}

				//update modal window with arrived content from the server
				var modal = $('#myModal'), html = $(data), form = html.find('#content-column form');
				modal.find('.modal-title').html(html.find('#content-column h2').text());
				modal.find('.modal-body').html(form);

				//init our edit form
				initEditStudentForm(form, modal);

				//setup and show modal window finally
				modal.modal({
					'keyboard': false,
					'backdrop': false,
					'show': true
				});
			},
			'error': function() {
				alert('Помилка на сервері. Спробуйте пізніше.');
				return false;
			}
		});
		//чтобы браузер не перешел по ссылке, 
		//а только открылось модальное окно:
		return false;
	});
}

function initAddStudentPage() {
	$('a.add-button').click(function(event){
		var modal = $('#myModal');
		modal.modal('show');
		return false
	});
}



$(document).ready(function(){
	initJournal();
	initGroupSelector();
	initDateFields();
	initDateTimeFields();
	initEditStudentPage();
	initAddStudentPage();
});