var ReactComments = require('adhocracy4').comments
var ReactFollow = require('../../../apps/follows/static/follows/react_follows.jsx')
var ReactSupport = require('../../../apps/ideas/static/advocate_europe_ideas/react_supports.jsx')

require('../../../advocate_europe/assets/js/advocate_europe')

module.exports = {
  'renderComment': ReactComments.renderComment
}

var initialiseWidget = function (project, name, initialiser) {
  if (!initialiser) {
    initialiser = name
    name = project
    project = 'ae'
  }

  document.addEventListener('DOMContentLoaded', function () {
    var els = document.querySelectorAll('[data-' + project + '-widget=\'' + name + '\']')

    for (var i in els) {
      if (els.hasOwnProperty(i)) {
        initialiser(els[i])
      }
    }
  })
}

initialiseWidget('follows', ReactFollow.renderFollow)
initialiseWidget('supports', ReactSupport.renderSupports)
