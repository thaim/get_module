FROM python

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       subversion \
       git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && /usr/bin/git config --global http.sslVerify false \
    && pip install requests \
    && pip install pyyaml \
    && pip install gitpython \
    && pip install svn \
    && mkdir /modules

COPY ../get_modules.py /usr/local/bin/get_modules.py

VOLUME ["/modules"]

ENTRYPOINT ["/usr/local/bin/get_modules.py"]

CMD ["/etc/modulelist.yml", "/modules/" ]
