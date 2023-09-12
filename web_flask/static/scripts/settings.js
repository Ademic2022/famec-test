$('.special.cards .image').dimmer({
    on: 'hover'
});

$(function() {
    $("#upload-image").click(function() {
        $(".upload-image").modal('show');
    });

    $(".new_task").modal({
        closable: true
    });
});