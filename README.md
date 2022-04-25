# GitHub Wiki Page Index

This package will generate a file index for your GitHub Wiki, and
optionally insert it into the Home.md file. It can also be set up as 
a GitHub Action to auto-update the Home.md file when the wiki is 
edited. 

* Version: 0.1
* License: BSD 3-clause

## Usage

To start, clone your GitHub repo's wiki to your local file system:
```
  git clone https://github.com/paulsuh/<reponame>.wiki.git
```

There are then two modes of running the code: 

1) Generate the ToC and print it to stdout. You can then paste this 
   into your Home.md. 
    ```
    python generate_wiki_file_index.py <path to cloned wiki>
    ```

2) Have the ToC automatically inserted into your Home.md.

    ```
    python generatetoc.py --insert <path to cloned wiki>
    ```

## Tagging

You can place a line of text containing tags in each page. The 
script will scan for the first line that starts with "Tags:" and use 
that to list the page in a section. Only one line is used, so it is 
most efficient if the tags are put on the first line of the file. 

Tags are snake case and case-sensitive. `Tag_one` and `Tag_One` are 
considered to be two different tags. When the headings are rendered, 
underscores are turned into spaces. A page can have any number of 
tags.   

Tags can be hierarchical, with segments separated by a hyphen ('-'). 
For example, `Tag_Level_One-Level_Two-Subtag_Level_Three` will produce 
a structure that looks like:  

>##Tag Level One
>### Level Two
>#### Subtag Level Three

The first part of the page index will the pages that have no tags, 
listed in alphabetical order. Then, each tag will have a section 
listing the pages that have that tag, and then subheadings for pages 
that are tagged with hierarchical tags. 

## Deployment

Use the Docker image and supply the following four environment 
variables: 
* REPO_NAME: formatted as <username>/<reponame>. The 
  https://github.com/ prefix and the .wiki suffix will be added 
  automatically. 
* AUTH_TOKEN: authentication token to allow content to be pushed. 
  Generate this in GitHub. 
* USERNAME: does not need to be a real user, just needed for 
  commit messages. 
* USER_EMAIL: does not need to be a real user, just needed for 
    commit messages.

The Docker image will automatically clone the wiki, insert the page 
index, commit, and push the wiki back up to GitHub. This is intended 
to be used as a GitHub Action, but it is not quite ready for that yet. 

