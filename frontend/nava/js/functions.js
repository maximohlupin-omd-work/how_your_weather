(function ($) {
   $('.btn-default').on('click', function (e) {
      e.preventDefault();
      var obj = $(this);

      obj.addClass('active');

      setTimeout(function () {
         obj.removeClass('active');
      }, 1500);

      // Load Boats
      if (obj.hasClass('btn-load-boats')) {
         if (!$('.load-boats-box').hasClass('open')) {
            $('.load-boats-box').slideToggle(1000);
            setTimeout (function () {
               $('.load-boats-box').addClass('open');
            }, 700);
         }
      }

      // Load Boats
      if (obj.hasClass('btn-load-destination')) {
         if (!$('.load-destinations-box').hasClass('open')) {
            $('.load-destinations-box').slideToggle(1000);
            setTimeout (function () {
               $('.load-destinations-box').addClass('open');
            }, 700);
         }
      }
   });

    $('.destinations-form').on('click', function (e) {
        var search_item = $("input").val();

        var key_list = ["city", "temperature", "wind"];

        if (search_item != ""){

         $.ajax({
            url: "/weather",
            type: "POST",
            crossDomain: true,
            data: JSON.stringify({"city": search_item}),
            dataType: "json",
            success: function (response) {
              var stat_items = $('.statistics-item');
              stat_items.each(function(idx) {
                $(this).children(":first").text(response[key_list[idx]]);
              });
            },
            error: function (xhr, status) {
            }
        });
        };
    });

   // Fade In Page
   $(document).ready(function () {
      setTimeout(function () {
         $('body').addClass('dom-ready');
           var key_list = ["city", "temperature", "wind"];

           $.ajax({
                url: "/weather_me",
                type: "GET",
                crossDomain: true,
                dataType: "json",
                success: function (response) {
                  var stat_items = $('.statistics-item');
                  stat_items.each(function(idx) {
                    $(this).children(":first").text(response[key_list[idx]]);
                  });
                },
                error: function (xhr, status) {

                }
        });

      }, 300);
   });
})(jQuery);
