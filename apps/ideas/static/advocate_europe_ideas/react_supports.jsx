let SupportButton = require('./SupportButton')
let React = require('react')
let ReactDOM = require('react-dom')

module.exports.renderSupports = function (el) {
  let supports = el.getAttribute('data-supports')
  let props = JSON.parse(el.getAttribute('data-attributes'))
  ReactDOM.render(<SupportButton {...props} />, el)
}
