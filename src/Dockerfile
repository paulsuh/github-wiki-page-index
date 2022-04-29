FROM python:3.10-alpine

RUN apk add git

RUN mkdir /checkoutdir

COPY githubwikipageindex /
COPY generate_wiki_page_index.py /
COPY entrypoint.sh /entrypoint.sh

RUN /bin/chmod a+x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
