# Image processing server

An image processing server using Python, OpenCV, Flask and PostgreSQL.
Upload an image and execute single or multiple manipulations on it via query string.

## Supported image manipulations

- rotate
- resize
- crop
- flip
- grayscale

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`DATABASE_URL=postgresql://{username}:{password}@{host}:{port}/{db_name}`

`SECRET_KEY={secret_key}`

`ORIGINAL_UPLOAD_FOLDER = /static/original_images/`

`PROCESSED_UPLOAD_FOLDER = /static/processed_images/`

## Run Locally

Clone the project

```bash
  git clone https://github.com/MartinKraychev/Image-processing-server.git
```

Go to the project directory

```bash
  cd Image-processing-server
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  flask run
```

## Example query strings

The query string should follow a strict naming convention.
Double quotes are mandatory.

- rotate - {"rotate":{"angle":45}}
- resize - {"resize":{"height":300,"width":300}}
- crop - {"crop":{"height":300,"width":300}}
- flip - {"flip":{"code":1}}
- grayscale - {"grayscale":{}}

## Example local URLs

- rotate:
  ```http://localhost:5000/image/{id}?rotate={"angle":90}```
- resize:
  ```http://localhost:5000/image/{id}?resize={"height":300,"width":400}```
- crop:
  ```http://localhost:5000/image/{id}?crop={"height":100,"width":100}```
- flip:
  ```http://localhost:5000/image/{id}?flip={"code":-1}```
- grayscale:
  ```http://localhost:5000/image/{id}?grayscale={}```
- chaining multiple image manipulations:
  ```http://localhost:5000/image/{id}?resize={"height":300,"width":150}&flip={"code":1}&rotate={"angle":90}&grayscale={}```

## API Reference

#### Upload an image

```http
  POST http://localhost:5000/images
```
 If you are using Postman in the body go to form-data and add parameter 'file' as key and add the image as value.
 Maximum upload size is 1MB and allowed extensions are jpg, jpeg and png.

#### GET the processed image

```http
  GET //localhost:5000/image/{id}?{query_params}
```

| Parameter  | Type     | Description                         |
|:-----------|:---------|:------------------------------------|
| `filename` | `string` | **Required**. UUID of item to fetch |

## Authors

- [@MartinKraychev](https://github.com/MartinKraychev)
- [@haraGADygyl](https://github.com/haraGADygyl)

## License

[MIT](https://choosealicense.com/licenses/mit/)
