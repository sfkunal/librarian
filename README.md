# Librarian
##### Kunal Srivastava
### Problem
Students are generally and consistently unaware of recently-made tools allowing them to leverage their own work in their learning. 

AI is changing the workforce -- studies show that technologies like CoPilot and GPTs can increase engineer productivity by up to 4 times. Academia has had an interesting response to this generative AI cycle, defaulting to defensive ideas like academic dishonesty, and a natural preference to adhere to the native guidelines that have held up academia for so long. 

I, along with other technology enthusiasts, believe the whole world of education is nearing a turning point. Education is going to flip on its head, through the transition of public education to private education. Before, due to limited resources like money and teachers, privatized education for every student in a equalized, accessible manner was not possible. 

However, given the appearance of AI tooling (generally speaking to generative AI that produces an output given input), we will most definitely see a rise in private AI education. It's just a more personalized way to teach. Students will simply learn more, in less time. In the end, data leads to insights. And traditional teachers just don't (1) have the brain power to hold historical learning data of every single student and (2) adopt their teaching styles to each individual student. Unlike traditional teachers, computers now have the ability to do both (1) and (2) at extremely high accuracies. 

### Solution
I'm going to build a generative AI platform for students. By incorporating student-specific integrations (so far Canvas and Notion), this platform will have additional user-specific context. I will employ a technique called Retrieval Augmented Generation (RAG) to reduce the knowledge context of an LLM to this additional user-specific context. This means that LLMs on-platform will **only** be an expert in the imported integrated content. 

#### Inefficiencies Students Face
1. Usually, once I write something, I don't read it ever again
2. It's really hard to locate specific *ideas* across my edu-verse (edu-verse: all virtual locations of my work)
3. Studying! Imagine if I could use my previous documents to generate future documents to aide my learning. That's powerful.
#### Product
##### Libraries
Users will have access to the Libraries feature. This feature allows them to upload their own documents (.pdf, .doc, .ppt, .md, and more). These libraries are uploaded as context knowledge bases to our backend, thus allowing the user to effectively query these libraries like chatbots at high accuracies and low hallucination rates
##### Document Viewer
We also want to incorporate a document viewer into the product. This is an extremely important feature because it connects our new (and potentially foreign) product to a student's past work. They can see the document in question in the viewer, and additionally we can highlight/cite specific parts of this viewable document to provide evidence when the user is conversing with the chatbot. 
##### Chat Interface
I want to create a chat interface, that given a large corpus of relevant historical data, supports these 3 broad features:

1. Find (an idea, given Libraries)
2. Create (study material, given Libraries)
3. Answer (given Libraries)

I've thought a lot about what the core components of this product would be, and I really think that value comes down to these three. Current AI systems can only do (3), but even then at hallucinatory levels. By reducing context down to only the Libraries, chatbots can become increasingly accurate. 
##### Canvas Integration
It is technically feasible to have a user log in with Canvas, select the classes they want to import, and literally import every document from their Canvas course into a Library. The average course holds at least 30-40 informative documents that can be leveraged for content mastery. This personal integration is probably the biggest advantage we have.
##### Notion/Google Drive Integration
It is very feasible for users to connect documents from other workspaces (Notion and Google Drive) and import them natively into our Libraries. This allows for higher personalization and context awareness when interacting with this product. 


### Backend:
1. **Programming Language:** Python
   - Reason: Python has extensive libraries and frameworks suitable for AI/ML development.

2. **Framework:** FastAPI
   - Reason: FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints. It is easy to use and highly performant.

3. **Database:** MongoDB
   - Reason: MongoDB is a NoSQL database that allows flexibility in handling unstructured data. It is suitable for storing document-based information and can handle large volumes of data efficiently.

4. **AI/ML Framework:** Hugging Face Transformers
   - Reason: Hugging Face Transformers provides pre-trained models for natural language processing tasks, including the retrieval augmented generation (RAG) algorithm. It's widely used in the NLP community and has good support for model deployment.

