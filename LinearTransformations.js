var scaleF, aScale; // scaling factor
var axisWidth = 3; // width of the x-y axis
var x = 200, y = 200, xC, yC, xP, yP;  // x and y coordinates

var v2;
var v;
var u;
var f = 0;

draw = function() {
    background(255, 255, 255);
    var v1 = new PVector(1.12, 1.30);
    f = 670;
    var A = [ [cos(f), -sin(f)], 
          [sin(f),  cos(f)] ];
    scaleF = 100;  // scale factor
    aScale = 100;  // axis scale
    
    stroke(0, 0, 0);
    strokeWeight(axisWidth);  //  xy-axis
    
    line(0, 200, 400, 200); // x-axis centered at y: 200
    line(200, 0, 200, 400); // y-axis centered at x: 200
    //  to make the markers
    for(var i = 0; i <= 400; i += aScale)
    {
        line(i, 195, i, 205);
        line(195, i, 205, i);
    }
    // reset vectors
    u = [0,0];
    v = [0,0];
    
    
    // vector component assignment
    v[0] = v1.x*scaleF;  // vector component s x & y
    v[1] = (-1)*v1.y*scaleF; // component y
    
    
    for(var row = 0; row < A.length; row++)
    {
        for(var col = 0; col < A[0].length; col++)
        {
            if(row === 0){
                u[0] += A[row][col] * v[col];
            } else if(row === 1) {
                u[1] += A[row][col] * v[col];
            }
        }
    }
    
    stroke(255, 0, 0);
    line(x, y, x + v[0], y + v[1]); // original vector
    stroke(75, 224, 0);
    line(x, y, x + u[0], y + u[1]); // transformed vector
};
