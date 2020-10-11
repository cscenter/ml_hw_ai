FROM python:3.7.1-slim

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ARG agent_cls_path=agent.my_agent.MyAgent
ENV AGENT_CLS_PATH=$agent_cls_path

RUN python3 ./agent_test.py "$AGENT_CLS_PATH"

CMD [ "python3", "./client.py" ]
