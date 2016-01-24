FROM debian:jessie

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       curl \
       python \
       subversion \
       git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && /usr/bin/git config --global http.sslVerify false \
    && /usr/bin/curl -kL https://raw.github.com/pypa/pip/master/contrib/get-pip.py | python \
    && pip install requests \
    && pip install pyyaml \
    && pip install gitpython \
    && pip install svn \
    && mkdir /modules

COPY ../get_modules.py /usr/local/bin/get_modules.py
COPY ../modulelist.yml /etc/modulelist.yml
COPY docker-entrypoint.sh /

VOLUME ["/modules"]

ENTRYPOINT ["/docker-entrypoint.sh"]

CMD ["/etc/modulelist.yml", "/modules/" ]
