// Bind dept list even
$(document).ready(function() {
    loadDeptList();
});

function dumpList(data) {
    $.each(data, function (key, item){
        var html_code = "<div id='" + item.model + "-" + item.pk +"' class='list-item list-item-new psbutton'>" +
            "<div class='creation-text'><span class='fa'>" + item.fields.title +
            "</span><form action='' method='DELETE'><input type='hidden' value='" + item.pk +
            "'><input type='submit' value='×'></form></div></div>";
        $('#departments-list').append(html_code)
    });
}

function renewDepts(data){
    $('#departments-list').empty();
    dumpList(data);
}

// AJAX for list department
function loadDeptList() {
    //console.log("create post is working!");
    $.ajax({
        url : "",
        type : "GET",
        data : {  },

        // handle a successful response
        success : function(json) {
            var departments = $.parseJSON(json);
            renewDepts(departments);
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
}
