FROM ubuntu

RUN apt-get update

RUN apt-get install -y python3 python3-pip
RUN pip3 install pandas numpy seaborn matplotlib scikit-learn scipy

RUN mkdir /home/doc-bd-a1/

COPY tit_dataset.csv /home/doc-bd-a1/tit_dataset.csv

CMD ["/bin/bash"]