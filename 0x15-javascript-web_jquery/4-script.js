$(function() {
  $("#toggle_header").on("click", function() {
    var header = $("header");
    if (header.hasClass("red")) {
      header.removeClass("red").addClass("green");
    } else {
      header.removeClass("green").addClass("red");
    }
  });
});
