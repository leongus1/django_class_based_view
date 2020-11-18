$(document).ready(function () {
    // window.addEventListener("load", highlightSummarySentences , false); 

    function getCookie(cname) {
      var name = cname + "=";
      var ca = document.cookie.split(";");
      for (var i = 0; i < ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == " ") c = c.substring(1);
        if (c.indexOf(name) == 0) return c.substring(name.length, c.length);
      }
      return "";
    }

    $('.delete-prod').click(function (e) {
        e.preventDefault();
        var prod_id = $(this).attr('prod-id')
        console.log(prod_id)
        $.ajax({
        url: "/products/" + prod_id,
        method: "DELETE",
        beforeSend: function (xhr) {
            xhr.setRequestHeader("X-CSRFToken", getCookie("csrftoken"));
        },
        success: function () {
            console.log("Delete this thing");
            window.location.href = "/";
        },
        });
    })


})
