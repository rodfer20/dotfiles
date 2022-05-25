# archlinux :: hackbox
FROM archlinux:latest
WORKDIR /root
COPY hello.sh .
RUN ./hello.sh
COPY hackbox-init.sh .
RUN echo "Y" | ./hackbox-init.sh
RUN rm hackbox-init.sh
RUN rm hello.sh
