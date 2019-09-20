FROM python:3.6

# make dir for Dash app python code
RUN mkdir /code
ADD . /code
RUN chmod -R 755 /code
WORKDIR /code

RUN pip install -r requirements.txt

EXPOSE 8050

# the -u option means it's executed as 'unbuffered' which means all print statements are sent to std.out, which means they're printed in docker-compose (use for debugging)
CMD ["python3", "-u", "index.py"]
