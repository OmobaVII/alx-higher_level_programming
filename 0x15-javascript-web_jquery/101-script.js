// adds, removes and clears LI elements from a list when the user clicks
document.addEventListener('DOMContentLoaded', function () {
  $('#add_item').click(
    function () {
      $('UL.my_list').append('<li>Item</li>');
    }
  );
  $('#remove_item').click(
    function () {
      $('UL.my_list li:last-child').remove();
    }
  );
  $('#clear_list').click(
    function () {
      $('UL.my_list').empty();
    }
  );
});
