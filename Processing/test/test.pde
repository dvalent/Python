int cols = 100;
int rows = 100;
int [][] grid = new int[rows][cols];

int [][] next;


void setup() {

        size(500,500);
        background(51);

        for ( int i = 0; i < cols; i++) {
                for ( int j = 0; j < rows; j++) {

                        grid[i][j] = int(random(2));
                }
        }

}



void draw() {

        for (int i = 0; i < cols; i++) {
                for (int j = 0; j <  rows; j++) {

                        if ( grid[i][j] == 0) {

                                stroke(255,0,0);
                                strokeWeight(2);
                                point(i*(width/cols),j*(height/rows));

                        }


                }

        }




}
