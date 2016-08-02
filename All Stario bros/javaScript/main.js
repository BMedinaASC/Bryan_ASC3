var space;

function preload()
{

}

function setup()
{
	space = loadImage("spaceBackground.jpg");
	createCanvas(1024, 600);
}

function draw()
{
	background(120, 0, 120);
	var floor = createSprite(10, 550, 2048, 30);
	floor.shapeColor = color(139,69,19);
	drawSprites();
}