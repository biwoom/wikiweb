var ToC =
  "<nav role='navigation' class='table-of-contents'>" +
    "<h2>table of contents</h2>" +
    "<ul>";

var newLine, el, title, link, tocclass;

$("h1,h2,h3,h4,h5,h6").each(function() {

  el = $(this);
  title = el.text();
  link = "#" + el.attr("id");
  toc_class = "toc_" + el.get(0).tagName;

  newLine =
    "<li class='" + toc_class + "'>" +
      "<a href='" + link + "'>" +
        title +
      "</a>" +
    "</li>";

  ToC += newLine;

});

ToC +=
   "</ul>" +
  "</nav>";

$(".toc_auto").prepend(ToC);