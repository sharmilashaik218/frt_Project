$(document).ready(function(){
    // Initialize carousel
    $('#heroCarousel').carousel({
        interval: 5000, // Carousel slide interval in milliseconds
        pause: 'hover'  // Pause the carousel on mouse hover
    });

    $('#teamCarousel').carousel({
        interval: 10000, // Carousel slide interval in milliseconds for team section
        pause: 'hover'  // Pause the carousel on mouse hover
    });

    // Smooth scrolling for links
    $("a").on('click', function (event) {
        if (this.hash !== "") {
            event.preventDefault();
            var hash = this.hash;

            $('html, body').animate({
                scrollTop: $(hash).offset().top
            }, 800, function () {
                window.location.hash = hash;
            });
        }
    });

    // Animations on scroll
    $(window).on('scroll', function () {
        $('.service-card, .about-section img, .contact-section, .testimonial-card, .team-section img, .news-card').each(function () {
            if ($(this).offset().top < $(window).scrollTop() + $(window).height() - 100) {
                $(this).addClass('animate');
            }
        });
    });

    // Trigger animations on load
    $(window).on('load', function () {
        $('.service-card, .about-section img, .contact-section, .testimonial-card, .team-section img, .news-card').each(function () {
            $(this).addClass('animate');
        });
    });

    // Form submission handling (optional)
    $('form').on('submit', function(event) {
        event.preventDefault();
        // Basic form submission handling, you can enhance this with actual form submission logic
        alert('Message sent! Thank you for contacting us.');
        $(this).trigger('reset');
    });
});
