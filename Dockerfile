FROM python:3

RUN git clone https://github.com/Sebacompu/proyecto-personal
WORKDIR /proyecto-personal

RUN pip install -r requirements.txt
RUN pip install parameterized

CMD [ "python3" , "Testsudoku.py" ]