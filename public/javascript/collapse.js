$(function() {
    $('.clickable').on('click', function() {
        var effect = $(this).data('effect');
        $('#statistics')[effect]();
    })

    $('.stat').on('click', function() {
        $('#statistics').fadeIn("slow");
    })
})
