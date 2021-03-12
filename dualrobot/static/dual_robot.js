	// Linus Movement
$('#up').on('mousedown', function(){
	$.get('/forward');
	});
$('#up').on('mouseup', function(){
	$.get('/stop');
	});
$('#down').on('mousedown', function(){
	$.get('/backward');
	});
$('#down').on('mouseup', function(){
	$.get('/stop');
	});
$('#left').on('mousedown', function(){
	$.get('/left');
	});
$('#left').on('mouseup', function(){
	$.get('/stop');
	});
$('#right').on('mousedown', function(){
	$.get('/right');
	});
$('#right').on('mouseup', function(){
	$.get('/stop');
	});
	// Linus Eye
$('#linus').on('mousedown', function(){
	$.get('/eyeon');
	});
$('#linus').on('mouseup', function(){
	$.get('/eyeoff');
	});
// Torvalds movement
$('#north').on('mousedown', function(){
	$.get('/up');
	});
$('#north').on('mouseup', function(){
	$.get('/stop2');
	});
$('#south').on('mousedown', function(){
	$.get('/down');
	});
$('#south').on('mouseup', function(){
	$.get('/stop2');
	});
$('#west').on('mousedown', function(){
	$.get('/west');
	});
$('#west').on('mouseup', function(){
	$.get('/stop2');
	});
$('#east').on('mousedown', function(){
	$.get('/east');
	});
$('#east').on('mouseup', function(){
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
