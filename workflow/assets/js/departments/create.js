// form helper
var fh = new FormHelper('dept-form');
// dept form selector
var form = $('#dept-form');

// Bind create dept even
form.on('submit', function(event){
    event.preventDefault();
    fh.clean();
    create_dept();
});

// Bind create dept even
form.on('reset', function(event){
    fh.clean();
});

// AJAX for department create

function create_dept() {
    $.ajax({
        url : "",
        type : "POST",
        data : { title : $('#title').val() },

        // handle a successful response
        success : function(json) {
            $('#title').val(''); // remove the value from the input
            fh.successMessage(json['success']);
            loadDeptList();
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            //$('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
            //    " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            //console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            var errors = $.parseJSON(xhr.responseText);
            fh.errorMessage('Форма заполненна некорректно!');
            fh.showErrors(errors.errors);
        }
    });
}