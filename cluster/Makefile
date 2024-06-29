svc-cluster:
	kubectl apply -f svc-headless-broker.yml | true
	kubectl apply -f svc-headless-controller.yml | true
	kubectl apply -f svc-np-broker-cluster.yml | true
	kubectl apply -f svc-np-broker-0.yml | true
	kubectl apply -f svc-np-broker-1.yml | true
	kubectl apply -f svc-np-broker-2.yml | true
	kubectl apply -f svc-np-controller-0.yml | true
	kubectl apply -f svc-np-controller-1.yml | true
	kubectl apply -f svc-np-controller-2.yml | true

svc-cluster-delete:
	kubectl delete -f svc-headless-broker.yml | true
	kubectl delete -f svc-headless-controller.yml | true
	kubectl delete -f svc-np-broker-cluster.yml | true
	kubectl delete -f svc-np-broker-0.yml | true
	kubectl delete -f svc-np-broker-1.yml | true
	kubectl delete -f svc-np-broker-2.yml | true
	kubectl delete -f svc-np-controller-0.yml | true
	kubectl delete -f svc-np-controller-1.yml | true
	kubectl delete -f svc-np-controller-2.yml | true

kafka-cluster:
	kubectl apply -f sts-cluster-kafka.yml | true
	@echo "waiting for few seconds..."
	@sleep 5 #dfsadfds

kafka-cluster-delete:
	kubectl delete -f sts-kafka-cluster.yml | true

cluster: kafka-cluster svc-cluster

cluster-delete: kafka-cluster-delete svc-cluster-delete

