(function ($) {
  var dirtyFlag = 'safeFormDirty'

  var initDirtyChecks = function () {
    $(document).on('input keyup paste change', 'form[data-safe-form]', function (event) {
      var $form = $(this)
      $form.data(dirtyFlag, true)
    })
  }

  var initSafeExits = function () {
    $(document).on('click', 'a[data-safe-exit]', function (event) {
      var $exit = $(this)
      var formName = $exit.data('safeExit')
      var $form = $('form[data-safe-form="' + formName + '"]')

      if ($form.data(dirtyFlag)) {
        event.preventDefault()
        var $modal = $form.find('#' + formName + 'ExitModal')
        $modal.find('#save').attr('name', 'next').attr('value', $exit[0].pathname)
        $modal.find('#discard').attr('href', $exit.attr('href'))
        $modal.modal({
          show: true
        })
      }
    })
  }

  initDirtyChecks()
  initSafeExits()
})(window.jQuery)
