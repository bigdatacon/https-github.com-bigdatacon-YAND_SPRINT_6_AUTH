#FROM docker.elastic.co/beats/filebeat:7.3.2
FROM docker.elastic.co/beats/filebeat:8.3.3
COPY filebeat.yml /usr/share/filebeat/filebeat.yml
USER root
RUN chown root:filebeat /usr/share/filebeat/filebeat.yml
RUN chmod 644 /usr/share/filebeat/filebeat.yml
USER filebeat
