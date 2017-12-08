var api = require('adhocracy4').api
var django = require('django')
var React = require('react')

class FollowButton extends React.Component {
  constructor (props) {
    super(props)

    this.state = {
      followed: undefined,
      follows: 0
    }
  }
  setFollow (enabled) {
    if (enabled === this.state.followed) {
      return false
    }

    api.follow.change({ enabled: enabled }, this.props.followable)
      .done((follow) => {
        this.setState({
          followed: follow.enabled,
          follows: follow.follows
        })
      })
  }
  enableFollow () {
    this.setFollow(true)
  }
  disableFollow () {
    this.setFollow(false)
  }
  componentDidMount () {
    api.follow.get(this.props.followable)
      .done((follow) => {
        this.setState({
          followed: follow.enabled || false,
          follows: follow.follows
        })
      })
  }
  renderDropdownMenu () {
    return (
      <span className='dropdown-menu' aria-labelledby='follow-dropdown'>
        <button className='dropdown-item select-item' onClick={this.disableFollow.bind(this)}>
          {!this.state.followed
                 ? <i className='fa fa-check select-item-indicator' aria-hidden='true' />
                 : null}
          <span className='select-item-title'>{django.gettext('Not watching')}</span>
          <span className='select-item-desc'>
            {django.gettext('Never be notified.')}
          </span>
        </button>
        <button className='dropdown-item select-item' onClick={this.enableFollow.bind(this)}>
          {this.state.followed
                 ? <i className='fa fa-check select-item-indicator' aria-hidden='true' />
                 : null
                }
          <span className='select-item-title'>{django.gettext('Watching')}</span>
          <span className='select-item-desc'>
            {django.gettext('Be notified if something happens in the idea.')}
          </span>
        </button>
      </span>
    )
  }
  render () {
    return (
      <span className='dropdown dropdown-follow'>
        <button className='btn btn-follow' type='button' id='follow-dropdown' data-toggle='dropdown' aria-haspopup='true' aria-expanded='false'>
          <i className={this.state.followed ? 'fa fa-eye-slash' : 'fa fa-eye'} aria-hidden='true' />&nbsp;
          <span className='btn-follow-label'>
            {this.state.followed ? django.gettext('Unwatch') : django.gettext('Watch')}
          </span>
        </button>
        {this.renderDropdownMenu()}
      </span>
    )
  }
}

module.exports = FollowButton
