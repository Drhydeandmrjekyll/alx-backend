// 4-redis_advanced_op.js

import redis from 'redis';

// Create a new Redis client
const client = redis.createClient();

// Event listener for successful connection
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Event listener for connection error
client.on('error', (error) => {
  console.error(`Redis client not connected to the server: ${error}`);
});

// Event listener for connection close
client.on('end', () => {
  console.log('Connection to Redis server closed');
});

// Function to create and store hash in Redis
function createHash() {
  client.hset('HolbertonSchools', 'Portland', 50, redis.print);
  client.hset('HolbertonSchools', 'Seattle', 80, redis.print);
  client.hset('HolbertonSchools', 'New York', 20, redis.print);
  client.hset('HolbertonSchools', 'Bogota', 20, redis.print);
  client.hset('HolbertonSchools', 'Cali', 40, redis.print);
  client.hset('HolbertonSchools', 'Paris', 2, redis.print);
}

// Function to display hash stored in Redis
function displayHash() {
  client.hgetall('HolbertonSchools', (error, result) => {
    if (error) {
      console.error(error);
    } else {
      console.log(result);
    }
  });
}

// Calling functions as per requirements
createHash();
displayHash();
