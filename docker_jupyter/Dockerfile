FROM ubuntu:latest

RUN apt-get update && apt-get install -y python3 \
    python3-pip
   
#WORKDIR jupyter

#ADD requirements.txt jupyter

#RUN pip3 install --trusted-host pypi.python.org -r requirements.txt

RUN pip3 install jupyter

RUN useradd -ms /bin/bash jupyter
USER jupyter


#RUN pip3 install -r requirements.txt
      
ENTRYPOINT ["jupyter", "notebook", "--ip=*"]






