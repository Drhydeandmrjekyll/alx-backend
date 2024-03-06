// 2-redis_op_async.js

import redis from 'redis';
import { promisify } from 'util';

// Create new Redis client
const client = redis.createClient();

// Promisify get method of the Redis client
const getAsync = promisify(client.get).bind(client);

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

// Function to set value for a new school in Redis
function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

// Async function to display value for a school in Redis
async function displaySchoolValue(schoolName) {
  try {
    const value = await getAsync(schoolName);
    console.log(value);
  } catch (error) {
    console.error(error);
  }
}

// Calling functions as per requirements
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
