ARG BUILD_FROM
FROM ${BUILD_FROM}

RUN apt-get update -y && \
    apt-get install gpg python3 python3-pip --no-install-recommends -y

RUN curl https://raw.githubusercontent.com/fluent/fluent-bit/master/install.sh | sh

COPY run.py /run.py
CMD ["python3", "-u", "/run.py"]
