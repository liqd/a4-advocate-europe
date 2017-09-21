let api = require('adhocracy4').api
let django = require('django')
let React = require('react')

class SupportButton extends React.Component {

  constructor (props) {
    super(props)

    this.state = {
      supports: this.props.supports,
      userHasSupport: this.props.userSupport !== null,
      userSupport: this.props.userSupport,
      userSupportId: this.props.userSupportId
    }
  }

  handleSupportCreate (number) {
    api.rating.add({
      urlReplaces: {
        objectPk: this.props.objectId,
        contentTypeId: this.props.contentType
      },
      value: number
    }).done(function (data) {
      this.setState({
        supports: data.meta_info.positive_ratings_on_same_object,
        userSupport: data.meta_info.user_rating_on_same_object_value,
        userHasSupport: true,
        userSupportId: data.id
      })
    }.bind(this))
  }

  handleSupportModify (number, id) {
    api.rating.change({
      urlReplaces: {
        objectPk: this.props.objectId,
        contentTypeId: this.props.contentType
      },
      value: number
    }, id)
      .done(function (data) {
        this.setState({
          supports: data.meta_info.positive_ratings_on_same_object,
          userSupport: data.meta_info.user_rating_on_same_object_value
        })
      }.bind(this))
  }

  updateSupport (e) {
    e.preventDefault()
    if (this.state.userHasSupport) {
      var number
      if (this.state.userSupport === 1) {
        number = 0
      } else {
        number = 1
      }
      this.handleSupportModify(number, this.state.userSupportId)
    } else {
      this.handleSupportCreate(1)
    }
  }

  render () {
    if(this.props.renderMobile) {
      return (
          <button
            href="#"
            onClick={this.updateSupport.bind(this)}
            class="btn btn-idea"
            disabled={this.props.isReadOnly}
            role="button"
            className="btn btn-support"
            aria-label="{django.gettext('Support')}">
              {this.state.userSupport == 1
                ? <i className="fa fa-heart" aria-hidden="true"></i>
                : <i className="fa fa-heart-o" aria-hidden="true"></i>
              }
            <span class="support-count"> {this.state.supports}</span>
            <p class="btn-idea-label">{django.gettext('Support')}</p>
          </button>
      )
    }
    else {
      return (
        <div className="btn-group ideadetail-support-btn-group" role="group">
          <button
            className="btn btn-primary"
            disabled={this.props.isReadOnly}
            onClick={this.updateSupport.bind(this)}>
            {this.state.userSupport == 1
              ? <i className="fa fa-heart" aria-hidden="true"></i>
              : <i className="fa fa-heart-o" aria-hidden="true"></i>
            } {django.gettext('Support')}
          </button>
          <div className="btn btn-addon">{this.state.supports}</div>
        </div>
      )
    }
  }

}

module.exports = SupportButton
