jQuery(document).ready(function() {
    $('span[id]').each (function(index) {
        var id = $(this).attr("id");
        var datetime = $(this).text();
        if (id == "full-datetime") {
            $(this).text(moment(datetime).format("D MMM YYYY, hh:mm a"));
        } else if (id == "full-date") {
            $(this).text(moment(datetime).format("D MMM YYYY"));
        } else if (id == "date-only") {
            $(this).text(moment(datetime).format("D"));
        } else if (id == "month-only") {
            $(this).text(moment(datetime).format("MMM"));
        }
    });

    $("a[id='blog-url']").each(function(){
        var datetime = $(this).attr("datetime");
        var currentHref = $(this).attr('href');
        var hrefs = currentHref.split('/');
        $(this).attr('href', '/' + hrefs[1] + '/' + moment(datetime).format("YYYY") + '/' + moment(datetime).format("MM") + '/' + moment(datetime).format("DD") + '/' + hrefs[2]);
    });
});