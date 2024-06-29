## Kafka (KRaft Mode) deployment on kubernetes

This repo contains kube manifest for deploying vanilla `Apache/Kafka` docker image with KRaft mode in kubernetes.

The setup (single and cluster) targets deployment of either single node and cluster(of 3 nodes)

In the folders is a Makefile for quicker bootstrap and teardown in a kube cluster

For the cluster mode, separate headless and nodeport services were created in order to allow for communication between the brokers and controllers

The pods are created using a StatefulSet since it offers predictable pod names which will be used to setup the services and kafka listeners

Also included is a test kafka client in python using `confluent-kafka` library
