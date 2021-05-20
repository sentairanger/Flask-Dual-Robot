	// Linus Movement
$('#up').on('touchstart', function(){
	$.get('/forward');
	});
$('#up').on('touchend', function(){
	$.get('/stop');
	});
$('#down').on('touchstart', function(){
	$.get('/backward');
	});
$('#down').on('touchend', function(){
	$.get('/stop');
	});
$('#left').on('touchstart', function(){
	$.get('/left');
	});
$('#left').on('touchend', function(){
	$.get('/stop');
	});
$('#right').on('touchstart', function(){
	$.get('/right');
	});
$('#right').on('touchend', function(){
	$.get('/stop');
	});
	// Linus Eye
$('#linus').on('touchstart', function(){
	$.get('/eyeon');
	});
$('#linus').on('touchend', function(){
	$.get('/eyeoff');
	});
// Torvalds movement
$('#north').on('touchstart', function(){
	$.get('/up');
	});
$('#north').on('touchend', function(){
	$.get('/stop2');
	});
$('#south').on('touchstart', function(){
	$.get('/down');
	});
$('#south').on('touchend', function(){
	$.get('/stop2');
	});
$('#west').on('touchstart', function(){
	$.get('/west');
	});
$('#west').on('touchend', function(){
	$.get('/stop2');
	});
$('#east').on('touchstart', function(){
	$.get('/east');
	});
$('#east').on('touchend', function(){
	$.get('/stop2');
	});
 // Servo Slider values
var slider = document.getElementById("myRange");
var output = document.getElementById("demo");
output.innerHTML = slider.value;

slider.oninput = function() {
  output.innerHTML = this.value;
};
var slider2 = document.getElementById("myRange2");
var output2 = document.getElementById("demo2");
output2.innerHTML = slider2.value;

slider2.oninput = function() {
  output2.innerHTML = this.value;
};

// PWM values
var slider3 = document.getElementById("myRange3");
var output3 = document.getElementById("demo3");
output2.innerHTML = slider2.value;

slider3.oninput = function() {
  output3.innerHTML = this.value;
};
var slider4 = document.getElementById("myRange4");
var output4 = document.getElementById("demo4");
output4.innerHTML = slider2.value;

slider4.oninput = function() {
  output4.innerHTML = this.value;
};
