# main

## System/Docker overview
<img width="758" alt="image" src="https://user-images.githubusercontent.com/901975/183826557-3dd15735-865c-4db2-abcd-9d66caba2473.png">

### Docker preperation
For each directory: crawl_index, es_index, es_search, model_serv do `make build push`

### Docker Compose
```
cd main
make up 
```

#### Crawl & Index
```
docker exec -it crawl-index-container /bin/bash
# crawl.sh  
```

#### Search test
http://localhost:8890

### Kubernates
```
minikube start
cd main
make kup
```
#### Crawl & Index
```
kubectl exec --stdin --tty crawl-index-... -- /bin/bash
# crawl.sh
```

#### Search test
```
kubectl port-forward --address 0.0.0.0 services/es-search 9977:8890
```

http://localhost:9977

## Lectures topics (Tentative)
1. (Sep 9, No class, Happy holidays!)
    - Docker1: https://www.youtube.com/watch?v=eGz9DS-aIeY&ab_channel=NetworkChuck
    - Docker2 (long): https://www.youtube.com/watch?v=3c-iBn73dDE&ab_channel=TechWorldwithNana
    - K8S: https://www.youtube.com/watch?v=7bA0gTroJjw&ab_channel=NetworkChuck
    - https://docker-curriculum.com/#menu
    - https://www.eksworkshop.com/
    - https://medium.com/geekculture/from-apple-silicon-to-heroku-docker-registry-without-swearing-36a2f59b30a3  
1. Sep 16, MLOps overview, demo system (docker, kubernates) overview
1. Sep 23, Elastic search 101: Elastic search expert
1. Sep 30,  Streamlit + FastAPI
1. (Oct 7, No Class, Chinese National Day)
1. Oct 14, Filebeat + Kibana: Kibana expert (Jong Min)
1. Oct 21, Transformers 101: Training Transformer Transformer experts in the industry
1. Oct 28, Hugging face (TBA)
1. Nov 4, Google clud infra (training/serving)
1. Nov 11, AWS cloud infra (serving, ECS)(YJ Jeong from AWS)
    - https://sagemaker-workshop.com/
    - https://aws.amazon.com/blogs/machine-learning/host-hugging-face-transformer-models-using-amazon-sagemaker-serverless-inference/ 
1. Nov 18, Docker, k8, KFlow, KServe, Airflow, performance evaluation
1. Nov 25, Continual learning pipeline (logging, kibana, retraining, etc.) 
1. Dec 2, Final project presenations
