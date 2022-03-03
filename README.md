# payme-integration

## Setup project

### 1. Clone or Download zip to yourself

```sh
git clone https://github.com/SanjarbekSaminjonov/payme-integration.git
```

### 2. Set credentials

- Create '.env' file
- Generate Django 'SECRET_KEY'

```environs
export SECRET_KEY=SECRET_KEY
export DEBUG=true
export ID=Merchant_ID
export KEY=KEY
export TEST_KEY=TEST_KEY
```

Merchant_ID, KEY and TEST_KEY are credentials that payme gave you

### 3. Migrite migrations

```Python
python manage.py migrate
```

### 4. Create Paycom user

- Username - Paycom
- Password - KEY or TEST_KEY
