# Librarian

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