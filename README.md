## Starlabs-Assignment

Webiste Preview:
![image](https://github.com/RheagalFire/Starlabs-Assignment/assets/60213893/02e54c94-d730-4910-9425-0cd127e8c5c3)
Alternate Product 1 : 
![image](https://github.com/RheagalFire/Starlabs-Assignment/assets/60213893/b91ac3c8-67ef-4532-bbbc-220173d34b43)
Alternare Product 2 :
![image](https://github.com/RheagalFire/Starlabs-Assignment/assets/60213893/f50abe56-e6c2-43c1-8c3c-6dd51cfd8642)

## Alternate Groups Finder

The function takes in three Arguments. 
1. Domain Name of the store
2. Model (Model to calculate the embeddings)
3. Threshold to consider while taking cosing similarity(default 0.8)<br>
<p>
I have used paraphrase_MiniLM-L6-v2 model from huggingface to calculate the embeddings from the title of the products.<br>
The streamlit app lets you download the JSON for the whole alternate groups that exist.<br> 
Alternatively we can see 5 of the results in the UI of the APP.<br> 
</p>

## Setup on Local
```
git clone https://github.com/RheagalFire/Starlabs-Assignment.git 
```
```
docker build -t container_name
```
```
docker run -p 8501:8501 container_name
```
