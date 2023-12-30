from src.github_wiki_page_index.generate_wiki_page_index import _add_page_to_tag_dict


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
