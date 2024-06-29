
kafka-single:
	kubectl apply -f sts-kafka-single.yml | true
	@echo "waiting for few seconds..."
	@sleep 5

kafka-single-delete:
	kubectl delete -f sts-kafka-single.yml | true

svc-single:
	kubectl apply -f svc-np-broker-single.yml | true

svc-single-delete:
	kubectl delete -f svc-np-broker-single.yml | true

single: kafka-single svc-single

single-delete: svc-single-delete kafka-single-delete
