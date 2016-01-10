FROM debian:jessie

RUN curl -kL https://raw.github.com/pypa/pip/master/contrib/get-pip.py | python \
    && pip install requests \
    && pip install yaml \
    && pip install git

COPY get_module.py /usr/local/bin

ENTRYPOINT ["/usr/local/bin/get_module.py"]
