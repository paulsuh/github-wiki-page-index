from src.github_wiki_page_index.generate_wiki_page_index import (
    _add_page_to_tag_dict,
    _parse_args,
    _scan_line_for_tags,
)


def test_add_page_to_tag_dict():
    tag_dict = {"untagged": set()}
    tag_to_add = "foo-bar-baz"
    page_name = "test_page"
    result_dict = {
        "foo": {
            "bar": {"baz": {"untagged": {"test_page"}}, "untagged": set()},
            "untagged": set(),
        },
        "untagged": set(),
    }

    _add_page_to_tag_dict(page_name, tag_to_add, tag_dict)
    assert tag_dict == result_dict


def test_parse_args():
    namespace = _parse_args(["./wiki", "--insert", "--untagged-after"])

    assert namespace.wiki_dir == "./wiki"
    assert namespace.insert is True
    assert namespace.untagged_after is True


def test_scan_line_for_tags():
    tags_list = _scan_line_for_tags("Tags: foo foo-bar blah baz")
    assert tags_list == ["foo", "foo-bar", "blah", "baz"]
