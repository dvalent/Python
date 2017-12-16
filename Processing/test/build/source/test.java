import processing.core.*; 
import processing.data.*; 
import processing.event.*; 
import processing.opengl.*; 

import java.util.HashMap; 
import java.util.ArrayList; 
import java.io.File; 
import java.io.BufferedReader; 
import java.io.PrintWriter; 
import java.io.InputStream; 
import java.io.OutputStream; 
import java.io.IOException; 

public class test extends PApplet {

int cols = 100;
int rows = 100;
//int [][] grid = [rows][cols];

public void setup() {

background(51);


}



public void draw() {

for (int i = 0 ; i < cols; i=+5){

  for(int j = 0 ; j< cols; j=+5){
    println(i);
    rect(i,j,5,5);

  }
}

}
  public void settings() { 
size(500,500); }
  static public void main(String[] passedArgs) {
    String[] appletArgs = new String[] { "test" };
    if (passedArgs != null) {
      PApplet.main(concat(appletArgs, passedArgs));
    } else {
      PApplet.main(appletArgs);
    }
  }
}
