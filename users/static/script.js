window.addEventListener("scroll", bringmenu);
var lang = 'fa';

function menu() {
        if (document.getElementById("search-input").style.visibility == "hidden") {
                document.getElementById("search-input").style.visibility = "visible";
                document.getElementById("search-filter").style.visibility = "visible";
        }
        else {
                document.getElementById("search-input").style.visibility = "hidden";
                document.getElementById("search-filter").style.visibility = "hidden";
        }
}
function show_season(number) {
        filterSelection("fa");
        for (let index = 1; index < document.getElementsByClassName("season").length + 1; index++) {
                document.getElementById(String(index)).style.visibility = "none";
                document.getElementById("season-title-"+String(index)).style.backgroundColor="#303030";
        }
        document.getElementById(number).style.visibility = "visible";
        document.getElementById("season-title-"+String(number)).style.backgroundColor="#212121";
}
// window.onscroll = function() {myFunction()};
function search(n){
        if(document.getElementById("search_page").style.visibility == "hidden") {
                document.getElementById("search_page").style.visibility = "visible";
        }
        else {
                document.getElementById("search_page").style.visibility = "hidden";
        }
}
// function myFunction() {
//   if (document.documentElement.scrollTop > 50) {
//     document.getElementById("page-banner").style.visibility ="visicle";
//   } else {
//     document.getElementById("page-banner").style.visibility="hidden";
//   }
// }
window.onscroll = function() {myFunction()};
function myFunction() {
  if (document.documentElement.scrollTop > 500) {
    document.getElementById("up").style.visibility = "visible";
  } else {
    document.getElementById("up").style.visibility = "hidden";
  }
}
function upclick() {
        document.body.scrollTop = 0;
        document.documentElement.scrollTop = 0;
}
function filterSelection(c) {
  var x, i;
  x = document.getElementsByClassName("filterDiv");
  if (c == "all") c = "";
  // Add the "show" class (display:block) to the filtered elements, and remove the "show" class from the elements that are not selected
  for (i = 0; i < x.length; i++) {
    w3RemoveClass(x[i], "show");
    if (x[i].className.indexOf(c) > -1) w3AddClass(x[i], "show");
  }
}

// Show filtered elements
function w3AddClass(element, name) {
  var i, arr1, arr2;
  arr1 = element.className.split(" ");
  arr2 = name.split(" ");
  for (i = 0; i < arr2.length; i++) {
    if (arr1.indexOf(arr2[i]) == -1) {
      element.className += " " + arr2[i];
    }
  }
}

// Hide elements that are not selected
function w3RemoveClass(element, name) {
  var i, arr1, arr2;
  arr1 = element.className.split(" ");
  arr2 = name.split(" ");
  for (i = 0; i < arr2.length; i++) {
    while (arr1.indexOf(arr2[i]) > -1) {
      arr1.splice(arr1.indexOf(arr2[i]), 1);
    }
  }
  element.className = arr1.join(" ");
}

// Add active class to the current control button (highlight it)
var btnContainer = document.getElementById("myBtnContainer");
var btns = btnContainer.getElementsByClassName("btn");
for (var i = 0; i < btns.length; i++) {
  btns[i].addEventListener("click", function() {
    var current = document.getElementsByClassName("active");
    current[0].className = current[0].className.replace(" active", "");
    this.className += " active";
  });
}