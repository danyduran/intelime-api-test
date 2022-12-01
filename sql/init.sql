
\c intelimetrica;

CREATE TABLE Restaurants(
    id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    rating SMALLINT NOT NULL DEFAULT 0,
    name VARCHAR(255) NOT NULL,
    site VARCHAR(255) NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    phone VARCHAR(255) NULL,
    street VARCHAR(255) NULL,
    state VARCHAR(255) NULL,
    city VARCHAR(255) NULL,
    lat DECIMAL NULL,
    lng DECIMAL NULL
);
COPY Restaurants FROM '/tmp/restaurantes.csv' WITH (FORMAT csv);
