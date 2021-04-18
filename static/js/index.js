// Dynamic date setting, to include the current UK tax year in the homepage
const today = new Date;
const year = today.getFullYear();
if (today.getMonth() < 3) {
    $(".tax-year").text(`${year-1}/${year}`);
} else {
    $(".tax-year").text(`${year}/${year+1}`);
}

// Maintain the users scroll position when form submission occurs
$(window).scroll(function() {
    sessionStorage.scrollTop = $(this).scrollTop();
});

$(document).ready(function() {
  if (sessionStorage.scrollTop != "undefined") {
    $(window).scrollTop(sessionStorage.scrollTop);
  }
});