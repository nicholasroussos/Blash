
$('img.java-test').on('click', function() {
	var blah = $('img.java-test')
	var truthy = blah.hasClass('test-gif-2')
	if (truthy == true){
		blah.removeClass('test-gif-2');
		blah.addClass('test-gif');
		}
	else {
		blah.addClass('test-gif-2');
		blah.removeClass('test-gif');
		}
});

$('#forward-button').on('click', function() {
	var image_1 = $('#slide1');
	var image_1_bool = image_1.hasClass('slideshow-active');

	var image_2 = $('#slide2');
	var image_2_bool = image_2.hasClass('slideshow-active');

	var image_3 = $('#slide3');
	var image_3_bool = image_3.hasClass('slideshow-active');

	var image_4 = $('#slide4');
	var image_4_bool = image_4.hasClass('slideshow-active'); 

	if (image_1_bool == true) {
		image_1.removeClass('slideshow-active');
		image_1.addClass('slideshow-inactive');
		image_2.removeClass('slideshow-inactive');
		image_2.addClass('slideshow-active');
	} else if (image_2_bool == true) {
		image_2.removeClass('slideshow-active');
		image_2.addClass('slideshow-inactive');
		image_3.removeClass('slideshow-inactive');
		image_3.addClass('slideshow-active');
	} else if (image_3_bool == true) {
		image_3.removeClass('slideshow-active');
		image_3.addClass('slideshow-inactive');
		image_4.removeClass('slideshow-inactive');
		image_4.addClass('slideshow-active');
	} else {
		image_4.removeClass('slideshow-active');
		image_4.addClass('slideshow-inactive');
		image_1.removeClass('slideshow-inactive');
		image_1.addClass('slideshow-active');
	}
});
//back function
$('#back-button').on('click', function() {
	var image_1 = $('#slide1');
	var image_1_bool = image_1.hasClass('slideshow-active');

	var image_2 = $('#slide2');
	var image_2_bool = image_2.hasClass('slideshow-active');

	var image_3 = $('#slide3');
	var image_3_bool = image_3.hasClass('slideshow-active');

	var image_4 = $('#slide4');
	var image_4_bool = image_4.hasClass('slideshow-active'); 
	if (image_1_bool == true) {
		image_1.removeClass('slideshow-active');
		image_1.addClass('slideshow-inactive');
		image_4.removeClass('slideshow-inactive');
		image_4.addClass('slideshow-active');
	} else if (image_2_bool == true) {
		image_2.removeClass('slideshow-active');
		image_2.addClass('slideshow-inactive');
		image_1.removeClass('slideshow-inactive');
		image_1.addClass('slideshow-active');
	} else if (image_3_bool == true) {
		image_3.removeClass('slideshow-active');
		image_3.addClass('slideshow-inactive');
		image_2.removeClass('slideshow-inactive');
		image_2.addClass('slideshow-active');
	} else {
		image_4.removeClass('slideshow-active');
		image_4.addClass('slideshow-inactive');
		image_3.removeClass('slideshow-inactive');
		image_3.addClass('slideshow-active');
	}
});

