if ( !$('.errorlist').length ) {
    $('#resolution_form').hide();
}

$('#switch_resolution_form, #resolution_form_control').click(function () {
    $('#resolution_form').toggle('fast');
    $('#resolution_form_control').toggle('fast');
    $('#switch_resolution_form span').toggleClass(function(){
        if ($(this).hasClass('glyphicon-plus')) {
            $(this).removeClass('glyphicon-plus');
            return 'glyphicon-minus';
        } else {
            $(this).removeClass('glyphicon-minus');
            return 'glyphicon-plus';
        }
    })
});

$('*[data-confirm="true"]').on('click', function() {
    var resolution = $(this).parent().prev("td").text();
    return confirm("Вы уверенны, что хотите удалить резолюцию '" + resolution + "' ?");
});