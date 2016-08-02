var xChange = 0;
var yChange = 0;
var xEllipse = 30;
var yEllipse = 30;

function countPixels(array, value)
{
	var count = 0
	for (var i = 0; i < array.length; i++)
	{
		if (array[i] == value)
		{
			count += 1;
		}
	}
	return count;
}

function setup()
{
	createCanvas(600, 600);
	maxBlack = countPixels(pixels, 0)
	maxEndZone = countPixels(pixels, 255)
}

function draw()
{
	if(key === 'w')
	{
		yChange -= 1;
	}

	if(key === 'a')
	{
		xChange -= 1;
	}

	if(key === 's')
	{
		yChange += 1;
	}

	if(key === 'd')
	{
		xChange += 1;
	}

	currentBlack = countPixels(pixels, 0)
	currentEndZone = countPixels(pixels, 0)

	if (currentBlack < maxBlack)
	{
		xEllipse = 30;
		yEllipse = 30;
	}

	if (currentEndZone < maxEndZone)
	{
		text("You Win!", 280, 280);
	}

	background(0, 0, 0);

	//rect(xPos, yPos, width, height)
    fill(0,255,0);
    //rectMode(CENTER)
    rect(0,0,600,50);
    noStroke();
    rect(550,50,50,600);
    noStroke();
    rect(0,550,600,50);
    noStroke();
    rect(0,100,50,450);
    noStroke();
    fill(0,255,0);
    fill(255,0,0);
    rect(0,100,50,50);
    noStroke()
    fill(255,0,255)
    ellipse(xEllipse + xChange, yEllipse + yChange, 20, 20);


}

