window.onload=function(){
    document.getElementById('btn').addEventListener("click", function() {
        document.getElementById('file').click();
    });
    
}

var loadFile = function(event) {
    var image = document.getElementById('output');
    image.src = URL.createObjectURL(event.target.files[0]);
};