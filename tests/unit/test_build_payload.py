"""Tests build payload function"""
from model.restaurant import Restaurant
from slack import build_query_payload


def test_build_payload():
    """Tests successful build"""
    ok_data = Restaurant(
        name='My Restaurant',
        url='http://example.com',
        menu='Delicious menu'
    )
    payload = build_query_payload(ok_data)

    blocks = payload.get('blocks')
    assert blocks is not None
    assert isinstance(blocks, list)
    assert len(blocks) >= 2

    title_block = blocks[0]
    assert ok_data.url in title_block['text']['text'], 'Title should include link'
    assert ok_data.name in title_block['text']['text'], 'Title should include restaurant name'

    menu_block = blocks[1]
    assert ok_data.menu in menu_block['text']['text']


def test_use_default_url():
    """No link to restaurant"""
    data = Restaurant(name='Restaurant', menu='My Menu')
    payload = build_query_payload(data)

    title_block = payload['blocks'][0]
    title_text = title_block['text']['text']

    assert data.name in title_text
    assert f'|{data.name}>' not in title_text, "Should not construct link without URL"
