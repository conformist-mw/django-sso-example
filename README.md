# OIDC implementation example

#### Enable https

For every service:

```shell
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout $service.key -out $service.crt
```

#### Provider

superuser credentials:
  - username: `provider`
  - password: `provider`
