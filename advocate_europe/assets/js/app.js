var widget = require('adhocracy4').widget
var ReactComments = require('adhocracy4').comments
var ReactFollow = require('../../../apps/follows/static/follows/react_follows.jsx')
var ReactSupport = require('../../../apps/ideas/static/advocate_europe_ideas/react_supports.jsx')
var $ = window.jQuery = window.$ = require('jquery')

require('../../../advocate_europe/assets/js/advocate_europe')

$(function () {
  widget.initialise('a4', 'comment', ReactComments.renderComment)
  widget.initialise('ae', 'follows', ReactFollow.renderFollow)
  widget.initialise('ae', 'supports', ReactSupport.renderSupports)
})
