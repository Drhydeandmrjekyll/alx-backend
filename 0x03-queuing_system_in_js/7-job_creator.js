// 7-job_creator.js

import kue from 'kue';

// Array of job data
const jobs = [
  {
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account'
  },
  {
    phoneNumber: '4153518781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153518743',
    message: 'This is the code 4321 to verify your account'
  },
  // Add more job data as needed
];

// Create Kue queue
const queue = kue.createQueue();

// Process each job data
jobs.forEach((jobData, index) => {
  // Create new job in the queue
  const job = queue.create('push_notification_code_2', jobData);

  // Event listener for successful job creation
  job.on('enqueue', () => {
    console.log(`Notification job created: ${job.id}`);
  });

  // Event listener for job completion
  job.on('complete', () => {
    console.log(`Notification job ${job.id} completed`);
  });

  // Event listener for job failure
  job.on('failed', (errorMessage) => {
    console.log(`Notification job ${job.id} failed: ${errorMessage}`);
  });

  // Event listener for job progress
  job.on('progress', (progress, data) => {
    console.log(`Notification job ${job.id} ${progress}% complete`);
  });

  // Save job to queue
  job.save();
});
