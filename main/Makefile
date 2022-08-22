# https://medium.com/freestoneinfotech/simplifying-docker-compose-operations-using-makefile-26d451456d63
# https://stackoverflow.com/questions/67805969/wait-for-specific-container-when-using-docker-compose-up-d
#KUBECONFIG=dsa-mlops-kubeconfig.yaml 
up:
	docker-compose up -d 

down:
	docker-compose down

rm:
	docker-compose rm -f

kup:
	echo "Deploying to minikube"
	kubectl apply -f dsa-net-networkpolicy.yaml 
	#kubectl apply -f elasticsearch-deployment.yaml 
	#kubectl apply -f kibana-deployment.yaml 
	kubectl apply -f emb-model-serv-deployment.yaml 
	#kubectl apply -f emb-dep.yaml 
	kubectl apply -f es-index-deployment.yaml 
	kubectl apply -f es-search-deployment.yaml 
	kubectl apply -f crawl-index-deployment.yaml
	
	echo "URL for the service"
	minikube service es-search --url

kdown:
	echo "Deleting from minikube"
	kubectl delete -f dsa-net-networkpolicy.yaml 
	#kubectl delete -f elasticsearch-deployment.yaml 
	#kubectl delete -f kibana-deployment.yaml 
	kubectl delete -f emb-model-serv-deployment.yaml 
	kubectl delete -f es-index-deployment.yaml 
	kubectl delete -f es-search-deployment.yaml
	kubectl delete -f crawl-index-deployment.yaml

