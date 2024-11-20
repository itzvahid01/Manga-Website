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
        for (let index = 1; index < document.getElementsByClassName("season").length + 1; index++) {
                document.getElementById(String(index)).style.visibility = "hidden";
        }
        document.getElementById(number).style.visibility = "visible";
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
function menu_options(n,w) {
        if (w==0) {
                document.getElementById('manga_menu').style.display = "flex";
                document.getElementById('manga_menu').style.display = "visibility";
                if (n==0){
                        document.getElementById('manga_menu').style.display = "flex";
                }
                else {
                        document.getElementById('manga_menu').style.display = "none";
                }
        }else if (w==1) {
                document.getElementById('manhwa_menu').style.display = "flex";
                document.getElementById('manhwa_menu').style.display = "visibility";
                if (n==0){
                        document.getElementById('manhwa_menu').style.display = "flex";
                }
                else {
                        document.getElementById('manhwa_menu').style.display = "none";
                }
        } else if (w==2) {
                document.getElementById('manha_menu').style.display = "flex";
                document.getElementById('manha_menu').style.display = "visibility";
                if (n==0){
                        document.getElementById('manha_menu').style.display = "flex";
                }
                else {
                        document.getElementById('manha_menu').style.display = "none";
                }
        }
}