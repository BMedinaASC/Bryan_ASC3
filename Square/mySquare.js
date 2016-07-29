var x = 10;
var stop = true
function setup()
{
	createCanvas(500, 500);
}

function draw()
{
	background(28, 173, 240);
	rectMode(CENTER);
	rect(x, 250, 100, 100);
	x += 1;

	if(x > width/2 && stop)
	{
		stop = false;
		myButton = document.createElement("button");
		myButton.textContent = "Change Direction!";
		$("body").append(myButton);
	}
}