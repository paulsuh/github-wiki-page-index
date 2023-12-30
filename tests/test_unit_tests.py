from pytest import fixture

import src.github_wiki_page_index.generate_wiki_page_index as generate_wiki_page_index
from src.github_wiki_page_index.generate_wiki_page_index import (
    _add_page_to_tag_dict,
    _parse_args,
    _scan_line_for_tags,
    _render_tag_tree,
)


@fixture
def example_tag_dict():
    return {
        "foo": {
            "bar": {"baz": {"untagged": {"test-page"}}, "untagged": set()},
            "untagged": set(),
        },
        "untagged": set(),
    }


def test_add_page_to_tag_dict(example_tag_dict):
    tag_dict = {"untagged": set()}
    tag_to_add = "foo-bar-baz"
    page_name = "test-page"

    _add_page_to_tag_dict(page_name, tag_to_add, tag_dict)
    assert tag_dict == example_tag_dict


def test_parse_args():
    namespace = _parse_args(["./wiki", "--insert", "--untagged-after"])

    assert namespace.wiki_dir == "./wiki"
    assert namespace.insert is True
    assert namespace.untagged_after is True


def test_scan_line_for_tags():
    tags_list = _scan_line_for_tags("Tags: foo foo-bar blah baz")
    assert tags_list == ["foo", "foo-bar", "blah", "baz"]


def test_render_tag_tree(example_tag_dict):
    generate_wiki_page_index.untagged_after = False
    generate_wiki_page_index._setup()
    rendered_tree = _render_tag_tree(example_tag_dict)

    assert (
        rendered_tree
        == """## foo

### bar

#### baz

[test page](wiki/test-page)

"""
    )
