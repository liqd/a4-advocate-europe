import wagtail.admin.rich_text.editors.draftail.features as draftail_features
from wagtail.admin.rich_text.converters import html_to_contentstate
from wagtail.core import hooks


@hooks.register('register_rich_text_features')
def register_blockquote_feature(features):

    feature_name = 'blockquote'
    type_ = 'blockquote'
    tag = 'blockquote'

    control = {
        'type': type_,
        'label': '❝',
        'description': 'Blockquote'
    }

    features.register_editor_plugin(
        'draftail', feature_name, draftail_features.BlockFeature(control)
    )

    db_conversion = {
        'from_database_format': {
            tag: html_to_contentstate.BlockElementHandler(type_)
        },
        'to_database_format': {'block_map': {type_: tag}},
    }

    features.register_converter_rule(
        'contentstate', feature_name, db_conversion)

    features.default_features.append('blockquote')


@hooks.register('register_rich_text_features')
def register_quote_feature(features):

    feature_name = 'quote'
    type_ = 'quote'
    tag = 'quote'

    control = {
        'type': type_,
        'label': '❝',
        'description': 'Inlinequote',
        'style': {'background-color': 'yellow'}
    }

    features.register_editor_plugin(
        'draftail', feature_name, draftail_features.InlineStyleFeature(control)
    )

    db_conversion = {
        'from_database_format': {
            tag: html_to_contentstate.InlineStyleElementHandler(type_)
        },
        'to_database_format': {'style_map': {type_: tag}},
    }

    features.register_converter_rule(
        'contentstate', feature_name, db_conversion)

    features.default_features.append('quote')
