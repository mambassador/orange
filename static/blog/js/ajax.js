$(function () {

  /* Functions */

  var loadForm = function () {
    var link = $(this);
    $.ajax({
      url: link.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-contact .modal-content").html("");
        $("#modal-contact").modal("show");
      },
      success: function (data) {
        $("#modal-contact .modal-content").html(data.html_form);
      }
    });
  };

var showSuccessMessage = function (message) {
  var successHtml = '<div class="alert alert-success" role="alert">' + message + '</div>';
  $("#modal-contact .modal-content").html(successHtml);
};

  var saveForm = function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
     success: function (data) {
        if (data.form_is_valid) {
          showSuccessMessage(data.message);
          setTimeout(function () {
            $("#modal-contact").modal("hide");
          }, 2000); // Hide the modal after 2 seconds
        } else {
          $("#modal-contact .modal-content").html(data.html_form);
        }
      },
      error: function (xhr, status, error) {
        console.error(error);
      }
    });
    return false;
  };


  /* Binding */

  // Create contact
  $(".js-create-contact").click(loadForm);
  $("#modal-contact").on("submit", ".js-contact-create-form", saveForm);
});