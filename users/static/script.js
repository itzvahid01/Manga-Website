window.addEventListener("scroll", bringmenu);

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

// نمایش فصل انتخاب شده
// تابع نمایش فصل
function show_season(number) {
  // پنهان کردن تمام فصل‌ها
  var seasons = document.getElementsByClassName("season");
  for (var i = 0; i < seasons.length; i++) {
      seasons[i].style.display = "none"; // پنهان کردن فصل
      seasons[i].classList.remove("active"); // حذف کلاس فعال
  }

  // غیرفعال کردن عنوان تمام فصل‌ها
  var seasonTitles = document.getElementsByClassName("season-title");
  for (var j = 0; j < seasonTitles.length; j++) {
      seasonTitles[j].classList.remove("active");
  }

  // نمایش فصل مورد نظر
  var selectedSeason = document.getElementById(String(number));
  if (selectedSeason) {
      selectedSeason.style.display = "block"; // نمایش فصل
      selectedSeason.classList.add("active"); // اضافه کردن کلاس فعال
  }

  // فعال کردن عنوان فصل مورد نظر
  var selectedTitle = document.getElementById("season-title-" + number);
  if (selectedTitle) {
      selectedTitle.classList.add("active");
  }
}

// تابع فیلتر زبان
function filterSelection(c) {
  var x = document.getElementsByClassName("filterDiv");
  var seasonTitles = document.getElementsByClassName("btn");
  for (var j = 0; j < seasonTitles.length; j++) {
      seasonTitles[j].classList.remove("active");
  }
  // فعال کردن عنوان فصل مورد نظر
  var selectedTitle = document.getElementById("btn-" + c);
  if (selectedTitle) {
      selectedTitle.classList.add("active");
  }
  // اگر "همه" انتخاب شود، تمام عناصر نمایش داده شوند
  if (c === "all") {
      for (var i = 0; i < x.length; i++) {
          x[i].style.display = "inline-block";
      }
      return;
  }

  // مخفی کردن تمام عناصر
  for (var i = 0; i < x.length; i++) {
      x[i].style.display = "none";
  }

  // نمایش عناصری که شامل کلاس مورد نظر هستند
  for (var i = 0; i < x.length; i++) {
      if (x[i].classList.contains(c)) {
          x[i].style.display = "inline-block";
          
      }
  }
}
// فعال کردن دکمه‌های زبان
document.addEventListener("DOMContentLoaded", function () {
  var buttons = document.querySelectorAll("#myBtnContainer .btn");
  buttons.forEach(function (button) {
      button.addEventListener("click", function () {
          // حذف کلاس active از تمام دکمه‌ها
          buttons.forEach(function (btn) {
              btn.classList.remove("active");
          });

          // اضافه کردن کلاس active به دکمه فعال
          this.classList.add("active");
      });
  });
});