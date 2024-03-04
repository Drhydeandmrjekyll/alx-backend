import redis from 'redis';

// Create Redis client
const client = redis.createClient();

// Connect to Redis server
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Handle errors during connection
client.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err}`);
});

// End connection when script is interrupted
process.on('SIGINT', () => {
  client.quit();
});

// Gracefully handle process termination
process.on('exit', () => {
  client.quit();
});