5. **Vector Database:** Faiss (Facebook AI Similarity Search)
   - Reason: Faiss is a library for efficient similarity search and clustering of dense vectors. It's optimized for performance and can handle the indexing and retrieval requirements of the Libraries feature efficiently.

### Frontend:
1. **Framework:** React.js
   - Reason: React.js is a popular and efficient JavaScript library for building user interfaces. It allows for the creation of interactive and responsive frontends.

2. **State Management:** Redux
   - Reason: Redux is a predictable state container for JavaScript apps, which can help manage the state of the application in a consistent way, especially when dealing with complex data interactions.

### Chat Interface:
1. **Chatbot Framework:** Rasa
   - Reason: Rasa is an open-source natural language processing framework that allows for the building of chatbots. It provides advanced natural language understanding capabilities.

### Integrations:
1. **Canvas Integration:**
   - Utilize Canvas API for authentication and document retrieval.
   - Develop a custom module to handle the import of documents from Canvas into the Libraries.

2. **Notion/Google Drive Integration:**
   - Use Notion and Google Drive APIs for authentication and document retrieval.
   - Develop modules to import documents from these platforms into Libraries.

### Additional Tools:
1. **Document Viewer:**
   - Integrate a document viewer using a tool like PDF.js for PDFs and other relevant libraries for different document types.

### Cloud Services:
1. **Hosting:** AWS (Amazon Web Services)
   - Reason: AWS provides a wide range of services, including compute, storage, and AI/ML services, making it suitable for hosting and scaling the application.

2. **Authentication:** OAuth 2.0 for Canvas and Google OAuth for Notion/Google Drive.
   - Reason: Standardized authentication protocols for secure integration with external platforms.

3. **Containerization:** Docker
   - Reason: Docker containers provide a consistent and reproducible environment for the application, making deployment and scaling more straightforward.

4. **Orchestration:** Docker Compose or Kubernetes
   - Reason: For managing and orchestrating multiple containers.

### DevOps:
1. **Version Control:** Git (GitHub or GitLab)
   - Reason: Standard version control for collaborative development.

2. **Continuous Integration/Continuous Deployment (CI/CD):** Jenkins or GitLab CI
   - Reason: Automate the testing and deployment processes.

3. **Monitoring:** Prometheus and Grafana
   - Reason: For monitoring the performance and health of the application.


# Setup

To get started with Librarian, follow the steps below to set up the backend and frontend components.

## Clone the Repository

Clone the full repository from GitHub:

```shell
git clone https://github.com/sfkunal/librarian
cd librarian
```

## Install Dependencies

### 1. Install Anaconda

If you haven't installed Anaconda, download and install it from [here](https://www.anaconda.com/products/distribution).

### 2. Install Docker

Ensure Docker is installed on your machine. You can find installation instructions [here](https://docs.docker.com/get-docker/).

## Set Up the Backend

Navigate to the backend folder:

```shell
cd librarian_backend
```

### 1. Create a New Virtual Environment

Open a terminal and run the following commands:

```shell
conda create -n llmware python=3.10
conda activate llmware
```

### 2. Install llmware

Install the llmware library:

```shell
pip install llmware
```

### 3. Initiate Docker Instance

Start the Docker containers with:

```shell
docker-compose up -d
```

### 4. Start the Backend Server

Run the following command to start the backend server:

```shell
python server/main.py
```

Ensure to check which port the server is served on, as it may be different from the default. For example, mine is http://127.0.0.1:5000

## Set Up the Frontend

If the backend is live, the frontend should work.

Open a new terminal, navigate to the frontend directory, and run:

```shell
npm start
```

## Configuration

Make sure to perform the following configurations:

### Backend Configuration

1. Set the API key in `librarian_backend/server/engine.py` on line 11.

2. Set the `UPLOAD_FOLDER` in `librarian_backend/server/main.py` on line 13. This path should be an absolute path to the `librarian_backend/library` folder, where the server downloads files.

3. Ensure the frontend is reaching out to the correct server. After running `python server/main.py`, it will tell you where the server is hosted. You may need to update this location in the frontend calls to the server. 

Now, Librarian is set up and ready to use!
