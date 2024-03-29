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

## Lectures topics Friday 2PM-4PM HKT (Tentative)
1. (2/10)
    - Docker1: https://www.youtube.com/watch?v=eGz9DS-aIeY&ab_channel=NetworkChuck
    - Docker2 (long): https://www.youtube.com/watch?v=3c-iBn73dDE&ab_channel=TechWorldwithNana
    - K8S: https://www.youtube.com/watch?v=7bA0gTroJjw&ab_channel=NetworkChuck
    - https://docker-curriculum.com/#menu
    - https://www.eksworkshop.com/
    - https://medium.com/geekculture/from-apple-silicon-to-heroku-docker-registry-without-swearing-36a2f59b30a3  
1. (2/10) MLOps overview, demo system (docker, kubernates) overview
1. (2/17)Streamlit + FastAPI
    - Tutorial: https://streamlitpython.com/ 
    - Book: Building Python Web APIs with FastAPI By Abdulazeez Abdulazeez Adeshina
    - Book: Web Application Development with Streamlit: Develop and Deploy Secure and Scalable Web Applications to the Cloud Using a Pure Python Framework By Mohammad Khorasani, Mohamed Abdou, Javier Hernández Fernández
3. (2/24) Elastic search 101: Elastic search expert (Jong Min)
6. (3/3) Filebeat + Kibana: Kibana expert (Jong Min)
7. (3/10)Large-scale transformer models (Kevin Ko, TUNiB)
8. (3/17) Project introduction
10. (3/24) Larage Language Model (Chatgpt) actions at MS
   - Project proposal (5 min talk)
9. (3/31) Google cloud infra training/serving (Chansung Park/Sayak Paul), Hugging face (Sayak Paul, Hugging Face)
11. (4/7) AWS cloud infra (serving, ECS)(YJ Jeong from AWS)
    - https://sagemaker-workshop.com/
    - https://aws.amazon.com/blogs/machine-learning/host-hugging-face-transformer-models-using-amazon-sagemaker-serverless-inference/ 
11. (4/14) LLM1: Alpaca
12. (4/21) No class -- Please work on project
13. (4/28) Last Lecture: LLM2: LLaMa 
13. (5/5) Final project presenations


