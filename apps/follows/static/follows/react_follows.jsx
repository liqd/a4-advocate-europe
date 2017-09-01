var FollowButton = require('./FollowButton')
var React = require('react')
var ReactDOM = require('react-dom')

module.exports.renderFollow = function (el) {
  let followable = el.getAttribute('data-followable')
  ReactDOM.render(<FollowButton followable={followable} />, el)
}
