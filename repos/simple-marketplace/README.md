
# Simple Marketplace

This is a simple marketplace application built with Python and Flask. It provides basic functionality for users to list items for sale and browse available items.

## Features

- User registration and authentication
- List items for sale
- Browse available items
- Search functionality
- Basic cart system

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/simple-marketplace.git
   cd simple-marketplace
   ```

2. Build the Docker image:
   ```
   ./scripts/build.sh
   ```

3. Run the application:
   ```
   ./scripts/run.sh
   ```

4. Access the application at `http://localhost:5000`

## Testing

To run the tests, use the following command:
```
docker exec -it simple-marketplace pytest
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
