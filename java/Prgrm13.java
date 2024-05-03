/*Create a Graphics package that has classes and interfaces for figures Rectangle, Triangle, Square and Circle. Test the package by finding the area of these figures.*/

import graphics.Circle;
import graphics.Rectangle;
import graphics.Triangle;
import graphics.Square;
class Prgrm13
{
	public static void main(String arg[])
	{
		Circle c1=new Circle();
		System.out.println("Circle Area = "+c1.area(10));
		
		Rectangle r1=new Rectangle();
		System.out.println("Rectangle Area = "+r1.area(10,10));
		
		Triangle t1=new Triangle();
		System.out.println("Triangle Area = "+t1.area(10,10));
		
		Square s1=new Square();
		System.out.println("Square Area = "+s1.area(10));
		
	}
}

/*
Circle Area = 314.0
Rectangle Area = 100.0
Triangle Area = 50.0
Square Area = 100.0
*/
