CREATE EXTENSION postgis;

CREATE TABLE IF NOT EXISTS master (
    id SERIAL PRIMARY KEY,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    point_type VARCHAR(50),
    name VARCHAR(255),
    address TEXT,
    description TEXT,
    location GEOMETRY(Point, 4326) NOT NULL
);

CREATE INDEX idx_location ON master USING GIST(location);