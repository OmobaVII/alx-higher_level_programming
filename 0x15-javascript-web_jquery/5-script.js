// Adds a <li> element to a list whe the user clickes on the tag add_item

$('#add_item').click(
  function () {
    $('UL.my_list').append('<li>Item</li>');
  }
);
