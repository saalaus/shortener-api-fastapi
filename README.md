# Url shortener API on FastAPI

## API Reference

#### Short new url

```http
  POST /api/url/new
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `url` | `string` | **Required**. Url to short |
| `name`| `string` | Name for shorten url|

#### Get url info

```http
  GET /api/url/${url_name}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `url_name`      | `string` | **Required**. Url name to fetch |

#### Update url info

```http
  PATCH /api/url/update
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `new_name`      | `string` | New url name |
| `url`      | `string` | New url |
| `active`      | `string` | Disable/enable url |

#### Delete url

```http
  DELETE /api/url/delete
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `name`      | `string` | **Required**. Name url to delete |


#### Redirect to url

```http
  GET /${url_name}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `url_name`      | `string` | **Required**. Url name to redirect |
