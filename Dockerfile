FROM python:3.10-alpine

RUN apk add git

RUN mkdir /checkoutdir

COPY entrypoint.sh /entrypoint.sh
COPY generate_wiki_page_index.py /generate_wiki_page_index.py

RUN /bin/chmod a+x /entrypoint.sh
RUN /bin/chmod a+x /generate_wiki_page_index.py

ENTRYPOINT ["/entrypoint.sh"]
