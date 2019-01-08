FROM sdnguru22/derrcart_movie_app:v1
MAINTAINER derrcart@cisco.com

WORKDIR /derrcart_movie_app

#RUN yum -y install git 
#RUN curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
#RUN python get-pip.py

CMD ["mkdir", "/derrcart_movie_app"]

COPY README.md /derrcart_movie_app/README.md
COPY requirements.txt /derrcart_movie_app/requirements.txt
RUN pip install -r /derrcart_movie_app/requirements.txt

COPY get_movie.py /derrcart_movie_app/get_movie.py

ENTRYPOINT ["python", "/derrcart_movie_app/get_movie.py"]
