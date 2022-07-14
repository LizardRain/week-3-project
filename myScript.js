var x_pos = null;
var y_pos = null;
var tool = null;



function startLine(e){
    x_pos = e.offsetX;
    y_pos = e.offsetY;
}

function endLine(e){
    var temp_x = e.offsetX;
    var temp_y = e.offsetY;
    var canvas = document.querySelector('canvas');
    var ctx = canvas.getContext('2d');
    ctx.beginPath();
    ctx.lineWidth = "5";
    ctx.strokeStyle = "black";
    ctx.moveTo(x_pos, y_pos);
    ctx.lineTo(temp_x, temp_y);
    ctx.stroke();
}