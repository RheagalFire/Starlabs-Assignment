import requests
import json
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def FindAlternateGroups(store_domain,model,cosine_thresh=0.8):
    '''
    store domain: don't give with https:// and ensure no backtick at the end of the URL.
    model : The huggingface modelfile for creating embeddings.
    cosine_thresh = threshold for comparing products.
    '''
    page = 1
    all_products = []
    
    while True:
        response = requests.get(f"https://{store_domain}/collections/all/products.json?page={page}")
        data = json.loads(response.text)
        products = data.get('products', [])
        
        if not products:
            # if there are no more products, break the loop  
            break
        # For the ease of creating embeddings right now let us just consider the title of the product
        for product in products:
            product_title = product.get('title', '')
            product_link = f"https://{store_domain}/products/{product.get('handle', '')}"
            all_products.append((product_title, product_link))
        
        page += 1
    
    # Create a list of product titles and links separately
    product_titles = [title for title, link in all_products]
    product_links = [link for title, link in all_products]

    # Generate embeddings for all product titles
    embeddings = model.encode(product_titles)

    # Compute the cosine similarity matrix
    similarity_matrix = cosine_similarity(embeddings)

    # Find the indices of the products that have a cosine similarity above a threshold (for example, 0.8)
    similar_product_indices = np.where(similarity_matrix > cosine_thresh)

    # Group the similar products together
    product_alternate_groups = []
    for i in range(len(similar_product_indices[0])):
        if similar_product_indices[0][i] != similar_product_indices[1][i]:  # ignore the diagonal elements
            product_alternate_groups.append({
                "product alternates": [
                    product_links[similar_product_indices[0][i]],
                    product_links[similar_product_indices[1][i]]
                ]
            })
    
    return product_alternate_groups