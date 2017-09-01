var ReactComments = require('adhocracy4').comments
var ReactRatings = require('adhocracy4').ratings
var ReactFollow = require('../../../apps/follows/static/follows/react_follows.jsx')

require('../../../advocate_europe/assets/js/advocate_europe')

module.exports = {
  'renderComment': ReactComments.renderComment,
  'renderRatings': ReactRatings.renderRatings
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
