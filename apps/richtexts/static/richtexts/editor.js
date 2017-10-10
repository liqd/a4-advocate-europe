(function($){
  let Quill = window.Quill
  let BlockEmbed = Quill.import('blots/block/embed');

  class A4ImageBlot extends BlockEmbed {
    static create(value) {
      let node = super.create()
      node.setAttribute('alt', value.alt)
      node.setAttribute('src', value.url)
      node.setAttribute('class', value.style || '')
      return node
    }

    static value(node) {
      return {
        alt: node.getAttribute('alt'),
        url: node.getAttribute('src'),
        style: node.getAttribute('style')
      }
    }
  }
  A4ImageBlot.blotName = 'a4image'
  A4ImageBlot.tagName = 'img'

  Quill.register(A4ImageBlot)

  $(function() {
    var quill = new Quill('.richtext', {
      formats: ['bold', 'italic', 'underline', 'strike', 'link', 'a4image'],
      modules: {
        toolbar: [['bold', 'italic', 'underline', 'strike'], ['link', 'a4image']]
      }
    })

    var toolbar = quill.getModule('toolbar');
    toolbar.addHandler(
      'a4image',
      function selectImage() {
        window.ModalWorkflow({
         url: '/richtexts/uploadimage',
          urlParams: {},
          responses: {
            imageChosen: function(imageData) {
              let range = quill.getSelection(true);
              quill.insertText(range.index, '\n', Quill.sources.USER)
              quill.insertEmbed(range.index + 1, 'a4image', imageData, Quill.sources.USER)
              quill.setSelection(range.index + 2, Quill.sources.SILENT)
            }
          }
        });
      }
    )

  })





  // tinymce.init({
  //   selector: '.richtext',
  //   inline: true,
  //   plugins: 'link image',
  //   toolbar: 'undo redo | italic bold underline | link image',
  //   statusbar: 'false',
  //   menubar: 'false',

  //   // configure link plugin
  //   target_list: false,

  //   images_upload_url: '/tinymce/upload',
  //   image_dimensions: false,
  //   image_class_list: [
  //     {title: 'Centered', value: ''},
  //     {title: 'On the left', value: 'richtext-image-left'},
  //     {title: 'On the right', value: 'richtext-image-right'}
  //   ]
  // });

})(window.jQuery);


// Schamelessly stolen from boostrap
