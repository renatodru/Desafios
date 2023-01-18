#!/bin/bash
sudo wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-8.0.0-amd64.deb
sudo wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-8.0.0-
amd64.deb.sha512
sudo shasum -a 512 -c elasticsearch-8.0.0-amd64.deb.sha512
sudo dpkg -i elasticsearch-8.0.0-amd64.deb
sudo wget https://artifacts.elastic.co/downloads/kibana/kibana-8.0.0-amd64.deb
sudo dpkg -i kibana-8.0.0-amd64.deb
sudo wget https://artifacts.elastic.co/downloads/logstash/logstash-8.0.0-amd64.deb
sudo dpkg -i logstash-8.0.0-amd64.deb
sudo wget https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-8.0.0-amd64.deb
sudo dpkg -i filebeat-8.0.0-amd64.deb
sudo apt-mark hold elasticsearch 
sudo adduser $USER elasticsearch
sudo adduser $USER kibana
sudo adduser $USER logstash
