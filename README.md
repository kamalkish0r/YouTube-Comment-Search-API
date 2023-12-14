# YouTube Comment Search API

This repository hosts a Flask-based API to search and filter YouTube comments based on various parameters such as author, text content, likes, replies, and dates.

## Getting Started

### Prerequisites

- Python (preferably Python 3.x) installed.
- Ensure `pip` is available.

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/YouTube-Comment-Search-API.git
   cd YouTube-Comment-Search-API
   ```

2. **Setup Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # For Windows, use venv\Scripts\activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the Application**

   ```bash
   python api.py
   ```

2. **Access the API**

   Once the application is running, you can access the API at:

   ```
   http://localhost:5000/search
   ```

   Use query parameters like `search_author`, `search_text`, `like_from`, `like_to`, `reply_from`, `reply_to`, `at_from`, and `at_to` to filter comments.

## API Endpoint

### `GET /search`

- **Parameters:**

  - `search_author`: Search comments by author's name.
  - `search_text`: Search comments by text content.
  - `like_from`, `like_to`: Filter comments by the number of likes.
  - `reply_from`, `reply_to`: Filter comments by the number of replies.
  - `at_from`, `at_to`: Filter comments by date range (format: `dd-mm-yyyy`).

- **Example Usage:**

  ```
  http://localhost:5000/search?search_author=Fredrick&at_from=01-01-2023&at_to=01-02-2023&like_from=0&like_to=5&reply_from=0&reply_to=5&seach_text=economic
  ```

## Contributing

Contributions are welcome! Please follow the standard guidelines when contributing.

## License

This project is licensed under the [MIT License](LICENSE).
