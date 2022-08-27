# Coderhouse Python - Our First MVT

This demo application will allow you start managing your family members and query them.

Once you cloned this repo, you can start this app by executing the following commands:

```shell
python manage-py runserver 
```

## Query family members

- **URL**

  family-member/


- **Method**

  `GET`


- Example

    http://localhost:8000/family-member/

## Start managing a family member

- **URL**

  family-member/registration/:first_name/:last_name/:age/:birthdate


- **Method**

  `GET`


-  **URL Params**

   **Required:**

    - `first_name=[string]`
    - `last_name=[string]`
    - `age=[integer]`
    - `birthdate=[string]{YYYY-MM-DD}`


- Example

    http://localhost:8000/family-member/registration/Pepe/Sanchez/26/1996-04-17
