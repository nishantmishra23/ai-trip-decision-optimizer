CREATE DATABASE IF NOT EXISTS ai_trip_optimizer;
USE ai_trip_optimizer;

CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    role ENUM('USER', 'ADMIN') DEFAULT 'USER',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE destinations (
    destination_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(150) NOT NULL,
    country VARCHAR(100),
    description TEXT,
    average_daily_cost DECIMAL(10,2),
    popularity_score DECIMAL(5,2),
    rating DECIMAL(3,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE hotels (
    hotel_id INT AUTO_INCREMENT PRIMARY KEY,
    destination_id INT NOT NULL,
    name VARCHAR(150) NOT NULL,
    price_per_night DECIMAL(10,2),
    rating DECIMAL(3,2),
    hotel_type VARCHAR(100),
    FOREIGN KEY (destination_id) REFERENCES destinations(destination_id)
);

CREATE TABLE restaurants (
    restaurant_id INT AUTO_INCREMENT PRIMARY KEY,
    destination_id INT NOT NULL,
    name VARCHAR(150) NOT NULL,
    cuisine VARCHAR(100),
    average_cost DECIMAL(10,2),
    rating DECIMAL(3,2),
    FOREIGN KEY (destination_id) REFERENCES destinations(destination_id)
);

CREATE TABLE activities (
    activity_id INT AUTO_INCREMENT PRIMARY KEY,
    destination_id INT NOT NULL,
    name VARCHAR(150) NOT NULL,
    category VARCHAR(100),
    price DECIMAL(10,2),
    rating DECIMAL(3,2),
    FOREIGN KEY (destination_id) REFERENCES destinations(destination_id)
);

CREATE TABLE transportation (
    transport_id INT AUTO_INCREMENT PRIMARY KEY,
    destination_id INT NOT NULL,
    transport_type VARCHAR(100),
    estimated_cost DECIMAL(10,2),
    duration_minutes INT,
    rating DECIMAL(3,2),
    FOREIGN KEY (destination_id) REFERENCES destinations(destination_id)
);

CREATE TABLE weather_records (
    weather_id INT AUTO_INCREMENT PRIMARY KEY,
    destination_id INT NOT NULL,
    record_date DATE,
    temperature DECIMAL(5,2),
    rainfall DECIMAL(6,2),
    weather_condition VARCHAR(100),
    FOREIGN KEY (destination_id) REFERENCES destinations(destination_id)
);

CREATE TABLE trips (
    trip_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    destination_id INT,
    start_date DATE,
    end_date DATE,
    travelers INT DEFAULT 1,
    total_budget DECIMAL(12,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (destination_id) REFERENCES destinations(destination_id)
);

CREATE TABLE trip_preferences (
    preference_id INT AUTO_INCREMENT PRIMARY KEY,
    trip_id INT NOT NULL,
    travel_style VARCHAR(100),
    interests TEXT,
    accommodation_preference VARCHAR(100),
    food_preference VARCHAR(100),
    weather_preference VARCHAR(100),
    transport_preference VARCHAR(100),
    FOREIGN KEY (trip_id) REFERENCES trips(trip_id) ON DELETE CASCADE
);

CREATE TABLE recommendations (
    recommendation_id INT AUTO_INCREMENT PRIMARY KEY,
    trip_id INT NOT NULL,
    destination_id INT,
    score DECIMAL(6,2),
    explanation TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (trip_id) REFERENCES trips(trip_id) ON DELETE CASCADE,
    FOREIGN KEY (destination_id) REFERENCES destinations(destination_id)
);

CREATE TABLE itineraries (
    itinerary_id INT AUTO_INCREMENT PRIMARY KEY,
    trip_id INT NOT NULL,
    title VARCHAR(200),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (trip_id) REFERENCES trips(trip_id) ON DELETE CASCADE
);

CREATE TABLE itinerary_items (
    item_id INT AUTO_INCREMENT PRIMARY KEY,
    itinerary_id INT NOT NULL,
    day_number INT,
    activity_name VARCHAR(200),
    start_time TIME,
    end_time TIME,
    estimated_cost DECIMAL(10,2),
    FOREIGN KEY (itinerary_id) REFERENCES itineraries(itinerary_id) ON DELETE CASCADE
);

CREATE TABLE search_history (
    search_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    search_query TEXT,
    searched_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

CREATE TABLE api_logs (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    api_name VARCHAR(100),
    endpoint VARCHAR(255),
    status_code INT,
    response_time_ms INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);