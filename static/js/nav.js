function myfunction() {
    var x = document.getElementById("sidebar");

    if (x.style.left == "-100%") {
        x.style.left = "0";
    } else {
        x.style.left = "-100%";
    }
}