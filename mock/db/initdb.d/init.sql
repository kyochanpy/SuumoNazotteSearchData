CREATE EXTENSION postgis;

CREATE TABLE IF NOT EXISTS master (
    id SERIAL PRIMARY KEY,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    point_type VARCHAR(50) NOT NULL,
    name VARCHAR(255) NOT NULL,
    address TEXT NOT NULL,
    description TEXT,
    location GEOMETRY(Point, 4326) NOT NULL
);

CREATE INDEX idx_location ON master USING GIST(location);