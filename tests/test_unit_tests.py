from pytest import fixture

import src.github_wiki_page_index.generate_wiki_page_index as generate_wiki_page_index
from src.github_wiki_page_index.generate_wiki_page_index import (
    _add_page_to_tag_dict,
    _parse_args,
    _scan_line_for_tags,
    _render_tag_tree,
    generate_page_index,
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


@fixture
def run_setup():
    generate_wiki_page_index.untagged_after = False
    generate_wiki_page_index._setup()


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


def test_render_tag_tree(example_tag_dict, run_setup):
    rendered_tree = _render_tag_tree(example_tag_dict)

    assert (
        rendered_tree
        == """## foo

### bar

#### baz

[test page](wiki/test-page)

"""
    )


def test_generate_page_index(monkeypatch, run_setup):
    def return_dummy_tag_list():
        return [
            ("file1", []),
            ("file2", ["tag-subtag"]),
            ("file3", ["tag"]),
            ("file4", ["tag", "noindex"]),
        ]

    monkeypatch.setattr(
        generate_wiki_page_index, "_get_file_tags", return_dummy_tag_list
    )

    result = generate_page_index()

    assert (
        result
        == """<!--start Page Index-->

# Page Index

[file1](wiki/file1)

## tag

[file3](wiki/file3)

### subtag

[file2](wiki/file2)

<!--end Page Index-->
"""
    )
