// 0-redis_client.js

import redis from 'redis';

// Create new Redis client
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
