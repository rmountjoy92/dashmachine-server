FROM python:3.8

# add user
RUN useradd -r -s /bin/bash dm_user

# add project
ADD . /app
RUN chown -R dm_user:dm_user /app

USER dm_user

# set home & current env
ENV HOME /app
WORKDIR /app
ENV PATH="/app/.local/bin:${PATH}"

# set app config option
ENV CONFIG=dev

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt --user
RUN pip install --no-cache-dir uWSGI gevent --user

# start wsgi server
ENTRYPOINT ["uwsgi"]
CMD ["--http", ":5000", "--gevent", "1000", "--http-websockets", "--master", "--wsgi-file", "wsgi.py", "--callable", "app"]
